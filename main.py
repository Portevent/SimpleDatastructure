import time
from typing import List

from btree.bTree import BTree
from data.TableRow import TableRow
from data.data import Data


SIZE = 1000
FETCH_COUNT = 10000
MIN_ELEMENTS = 2
MAX_ELEMENTS = 10

print(f"Testing : {SIZE} elements that will each be fetched {FETCH_COUNT} times")

datas: List[Data] = [TableRow(i, f"{i}") for i in range(SIZE)]

test: BTree = BTree(MIN_ELEMENTS, MAX_ELEMENTS)
simple_dict = {}
simple_list = []

start = time.time()

for data in datas:
    test = test.insert(data)

for i in range(FETCH_COUNT):
    for data in datas:
        if data != test.fetch(data):
            raise Exception(f"{data} not found at {test.fetch(data)}")

end = time.time()

print(f"BTree({MIN_ELEMENTS}-{MAX_ELEMENTS}) ended in {end-start}")

start = time.time()

for data in datas:
    simple_dict[data.get_key()] = data

for i in range(FETCH_COUNT):
    for data in datas:
        if data != simple_dict[data.get_key()]:
            raise Exception(f"{data} not found at {simple_dict[data.get_key()]}")

end = time.time()

print(f"Simple dict ended in {end-start}")


start = time.time()

for data in datas:
    simple_list.append(data)


def search(elements: List[Data], looking_for: Data):
    for element in elements:
        if element == looking_for:
            return element
    raise Exception(f"{looking_for} not found in {list}")


for i in range(FETCH_COUNT):
    for data in datas:
        search(simple_list, data)

end = time.time()

print(f"Simple list ended in {end-start}")
