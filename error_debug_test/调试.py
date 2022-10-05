# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO) # 默认级别是 warn

# 方式1 print

# 方式2 assert

a = 1
assert a != 0, 'a can not be zero'
print(a)

# 方式3 logging
logging.warning('num is %s' % a)

# 方式4 是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态

# IDE

