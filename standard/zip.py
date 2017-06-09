# zip and unzip file and folder
# zip is to loop list meanwhile (see container)

import zipfile
import os
import shutil


# zip folder
def zip_directory(path):
    zip_targets = []
    # pathからディレクトリ名を取り出す
    base = os.path.basename(path)
    # 作成するzipファイルのフルパス
    zipfilepath = os.path.abspath('%s.zip' % base)
    # walkでファイルを探す
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            # 作成するzipファイルのパスと同じファイルは除外する
            if filepath == zipfilepath:
                continue
            arc_name = os.path.relpath(filepath, os.path.dirname(path))
            print(filepath, arc_name)
            zip_targets.append((filepath, arc_name))
        for dirname in dirnames:
            filepath = os.path.join(dirpath, dirname)
            arc_name = os.path.relpath(filepath, os.path.dirname(path)) + os.path.sep
            print(filepath, arc_name)
            zip_targets.append((filepath, arc_name))

    # zipファイルの作成
    zip = zipfile.ZipFile(zipfilepath, 'w')
    for filepath, name in zip_targets:
        zip.write(filepath, name)
    zip.close()

if __name__ == '__main__':
    file1 = './new.zip'
    file2 = './packages.zip'

    if os.path.exists(file1):
        os.remove(file1)

    if os.path.exists(file2):
        os.remove(file2)

    # ZIP_STORED: no compression
    # ZIP_DEFLATED: compression
    zFile = zipfile.ZipFile(file1, 'w', zipfile.ZIP_STORED)
    zFile.write('class_compare.py')
    zFile.write('class_inherit.py')
    zFile.close()
    # zip dir
    zip_directory('./packages')
    # unzip file or folder
    unzip_dir = 'unzip_folder'
    if os.path.exists(unzip_dir):
        shutil.rmtree(unzip_dir)
    os.mkdir(unzip_dir)
    with zipfile.ZipFile(file1, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)
    with zipfile.ZipFile(file2, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)
