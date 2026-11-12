def get_uniqe_id(products):
    latest_id = max(products, key=lambda p: p["id"])
    return latest_id["id"] + 1
