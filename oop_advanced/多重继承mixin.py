# -*- coding: utf-8 -*-

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

"""
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
"""

"""
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
"""

"""
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
"""

# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类