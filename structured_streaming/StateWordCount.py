import os
import shutil
import time
from pathlib import Path
from typing import Tuple, Iterator

import pandas as pd
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
from pyspark.sql.streaming.state import GroupState, GroupStateTimeout

# reference: https://www.databricks.com/blog/2022/10/18/python-arbitrary-stateful-processing-structured-streaming.html
if __name__ == '__main__':
    # NOTE: set `basedir` with the fused path, e.g., "/dbfs/tmp" in Databricks
    # notebook.
    basedir = "/Users/fei.xiao/IdeaProjects/python-learning"

    # My text files containing words will be created in this directory later
    # after cleaning 'words_dir' directory up in case you already ran this
    # example below.
    words_dir = os.path.join(basedir, "words_dir")
    shutil.rmtree(words_dir, ignore_errors=True)
    os.makedirs(words_dir)

    builder = (
        SparkSession.builder.appName("local_spark")
    )

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    # Now, start a streaming query that ingests 'words_dir' directory.
    # Every time when there are new text files arriving here, we will process them.
    lines = spark.readStream.text(Path(words_dir).as_uri())

    # Split the lines into words.
    events = lines.select(explode(split(lines.value, " ")).alias("session"))


    def func(
            key: Tuple[str], pdfs: Iterator[pd.DataFrame], state: GroupState
    ) -> Iterator[pd.DataFrame]:
        if state.hasTimedOut:
            (word,) = key
            (count,) = state.get
            state.remove()
            yield pd.DataFrame({"session": [word], "count": [count]})
        else:
            # Aggregate the number of words.
            count = sum(map(lambda pdf: len(pdf), pdfs))
            if state.exists:
                (old_count,) = state.get
                count += old_count
            state.update((count,))
            # Set the timeout as 10 seconds.
            state.setTimeoutDuration(10000)
            yield pd.DataFrame()


    # Group the data by word, and compute the count of each group
    output_schema = "session STRING, count LONG"
    state_schema = "count LONG"
    sessions = events.groupBy(events["session"]).applyInPandasWithState(
        func,
        output_schema,
        state_schema,
        "append",
        GroupStateTimeout.ProcessingTimeTimeout,
    )

    # Start running the query that prints the windowed word counts to the console.
    query = sessions.writeStream.foreachBatch(lambda df, _: df.show()).start()

    # Now, we will write words to be processed in a streaming manner
    # Write 1 banana, 2 grapes, and 3 apples.
    with open(os.path.join(words_dir, "words.txt"), "w") as f:
        _ = f.write("banana grape apple\n")
        _ = f.write("banana apple apple\n")

    # Write 3 bananas and 3 grapes every second for 10 seconds.
    for i in range(10):
        time.sleep(1)
        with open(os.path.join(words_dir, f"words_{i}.txt"), "w") as f:
            _ = f.write("banana banana banana\n")
            _ = f.write("grape grape grape\n")

    # Wait enough for the query to finish the input.
    time.sleep(60)
    query.stop()
