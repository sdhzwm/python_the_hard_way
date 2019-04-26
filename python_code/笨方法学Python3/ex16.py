from sys import argv

#本章要点如下： 函数和文件操作
#1. from sys :模组(modules) | 库 (libraries), 把sys模组 import 进来
#2. import ：这是将python的功能引入脚本的方法. 要什么就调用什么,“import”可以作为提示，明白代码用到了哪些功能。
#3. argv  ：是所谓的“参数变量(argument variable)”，这个变量包含了传递给Python的参数。
#4. open(*) 打开文件
#5. *.read() 读取打开的文件
#6. close() – 关闭文件。跟你编辑器的   一个意思。
#7. readline() – 读取文本文件中的一行。
#8. truncate – 清空文件，请小心使用该命令。
#9. write(stuff) – 将 stuff 写入文件。
#10. python3 ex15.py ****.text

## ==============01：写入文件 ===================
script, filename = argv

def fileWrite(fileName):
	print("We're going to erase %r." % fileName)
	print("If you don't want that, hit CTRL-C (^C).")
	print("If you do want that, hit RETURN.")
	input("?")
	print("Opening the file...") 
	target = open(fileName, 'w')
	print("Truncating the file. Goodbye!")
                                          
	target.truncate()

	print("Now I'm going to ask you for three lines.")
	line1 = input("line 1: ")
	line2 = input("line 2: ")
	line3 = input("line 3: ")
	print("I'm going to write these to the file.")

	target.write(line1)
	target.write("\n") 
	target.write(line2) 
	target.write("\n") 
	target.write(line3) 
	target.write("\n")

	print("And finally, we close it.") 
	target.close()

## ==================02：读取文件 ===============

def fileRead(fileName):
	newText = open(fileName)
	print("file:\n%s"%newText.read())
	newText.close()

## ==================03：读取文件 ===============

def fileTruncate(fileName):
	text = open(fileName, 'w')
	text.truncate()
	text.close


fileWrite(filename)
fileRead(filename)
fileTruncate(filename)
fileRead(filename)



