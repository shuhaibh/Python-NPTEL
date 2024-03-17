'''
Accept a string as input. Your task is to determine if the input string is a valid password or not. For a string to be a valid password, it must satisfy all the conditions given below:
(1) It should have at least 8 and at most 32 characters
(2) It should start with an uppercase or lowercase letter
(3) It should not have any of these characters: / \ = ' "
(4) It should not have spaces
It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). Output True if the string forms a valid password and False otherwise.
'''
password=input()
result = 8 <= len(password) <= 32 and password[0].isalpha() and all(char not in "/\\='\"" for char in password) and ' ' not in password
print(result, end="")
