'''
You are given the dates of birth of two persons,
not necessarily from the same family. Your task is to find the younger of the two.
If both of them share the same date of birth,
then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).

The input will have four lines. The first two lines correspond to the first person,
while the last two lines correspond to the second person.
For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format.
Your output should be the name of the younger of the two.
'''
from datetime import datetime
def calculate_age(date_of_birth):
    today = datetime.now()
    birth_date = datetime.strptime(date_of_birth, "%d-%m-%Y")
    return (today - birth_date).days // 365

name1 = input().strip()
dob1 = input().strip()

name2 = input().strip()
dob2 = input().strip()

age1 = calculate_age(dob1)
age2 = calculate_age(dob2)

print(name1 if age1 < age2 or (age1 == age2 and name1 < name2) else name2 ,end="")
