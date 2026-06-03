import random 


kanji = {

    "一" : "one",
    "二" : "two",
    "三" : "three",
    "四" : "four",
    "五" : "five",
    "六" : "six", 
    "七" : "seven",
    "八" : "eight",
    "九" : "nine",
    "十" : "ten",
    "百" : "hundred",
    "千" : "thousand",
    "万" : "ten thousand",
    "日" : "sun",
    "月" : "moon",
    "火" : "fire",
    "水" : "water",
    "木" : "tree",
    "金" : "gold",
    "土" : "soil",
    "本" : "book",
    "語" : "language",
    "人" : "person",
    "女" : "woman",
    "男" : "man",
    "子" : "child",
    "友" : "friend",
    "国" : "country",
    "学" : "study",
    "校" : "school",
    "小" : "small",
    "大" : "big", 
    "少" : "few",
    "多" : "many",
    "時" : "hour",
    "分" : "minute",
    "年" : "year",
    "名" : "name",
    "前" : "in front",
    "後" : "behind",
    "山" : "mountain",
    "川" : "river",
    "花" : "flower",
    "魚" : "fish",
    "上" : "above",
    "中" : "inside",
    "下" : "below",
    "左" : "left",
    "右" : "right",
    "外" : "outside",
    "雨" : "rain", 
    "電" : "electricity",
    "天" : "sky",
    "店" : "store",
    "手" : "hand",
    "古" : "old",
    "新" : "new",
    "買" : "buy",
    "生" : "live",
    "午" : "noon",
    "口" : "mouth",
    "入" : "enter",
    "出" : "exit", 
    "長" : "long",
    "高" : "tall",
    "円" : "yen",
    "北" : "north", 
    "南" : "south",
    "東" : "east",
    "西" : "west",
    "食" : "eat",
    "飲" : "drink",
    "駅" : "station",
    "目" : "eye",
    "見" : "watch", 
    "耳" : "ear",
    "聞" : "listen",
    "足" : "foot",
    "行" : "go",
    "来" : "come",
    "社" : "company",
    "休" : "rest",
    "車" : "car",
    "道" : "road",
    "空" : "air",
    "言" : "word",
    "話" : "talk",
    "読" : "read",
    "母" : "mother",
    "父" : "father",
    "毎" : "every",
    "気" : "feeling",
    "白" : "white",
    "何" : "what",
    "週" : "week", 
    "間" : "between",
    "半" : "half",
    "今" : "now"

}

print("All N5 kanji")
print("If you want to quit enter 'quit'")
print("はじめまして")
print("")

t = 0
while True:
    
    b = list(kanji.keys()) # random.sample requires sequesce so keys are in list form for sequence
    c = list(kanji.values())

    if b == [] : # this shows when list is blank exit 
        break


    option = (random.sample(b, 1)[0]) # this returns list for it to be string we give that one element a index so now its data type is str
    print(option)
            
            
    mean = str(input("Enter meaning: "))
    mean = mean.lower()
    

    if mean == "quit":
        break
    

    def meaning():
        i = 0
        while i < len(c):
            c[i] = str(c[i])
            if c[i] == mean:
                return(i)
            i += 1
        return()

    def kanji_index():
        i = 0
        while i < len(b):
            b[i] = str(b[i])
            if b[i] == option:
                return(i)
            i += 1
        return()
    
    
    if kanji_index() == meaning() :
        print("correct")
    else:
        print("failure")
        print("correct ans is ", kanji[option])

    
    if kanji_index() == meaning() :
        t += 1
    
    print("score: ",t)
    print("")
    
    del kanji[option] # this is so kanji wont repeat


    
    

   