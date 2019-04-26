
#=========================ex9================================#
#本章要点如下：#
#1. \n 可进行换行
#2. “”“” 可进行多行打印
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like. Even 4 lines if we want, or 5, or 6.
""")

#=========================ex10================================#
#本章要点如下：
#1. \n 可进行换行
#2. “”“” 三引号
#3、\t的用法
#4、\\双反斜杠(double back-slash)这两个字符组合会打印出一个反斜杠
  

"I am 6'2\" tall." # 将字符串中的双引号转义 
'I am 6\'2" tall.' # 将字符串种的单引号转义

tabby_cat = "\tI'm tabbed in." 
persian_cat = "I'm split\non a line." 
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """ I'll do a list: 
\t* Cat food 
\t* Fishies
\t* Catnip\n
\t* Grass """

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#=========================ex11================================#
#本章要点如下：
#1. input

print("How old are you?"), #放逗号

age = input()

print("How tall are you?",) #内部放逗号

height = input()

print("How much do you weight?")#不放逗号

weight = input()

print("So, you're %r old, %r tall and %r heavy." %( age, height, weight))




