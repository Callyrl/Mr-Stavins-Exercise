def palindrome(word):
    if len(word) <1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
        
message = str(input("Enter a string:"))
if (palindrome(message) == True):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

