# -*- coding:utf-8 -*-
'''
This is a script for creating Japanese lyric furigana in MoegirlPedia
(https://zh.moegirl.org.cn/) or any Mediawiki site you want. 
This script is written by a Python beginner.
You have to modify the prefix and suffix to suit your own need.
In regular MediaWiki you may want to use {{ruby|word|read}}

IMPORTANT NOTICE: 
ALL THE FURIGANA GENERATED BY THE SCRIPT NEED MANUAL CHECKING.

Since the context info was lost because of the program design,
MeCab sometimes cannot generate appropriate furigana.
But it is quite a relief compared to manually adding furigana.
You can copy the generated lyrics from the console.
'''

'''
ranges = [
  {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
  {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
  {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
  {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
  #{'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
  #{"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
  {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
  {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
  {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
  {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
  {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
  {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
  {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
]
#Complementary unicode sets
'''
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

def k2h(input_str_k):
    input_str_k = str(input_str_k
        .replace ( 'ア','あ' )
        .replace ( 'イ','い' )
        .replace ( 'ウ','う' )
        .replace ( 'エ','え' )
        .replace ( 'オ','お' )
        .replace ( 'カ','か' )
        .replace ( 'キ','き' )
        .replace ( 'ク','く' )
        .replace ( 'ケ','け' )
        .replace ( 'コ','こ' )
        .replace ( 'サ','さ' )
        .replace ( 'シ','し' )
        .replace ( 'ス','す' )
        .replace ( 'セ','せ' )
        .replace ( 'ソ','そ' )
        .replace ( 'タ','た' )
        .replace ( 'チ','ち' )
        .replace ( 'ツ','つ' )
        .replace ( 'テ','て' )
        .replace ( 'ト','と' )
        .replace ( 'ナ','な' )
        .replace ( 'ニ','に' )
        .replace ( 'ヌ','ぬ' )
        .replace ( 'ネ','ね' )
        .replace ( 'ノ','の' )
        .replace ( 'ハ','は' )
        .replace ( 'ヒ','ひ' )
        .replace ( 'フ','ふ' )
        .replace ( 'ヘ','へ' )
        .replace ( 'ホ','ほ' )
        .replace ( 'マ','ま' )
        .replace ( 'ミ','み' )
        .replace ( 'ム','む' )
        .replace ( 'メ','め' )
        .replace ( 'モ','も' )
        .replace ( 'ヤ','や' )
        .replace ( 'ユ','ゆ' )
        .replace ( 'ヨ','よ' )
        .replace ( 'ラ','ら' )
        .replace ( 'リ','り' )
        .replace ( 'ル','る' )
        .replace ( 'レ','れ' )
        .replace ( 'ロ','ろ' )
        .replace ( 'ワ','わ' )
        .replace ( 'ヲ','を' )
        .replace ( 'ン','ん' )
        .replace ( 'ガ','が' )
        .replace ( 'ギ','ぎ' )
        .replace ( 'グ','ぐ' )
        .replace ( 'ゲ','げ' )
        .replace ( 'ゴ','ご' )
        .replace ( 'ザ','ざ' )
        .replace ( 'ジ','じ' )
        .replace ( 'ズ','ず' )
        .replace ( 'ゼ','ぜ' )
        .replace ( 'ゾ','ぞ' )
        .replace ( 'ダ','だ' )
        .replace ( 'ヂ','ぢ' )
        .replace ( 'ヅ','づ' )
        .replace ( 'デ','で' )
        .replace ( 'ド','ど' )
        .replace ( 'バ','ば' )
        .replace ( 'ビ','び' )
        .replace ( 'ブ','ぶ' )
        .replace ( 'ベ','べ' )
        .replace ( 'ボ','ぼ' )
        .replace ( 'パ','ぱ' )
        .replace ( 'ピ','ぴ' )
        .replace ( 'プ','ぷ' )
        .replace ( 'ペ','ぺ' )
        .replace ( 'ポ','ぽ' )
        .replace ( 'ァ','ぁ' )
        .replace ( 'ィ','ぃ' )
        .replace ( 'ゥ','ぅ' )
        .replace ( 'ェ','ぇ' )
        .replace ( 'ォ','ぉ' )
        .replace ( 'ャ','ゃ' )
        .replace ( 'ュ','ゅ' )
        .replace ( 'ョ','ょ' )
        .replace ( 'ッ','っ' )
        .replace ( 'ヮ','ゎ' )
               )
    return input_str_k
#A dumb replace function.




import MeCab
mecab = MeCab.Tagger ("-Oyomi")


yomi = ""
x = "{{Photrans|"  #prefix
z = "}}"           #suffix
c = "|"            #separater
txt = open("test.txt","rb") #filename

for line in txt : 
  line = line.decode("utf-8")
  string = line
  for sub in cjk_substrings(string):
    string = string.replace(sub, x + sub + z)
    if x+x+x+x or z+z+z+z in string:    #Idk why I have to write like this
      string = string.replace(x+x+x+x, x) #but it just works.
      string = string.replace(z+z+z+z, z)  #Sometimes it will have excessive
      if x+x+x or z+z+z in string:          #generated things, remove them manually.
        string = string.replace(x+x+x, x)
        string = string.replace(z+z+z, x) 
        if x+x or z+z in string: 
          string = string.replace(x+x, x)
          string = string.replace(z+z, z)
          yomi = mecab.parse(sub)
          yomi = yomi.join(yomi.split())
          yomi = k2h(yomi)
          string = string.replace(x+sub+z, x+sub+c+yomi+z)   
            
  print(string,end="")
            
txt.close()
#Make sure to check the generated lyric with furigana.
#At least 20% of the furigana is wrong and need manual correction!
