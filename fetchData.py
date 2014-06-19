#!/usr/bin/env python3
import os,os.path  
import string,base64
import string

def fetch():
    filename=input("请输入文件名:")
    read=open(filename,'r',encoding='utf-8')
    write=open("fetch.sql",'w')
    for eachline in read:
        if "INSERT" in eachline or "insert" in eachline :
            write.write(eachline)
    write.write("===========")
    write.close()
    read.close()

    
if __name__=='__main__':  
    fetch()  
