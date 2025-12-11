print("Enter your name")
a = input()
print("enter if you want the dialog to be formal y/n")
b = input()
if b == 'y':
    formal = True
    print(f"The pleasure is mine, {a}")
else:
    formal = False
    print(f"Hi, {a}!")
