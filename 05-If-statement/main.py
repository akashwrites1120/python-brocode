
# if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age <=0:
    print("You are not born yet")
elif age >=18:
    print("You are now signed up!")
else:
    print("You are a minor therefore you can't sign up")