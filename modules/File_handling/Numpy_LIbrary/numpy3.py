import numpy as np
n = int(input("Enter an even number = "))
# condition for 0 and negative
if n <= 0:
    print("Number should be greater than 0")
    exit()
even_num = []
for i in range(1, n):
    if n % i == 0 and i % 2 == 0:
        even_num.append(i)
array2 = np.array(even_num)
print("Even array:", array2)