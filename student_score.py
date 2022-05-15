import pandas as pd     # 用于处理表格数据
import os.path          # 用于检测文件是否存在
import openpyxl         # 用于创建表格


class Sys:

    if os.path.exists('D:/python/pythonProject/student_scores.xlsx'):   # 检测文件是否存在
        pass            # 如果存在就跳过
    else:
        wb = openpyxl.Workbook()
        wb.save('D:/python/pythonProject/student_scores.xlsx')          # 如果不存在就通过Workbook来创建
    data = pd.read_excel('D:/python/pythonProject/student_scores.xlsx')     # 读取表格中的数据并赋值给data

    def __init__(self):     # 定义初始化函数
        self.data = Sys.data    # 定义类变量，将类变量data赋值给实例化变量
        self.operation()        # 执行operation函数


    def save(self):             # 定义一个将frame导出到excel文件的函数
        self.data.to_excel('D:/python/pythonProject/student_scores.xlsx', index=False)  # index=False，不添加索引

    def entering(self):         # 定义一个录入成绩的函数
        stu_num = int(input("请输入学生的学号："))
        # new_frame =  pd.DataFrame([[stu_num, pd.NaT, pd.NaT]], columns=["ID", "Name", "score"])
        # self.data = pd.concat([self.data, new_frame])
        # 上面两行是另一种实现方式，但是这种方式会产生重复的数据，即系统不管有没有这个学号，都会在末尾追加数据。
        stu_score = int(input("请输入{}的成绩:".format(self.data.iloc[stu_num-1, 1])))
        # iloc用于定位数据的位置，这里使用iloc读取学号为stu_num的学生姓名
        self.data.iat[stu_num-1, 2] = stu_score     # 使用iat函数定位，并将分数放在这个位置。
        self.save()

    def modify(self):   # 定义一个修改学生成绩的函数，其实和添加成绩是同一个实现方式。
        stu_num = int(input("请输入要修改成绩学生的学号："))
        stu_score = int(input("请输入{}的成绩:".format(self.data.iloc[stu_num-1, 1])))
        self.data.iat[stu_num-1, 2] = stu_score
        self.save()

    def query(self):    # 定义一个根据学号查询成绩的函数
        stu_num = int(input("请输入要查询的学号："))
        print("{}的成绩是{}".format(self.data.loc[stu_num-1, "Name"], self.data.loc[stu_num-1, "score"]))
        # 这里使用了loc来进行定位，loc使用行列标签定位，iloc使用行列位置定位

    def dlt(self):  # 定义一个只删除成绩，不删除学生信息的函数。
        stu_num = int(input("请输入要删除成绩的学号："))
        self.data.iat[stu_num-1, 2] = pd.NaT    # 使用iat定位，并将pandas自带的空值NaT赋值给score。
        self.save()

    def browse(self):   # 定义一个浏览成绩的函数
        rank = self.data.sort_values(by='ID')   # 以ID值大小为表格排序
        print(rank)

    def rank(self):     # 定义一个按照成绩高低来排序的函数
        rank = self.data.sort_values(by='score')    # 以score值大小为表格排序，默认降序
        print(rank.iloc[::-1])      # 倒序输出

    def stu_entering(self):     # 定义一个添加学生的函数
        stu_num = int(input("请输入新学生的学号："))
        stu_name = input("请输入新学生的姓名：")
        new_stu = pd.DataFrame([[stu_num, stu_name, pd.NaT]], columns=["ID", "Name", "score"])
        # 将新学生信息存储为dataframe格式，默认成绩为空，即pd.NaT
        self.data = pd.concat([self.data, new_stu])     # 在原有的dataframe（self.data）上扩展新的dataframe（new_stu)
        self.save()

    def operation(self):  # 定义一个流程控制函数
        while True:
            oper_num = input("1-录入成绩\t2-修改成绩\t3-查询成绩\t4-删除成绩\n5-查看所有\t6-查看排名\t7添加学生\t8-退出\n请选择您要进行的操作:")
            try:
                operation_select = int(oper_num)
                if operation_select == 1:
                    self.entering()
                elif operation_select == 2:
                    self.modify()
                elif operation_select == 3:
                    self.query()
                elif operation_select == 4:
                    self.dlt()
                elif operation_select == 5:
                    self.browse()
                elif operation_select == 6:
                    self.rank()
                elif operation_select == 7:
                    self.stu_entering()
                elif operation_select == 8:
                    print("欢迎再次使用^_^")
                    break
                else:
                    print("请输入列出的数字")
            except ValueError:
                print("只能输入数字来选择操作")


if __name__ == '__main__':
    Sys()


# Sys().entering()
# Sys().query()
# print(Sys.data)
# Sys().browse()
# Sys().rank()
# 按标签赋值：
#
# In[48]: df.at[dates[0], 'A'] = 0
# 按位置赋值：
#
# In[49]: df.iat[0, 1] = 0

# df = pd.DataFrame({'ID': [1, 2, 3], "Name": ['Eric', 'Alice', 'Smith'], "score": [60, 98, 80]})
# df.to_excel('D:/python/pythonProject/student_scores.xlsx')
# df2 = df.set_index('ID')
# print(df)
# print(df2)
# print(df.shape)
# print(df.columns)
# print(df.head(2))
# print(df.tail(2))
#
# df = pd.read_excel('D:/python/pythonProject/student_scores.xlsx', header=2)
# print(df)
# df = pd.DataFrame({'ID': [1, 2, 3], "Name": ['Eric', 'Alice', 'Smith'], "score": [60, 98, 80]})
# df.to_excel('D:/python/pythonProject/student_scores.xlsx', index=False)
# df = df.set_index('ID')
# print(df)
# 添加行
# df2 = pd.DataFrame([[4, "Bob", 80], [5, "Mike", 70]], columns=["ID", "Name", "score"])
# df = pd.concat([df, df2])
# df.to_excel('D:/python/pythonProject/student_scores.xlsx', index=False)
# # df = pd.read_excel('D:/python/pythonProject/student_scores.xlsx')
# print(df)
# 删除行
