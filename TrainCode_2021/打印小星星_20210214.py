'''
样图一：2021-02-13
      *
    * * *
  * * * * *
* * * * * * *

思路：
参数化总行数
找行数与个数的关系
找行数与空格的关系
'''
line_count=4 #行数
for current_line in range(1,line_count+1): #n 代表当前行
    # 行数与空格个数的关系
    for null in range(line_count-current_line):
        print("  ",end="")

    # 行数与星星个数的关系
    for  null in range(2*current_line-1):
        print("* ",end="")
    print("\n",end="") #一行结束后换行

'''
样图二：2021-02-13
* * * * * * * 
 * * * * * 
  * * * 
    * 
'''
for i in range(1,line_count+1)[::-1]:
    #行数与空格个数的关系
    for null in range(line_count-i):
        print("  ",end="")
    #行数与星星个数的关系
    for null in range(i*2-1):
        print("* ",end="")
    print("\n",end="")

print("----------------")
'''
样例三：2021-2-14
     *
   *    *
*    *     *
'''
n1=4
for k in range(1,n1+1):
    for i in range(n1-k):
        print(" ",end="")
    for j in range(k):
        print("* ",end="")
    print("\n",end="")