import os
import shutil
def findrm(strDirWork,strName,isFindFile):
	os.chdir(strDirWork)
	for obj in os.listdir(os.curdir):
		if(obj == strName):
			if((os.path.isfile(obj) and isFindFile)):
				os.remove(os.getcwd()+os.sep+obj)
				print("remove:" + os.getcwd()+os.sep+obj)
			if(os.path.isdir(obj) and (not isFindFile)):
				shutil.rmtree(os.getcwd()+os.sep+obj)
				print("remove:" + os.getcwd()+os.sep+obj)

		if (os.path.isdir(obj) and (os.path.exists(obj))):
			findrm(obj,strName,isFindFile)
	os.chdir(os.pardir)

strDirWork=input("dir path where to search:")
strName=input("target name:")
isFindFile=bool(input("find file input True,else input False:") == "True")

findrm(strDirWork,strName,isFindFile)
