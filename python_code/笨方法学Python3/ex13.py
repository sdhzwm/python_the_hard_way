

#本章要点如下： 
#1. from sys :模组(modules) | 库 (libraries), 把sys模组 import 进来
#2. import ：这是将python的功能引入脚本的方法. 要什么就调用什么,“import”可以作为提示，明白代码用到了哪些功能。
#3. argv  ：是所谓的“参数变量(argument variable)”，这个变量包含了传递给Python的参数。
#4. python3 ex13.py 1 2 3     ex13.py部分就是所谓的“参数 (argument)”

from sys import argv
script, first, second, third = argv

print("The script is called:",script) 
print("Your first variable is:", first)
print("Your second variable is:", second) 
print("Your third variable is:", third)