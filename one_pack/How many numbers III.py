# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
'''
We want to generate all the numbers of three digits where:
    the sum of their digits is equal to 10
    their digits are in increasing order (the numbers may have two or more equal contiguous digits)
The numbers that fulfill these constraints are: [118, 127, 136, 145, 226, 235, 244, 334].
There're 8 numbers in total with 118 being the lowest and 334 being the greatest.
Implement a function which receives two arguments:
    the sum of digits (sum)
    the number of digits (count)
This function should return three values:
    the total number of values which have count digits that add up to sum and are in increasing order
    the lowest such value
    the greatest such value
Note: if there're no values which satisfy these constaints,
you should return an empty value (refer to the examples to see what exactly is expected).
'''
from itertools import combinations_with_replacement as cwr



def find_all(sum_dig, digs):
    return [len(l), int(l[0]), int(l[-1])] if (l := [''.join(map(str, el)) for el in cwr(range(1, 10), digs) if sum(el) == sum_dig]) else []


assert find_all(10, 3)  ==  [8, 118, 334]
assert find_all(27, 3)  ==  [1, 999, 999]
assert find_all(84, 4)  ==  []
assert find_all(10, 3)  ==  [8, 118, 334]
assert find_all(35, 6)  ==  [123, 116999, 566666]
