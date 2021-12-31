
#%%
# 1. Create a function which takes in the name, age, and email of a user trying to create a new profile on our application
# 2. Check the name does not contain any of "!@£$%^&*()"
# 3. Check the email is valid by making sure it contains "@"
# 4. Check the age > 12
# 5.Turn each step above into a function, so that you have one function, which calls 3 other functions inside
# 6. Print a friendly error to explain the issue to the user if any of these checks does not pass


# %%
import re

name = ''
age = ''
email = ''
val = True
special_sym = list("!@£$%^&*()")
err_msgs = []

def main():
    profile_validation()


def profile_validation():
    global name, age, email
  
    name = input('Enter full name: \n')
    age = int(input('Enter age: \n'))
    email = input('Enter email: \n')

    age_val = check_age(age)
    name_val = check_name(name)
    email_val = check_email(email)

    if age_val[0] == True and name_val[0] == True and email_val[0] == True:
        print("Profile Validated")

    elif age_val[0] == False or name_val[0] == False or email_val[0] == False:


        if age_val[0] == False:
            err_msgs.append(age_val[1])
    
        if name_val[0] == False:
            err_msgs.append(name_val[1])
        
        if email_val[0] == False:
            err_msgs.append(email_val[1])

    if len(err_msgs) != 0:
        for msg in err_msgs:
             print(msg)




def check_age(age):
    if age > 12:
        
        return True, None
    else:
        err_msg = "You must be older than 12 years"
        return False, err_msg

def check_name(name):
    
    if any(char in special_sym for char in name):
        err_msg = "Name should not contain special characters" 
        return False, err_msg
    else:
        return True, None

def check_email(email):
    if '@' in email:
        return True, None
    else:
        err_msg = 'email should contain @'
        return False, err_msg


if __name__ == '__main__':
    main()

# %%
