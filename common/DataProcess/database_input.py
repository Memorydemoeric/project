from purchase.models import Purchase, PurchaseDetail
from storage.models import StorageProduct


def purchase_detail_input(pro_id, ord_id, pro_count):
    pro_infos = StorageProduct.objects.filter(pro_id=pro_id).filter(is_delete=False)
    pur_infos = Purchase.objects.filter(pk=ord_id).filter(is_delete=False)
    repeat_pro = PurchaseDetail.objects.filter(pur_id_id=ord_id).filter(pur_pro_id=pro_id)
    if pro_infos and pur_infos:
        pro_info = pro_infos.first()
        pur_info = pur_infos.first()
        if repeat_pro:
            pur_detail = repeat_pro.first()
            pur_detail.pur_pro_count += int(pro_count)
            pur_detail.pur_pro_price += round(int(
                pro_count) * pro_info.pro_sell_unit_price * pur_info.cust_id.cust_rebate / 100, 2)
            return pur_detail
        else:
            pur_detail = PurchaseDetail()
            pur_detail.pur_pro_id = pro_id
            pur_detail.pur_pro_type = pro_info.pro_type
            pur_detail.pur_pro_count = pro_count
            pur_detail.pur_pro_unit_price = pro_info.pro_sell_unit_price
            pur_detail.pur_pro_price = round(int(
                pro_count) * pro_info.pro_sell_unit_price * pur_info.cust_id.cust_rebate / 100, 2)
            pur_detail.pur_id_id = ord_id
            return pur_detail