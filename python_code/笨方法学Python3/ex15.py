#本章要点如下： 
#1. from sys :模组(modules) | 库 (libraries), 把sys模组 import 进来
#2. import ：这是将python的功能引入脚本的方法. 要什么就调用什么,“import”可以作为提示，明白代码用到了哪些功能。
#3. argv  ：是所谓的“参数变量(argument variable)”，这个变量包含了传递给Python的参数。
#4. open(*) 打开文件
#5. *.read() 读取打开的文件
#6. python3 ex15.py ****.text

from sys import argv

##传参获取文件名
script, fileName = argv
##打开文件
text = open(fileName)
##打印文件名
print("Here's your file %r:"%fileName)
##读取文件内容
print(text.read())

print("Type the filename again:")
##输入文件名
file_again = input("> ")
##再次打开文件
txt_again = open(file_again)
##打印打开文件
print(txt_again.read())

text.close()