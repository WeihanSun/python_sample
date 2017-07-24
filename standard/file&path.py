#
# file & path
# import, from

import os
import glob
#import shutil
#import codecs

# system separator
print(os.sep)
print(os.pathsep)
print(os.extsep)


PROJECT_DIR = 'C:¥python-izm'
SETTINGS_FILE = 'settings.ini'
print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.exists('C:\Program Files'))  # path exist
print(os.path.exists("./test1/test1.doc"))  # file exist
print(os.path.isfile('./test1/test1.doc'))  # file exist
print(os.path.isdir('C:\Program Files'))
fileName, extName = os.path.splitext('./test1/test1.doc')  # get extension name
pathName, fileName = os.path.split('./test1/test1.doc')  # get path name

# file open,
f = open('main.py')
try:
    pass
except:
    pass
finally:  # file close even if failures
    f.close()

'''
# codecs
fin  = codecs.open('read.txt', 'r', 'shift_jis')
fout_euc = codecs.open('euc_out.txt', 'w', 'euc_jp')
fout_utf = codecs.open('utf-8.txt', 'w', 'utf-8')
fin.close()
fout_euc.close()
fout_utf.close()

# file system operation
os.mkdir("./test") # mkdir
shutil.copyfile('src', 'des')  # copy create date
shutil.copy('src', 'des')  # copy create date
shutil.copy2('src', 'des')  # create date refresh
shutil.copytree('src_folder', 'des_folder') # すでにあるフォルダにコピーしようとするとエラーがでる
from distutils.dir_util import copy_tree
copy_tree('src_folder', 'des_folder') # すでにあるディレクトリにコピーしたい場合
os.remove("./test1.txt")  # file delete 
shutil.rmtree("folder")  # folder delete recursively 
shutil.move("./test2/test1.txt", ".")  # file move
os.rename("./test1.txt", "./test2.txt")  # rename file or folder
'''

print(glob.glob('./*.py'))
print(os.listdir('./'))


print(os.getcwd())  # get current work directory
os.chdir('..')  # change cwd
print(os.getcwd())

# import
import test_module
print(test_module.TestClass().get_name())

from test_module import TestClass
print(TestClass().get_name())

city1 = test_module.City('China', 'Tianjin')
city2 = test_module.City('China', 'Bejing')
print(city1.city_name)
print(city1 == city2)  # call parent's overload function ==

# separator
print(os.sep)
print(os.pathsep)
print(os.extsep)



