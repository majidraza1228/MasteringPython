from dataclasses import dataclass

@dataclass
class DataClass:
    name: str
    value:int
    
test = DataClass("Helloworld",1234)

print(test.value)

from collections import namedtuple
NamedTupleCard = namedtuple('NamedTupleCard',['rank','suit'])
queen_of_heart= NamedTupleCard('Q', 'Hearts')
print(queen_of_heart.rank)



