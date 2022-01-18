import os
import re




print("""
=================================
此脚本可用于将当前目录的所有子文件夹下一层的图片文件名改为
五位数字加后缀（类似于“00001.jpg”，“00102.png”）并移动到当前路径。
【！！！使用前请确保当前目录下没有无关的文件夹！！！】
【关于输出的文件顺序：子文件夹和子文件夹下的文件名默认按照
名称中包含的数字排序，（如aaa1，aaa2，aaa3或001，002，010），
如子文件夹中部分文件名中不包含数字，则文件顺序为os.listdir()
输入列表的默认排序。】
--------------
假设当前文件目录为
├── rename.py（本脚本）
└── folder1
    ├── 1.jpg
    └── 2.jpg
└── folder2
    ├── 1.jpg
    └── 2.jpg
└──...
---------------
合并后将会得到
├── rename.py（本脚本）
├── 00001.jpg
├── 00002.jpg
├── 00003.jpg
├── 00004.jpg
├── ...
---------------
输入y/Y继续，其它任意键退出
""")


# ask for confirmation
x = input("""
=================================
【WARNING】: This program will rename every file with jpg/png
 extension in the subdirectories and move them to current
directory, do you want to continue? 
【y/Y for yes, any other key to escape】:
=================================
""")
if x == 'y' or x == 'Y':
    pass
else: 
    exit()


ori_cwd = os.getcwd()
print(ori_cwd)
folder_list = [f for f in os.listdir('.') if os.path.isdir(f)]
try:
    folder_list.sort(key=lambda f: int(re.sub('\D', '', f)))
except:
    pass
ex_list = ['.png', '.jpg']
offset = 0

for folder in folder_list:
    cwd =  ori_cwd + '\\' + folder + '\\'
    filelist = os.listdir(cwd)
    filelist = [file for file in filelist if os.path.splitext(file)[1] in ex_list]
    len_f = len(filelist)
    try:
        filelist.sort(key=lambda f: int(re.sub('\D', '', f)))
    except:
        pass

    # check the file order
    print("=================================")
    print(f"The original file order in the folder [{folder}] be:\n\n")
    for file in filelist:
        print(file)

    # loop through all files in subdirectory.
    for num in range(0, len_f):
        new_num = num + offset
        file = filelist[num]
        filename = os.path.splitext(file)[0]
        ex = os.path.splitext(file)[1]

        filename_new = str(new_num).zfill(5) + ex
        try:             
            os.rename(cwd+file, filename_new)
        except:
            print(f"Failed to rename file [{filename}] -> [{filename_new}], "
                     "check it out!")

    offset += len_f    
    try:
        os.removedirs(cwd)
    except:
        print(f"Failed to delete directory [{folder}]! Maybe it's not empty! ")
    print("=================================")

if input("""
=================================
All done! Any key to exit
=================================
"""):
    exit()
