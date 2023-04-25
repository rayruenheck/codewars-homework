import timeit
#question 1 
# Factorials are often used in probability and are used as an introductory problem for looping constructs. In this kata you will be summing together multiple factorials.

def sum_factorial(lst):
    output_sum = 0 #O(1)
    for e in lst: #O(n)
        factorial = 1 #O(1)
        for num in range(1, e + 1):#O(n)
            factorial *= num #O(1)
        output_sum += factorial#O(1)
    return output_sum#O(1)
#  time complexity = #O(n^2) or quadratic
lst = [4,6]

print(sum_factorial(lst))

print(timeit.timeit('sum_factorial(lst)', globals=globals(), number=1000))
