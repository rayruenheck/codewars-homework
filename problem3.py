import timeit

# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

# Example:

# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

def flatten_and_sort(array):
    item = []#O(1)
    for e in array:#O(n)
        for x in e:#(n)
            item.append(x)#O(1)
    
    item.sort()#O(1)
    return item#O(1)
# time complexity = O(n^2) or quadratic
array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
print(flatten_and_sort(array))
print(timeit.timeit('flatten_and_sort(array)', globals=globals(), number=1000))
