
#Checks if a given word is a palindrome
#A Palindrome is a word that is the same even it is spelt backwards

# %%
print('Let\'s Check if a word is a palindrome')
word = input("Enter a word")

#these two statements reverses the string, use any variable
reverse_word = word[::-1]
rev_word = ''.join(list(reversed(word)))

#checks word 
if word == reverse_word:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not a Palindrome")

