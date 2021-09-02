
elements = [100,5,10,25,50,15,125,24,1251,64,70]
largestElements = []

for i in range (3):
    maxValue = max(elements)
    print(maxValue)
    largestElements.append(maxValue)
    elements.remove(maxValue)

print("Largest elements of array are: ")
print(largestElements)