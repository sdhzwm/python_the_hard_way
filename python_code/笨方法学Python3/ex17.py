
#本章要点如下： **复制文件内容**
#1. exists: 文件名字符串作为参数，如果文件存在的话，它将返回True 否则返回False
#2. len() : 用来计算字符串的长度


from sys import argv
from os.path import exists


script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))
# 打开文件
in_put = open(from_file) 
# 读取文件
indata = in_put.read()
# 打印文件内容的长度
print("The input file is %d bytes long" % len(indata))
if len(indata) == 0:
	indata = "随便写点东西"
# 打印是否存在复制文件
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# 打开文件并且为可写入
output = open(to_file, 'w')
output.write(indata)
            
print("Alright, all done.")
output.close() 
in_put.close()