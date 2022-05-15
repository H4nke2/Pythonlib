import os


file_db = []


def scan():
    print("正在初始化...")
    for url in ("C:\\", "D:\\", "E:\\", "F\\", "G:\\", "H:\\"):     # 如果有更多磁盘，可以继续添加
        for root, dirs, files in os.walk(url):
            for file in files:
                file_db.append(os.path.join(root, file))
    os.system("cls")


def check():
    new_file_db = []
    filename = input("请输入要搜索的文件名：")
    # start_time = time.time()
    for file in file_db:
        if filename in file:
            new_file_db.append(file)
    # num = list(range(len(new_file_db)))
    # for n, f in zip(num, new_file_db)
    # end_time = time.time()
    # time_use = end_time - start_time
    # print("结果：")
    for num, add_new_file in enumerate(new_file_db):
        print(num+1, add_new_file)
    # print("搜索消耗时间：{}秒".format(time_use))


scan()
while True:
    check()
