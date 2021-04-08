import xlrd
import xlwt
import urllib.request
import os




def read_excel(path,sheet_index):
    # 打开excel文件
    wb = xlrd.open_workbook(path)


    # 获取所有表格名字
    # print(wb.sheet_names())

    # 通过索引获取表格
    sheet1 = wb.sheet_by_index(sheet_index)
    # print(sheet1.name, sheet1.nrows, sheet1.ncols)

    # 获取行内容
    # rows = sheet1.row_values(2)
    # print(rows)

    # 获取列内容
    # cols = sheet1.col_values(3)
    # print(cols)

    # 获取表格里的内容，三种方式
    # print(sheet1.cell(1, 0).value)
    # print(sheet1.cell_value(1, 0))
    # print(sheet1.row(1)[0].value)


    for i in range(sheet1.nrows):
        if i==0:
            continue
        row_val=sheet1.row_values(i)
        print(row_val)
#
def write_excel():
    f = xlwt.Workbook()

    # 添加sheet
    sheet1 = f.add_sheet('Students', True)

    # 创建杭数据和列数据
    row0 = ["qq", "ddd", "fgg", "hjj"]
    column0 = ["zsfsd", "ghg", "Python", "fs", "fgsf", "zbg"]

    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])

    # 写第一列
    for i in range(0, len(column0)):
        sheet1.write(i + 1, 0, column0[i])

    # 保存文件为xls格式，xlsx格式不能打开
    f.save('test.xls')


def readCsv(filepath):
    f=open(filepath)
    for line in f.readlines():

        line=line.strip("\n")
        sp_line=line.split(",")
        # print(len(sp_line),sp_line)
        url=sp_line[-1]
        print(url)
        file_name=os.path.basename(url)
        print(file_name)
        if url.startswith("http") and url.endswith(".pdf"):
            urllib.request.urlretrieve(url,file_name)



if __name__=="__main__":
    readCsv("/Users/noelsun/Documents/github/spider/pdfToTxt/df001.csv")