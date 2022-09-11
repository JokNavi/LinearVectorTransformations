def WrongWay():
    Gender = input()
    if Gender == "Male":
        print("You are a Male!")
    else:
        print("You are a Female!") 

def RightWay():
    Gender = input()
    if Gender == "Male":
        print("You are a Male!")
    elif Gender == "Female":
        print("You are a Female!")
    else: 
        print("wrong input")
RightWay()