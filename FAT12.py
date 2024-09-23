def open_fat12(path):
    with open(path, 'rb') as fat_fs:
        fs_obj = fat_fs.read()
    
