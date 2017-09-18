# 65-90,97-122 +4
path = "C:\\Users\\pengc\\Downloads\\道德经txt.txt"
with open(path,'a') as files:
    contents = files.read()

for f in contents[:]:  # 循环
    f = str(f)
    f = ord(f)  # 把字母转换成ASCII码
    m = int(f)  # 转换成数字
    m += 4
    m = chr(m)
    f = str(m)
    print(f)

