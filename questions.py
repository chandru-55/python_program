'''
# Python If-Else condition
​
# Task 
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
​
# Input Format
# A single line containing a positive integer, n.
​
# Constraints
# 1 <= n <= 100
​
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
'''
'''

 Using for loop : Iterate each element in the list using for loop and check if num % 2 != 0. If the condition satisfies, then only print the number.
​
2. Using While loop:
​
3. Using list comprehension :
​
4. Using lambda function :
'''
'''
the code appearing below shows two nested loops, an outer for loop over the values of i and an inner for loop over the values of j to multiply inside the inner loop all nine elements of a 3x3 matrix A by a factor f that changes according to the outer loop iteration.
​
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
​
f = 1
print(A)
for i in range(0, 3):
    f *= 10
    for j in range(0, 3):
       A[i][j] *= f
print(A)
​
​
​
Therefore, the outer loop executes 3 iterations (i equal to 0, 1, and 2), and at each iteration it's executed:
​
The multiplication of the factor f by 10
​
The execution of the inner loop that has 3 iterations (j equal to 0, 1, and 2), and at each iteration the element i,j of A is multiplied by f
​
https://docs.python.org/3/reference/simple_stmts.html#grammar-token-nonlocal-stmt
​
​
Maps ands Lambda function
​
https://www.programiz.com/python-programming/methods/built-in/map
'''		