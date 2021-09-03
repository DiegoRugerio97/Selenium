#In Python we can use try...except...finally blocks of code to deal with errors and exceptions.

lines=[]

# If we have suspicions of an error ocurring in run time we can put that block of code inside a try.
# This way if the program fails, it won't stop abruptly, control of the program will be passed on to the code on the
# except block
# text.txt doesn't exist, without a try...except block, script would encounter an exception and immediately crash.
try:
    with open('text.txt','r') as file:
        lines = file.readlines()

# With except block we can catch that exception and continue the program.
except Exception as e:
    print("File not found")
    #Printing the information of the exception
    print(e)

# finally block of code will run regardless of an exception ocurring.
finally:
    print("Finally block of code!")
    print(len(lines))

#It is possible to assert certain conditions and raise an exception if these aren't met.

assert(len(lines) != 0)

#We can also raise custom exceptions

if len(lines) == 0:
    raise print("Couldn't read any lines")

