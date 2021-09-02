
evaluationString = "940 These are letters 123 460 String ###!!!***"
specialCharacters = "!#$%&/()='¡_:[]¨*?{@}¿"
digits = 0
chars = 0
spaces = 0
specChars = 0

for c in evaluationString:
    if c in specialCharacters:
        specChars += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
    else:
        chars +=1
    
print("Digits in string: {}".format(digits))
print("Spaces in string: {}".format(spaces))
print("Letters in string: {}".format(chars))
print("Special Characters in string: {}".format(specChars))