import os
import datetime

from project import settings


def output_purchase_file(cust_name, file):
    base_path = settings.PURCHASE_BAK
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    year_month = year + '.' + month
    path = os.path.join(base_path, year_month)
    if not os.path.exists(path):
        print('不存在的文件')
        os.makedirs(path)
    else:
        print('文件已存在')
    file_name = month + '.' + day + '_' + cust_name + '.xls'
    with open(os.path.join(path, file_name), 'wb') as wf:
        for foo in file.chunks():
            wf.write(foo)
            wf.flush()
    return os.path.join(path, file_name)




if __name__ == '__main__':
    output_purchase_file('小龟龟', 1)
    print(settings.BASE_DIR)