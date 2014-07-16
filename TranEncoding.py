#!/usr/bin/env python3  
import os,os.path  
import string,base64
import codecs

def readByEncoding(filename,exEncoding_num):
    if exEncoding_num == "1":
        f=open(filename,'r',encoding=encoding[exEncoding_num])
        return f
    if exEncoding_num == "2":
        f=open(filename,'r')
        return f
    if exEncoding_num =="3":
        f=open(filename,'r')
        return f
    if exEncoding_num == "4":
        f=open(filename,'r',encoding=encoding[exEncoding_num])
        return f
    
    
def writeByEncoding(filename,trEncoding_num):
    if trEncoding_num=="1":
        f=open("hasTran/"+filename,'w',encoding=encoding[trEncoding_num])
        return f
    if trEncoding_num=="2":
        f=open("hasTran/"+filename,'w',encoding="gbk")
        return f
    if trEncoding_num=="3":
        f=open("hasTran/"+filename,'w')
        return f
    if trEncoding_num=="4":
        f=open("hasTran/"+filename,'w')
        return f

if __name__=='__main__':
    dirname=os.getcwd()
    if(os.path.exists("hasTran") == False):
        os.mkdir("hasTran")
    print("1---   UTF-8")
    print("2---   GBK")
    print("3---   ANSI")
    print("4---   ISO")
    exEncoding_num=input("请选择原文件的编码：")
    global trEncoding_num
    trEncoding_num=input("请选择将要转换的编码：")
    global encoding
    encoding={'1':"utf-8",'2':"GBK",'3':"ASCII",'4':"ISO",'5':"ANSI"}
    
    for filename in os.listdir(dirname):
        if filename != "TranEcoding.py" and filename!= "hasTran":
            #file=readByEncoding(filename,encoding[exEncoding_num])
            #writeByEncoding(filename,encoding[trEncoding_num],file)
            ex_content=readByEncoding(filename,exEncoding_num)
            tran_content=writeByEncoding(filename,trEncoding_num)
            for line in ex_content:
                tran_content.write(line)
            print(filename+"转码已经完成")
            ex_content.close()
            tran_content.close()
    print("所有文件转码已经完成，转码后的文件保存在  hasTran文件夹中")
            
            
            
        
    
