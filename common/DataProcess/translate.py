def querydict_to_dict(querydict):
    dict = {}
    for k, v in querydict.items():
        dict.update({k: v})
    return dict