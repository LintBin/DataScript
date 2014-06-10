#!/usr/bin/env python3  
import os,os.path  
import string,base64
import string
def main():
    tableName=input("请输入数据表名:")
    typeDir={}
    typeDir=check(typeDir)
    print(typeDir.item)
    '''f=open("inserData.sql",'w')
    i=1
    num=input("将要生成的sql语句多少条？:")
    numStr=str(num)
    while i<int(num):
        sql=createsql(table,li,str(i))
        i=i+1
        print(sql)
        
    '''
    #sql="insert into values "+table+"("+li[0]+"','"
    #print(sql)
 
    #f.close()

#递归，检查是否需要输入字段
def check(typeDir):
    flag=input("是否还有列要输入，是则输入'y'，没有则输入'n':")
    if flag=="y":
        print("1--int型")
        print("2---字符型(包括char和carchar)")
        print("3---data型")
        columnType=input("选择所需要添加字段的类型:")
        columnNum=input("此字段需要多少个？:")
        columnDir={}
        if columnType=="1":
            #多次输入需要的字段名,每一个字段配一个字典
            i=0
            while i<int(columnNum):
                i=i+1
                columnNmae=input("请输入字段名")
                #inpitColumn是字段名，而intDeal返回的是其相对应的字典
                columnDir[columnNmae]=intDeal()
            typeDir["intDir"]=columnDir
            check(typeDir)
            return typeDir
        if columnType=="2":
            i=0
            while i<int(columnNum):
                i=i+1
                columnNmae=input("请输入字段名:")
                columnDir[columnNmae]=stringDeal()
            typeDir["stringDir"]=columnDir
            check(typeDir)
            return typeDir
    if flag=="n":
        return typeDir
    else:
        return typeDir
    
def createsql(tableName,typeDir,numStr):
    sql="insert into "+table+"("
    for element in li:
        sql=sql+"'"+element+numStr+"',"
    sql=sql[:-1]
    sql=sql+")"
    return sql

#列为int型时的处理
def intDeal():
    print("1--自增")
    print("2--设置固定值")
    detailDir={}
    addself=input("是否自增：")
    if addself=="1":
        beginNumStr=input("自增开始数值:")
        beginNumInt=int(beginNumStr)
        detailDir["addself"]="1"
        detailDir["beginNum"]=beginNumStr
        return detailDir
        
    if addself=="2":
        setNumStr=input("数值固定为:")
        setNumInt=int(setNumStr)
        detailDir["addself"]="2"
        detailDir["setNum"]=setNumInt
        return detailDir

def stringDeal():
    print("1--字段名加自增的数字")
    print("2--设置固定值")
    detailDir={}
    addself=input("是否固定")
    if addself=="1":
        beginNumStr=input("自增开始数值:")
        detailDir["addself"]="1"
        detailDir["beginNum"]=beginNumStr
        return detailDir
    if addself=="2":
        setNumStr=input("数值固定为:")
        detailDir["addself"]="2"
        detailDir["setNum"]=setNumStr
        return detailDir
    
if __name__=='__main__':  
    main()


