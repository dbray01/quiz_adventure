# Our quiz!

score = 0

def quiz():
    global score

    name = input ("Enter your name: ")
    score = 0

    question1()
    question2()
    question3()
    

    print(name + ":", score)




    
def question1():
    global score
    
    print("What company is the richest in the world?")
    print("A.Asda (Walmart)")
    print("B.Apple") 
    print("C.Google")
    print("D.Microsoft")
    print("E.Sony") 

    answer = input("Answer: ")

    if answer.upper() == "A":
          score = score+1
          print("Well done.")

    else:
        print("Incorrect")

def question2():
    global score
    
    print("Which FaZe member is the shortest?")
    print("A.Temperr")
    print("B.Rain")
    print("C.Blaziken")
    print("D.Apex")
    print("E.Censor")

    answer = input("Answer: ")

    if answer.upper() == "D":
        score = score+1
        print("Apex is short")

    else:
        print("Apex is short")

def question3():
    global score
    
    print("What pasta dish is the best?")
    print("A.Lasagne")
    print("B.Spaghetti") 
    print("C.Carbonara")
    print("D.Mac n' Cheese")
    print("E.Ravioli") 

    answer = input("Answer: ")


    if answer.upper() == "A":
          score = score+1
          print("Well done")

    else:
        print("If you didn't pick lasange. Seek medical guidance.")





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
