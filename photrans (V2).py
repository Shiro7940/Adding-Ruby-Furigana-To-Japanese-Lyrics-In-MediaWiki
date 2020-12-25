from furigana.furigana import *  # https://github.com/MikimotoH/furigana
import pyperclip

def linenum(filename):
   text = open(filename,"rb") #filename
   num = 0
   total = 0
   for line in text : 
      line = line.decode("utf-8")
      total += 1
      if len(line) >= 3:
         num += 1
      elif len(line) < 3:
         print(num,end=" ")
         num=0
   print(num)
   print("Total: "+str(total))
   txt.close()

def reph():   
   txt = open("test2.txt","rb") #filename
   x = "{{Photrans|"  #prefix
   z = "}}"           #suffix
   c = "|"            #separator
   all_str = ""
   for line in txt : 
      line = line.decode("utf-8")
      string = line
      string=string.replace( '<ruby><rb>',x )
      string=string.replace( '</rb><rt>',c )
      string=string.replace( '</rt></ruby>',z )
      string=string.replace( '<br />',"" )
      string=string.replace( '</div>',"" )
      all_str+=string
   print(all_str,end="")
   pyperclip.copy(all_str)
   txt.close()
   
def repu():
   x = "{{Photrans|"  #prefix
   z = "}}"           #suffix
   c = "|"            #separator
   txt = open("test2.txt","rb") #filename
   all_str = ""
   for line in txt : 
      line = line.decode("utf-8")
      string = line
      string = string.replace( '<span class="ruby"><span class="rb">',x )
      string = string.replace( '</span><span class="rt">',c )
      string = string.replace( '</span></span>',z )
      string = string.replace( '<br />',"" )
      string = string.replace( '</div>',"" )
   all_str += string
   print(all_str,end="")  
   pyperclip.copy(all_str)
   txt.close()

txt = open("test.txt","r",encoding="utf-8")
for line in txt : 
   try:
      print_html(line)
   except:
      string = ""
      
txt.close()