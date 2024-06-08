import random


def random_test(num_trials=10000):
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for _ in range(num_trials):
        result = random.choices([1, 2, 3], weights=[0.3636, 0.3322, 0.3042])[0]
        if result == 1:
            count_1 += 1
        elif result == 2:
            count_2 += 1
        else:
            count_3 += 1

    print(f"Number of trials: {num_trials}")
    print(f"Count of 1: {count_1} ({count_1 / num_trials * 100:.2f}%)")
    print(f"Count of 2: {count_2} ({count_2 / num_trials * 100:.2f}%)")
    print(f"Count of 3: {count_3} ({count_3 / num_trials * 100:.2f}%)")


if __name__ == "__main__":
    random_test()
