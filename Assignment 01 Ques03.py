# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

x = [1,2,3,4,5,6,7,8,9]

count_even = 0
count_odd = 0
for i in x:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"The count of even numbers in the given series is: {count_even}")
print(f"The count of odd numbers in the given series is: {count_odd}")

