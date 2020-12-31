#import re

txt = open("test3.txt","r",encoding="utf-8")
rbnum=[]
lbnum=[]
rbcolor=[]
lbcolor=[]
lb=[]
rb=[]
i=0
c=0
x=0
y=0
z=0
txtlst=["null"]
for line in txt:
    txtlst.append(str(line))
    
for item in txtlst:
    if "lb-text" in item:
        lbnum.append(i)
    if "rb-text" in item:
        rbnum.append(c) 
        
    i+=1
    c+=1    
rbnum.append(c)    


for item in txtlst:
    if "lb-color" in item:
        lbcolor.append(item)  
    if "rb-color" in item:
        rbcolor.append(item) 

print(lbcolor)
print(rbcolor)
'''        
i=0
a="#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
a=re.compile(a)
b=re.compile("=([A-z]+)")
for item in lbcolor:
    s=re.findall(a,item)
    if (len(s)) == 0:
        s=re.findall(b,item)
    print(s)
    lbcolor[i]=s[0]
    i+=1
i=0
for item in rbcolor:
    s=re.findall(a,item)
    if (len(s)) == 0:
        s=re.findall(b,item)
    print(s)
    rbcolor[i]=s[0]
    i+=1

'''
color=input("Have color: ")#""
if color == "":
    while x in range(len(rbnum)-1):
        lb+=txtlst[lbnum[x]:rbnum[x]]
        lb+=["\n"]
        x+=1
    
    while y in range(len(lbnum)-1):
        rb+=txtlst[rbnum[y]:lbnum[y+1]]
        rb+=["\n"]
        y+=1
    rb+=txtlst[rbnum[-2]:rbnum[-1]]
    
    for sentence_rb in rb:
        if "lb-color" in sentence_rb:
            rb.pop(z)
        if "rb-text" in sentence_rb:
            rb.pop(z)        
        z+=1
    if rb[-1] == "}}":
        rb.pop(-1)

    z=0
    for sentence_lb in lb:
        if "lb-text" in sentence_lb:
            lb.pop(z)
        if "rb-color" in sentence_lb:
            lb.remove(sentence_lb)        
        z+=1
    z=0

        
    print("{{LyricsKai")
    print("|lstyle=color:#000;|rstyle=color:#000;")
    print("|original=")
    for line_lb in lb:
        print(line_lb,end="")   
    print("|translated=")
    for line_rb in rb:
        print(line_rb,end="")
    print("}}")
    
else:
    while x in range(len(rbnum)-1):
        lb+=txtlst[lbnum[x]:rbnum[x]]
        lb+=["\n"]
        x+=1
    
    while y in range(len(lbnum)-1):
        rb+=txtlst[rbnum[y]:lbnum[y+1]]
        rb+=["\n"]
        y+=1
    rb+=txtlst[rbnum[-2]:rbnum[-1]]
    
    z=0
    k=1
    while z in range(len(rb)-1):
        if "rb-text" in rb[z]:
            rb.pop(z)
        if "|lb-c" in rb[z]:
            rb.pop(z)    
        if (rb[z] == "\n"):
            k+=1        
        if ("{{color|" not in rb[z]) and (rb[z] != "\n"):
            rb[z]=rb[z].replace("\n","")
            rb[z]="{{color|#00"+str(k)+"r|"+str(rb[z])+"}}\n"
        z+=1
    if rb[-1] == "}}":
        rb.pop(-1)
        
    z=0
    k=1
    while z in range(len(lb)-1):
        if "lb-text" in lb[z]:
            lb.pop(z)
        if "|rb-c" in lb[z]:
            lb.pop(z)    
        if (lb[z] == "\n"):
            k+=1
        if ("{{color|" not in lb[z]) and (lb[z] != "\n"):
            lb[z]=lb[z].replace("\n","")
            lb[z]="{{color|#00"+str(k)+"l|"+str(lb[z])+"}}\n"
        z+=1
        
    print("{{LyricsKai")
    print("|lstyle=color:#000;|rstyle=color:#000;")
    print("|original=")
    for line_lb in lb:
        print(line_lb,end="")   
    print("|translated=")
    for line_rb in rb:
        print(line_rb,end="")
    print("}}")
