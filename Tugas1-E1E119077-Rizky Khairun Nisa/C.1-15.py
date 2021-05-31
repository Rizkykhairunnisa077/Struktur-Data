from typing import List


def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)


data1 = [6, 4, 2, 5, 3, 1]
data2 = [5, 4, 2, 7, 5, 4]
print(areDistinct(data1))
print(areDistinct(data2))
