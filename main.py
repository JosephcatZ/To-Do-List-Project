import sys

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])
todo = []
def update(TODO):
    Max = 0
    global todo
    for i in TODO:
        if i[len(i)-1] == "\n":
            i = i[0:len(i)-1]
        i = " "+i 
        todo.append(i)
        Max+=1
    return(Max)
on = 0
with open("List.txt","r+") as TODO:
    Max = update(TODO)
m = 0
def drawScreen():
    gotten = False
    on = 0
    for i in todo:
        global m
        if i[0] == strike("hi")[0]:
            print(i)
        elif gotten == False:
            m = 1
            print(i)
            gotten = True
        else:
            return(on)
        on += 1
        



def onFrame():
    global on
    global Max
    i = input()
    if i[0:3].lower()=="add":
        file1 = open("List.txt","a")#write mode 
        file1.write("/n"+str(Max+1)+". "+i[4:len(i)])
        todo.append(str(Max+1)+". "+i[4:len(i)])
        file1.close() 
        Max += 1
        
    elif i[0:4].lower()=="done":
        if on+1 < len(todo):
            z = todo[on+1]
            todo[on+1] = strike(z[1:len(z)])
            on += 1
    
    elif i[0:5].lower()=="save":
        List = open("List.txt","w")
        List.write("")
        List.close
        List = open("List.txt","a")
        for i in todo:
            List.write(i+"\n ")
    else:
        return(0)
    drawScreen()
drawScreen()
while True:
    onFrame()
