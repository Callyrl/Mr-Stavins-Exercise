#%%
p1 = input("Enter your name:")
p2 = input("Enter your name:")
print("Welcome! let's play family feud!")
    
p1score = 0
p2score = 0
    
def q1():
    global p1score
    global p2score
    answers = {"javascript" : 75, "html" : 50, "python" :35, "C++" : 25, "Basics" : 15}    
    anscopy = answers.copy()
    p1ans = input("Enter answer:")
    if p1ans in anscopy:
        p1score += answers[p1ans]
        anscopy.pop(p1ans)
        #print(anscopy)
        p2ans = input("Enter answer:")
        if p2ans in anscopy:
            p2score += answers[p2ans]
            anscopy.pop(p2ans)
        else:
            print("Answer not valid.")
    else:
        print("Answer is not valid")  


def q2(): 
    global p1score
    global p2score
    answers = {"pen" : 75, "pencil" : 50, "highlighter" :35, "eraser" : 25, "ruler" : 15} 
    anscopy = answers.copy()
    p1ans = input("Enter answer:")
    if  p1ans in anscopy:
        p1score += answers[p1ans]
        anscopy.pop(p1ans)
        p2ans = input("Enter answer:")
        if p2ans in anscopy:
            p2score += answers[p2ans]
            anscopy.pop(p2ans)
        else:
            print("Answer not valid.")
    else:
        print("Answer is not valid") 
        
def q3():
    global p1score
    global p2score
    answers = {"heart" : 75, "brain" : 50, "lungs" :35, "eyes" : 25, "skin" : 15}    
    anscopy = answers.copy()
    p1ans = input("Enter answer:")
    if  p1ans in anscopy:
        p1score += answers[p1ans]
        anscopy.pop(p1ans)
        p2ans = input("Enter answer:")
        if p2ans in anscopy:
            p2score += answers[p2ans]
            anscopy.pop(p2ans)
        else:
            print("Answer not valid.")
    else:
        print("Answer is not valid") 
         
def q4():
    global p1score
    global p2score
    answers = {"facebook" : 75, "instagram" : 50, "whatsapp" :35, "line" : 25, "twitter" : 15} 
    anscopy = answers.copy()
    p1ans = input("Enter answer:")
    if  p1ans in anscopy:
        p1score += answers[p1ans]
        anscopy.pop(p1ans)
        p2ans = input("Enter answer:")
        if p2ans in anscopy:
            p2score += answers[p2ans]
            anscopy.pop(p2ans)
        else:
            print("Answer not valid.")
    else:
        print("Answer is not valid") 
            
def q5():
    global p1score
    global p2score
    answers = {"sleep" : 75, "eat" : 50, "game" :35, "watch" : 25, "read" : 15} 
    anscopy = answers.copy()
    p1ans = input("Enter answer:")
    if  p1ans in anscopy:
        p1score += answers[p1ans]
        anscopy.pop(p1ans)
        p2ans = input("Enter answer:")
        if p2ans in anscopy:
            p2score += answers[p2ans]
            anscopy.pop(p2ans)
        else:
            print("Answer not valid.")
    else:
        print("Answer is not valid") 
  

def qna():
    Questions =["Name 1 famous programming language you know:", "Name 1 common stationary:", "Name 1 major organ in your body", "Name 1 common social media:", "What do people do when they are bored?"]
    for q in range(len(Questions)):
        if q == 0:
            print(Questions[q])
            q1()
        elif q == 1:
            print(Questions[q])
            q2()
        elif q == 2:
            print(Questions[q])
            q3()
        elif q == 3:
            print(Questions[q])
            q4()
        else:
            print(Questions[q])
            q5()
            
def winner():
    if p1score >= 200 and p1score > p2score:
        print ("The winner is: ", p1)
    elif p2score >= 200 and p2score > p1score:
        print ("The winner is: ", p2)

 

qna()
winner()
print ("Thanks for playing!")


