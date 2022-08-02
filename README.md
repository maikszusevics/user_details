# concatenation, casting, and methods in python
**Concatenation** in python is the combination of two or more strings. In this document, it will be used to combine several user inputs into one variable which can be displayed with correct grammar by use of python *methods*. It will also show how casting is used to convert data types of variables (e.g. integer --> string)

#### Methods
Python has many built in functions called methods. They are used by typing a "." at the end of a variable. In pycharm, doing this will bring up a menu listing all the methods available to you. 

![image](https://user-images.githubusercontent.com/110176257/182266282-8089c67d-d76c-4925-a8c4-04450a336498.png)

In the example code below a method, `.upper()` is used to make sure any data entered in the "postcode" variable is displayed back correctly in all caps.
```
postcode = "nn14hw"
print(postcode.upper())
```


#### Casting
Casting is the conversion of the type of data stored in a varaible. It is done by adding the prefix of your desired datatype before the variable, and putting the varaible in brackets after the prefix. For example, in the code below the data in variable "age" is cast from a string into an integer in order to allow it to be compared to the integer value of 18:
```
# The data stored in age is a string
age = "47"
# age is converted into an integer by "int()"
legal_alcohol_check = (int(age) >= 18)
print(legal_alcohol_check)
``` 
*note: in the above code, a **comparative operator** is used to check if the value of age is greater than or equal to 18. It retuns a boolean true or false value.



## the following code uses concatenation, methods, and casting
```
# introduction
print("hello user") 
# asks for first name and allows user to input
firstname = input("please enter your first name: ") 
# asks for last name
lastname = input("please enter your last name: ")

#concatenates first and last name, uses .capitalize method to make sure first letters pf name are capitals
name = (firstname.capitalize()  + " " + lastname.capitalize())
print("hello, " + name) #greeting user

# asks user for address details to later concatenate
street_name = input("please enter your street name: ") 
house_number = input("please enter your house number: ")
postcode = input("please enter your postcode: ")

# asks for course and salary
salary = input("what is your salary? ") 
course = input("what course are you taking? ") 

# casts house number into a string for allowing concatenation with + sign, also uses .upper method to convert it all into capitals
address = (str(house_number) + " " + street_name.upper() + ", " + postcode.upper())

print(name +"'s address is: " + address)

print(name + " is taking the " + course + " " + "course, which pays you a salary of: " + str(salary))

```
Here is an example of the above code being run with user inputs:

![image](https://user-images.githubusercontent.com/110176257/182269724-26c70111-d0e9-498e-b6d2-a74c9e9e9fac.png)

You can see that the name which was entered seperately and with incorrect grammar has been corrected to have capitals at the start of each name using the `.capitalize` method and has been concatinated into a single string. It also shows that the integer value of `house_number` has been cast as a string by the `str()` prefix, and has been concatinated with the `street_name` and `postcode` to form a single `address` string variable.


## String Indexing 
String indexing refers to the numerical order value of the characters in a string, for example `"Hello"` indices are: 
- H=0 
- e=1 
- l=2 
- l=3 
- o=4

as you can see above, strings are indexed starting with 0

When you add indices in your print statement it will only print from where you have specified in the string, for example:
This code
```
greeting = "Hello World!"
print(greeting[4:])
print(greeting[7:-2])
print(greeting[:6])
```
will return:
```
o World!
orl
Hello 
```

### Creating a gitignore file in Pycharm.
In order to create a gitignore file, you simply have to right click on your project folder in pycharm, select new, and select file.
![image](https://user-images.githubusercontent.com/110176257/182268126-baac5009-0fac-4d12-8b38-74337aa79f1f.png)

Next you will have to name it as `.gitignore`
`*.file`	All files withe .file extention will be ignored by push
`*name/`	All folders ending with "name" will be ignored by push


## Definition of Ready (DoR)
- All acceptance critera have been met:

![image](https://user-images.githubusercontent.com/110176257/182269434-31bedc26-097e-4623-b99d-f652056af3e9.png)


## Definition of Done (DoD)
- The task is ready to be shown and explained in the morning stand up

