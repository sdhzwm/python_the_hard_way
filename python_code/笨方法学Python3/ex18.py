#本章要点如下： **复制文件内容**
#1. 函数：function.
#2. 函数的作用(新人必读) :
#2.1 给代码片段命名，就跟变量给字符串和数字命名一样。
#2.2 他们可以接受参数，就跟脚本接受argv一样
#2.3 可以创建小脚本或小命令
#3. def 是定义函数的意思，即define
#4.*args：预先并不知道, 函数使用者会传递多少个参数给你, *args 是用来发送一个非键值对的可变数量的参数列表给一个函数
#5.arg1,arg2: 指传递几个参数
#6. 
from sys import argv

def print_two(*args):
	arg1,arg2 = args
	print("arg: %r,arg2: %r" %(arg1,arg2))

def print_two_again(arg1,arg2):
	print("arg: %r,arg2: %r" %(arg1,arg2))

def print_one(arg1):
	print("arg: %r" %arg1)

def print_none():
	print("I got nothin")

print_two("m","f")
print_one("w")
print_two_again("m","f")
print_none()


