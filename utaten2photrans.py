def linenum(filename):
   text=txt = open(filename,"rb") #filename
   num=0
   for line in text : 
      line = line.decode("utf-8")
      if len(line)>=3:
         num+=1
      elif len(line)<3:
         print(num,end=" ")
         num=0
   print(num)

x = "{{Photrans|"  #prefix
z = "}}"           #suffix
c = "|"            #separater
txt = open("test2.txt","rb") #filename

for line in txt : 
   line = line.decode("utf-8")
   string = line
   string=string.replace( '<span class="ruby"><span class="rb">',x )
   string=string.replace( '</span><span class="rt">',c )
   string=string.replace( '</span></span>',z )
   string=string.replace( '<br />',"" )
   string=string.replace( '</div>',"" )
   print(string,end="")