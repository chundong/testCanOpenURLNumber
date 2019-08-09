#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import sys
import subprocess

def changeStr(filePath,old_str,new_str) :
    backup_path = "%s.backup" % filePath

    file = open(filePath, "r")
    new_file = open(backup_path, "w")
    for line in file :
        if old_str in line :
            print("-:   " + line)
            line = line.replace(old_str,new_str)
            print("+:   " + line)
        new_file.write(line)

    os.remove(filePath)
    os.rename(backup_path,filePath)


# ***********  修改证书配置 **********

pbxprojPath="ios/Runner.xcodeproj/project.pbxproj"
for i in range(0,100):
    fmt = 'PRODUCT_BUNDLE_IDENTIFIER = fm.collect.test'
    oldStr = '%s%d;' % (fmt,i-1)
    newStr = '%s%d;' % (fmt,i)
    changeStr(pbxprojPath,oldStr,newStr)
    xmlpath = 'ios/Runner/Info.plist'

    oldStr = '<string>testApp%d</string>' %(i-1)
    newStr = '<string>testApp%d</string>' %(i)
    changeStr(xmlpath,oldStr,newStr)
    oldStr = '<string>testurl%d</string>' % (i-1)
    newStr = '<string>testurl%d</string>' % i
    changeStr(xmlpath,oldStr,newStr)
    cmd = ['flutter', 'run']
    print cmd
    allLines = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False).stdout.readlines()
    



 



