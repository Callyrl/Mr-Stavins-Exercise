string = input("Enter a string:")
def findlist(x,lists):
    for i in range(len(lists)):
        if x == lists[i]:
            return i

def countletter(string):
    alphabets = []
    val = []
    for i in string:
        if i not in alphabets:
            alphabets.append(i)
            val.append(1)
        else:
            x = findlist(i, alphabets)
            val[x]+=1
    for i in range(len(alphabets)):
        print(alphabets[i],"=",val[i])
                
countletter(string)