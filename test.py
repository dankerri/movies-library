import os
import subprocess
import updateDB

# subprocess.call('ls -l ./temp/pictrue', shell=True)

picList = os.listdir("./temp/pictrue")

for i in picList:
    subprocess.call('convert ./temp/pictrue/%s -resize 500x325! ./static/source/image/resize/%s'%(i, i), shell=True)
# convert ../ambi05.jpg -resize 500x325! r_ambi05.jpg
