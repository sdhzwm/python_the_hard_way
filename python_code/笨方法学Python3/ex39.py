# 本章要点：list的操作
# 1. split  ：根据某个字符进行字符串的分割
# 2. pop: 移除list中的元素，默认是从最后一个移除
# 3. append： 追加
# 4. join: 要连接的元素序列。
# 5. [3:5] 取index 3 - index5中间的值

ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print("Wait there's not 10 things in that list,let's fix that.")

stuff = ten_things.split(" ")
# print(stuff)

more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10 :
	next_one = more_stuff.pop()
	print("Adding: ",next_one)
	stuff.append(next_one)
	print("There's %d items now" %len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff")


print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print("".join(stuff))
print("#".join(stuff[3:5]))
