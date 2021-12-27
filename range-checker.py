
#%%

#Write a function called in_range which takes in a lower bound, an upper bound, and a number
#If it is, return " is between and ."
#If it isn't, return " is NOT between and ."
# Call your function to test it


# %%
#defining the function
def in_range(l_bound, u_bound, number):
    if number > l_bound and number < u_bound:
         print(f'{number} is between {l_bound} and {u_bound}')
    else:
         print(f'{number} is not between {l_bound} and {u_bound}')


# %%
#calling the function
l_bound = input('Enter the lower bound: ')
u_bound = input('Enter the upper bound: ')
number = input('Enter the number: ')

in_range(l_bound,u_bound,number)