def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    return [{"item_id": item_id} for item_id in item_ids]

