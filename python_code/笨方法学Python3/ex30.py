# 本章要点
#1. If 语句为代码创建了一个所谓的“分支”，会告诉脚本:“如果这个布尔表达式为真，就运行接下来的代码，否则就跳过这一段。”
#2.行尾的冒号的作用是告诉Python 接下来你要创建一个新的代码区段。
#3. 如果你没有缩进，你应该会看到 Python 报错。 Python 的规则里，只要一行以“冒号(colon)”:结尾，它接下来的内容就应该有缩进。
#4. elif 和else 的含义

people = 30
cars = 40
buses = 15
if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if buses > cars:
	print("That's too many buses.")
elif buses < cars:
	print("Maybe we could take the buses.")
else:
	print("We still can't decide.")
if people > buses:
	print("Alright, let's just take the buses.")
else:
	print("Fine, let's stay home then.")