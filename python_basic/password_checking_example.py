# The Password Checking Example
for x in range(4):
    password = input("Enter Pass: ")
    if password == "123#@2":
        break
    print("Error, This is not correct ... Try again!")
else:
    print("The process is completed. Thanks!")
