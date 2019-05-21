writer = open("output.srt", "w")  #读取一个要修改的字幕文件
for i, line in enumerate(open("input.srt")):  #首先将该字幕文件的每一行，和它的内容编入一个元祖，行数与字幕内容一组。
    if i%4==2:        #如果当前的行数对4取余为2
        writer.write(" " + line)   #就把这行的内容前面加一个空格导进去
    else:
        writer.write(line)
writer.close()