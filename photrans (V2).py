from furigana.furigana import *  # https://github.com/MikimotoH/furigana
import pyperclip
        


def save(filename, contents): 
    file = open(filename, 'w',encoding="utf-8") 
    file.write(contents) 
    file.close() 
    
ranges = [{"from": ord(u"\u4e00"), "to": ord(u"\u9fff")}  ]
def is_cjk(char):
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])


def cjk_substrings(string):
    i = 0
    while i<len(string):
        if is_cjk(string[i]):
            start = i
            while is_cjk(string[i]): i += 1
            yield string[start:i]
        i += 1

def linenum(filename):
    try:
        text = open(filename,"rb") #filename
        num = 0
        total = 0
        emptylst = []
        for line in text :
            line = line.decode("utf-8")
            total += 1
            if len(line) >= 3:
                num += 1
            elif len(line) < 3:
                print(num,end=" ")
                emptylst.append(total)
                num=0
        print(num)
        print("Empty: " + str(emptylst))
        print("Total: " + str(total))
        txt.close()
    except:
        print("File not found")

def has_kana(string):
    for char in string:
        if 0x3040 < ord(char) <= 0x30FF:
            return True
    return False
    
def colors(txt:str,colors:list):
    txt = open(txt,"r",encoding="utf-8")
    i=0
    all_lines = ""
    for line in txt : 
        line = "{{color|"+str(colors[i])+"|"+line[:-1]+"}}\n"
        i += 1
        if i == len(colors):
            i = 0
        all_lines += line
    print(all_lines)
    pyperclip.copy(all_lines)
    txt.close()

def reph():   
    txt = open("test2.txt","rb") 
    x = "{{Photrans|"
    z = "}}" 
    c = "|" 
    all_str = ""
    for line in txt : 
        line = line.decode("utf-8")
        string = line
        string = string.replace( CHARA,'' )
        string = string.replace( '<sp>',' ' )
        string = string.replace( '<ruby><rb>',x )
        string = string.replace( '</rb><rt>',c )
        string = string.replace( '</rt></ruby>',z )
        string = string.replace( '<br />',"" )
        string = string.replace( '</div>',"" )
        all_str += string
    print(all_str,end="")
    pyperclip.copy(all_str)
    txt.close()
   
def repb():
    x = "{{Photrans|"  
    z = "}}"           
    c = "|"   
    try:
        bracket_type=int(input("Input bracket type: "))
    except:
        bracket_type=0
    if bracket_type>0:
        a = "（"
        b = "）"
    else:
        a = "("
        b = ")"
    txt = open("test2.txt","rb") 
    all_str = ""
    for line in txt : 
        line = line.decode("utf-8")
        string = line
        if EXEMPT in string:
            string = CHARA+string        
        if has_kana(string) and (CHARA not in string):
            for sub in cjk_substrings(string):
                string = string.replace(sub, x + sub)
                string = string.replace(a, c)
                string = string.replace(b, z)
                string = string.replace(x+x, x)
        else:
            string = string.replace(CHARA, "")
        all_str += string
    print(all_str,end="")
    pyperclip.copy(all_str)
    txt.close()
                
def repu():
    x = "{{Photrans|" 
    z = "}}" 
    c = "|" 
    txt = open("test2.txt","rb") 
    all_str = ""
    for line in txt: 
        line = line.decode("utf-8")
        string = line
        string = string.replace( CHARA,'' )
        string = string.replace( '<sp>',' ' )
        string = string.replace( '<span class="ruby"><span class="rb">',x )
        string = string.replace( '</span><span class="rt">',c )
        string = string.replace( '</span></span>',z )
        string = string.replace( '<br />',"" )
        string = string.replace( '</div>',"" )
        all_str += string
    print(all_str,end="")  
    pyperclip.copy(all_str)
    txt.close()

def getu(url:str,mode=None):
    import urllib.request
    romaji = 'class="romaji"'
    stop = "        </div>"
    gana = 'class="hiragana"'
    if mode == "g" or mode == None:
        start = gana
    else:
        start = romaji
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers) 
    a = urllib.request.urlopen(request)
    html = a.read()              
    html = html.decode("utf-8") 
    html = str(html)
    save("temp.txt",html)
    lyrics = ""
    count = False
    temp = open("temp.txt","rb")
    for line in temp:
        line = line.decode("utf-8")
        if stop in line:
            count = False
        if count == True:
            line = line.replace("          ","")
            line = line.replace("\r","")
            line = line.replace("<br />","")
            line = line.replace("        </div>","")
            lyrics+=line
        if start in line:
            count = True
    temp.close()
    save("temp.txt",lyrics)
    x = "{{Photrans|" 
    z = "}}" 
    c = "|" 
    txt = open("temp.txt","rb") 
    all_str = ""
    for line in txt: 
        line = line.decode("utf-8")
        string = line
        string = string.replace( CHARA,'' )
        string = string.replace( '?','？' )
        string = string.replace( '!','！' )
        string = string.replace( '<sp>',' ' )
        string = string.replace( '<span class="ruby"><span class="rb">',x )
        string = string.replace( '</span><span class="rt">',c )
        string = string.replace( '</span></span>',z )
        string = string.replace( '<br />',"" )
        string = string.replace( '</div>',"" )
        all_str += string
    print(all_str,end="")  
    pyperclip.copy(all_str)
    txt.close()    


CHARA = "^"
EXEMPT = "交叉颜色"
def pt():
    txt = open("test.txt","r",encoding="utf-8")
    for line in txt : 
        try:
            if CHARA not in line: #and has_kana(line):
                line = line.replace( ' ','<sp>' )
                print_html(line)
            else:
                print(line,end="")
        except:
            pass
        
    txt.close()
