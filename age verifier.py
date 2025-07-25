try:
    age = int(input("Enter your age:"))

    if age < 18:
        print("you are under-age")
    elif age >= 60:
        print("you are senior citizen")
    else:
        print("you are an adult") 
    
    
except ValueError:
    print("this input is not valid")
    