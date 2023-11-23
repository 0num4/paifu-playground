import random
import time

desired_length = len("615233210")

# 6で始まるランダムなIDを生成
first_digit = "6"

for i in range(100):
    random_id = first_digit + "".join([str(random.randint(0, 9)) for _ in range(desired_length - 1)])
    print(random_id)
    sleep_time = random.uniform(0.4, 1.7)

    # スリープ
    time.sleep(sleep_time)
