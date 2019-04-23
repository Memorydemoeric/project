def translate_order_detail(detail):
    order_detail = detail
    return order_detail


class OrderDetail(object):

    def __init__(self, pur_pro_id, pur_count=0, pur_pro_count=0, pur_half_count=0, pur_total=0):
        self.pur_pro_id = pur_pro_id
        self.pur_count = pur_count
        self.pur_pro_count = pur_pro_count
        self.pur_half_count = pur_half_count
        self.pur_total = pur_total