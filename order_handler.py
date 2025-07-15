# order_handler.py

import json
from config import ADMIN_ID

ORDER_FILE = "orders.json"

def load_orders():
    try:
        with open(ORDER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_order(order):
    orders = load_orders()
    orders.append(order)
    with open(ORDER_FILE, "w") as f:
        json.dump(orders, f, indent=4)

def get_orders_text():
    orders = load_orders()
    if not orders:
        return "No orders yet."
    msg = ""
    for i, order in enumerate(orders, 1):
        msg += f"🆔 Order #{i}\n👤 {order['username']} ({order['user_id']})\n"
        msg += f"📦 Qty: {order['quantity']}\n🌐 Country: {order['country']}\n"
        msg += f"🔑 Password: {'Custom' if order['custom_pass'] else 'Auto'}\n"
        msg += f"🔐 2FA: {'Yes' if order['two_fa'] else 'No'}\n"
        msg += f"📄 Backup: {'Yes' if order['backup_code'] else 'No'}\n"
        msg += f"💰 Price: ${order['price']}\n---\n"
    return msg
