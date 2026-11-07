"""
#variables
name = 'Phuc'
age = 23
GPA = 3.6
graduated = True

print (f'{name} is {age} years old, has a GPA of {3.6}, and graduated: {graduated}')

#inputs
name1 = input("What is your name?: ")
age1 = input("How old are you?: ")
fav_prog_lang = input("What is your favorit programming language?: ")

print (f'Hello {name1}!\nYou are {age1} years old\nYour favorite programming language is {fav_prog_lang}')


#if statements
age2 = int(input("What is your age?: "))

if age2 >= 18:
    print ("You are an adult")
elif age2 in range(13, 17):
    print("you are a teenager")
else:
    print("you are a child")


#grade calculator
grade = int(input("what is grade?: "))

if grade in range(90, 100):
    print("Grade: A")
elif grade in range(80, 90):
    print("Grade: B")
elif grade in range(70, 80):
    print("Grade: C")
elif grade in range(60, 70):
    print("Grade: D")
elif grade in range(0, 60):
    print("Grade: F")
else:
    print("invalid input")


#list
languages = ["Python", "Java", "JavaScript", "C++", "C#"]

print(languages)
print(languages[0])
print(languages[-1])
print(len(languages))
languages.append("SQL")
languages.remove("Python")
print(languages)


#for loops
numbers = [10, 25, 7, 42, 18, 31]
print("all numbers:")
for num in numbers:
    print (num)


print("numbers greater than 20")
for num in numbers:
    if num > 20:
        print(num)



#finding stuff in lists
employees = ["John", "Sarah", "Mike", "David", "Lisa"]

lowercase_employees = []
for employee in employees:
    lowercase_employees.append(employee.lower())
name = input("employee's name: ")

if name in lowercase_employees:
    print("employee found")
else:
    print("employee not found")

#Dictionaries
computer = {
    "brand": "Dell",
    "model": "OptiPlex",
    "ram": 32,
    "storage": 512,
    "os" : "Windows 11"

}


print ("Brand: " + computer["brand"])
print ("Model: " + computer["model"])
print ("RAM: " + str(computer["ram"]))
print ("Storage: " + str(computer["storage"]))
print ("OS: " + computer["os"])
# functions
def calculate_area(length, width):
    return length*width

area = calculate_area(5, 8)

print (area)



def check_password(password):
    if len(str(password)) < 8:
        return "password is too short"
    else:
        return "password accepted"

result = check_password("pokem")
print(result)
"""
numbers = [12, 45, 7, 89, 23, 56]

def find_largest(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

print(find_largest(numbers))



    

