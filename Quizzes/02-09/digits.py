
try:
    number = int(input("Give number: "))
except:
    print("Input must be a number")

digit = 0
digitList = []

print("The digits or the number {} are :".format(number))

while number > 0:
    digit = number % 10
    digitList.append(digit)
    number = number // 10

print(digitList[::-1])
