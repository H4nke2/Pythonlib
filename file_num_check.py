import os
import time
import numpy as np


class FileCheck:

    def __init__(self):
        # self.url = "D:\\"
        a = np.load("file_demo.npy", allow_pickle=True)
        b = np.load("dir_demo.npy", allow_pickle=True)
        self.ori_file_db, self.ori_dir_db = a.tolist(), b.tolist()
        self.ori_file_db2, self.ori_dir_db2 = a.tolist(), b.tolist()
        self.dir_db, self.file_db = [], []
        self.new_file_db, self.new_dir_db = [], []
        self.new_file_db2, self.new_dir_db2 = [], []
        self.check()
        self.increase()
        self.decrease()
        self.save()
        self.out()

    def check(self):
        for url in ("C:\\", "D:\\"):
            for root, dirs, files in os.walk(url):
                for file in files:
                    self.file_db.append(os.path.join(root, file))
                for d in dirs:
                    self.dir_db.append(os.path.join(root, d))

    def increase(self):
        for file in self.file_db:
            if file in self.ori_file_db:
                pass
            else:
                if "$RECYCLE.BIN" in file:
                    pass
                else:
                    self.new_file_db.append(file)
        for d in self.dir_db:
            if d in self.ori_dir_db:
                pass
            else:
                if "$RECYCLE.BIN" in d:
                    pass
                else:
                    self.new_dir_db.append(d)

    def decrease(self):
        for file in self.ori_file_db2:
            if file in self.file_db:
                pass
            else:
                if "$RECYCLE.BIN" in file:
                    pass
                else:
                    self.new_file_db2.append(file)
        for d in self.ori_dir_db2:
            if d in self.dir_db:
                pass
            else:
                if "$RECYCLE.BIN" in d:
                    pass
                else:
                    self.new_dir_db2.append(d)

    def save(self):
        m = np.array(self.file_db)
        n = np.array(self.dir_db)
        np.save("file_demo.npy", m)
        np.save("dir_demo.npy", n)

    def out(self):
        print("???????????????????????????")
        for add_new_file in self.new_file_db:
            print(add_new_file)
        print("??????????????????????????????")
        for add_new_dir in self.new_dir_db:
            print(add_new_dir)
        print("???????????????????????????")
        for del_new_file in self.new_file_db2:
            print(del_new_file)
        print("??????????????????????????????")
        for del_new_dir in self.new_dir_db2:
            print(del_new_dir)


def initialize():
    clean_list = []
    clean_np = np.array(clean_list)
    np.save("file_demo.npy", clean_np)
    np.save("dir_demo.npy", clean_np)
    print('???????????????')


def main():
    select = input("??????0?????????????????????ENTER??????????????????")
    if select == "0":
        initialize()
        main()
    else:
        print("\n?????????????????????CTRL C????????????\n")
        print("???????????????????????????????????????????????????\n")
        print("????????????...")
        FileCheck()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    time_use = end_time - start_time
    min_use = round(time_use/60)
    sec_use = round(time_use % 60)
    print("?????????????????????{}???{}???".format(min_use, sec_use))
    input("??????????????????")
