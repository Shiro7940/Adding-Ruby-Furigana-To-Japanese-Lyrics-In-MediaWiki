from furigana.furigana import *  # https://github.com/MikimotoH/furigana
import pyperclip

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

def has_kana(string):
    aa = ("ア"in string) or ("イ"in string) or ("ウ"in string) or ("エ"in string) or ("オ"in string) or ("あ"in string) or ("い"in string) or ("う"in string) or ("え"in string) or ("お"in string)
    
    ka = ("カ"in string) or ("キ"in string) or ("ク"in string) or ("ケ"in string) or ("コ"in string) or ("か"in string) or ("き"in string) or ("く"in string) or ("け"in string) or ("こ"in string)
    
    sa = ("サ"in string) or ("シ"in string) or ("ス"in string) or ("セ"in string) or ("ソ"in string) or ("さ"in string) or ("し"in string) or ("す"in string) or ("せ"in string) or ("そ"in string)
    
    ta = ("た"in string) or ("ち"in string) or ("つ"in string) or ("て"in string) or ("と"in string) or ("タ"in string) or ("チ"in string) or ("ツ"in string) or ("テ"in string) or ("ト"in string)
    
    na = ("な"in string) or ("に"in string) or ("ぬ"in string) or ("ね"in string) or ("の"in string) or ("ナ"in string) or ("ニ"in string) or ("ヌ"in string) or ("ネ"in string) or ("ノ"in string)
    
    ha = ("ハ"in string) or ("ヒ"in string) or ("フ"in string) or ("ヘ"in string) or ("ホ"in string) or ("は"in string) or ("ひ"in string) or ("ふ"in string) or ("へ"in string) or ("ほ"in string)
    
    ma = ("ま"in string) or ("み"in string) or ("む"in string) or ("め"in string) or ("も"in string) or ("マ"in string) or ("ミ"in string) or ("ム"in string) or ("メ"in string) or ("モ"in string)
    
    ra = ("ら"in string) or ("り"in string) or ("る"in string) or ("れ"in string) or ("ろ"in string) or ("ラ"in string) or ("リ"in string) or ("ル"in string) or ("レ"in string) or ("ロ"in string)
    
    ya = ("や"in string) or ("ゆ"in string) or ("よ"in string) or ("ヤ"in string) or ("ユ"in string) or ("ヨ"in string) or ("ゃ"in string) or ("ゅ"in string) or ("ょ"in string) or ("ャ"in string) or ("ュ"in string) or ("ョ"in string) or ("ー"in string)
    
    ga = ("が"in string) or ("ぎ"in string) or ("ぐ"in string) or ("げ"in string) or ("ご"in string) or ("ガ"in string) or ("ギ"in string) or ("グ"in string) or ("ゲ"in string) or ("ゴ"in string)
    
    za = ("ざ"in string) or ("じ"in string) or ("ず"in string) or ("ぜ"in string) or ("ぞ"in string) or ("ザ"in string) or ("ジ"in string) or ("ズ"in string) or ("ゼ"in string) or ("ゾ"in string)
    
    da = ("だ"in string) or ("ぢ"in string) or ("づ"in string) or ("で"in string) or ("ど"in string) or ("ダ"in string) or ("ヂ"in string) or ("ヅ"in string) or ("デ"in string) or ("ド"in string)
    
    ba = ("ば"in string) or ("び"in string) or ("ぶ"in string) or ("べ"in string) or ("ぼ"in string) or ("バ"in string) or ("ビ"in string) or ("ブ"in string) or ("ベ"in string) or ("ボ"in string)
    
    pa = ("ぱ"in string) or ("ぴ"in string) or ("ぷ"in string) or ("ぺ"in string) or ("ぽ"in string) or ("パ"in string) or ("ピ"in string) or ("プ"in string) or ("ペ"in string) or ("ポ"in string)
    
    sp = ("わ"in string) or ("を"in string) or ("ん"in string) or ("ワ"in string) or ("ヲ"in string) or ("ン"in string) or ("ぁ"in string) or ("ぃ"in string) or ("ぅ"in string) or ("ぇ"in string) or ("ぉ"in string) or ("ァ"in string) or ("ィ"in string) or ("ゥ"in string) or ("ェ"in string) or ("ォ"in string) or ("っ"in string) or ("ゎ"in string) or ("ッ"in string) or ("ヮ"in string) or ("ヰ"in string) or ("ヱ"in string) or ("ゐ"in string) or ("ゑ"in string)
    
    return (aa or ka or sa or na or ta or ha or ma or ra or ya or ga or za or da or ba or pa or sp)

def reph():   
    txt = open("test2.txt","rb") #filename
    x = "{{Photrans|"  #prefix
    z = "}}"           #suffix
    c = "|"            #separator
    all_str = ""
    for line in txt : 
        line = line.decode("utf-8")
        string = line
        #string = string.replace( CHARA,'' )
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
    if bracket_type<=0:
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
    x = "{{Photrans|"  #prefix
    z = "}}"           #suffix
    c = "|"            #separator
    txt = open("test2.txt","rb") #filename
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

txt = open("test.txt","r",encoding="utf-8")
CHARA = "^"
EXEMPT = ""
for line in txt : 
    try:
        if CHARA not in line:
            line = line.replace( ' ','<sp>' )
            print_html(line)
        else:
            print(line,end="")
    except:
        string = ""
      
txt.close()
