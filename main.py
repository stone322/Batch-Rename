import os
import zipfile
import sys
import getopt
import platform

sys_type = platform.system()

def mkdir(pdir, begin, end):
    cnt = begin
    while cnt <= end:
        cdir = pdir + '/' + '0816_' + str(cnt).zfill(2) + '_/'
        cnt = cnt + 1
        if not os.path.exists(cdir):
            os.makedirs(cdir)

def rename(path):
    if path[-1] != '/' or path[-1] != '\\':
        if sys_type == 'Windows':
            path = path + '\\'
        elif sys_type == 'Linux':
            path = path + '/'
    files = os.listdir(path)
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


def rename_zip_dds(path, date = ''):
    if path[-1] != '/' or path[-1] != '\\':
        if sys_type == 'Windows':
            path = path + '\\'
        elif sys_type == 'Linux':
            path = path + '/'
    files = os.listdir(path)
    for file in files:
        oldname = path + file 
        if date == '':
            newname = path + (path[-2:-6:-1])[::-1] + '_' + file + '_dds'
        else:
            newname = path + date + '_' + file + '_dds'
        try:
            print(oldname, '  -------->  ', newname)
            os.rename(str(oldname), str(newname))
        except Exception as e:
            print(e)
            print('ERROR: Rename file failed!!!')
        else:
            print('Rename file succeeded.')
            zipDir(str(newname), str(newname) + '.zip')
            print('Zip file succeeded.')
        
    return

def zipDir(dirpath, outFullName):
    '''
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    '''
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def print_help():
    print('rename: python3 main.py -p <file_path>')
    print('rename and zip: python3 main.py -rz <file_path>')

def main(argv):
    file_path = ''
    try:
        opts, args = getopt.getopt(argv, 'hp:', ['help', 'file_path='])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help()
            sys.exit()
        elif opt in ('-p', '--file_path'):
            file_path = arg
            rename(file_path)
        elif opt in ('-rz', '--rename_and_zip'):
            file_path = arg
            rename_zip_dds(file_path)
    return 

if __name__ == '__main__':
    main(sys.argv[1:])

    rename_zip_dds('D:\\luobaoming\\RTI_FILES\\1010')