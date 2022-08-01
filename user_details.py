print("hello user") # introduction
firstname = input("please enter your first name: ") # asks for first name and allows user to input
lastname = input("please enter your last name: ")# asks for last name and allows user to input
name = (firstname + " " + lastname) #concatenates first and last name
print("hello, " + name)
age = (input("what is your age? ")) # asks for age and has to be integer (i would like to add functionality that code wont crash if user inputs letters intead of numbers)
street_name = input("please enter your street name: ") # asks user for address and waits for input
house_number = (input("please enter your house number: "))
postcode = input("please enter your postcode: ")
salary = (input("what is your salary? ")) # asks user for salary and allows for decimal points
course = input("what course are you taking? ") # asks what course and waits for input

address = (str(house_number) + " " + street_name + ", " + postcode) #concantenation and casting

print(name +"'s address is: " + address)

print(name + " is taking the " + course + " " + "course, which pays you a salary of: " + str(salary))

