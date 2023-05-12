import zipfile
import pathlib
def make_archive(filepaths,dest_dir,name_compressed):
    name_string=f'{name_compressed}.zip'
    dest_path = pathlib.Path(dest_dir,name_string)
    with zipfile.ZipFile(dest_path,'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)

#testing
#if __name__ == "__main__":
#    make_archive(filepaths=["bonus1.py","bonus2.1.py"],dest_dir="dest")
