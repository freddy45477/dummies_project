
#Variables
'''name = 'Phuc'
age = 23
gpa = 3.6
isGraduate = True

print(f"{name} is {age} years old, has a GPA of {gpa}, and graduated: {isGraduate}")

#Input Syntax
user_name= input('What is your name? ')
user_age= input('What is your age? ')
user_langange = input ('What is your faavorite programming language?')

print(f"Hello {user_name}!\n You are {user_age} years old \n Your favorite language is {user_langange}")



#If Statments
u_age = int(input('Enter your age:'))

if u_age >= 18:
    print('you are an adult')
elif u_age > 13 and u_age <=17:
    print('you are a teenager')
else:
    print('You are a child')
'''
#Grade Calculator
'''grade = int(input("Enter your  grade: "))
if grade >= 90 and grade <= 100:
    print('A')
elif grade >=80 and grade >=89:
    print('B')
elif grade >=70 and grade <=79:
    print('C')
elif grade >= 60 and grade<= 69:
    print('D')
elif grade >= 0 and grade<60:
    print('F')
else:
    print('not a valid grade')'''

p_languages = ['python','ruby','C++','java','Swift']
print(p_languages)
print(p_languages[0])
#Remember about -1 
print(p_languages[-1])
print(len(p_languages))
p_languages.append('SQL')
p_languages.remove('java')
print(p_languages)


numbers = [10, 25, 7, 42, 18, 31]
for i in numbers:
    if i > 20:
     print(i)

user_employee = input("Enter your name: ")
employees = ["John", "Sarah", "Mike", "David", "Lisa"]

#practice more with slicing
#pratice with list comphresion
#

user_employee=user_employee[0].upper()+ user_employee[1:].lower()

if user_employee in employees:
   print('Employee found!')
else:
   print('Employee not found')