
#Write a for loop to count the sum of all even numbers, and the sum of all odd numbers between 1 and 100.

#variables to capture the sum of the numbers
sum_eve = 0
sum_odd = 0

#loops through the range, 
#checks if a number is odd or even, adds the numbers in each sequence
for loop in range(1,100):
    if loop % 2 == 0:
        sum_eve += loop
    else:
        sum_odd +=loop

print(f'sum of all even numbers is {sum_eve} \nsum of all odd numbers is {sum_odd}')

