
#本章要点如下： 
#1. from sys :模组(modules) | 库 (libraries), 把sys模组 import 进来
#2. import ：这是将python的功能引入脚本的方法. 要什么就调用什么,“import”可以作为提示，明白代码用到了哪些功能。
#3. argv  ：是所谓的“参数变量(argument variable)”，这个变量包含了传递给Python的参数。
#4. python3 ex14.py WM


from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)

likes = input(prompt)

print("Where do you live %s?" % user_name)

lives = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)

print("""
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. 
Nice.
""" % (likes, lives, computer))