'''
程序用途：程序用于对srt文件的操作。以下案例的文件结构是处理多个目录下的各个srt文件

目录及文件结构：
address1---这是当前总文件夹的路径
file_level1---用于存放所有要处理的目录路径
file_level2---用于存放每个目录下的srt文件

实现逻辑：
1.首先得获取整个操作文件夹的地址address1
2.然后读取address1文件下所有的目录文件
3.紧接着读取目录文件下的srt文件
4.先读取文件，放入临时的列表中，然后在写入文件。


注：
该项目下的chuli.py,input.srt,output.srt三个文件是实现读写文件逻辑的（就是复制文件进input.srt,然后运行chuli.py,output.srt能自动获得结果）,
无法实现对批量文件的处理，所以，可以忽视。
'''


import os
address1='/Users/luoming/Documents/学习/吴恩达 机器学习 中文字幕版/中文字幕 处理之后/' #address：当前总文件夹的路径

file_level1=os.listdir(address1)  #获取当前目录的路径



for f in file_level1:       #第一层遍历，获取所有的目录文件名
        if(f[0]=='.'):     #'.'开头的文件为系统文件，要删除
            pass
        else:
            file_level2=os.listdir(address1+f)     #将目录文件名与address1结合，形成每个目录的绝对路径


            for f2 in file_level2:    #遍历每个目录下的srt文件

                '''此模块是读文件'''
                list=[]   #声明一个list列表，用于存放每个srt文件中的每行内容
                reader = open(address1+f+'/'+f2, "r",encoding='utf-16')  # 读取一个要修改的字幕文件，这里的utf编码，根据需要自行更正
                list=reader.readlines()   #将每一行内容读取到list临时列表中
                reader.close()     #关闭读


                '''此模块是写文件'''
                writer=open(address1+f+'/'+f2, "w",encoding='UTF-16')   #开始写入一个文件
                #以下的操作，根据对修改字幕的不同需求进行改动。本案例是要将每个字幕前加个空格（我也不知道为什么MAC iina会出这样的bug）
                for index,line in enumerate(list):
                    if(index%4==2):
                        writer.write(' '+line)
                    else:
                        writer.write(line)



