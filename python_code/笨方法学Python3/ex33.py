#本章要点：do ... while
#1.  while-loop``(while 循环)。 会一直执行它下面的代码片段，直到它对应的布尔表达式为False时才会停下来。
#2. While 循环有一个问题，那就是可能会造成死循环。
#3. 尽量少用 while-loop，大部分时候 for-loop 是更好的选择
#4. 重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False 

i = 0 
numbers = []
while i < 6:
	print("Atthetopiis %d"%i)
	numbers.append(i)
	i = i + 1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)

print("The numbers: ")
for num in numbers: 
	print(num)