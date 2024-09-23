class fat_obj:
    def __init__(self, path):
        self.path = path
        self.fs_obj = ''
    def open_fat12(self.path):
        with open(self.path, 'rb') as fat_fs:
            fs_obj = fat_fs.read()
    
