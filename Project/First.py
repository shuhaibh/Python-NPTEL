#simple printing
print(10)

#inputting From user
name=input("What is your name?")
print("Your name is ",name)

#taking in numbers
c=int(input("Enter a number"))
print(c)

#if statement
if(c%2==0):
    print("You have Entered an Even number")
else:
    print("You have Entered an Odd number")

#loop
for i in range(10):
    print("Hi")
    
#list

Shopping=["Bread","Butter","Coffee","Oil"]
print(Shopping)

#printing list
for item in Shopping:
        print(item)
        
#another way of printing using index 
for i in range(4):
    print(Shopping[i])

#adding new item to list
Shopping.append("Brush")
print(Shopping)

#inserting item to a specific position
Shopping.insert(2,"Apple")
print(Shopping)

#count funtion
age=["10","20","20","35","48","56","75","34","74","75","20","35"]
age.count("20")

#to sort
age.sort()

#to reverse
age.reverse()

#slicing
#function_name[index_F:index_L+1]
