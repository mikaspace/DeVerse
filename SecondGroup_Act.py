import time
import random
from concurrent.futures import ThreadPoolExecutor
import threading

db_lock = threading.Lock()

def validate_payment(order_id):
    time.sleep(0.00004)
    return f"payment_ok_{order_id}"

def check_inventory(order_id):
    time.sleep(0.00003)
    return f"inventory_ok_{order_id}"

def calculate_shipping(order_id):
    time.sleep(0.00002)
    return round(random.uniform(3.5, 15.0), 2)

def generate_invoice(order_id):
    time.sleep(0.00003)
    return f"INV-{order_id:06d}"

def update_database(order_id, invoice_id):
    with db_lock:
        time.sleep(0.00008)
        return f"db_written_{order_id}"

def process_order(order_id):
    payment   = validate_payment(order_id)
    inventory = check_inventory(order_id)
    shipping  = calculate_shipping(order_id)
    invoice   = generate_invoice(order_id)
    db        = update_database(order_id, invoice)
    return {
        "order_id":  order_id,
        "payment":   payment,
        "inventory": inventory,
        "shipping":  shipping,
        "invoice":   invoice,
        "db":        db,
        "status":    "completed"
    }

def sequential_processing(orders):
    return [process_order(order) for order in orders]

def parallel_processing(orders, max_workers=80):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_order, orders))
    return results

if __name__ == "__main__":
    NUM_ORDERS  = 5000
    MAX_WORKERS = 80
    orders = list(range(1, NUM_ORDERS + 1))

    print(f"Orders: {NUM_ORDERS} | Workers: {MAX_WORKERS}\n")

    start = time.time()
    sequential_processing(orders)
    seq_time = time.time() - start

    start = time.time()
    parallel_processing(orders, max_workers=MAX_WORKERS)
    par_time = time.time() - start

    speedup = seq_time / par_time

    print(f"Sequential Time : {seq_time:.4f} seconds")
    print(f"Parallel Time   : {par_time:.4f} seconds")
    print(f"Speedup         : {speedup:.2f}x")
