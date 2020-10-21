def  addcomma(file,linecount):
    '''
    脚本功能：数据批量添加逗号
    :auth @konglingfeng
    :param file: 文件名称
    :param linecount: 指定每行行数
    :return:
    '''
    with open(file, 'r') as rf:
        count =1  #计数器
        lines = rf.readlines()

        for index,line in enumerate(lines):
            line = line.strip()
            if  index == len(lines)-1: #当前行是否是最后一行
                line =line
            else:
                # line = line + ','  # 字符串格式拼接
                format()
            print(line, end='')
            count = count +1
            if count >linecount :
                print('\n',end='')
                count=1

#---------*****--------------
addcomma('data01_demo.txt',6)

'''
readme:
文件数据格式：
196242418198016
196748383512064
197407334788608
197841890805760
197879356098560
197931177052160
198050002030080

输出格式：
196242418198016,196748383512064,197407334788608,197841890805760,197879356098560,197931177052160,
198050002030080,198064028962304,198088088604160,198155971513856,198333452544000,198362005006336,
198393803401216,201494160500736,201538393958400,201626399565824,201676001601536,201726474020864,
201766140602368,201824904243200

使用场景：select查询 in( )
'''

