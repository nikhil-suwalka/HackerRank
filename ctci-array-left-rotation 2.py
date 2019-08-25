'''

The print function uses sep to separate the arguments, and end after the last argument.

print('foo', 'bar')
foo bar
print('foo', 'bar', sep='')
footbar
'''

'''

A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array of n integers and a number,d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.
'''
import timeit

start = timeit.default_timer()


def array_left_rotation(a, n, k):
    return a[k:] + a[:k]


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')

print("Time :", timeit.default_timer() - start)
