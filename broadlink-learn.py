import time
import base64
import broadlink
import sys

device_ip = "192.168.1.2"
device = broadlink.hello(device_ip)

try:
    device.auth()
except Exception as e:
    print(f"Auth error: {e}")
    exit(1)

while True:
    label = input("Give me some label for next input button: ")
    device.enter_learning()

    ir_code = None
    start_time = time.time()
    while ir_code is None and time.time() - start_time < 10:
        try:
            ir_code = device.check_data()
        except Exception as e:
            time.sleep(1)
            print(f"Waiting for input...")

    if ir_code is None:
        print("Timeout or error.")
    else:
        base64_ir_code = base64.b64encode(ir_code).decode('utf-8')
        print(f"{label}: {base64_ir_code}")
