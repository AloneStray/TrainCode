#创建指定个数的节点
class  Node:
    #节点类
    def __init__(self,num):
        self.num = num
        self.next = None

head_node = Node(None)
head_node.next=None
p = head_node  #记录头节点位置

#循环创建节点
for i  in range(5):
    node = Node(i)
    p.next = node  #指向node1   、 node2 【node1.next 表示的是node1节点指向下一个节点】
                                        #【node1.next = node2 表示两个节点建立连接】
    node.next =None
    p = node     #【myerror: 遗漏了这行代码，改变p位置，指向本次循环当前节点】


#循环遍历
p = head_node.next #(node1开始）
while p != None:
    print("第%d个节点"%p.num)
    p = p.next

