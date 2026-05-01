class Order:
    def __init__(self, order_id, student_id, items, total_price, status="pending"):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.total_price = total_price
        self.status = status

def update_order_status(order_id, new_status):
    return {"order_id": order_id, "new_status": new_status}