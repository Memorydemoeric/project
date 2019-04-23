import prettyprint as prettyprint
import xlrd

# 获取Excel库存成品列表信息
def load_storage_excel(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows - 1):
        # print(table.row_values(i)[:6])
        lt.append(table.row_values(i)[:6])
    return lt


# 获取Excel库存半成品信息
def load_storage_half_excel(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows - 1):
        # print(table.row_values(i)[:6])
        lt.append(table.row_values(i)[:6])
        # print(type(table.row_values(i)[:6][1][1:]))
    return lt


# 获取Excel订单信息
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

# 获取Excel客户信息
def load_cust_info(path, sheet_num):
    lt = []
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_num]
    for i in range(1, table.nrows - 1):
        lt1 = [table.row_values(i)[j] for j in range(5)]
        lt.append(lt1)
    return lt





if __name__ == '__main__':
    # path1 = '/home/fish/Desktop/test/11.xls'
    # data1 = load_storage_half_excel(path1, 0)
    # print(data1)

    # path = '/home/fish/Desktop/test/cust_01.xls'
    # data = load_purchase_detail(path, 0)
    # print(data)

    path = '/home/fish/Desktop/test/cust_info.xls'
    data = load_cust_info(path, 0)
    lt = [(a, b, c, d, e) for (a, b, c, d, e) in data]
    map()
    print(lt)
    # print(dict())
    # print(data)