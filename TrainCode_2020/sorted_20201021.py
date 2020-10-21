'''
2020-10-21：字典排序
高阶函数sorted用法
写错误的地方，忘记写key=
key= 主要是用来进行比较的元素，只有一个参数
'''
dict1 = {'a':1,'b':6,'c':2}

a=sorted(dict1.items(),key=lambda x:x[1],reverse=False )

print(type(a))  #返回列表
print(dict(a))
b=dict1.keys()
print(type(b))
list1=[1,2,3]
list2=[4,5,6]
print(list(zip(dict1.keys(),dict1.values())))


'''
sort与sorted区别：
1.sort是应用在列表上的方法，sorted是对所有可迭代对象
2.sort是在原列表，sorted是产生新列表

'''