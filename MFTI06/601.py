# List comprehention
A = [x**2 for x in range(10)]
print(A)

B = [x**2 for x in A if x%2 == 0]
print(B)
