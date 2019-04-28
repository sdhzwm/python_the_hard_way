#本章要点如下：
#1. seek() 方法用于移动文件读取指针到指定位置。
#2. python3 ex20.py test.text

from sys import argv

script, input_file = argv

#定义打印函数，接受文件名称，进行读取
def print_all(f):
	print(f.read())
#定义函数，读取avg文件于移动文件读取下标为0的位置。
def rewind(f):
	f.seek(0)
#定义函数，读取avg文件于移动文件读取下标为0的位置。
def print_a_line(line_count, f): 
	print(line_count, f.readline())
#打开指定文件
current_file = open(input_file)

print("First let's print the whole file:\n")
#调用函数，打印当前文件
print_all(current_file)
print("Now let's rewind, kind of like a tape.")  
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1 
print_a_line(current_line, current_file)
