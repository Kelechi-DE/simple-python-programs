
#%%
#This python script takes two numbers and find the prime numbers between range
#Prime numbers are numbers that only divisible by itself and one i.e it has no factors asides itself and 1
#get numbers from user
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the first number: '))

#Handles scenario a user input smaller digit first
max = max(first_number,second_number)
min = min(first_number,second_number)


#creates iterator
for i in range(min,max):

    #prime numbers must be greater than 1 
    if i > 1:

        for x in range(2,i):

            #checks for factors of each number at each iteration
            if (i % x) == 0:
                print(i,"is not a prime number")
                print(x,"times", i//x ,"is", i)
                break
        else:
            print(i,"is a prime number")

    else:
        print(f"{i} is less than an it is not a prime number")
