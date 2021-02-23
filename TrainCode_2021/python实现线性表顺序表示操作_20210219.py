'''
线性表-顺序表示笔记：
1.位序与下标 ：位序从1开始   下标从0开始
2.顺序表示插入元素：从哪依次后移----从最后一个

'''
# 1.置空列表
L = [1, 2, 3]
def SetNull(L):
    L.clear()
    return L
SetNull(L)
print(SetNull(L))

# 2.求线性表的长度和表中元素的个数
def Length(L):
    num = 0  # 循环外层定义一个计数器
    for i in L:
        if i != None:
            num += 1
    return len(L), num

a = [None] * 20  # 初始化指定个数的空列表
for i in range(10): a[i] = i
print(Length(a))

# 3.获取列表中的第i个元素
L = [a for a in range(10)]
def Get(L, n):  # n从1开始
    if n < 0 or n > len(L):
        return
    else:
        return L[n - 1]
print(Get(L, 10))

# 4.获取列表中的第i个元素
L = [a for a in range(10)]
def GetPre(L, i):  # 获取前驱元素
    if not isinstance(i, int):  # 类型判断
        raise TypeError
    if i - 1 < 0 or i - 1 >= len(L) - 1:  # 前驱元素索引控制
        raise IndexError
    else:
        return L[i - 1]


def GetNext(L, i):
    if not isinstance(i, int):
        raise TypeError

    if i + 1 < 0 or i + 1 > len(L) - 1:  # 后继元素索引控制
        raise IndexError
    else:
        return L[i + 1]


print(GetPre(L, 9))  # 第i个元素：从0-9
print(GetNext(L, 3))

# 5.返回指定元素在列表中的位置
L = [1, 2, 3, 4]
print(L.index(4))

def Locate(L, x):
    # 异常判断：判断传入的值是否在列表中
    if x not in L:
        return "%s不在列表里" % x
    else:
        return L.index(x)  # 根据值获取索引index()
print(Locate(L, 10))

# 6.在某个位置插入新元素
'''
思路：利用下标赋值
从插入的位置依次向后移动即依次赋值，插入的位置赋值为新元素
'''
def Insert(L, i, x):
    if not isinstance(i, int):
        raise TypeError
    if i < 0:
        raise IndexError
    if i > len(L):
        L.append(x)
    num = 0
    for k in L:
        if k != None:
            num += 1

    # 其他的向依次移动,最多移动num个
    for k in range(num, i - 1, -1):
        L[k] = L[k - 1]

    # 插入的位置i赋值给新元素
    L[i] = x

    return L


# 7.删除某个元素
l = [None] * 30
for i in range(10): l[i] = i ** 2
print(Insert(l, 20, 99))

L = [i for i in range(10)]
def Delete(L, x):
    if x not in L:
        return "%s not in list" % x
    else:
        L.remove(x)
    return L

print(Delete(L, 1))

# 8.判断列表是否为空
'''
设置计数器，遍历每个元素，如果不等于空就+1
'''
def Empty(L):
    num = 0  # 初始值
    for i in L:
        if i != None:  # if通常是反向思考，怎样是不正常的
            num = num + 1  # 如果有值就+1
    # if num >=1:
    #     return  False
    # else:
    #     return True
    return num is 0


A = [None] * 10
print(Empty(A))