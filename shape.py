
#this python programs used nested for loop to create the shape be;
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *

# %%


#this tasks requires one outer loop and two nested loops
#the first increasing loop creates the first half of the shape 
# and the second decreasing loop creates the other half
for x in range(1):
    
    
    for y in range(1,6):
        print('*' * y )

    #reverses the output of range    
    for z in range(6,0,-1):
        print('*' * z)

