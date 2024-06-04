import random


def random_test():
    # 10回の試行を行う
    for _ in range(10):
        result = random.choices([1, 2, 3], weights=[35, 45, 20])[0]
        print(result)


if __name__ == "__main__":
    random_test()
