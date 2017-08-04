baseemail = input("Please input your email before the '@': ")
domain = input("Please Enter your domain part after the @: ")
choosing = True
while choosing:
    try:
        numberofemail = input("Please enter how many emails you want: ")
        numberofemail = int(numberofemail)
        if type(numberofemail) == int:
            choosing = False
    except (TypeError, ValueError):
        print("Make sure you type a number")
for i in range(numberofemail):
    print(baseemail + "+" + str(i) + "@" + domain)
