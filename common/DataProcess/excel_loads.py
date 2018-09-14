import prettyprint as prettyprint
import xlrd

def load_storage_excel(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows - 1):
        # print(table.row_values(i)[:6])
        lt.append(table.row_values(i)[:6])
    return lt


def load_storage_half_excel(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows - 1):
        # print(table.row_values(i)[:6])
        lt.append(table.row_values(i)[:6])
        # print(type(table.row_values(i)[:6][1][1:]))
    return lt


def load_purchase_detail(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows -1):
        # if isinstance(table.row_values(i)[0], int) or isinstance(table.row_values(i)[0], float):
            lt1 = [str(int(table.row_values(i)[0])), int(table.row_values(i)[1])]
            lt.append(lt1)
        # else:
        #     lt.append(table.row_values(i)[:2])
    return lt



if __name__ == '__main__':
    # path1 = '/home/fish/Desktop/test/11.xls'
    # data1 = load_storage_half_excel(path1, 0)
    # print(data1)

    path = '/home/fish/Desktop/test/cust_01.xls'
    data = load_purchase_detail(path, 0)
    print(data)

