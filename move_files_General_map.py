# -*- coding: utf-8 -*-
import sys
import locale
import os
import glob
import shutil


DataFolder = "C:\\py_WORK"
ResultFolder = "D:\\RESULT"
os.chdir(DataFolder)

"""# Проверка кодировок
print sys.getdefaultencoding()
print locale.getdefaultlocale()
print locale.getpreferredencoding()
print sys.stdout.encoding"""

DataFolderList = os.listdir(DataFolder)

VisimShapes= glob.glob("VISIM*.*")
for i in VisimShapes:
    FileCopy = ResultFolder + "\\" + i
    shutil.copy(i, FileCopy)

"""#Выборка по расширению
for files in DataFolderList:
    if files.endswith(".shp"):
        shutil.move(files,ResultFolder)"""