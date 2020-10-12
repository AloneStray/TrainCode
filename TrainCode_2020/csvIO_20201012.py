'''
2020-10-11:训练读写CSV

如何读写CSV：使用CSV库  读方法reader  写方法writer

需求：orders.csv 把支付订单金额大于50的写入另一个csv文件
逻辑梳理：按行读取、按行写入，后处理首行问题

'''

import  csv

with open('csvio_rders.csv','r') as rf: # rf--文件对象
    readerobj = csv.reader(rf)    # rederobj--CSV文件对象，可迭代

    with open('csvio_orders50.csv','w',newline='') as wf: #newline='' 默认不换行，从而防止写入出现空行
        writerobj = csv.writer(wf)  #CSV写对象

        headers = next(readerobj)  #返回第1行，同时readrobj变成从第2行开始

        writerobj.writerow(headers)
        for row in  readerobj:
            if float(row[-2])>50:         #写入前过滤操作
                writerobj.writerow(row)   #按行写入
