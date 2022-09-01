import os
import zipfile
import sys
import getopt

def mkdir(pdir, begin, end):
    cnt = begin
    while cnt <= end:
        cdir = pdir + '/' + '0816_' + str(cnt).zfill(2) + '_/'
        cnt = cnt + 1
        if not os.path.exists(cdir):
            os.makedirs(cdir)

def rename(path):
    files = os.listdir(path)
    print('path = ', path)
    print(files)
    for file in files:
        oldname = path + file 
        newname = path + (path[-2:-6:-1])[::-1] + '_' + file[0:5] + 'kph_dds' + (file[-1:-4:-1])[::-1]
        try:
            print(oldname, '  -------->  ', newname)
            os.rename(str(oldname), str(newname))
        except Exception as e:
            print(e)
            print('rename file fail')
        else:
            print('rename file success')
        
    return

def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

def zipdds(path):
    files = os.listdir(path)
    for file in files:
        zipDir(path + file, path + file + 'kph_dds.zip')
    return 

# mkdir('/home/luobm/Downloads/0816/', 1, 60)

# zipDir('/home/luobm/Downloads/0805/0805_01_5', '/home/luobm/Downloads/0805/0805_01_5.zip')
# zipdds('/home/luobm/Downloads/0805/')

def main(argv):
    file_path = ''
    try:
        opts, args = getopt.getopt(argv, "hp:", ['help', 'file_path='])
    except getopt.GetoptError:
        print('python3 main.py -p <file_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('python3 main.py -p <file_path>')
            sys.exit()
        elif opt in ('-p', '--file_path'):
            file_path = arg
            rename(file_path)
    return 

if __name__ == "__main__":
    main(sys.argv[1:])