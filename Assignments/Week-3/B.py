'''
Accept a string as input, convert it to lower case,
sort the string in alphabetical order,
and print the sorted string to the console.
You can assume that the string will only contain letters.
'''
input_str = input("")
lowerstr = input_str.lower()
sorted_string = ''.join(sorted(lowerstr))
print(sorted_string ,end="")
