#Palindrome checker
def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


print("Welcome to the Palindrome checker!!!")
word = input("Enter the word of your choice: ")
print(is_palindrome(word))
