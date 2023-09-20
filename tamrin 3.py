numbers=[]
i=1
while i != 0:
    i=int(input("Enter number: "))
    if i != 0:
        numbers.append(i)
print(numbers)
print(len(numbers))
numbers.sort()
max_number1= i-1
max_number2= i-2
print(numbers[max_number1])
print(numbers[max_number2])