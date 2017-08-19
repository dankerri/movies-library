# !/usr/bin/python
# _*_ coding:utf-8 _*_


# 1. 检查picture与video是否对应
# 2. 更新数据库
# 2. 生成对应的缩略图片
# 3. 移动文件

# ------------------------------------------------------------------------------------------

import os
import sqlite3
import subprocess


def getNameList(sourceList):
    finalList = []
    for i in sourceList:
        temp = i.split('.')
        finalList.append(temp[0])

    return finalList

def test(picList, vidList):
    if (not os.path.exists("./temp/error")):
        os.mkdir("./temp/error")
    for i in picList:
        if (not i in vidList):
            sourcePath = os.path.join('./temp/pictrue', i+".jpg")
            targetPath = os.path.join('./temp/error', i+".jpg")
            os.rename(sourcePath, targetPath)
    for i in vidList:
        if (not i in picList):
            sourcePath = os.path.join('./temp/video', i+".mp4")
            targetPath = os.path.join('./temp/error', i+".mp4")
            os.rename(sourcePath, targetPath)

def updateDB(moviesList):
    conn = sqlite3.connect('movies.db')
    print ("Opened database successfully")
    c = conn.cursor()
    for i in moviesList:
        c.execute("insert into movies (name, type, actress) values ('%s', '0','unknown');" %(i))
    print("insert end")
    conn.commit()
    conn.close()

def resize(moviesList):
    for i in moviesList:
        i = i + ".jpg"
        subprocess.call('convert ./temp/pictrue/%s -resize 500x325! ./static/source/image/resize/%s'%(i, i), shell=True)

def moveSource(moviesList):
    for i in moviesList:
        old = './temp/'
        new = './static/source/'
        os.rename(old+"pictrue/"+i+".jpg", new+"image/origin/"+i+".jpg")
        os.rename(old+"video/"+i+".mp4", new+"video/"+i+".mp4")


# 获取原始视频列表
tempPictrueList = os.listdir("./temp/pictrue")
tempVideoList = os.listdir("./temp/video")
pictrueList = getNameList(tempPictrueList)
videoList = getNameList(tempVideoList)

# 检测出无对应的图片或视频
test(pictrueList, videoList)

#获取检查后的视频列表
moviesList  = getNameList(os.listdir("./temp/video"))
#导入sqlite
updateDB(moviesList)
# 生成对应的缩略图
resize(moviesList)
# 移动文件到相应目录
moveSource(moviesList)
