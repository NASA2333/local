#coding=utf-8
import re
import os
def linesOfFile(filepath):
    lines = 0
    f= open(filepath,'r',encoding='utf-8')
    # with open(filepath) as f:
    for line in f:
        if line.strip() != "": #忽略空白行
        #print "line: " + line.strip()
            lines = lines + 1
    return lines
def walkPython(path):
    count = 0
    lines = 0
    for root, subFolder, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                count=count + 1
                print(os.path.join(root, file))
                lines = lines + linesOfFile(os.path.join(root, file))
    print ("Total Python File Number: " + str(count))
    print ("Tocal Lines of Python Source: " + str(lines))
if "__main__" == __name__:
        walkPython(r'D:\python')
