import zipfile

def unzip(filepath,dest_dir):
    with zipfile.ZipFile(filepath,'r') as myzip:
        myzip.extractall(dest_dir)

if __name__ == "__main__" :
    unzip('/home/tianlong55/Downloads/PyCharm_Projects/ExtraApps/compressed.zip','/home/tianlong55/Downloads/PyCharm_Projects/ExtraApps')
    print("DONE !!!")
