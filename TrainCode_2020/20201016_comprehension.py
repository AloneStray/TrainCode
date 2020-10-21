'''
推导式又叫解析式comprehension
列表推导式
字典推导式
集合推导式
体会：
1.字典推导式键值之间用 ：
2.学到函数或者XXX点进去看看源码，增加体会
3.返回的是【可迭代对象】，与list不同，走一步就少一个值
'''
from  random import  randint

for i in range(10):
    print(randint(-5,5))
#列表推导式
list1 =[randint(-10,10) for _ in range(5) ]  #生成一个随机列表
print([i for i in  list1  if i>0])  #筛选


#字典推导式
dict1={'student%d'%i:randint(60,100) for i in range(5)}  #创建新字典
print({k:v for k,v in  dict1.items() if v >70}) #筛选
#注意字典推导式键值之间用 ：

#循环迭代方式
for k1,v1 in dict1.items():
    if v1>70:
        print(k1,v1)

#filter函数
#入参函数与可迭代对象   返回可迭代对象
g=filter(lambda item:item[1]>76,dict1.items())  #返回结果是生成器
# for g2 in g:
#     print("*",g2)

print("打印g")
print(list(g))  #可迭代对象构造成列表：[('student2', 83), ('student3', 94), ('student4', 99)]
print(dict(g))  #{}




