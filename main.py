#!/usr/bin/env python3  
import os,os.path  
import string,base64
import string
def main():
    table=input("请输入数据表名:")
    li=[]
    li=check(li)
    f=open("inserData.sql",'w')
    i=1
    num=input("将要生成的sql语句多少条？:")
    numStr=str(num)
    while i<int(num):
        sql=createsql(table,li,str(i))
        i=i+1
        print(sql)
        
    
    #sql="insert into values "+table+"("+li[0]+"','"
    #print(sql)
 
    f.close()

def inputColumn():
    column=input("请输入列名:")
    return column
    
def check(li):
    flag=input("是否还有列要输入，是则输入'y'，没有则输入'n':")
    if flag=="y":
        li.append(inputColumn())
        check(li)
    if flag=="n":
        return li
    else:
        return li
def createsql(table,li,numStr):
    sql="insert into "+table+"("
    for element in li:
        sql=sql+"'"+element+numStr+"',"
    sql=sql[:-1]
    sql=sql+")"
    return sql


if __name__=='__main__':  
    main()
