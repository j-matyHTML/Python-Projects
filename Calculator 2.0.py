print("Hello welcome to calculator 2.0")

num1 = input("Enter number one")

print("Chose a operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operation = input("Please enter opearation 1,2,3,4")

num2 = input("Enter number two")

while True:
    if operation == '1':
        result1 = float(num1) + float(num2)
        print(result1)
    elif operation == '2':
        result2 = float(num1) - float(num2)
        print(result2)
    elif operation == '3':
        result3 = float(num1) * float(num2)
        print(result3)
    elif operation == '4':
        result4 = float(num1) / float(num2)
        print(result4)
    break

