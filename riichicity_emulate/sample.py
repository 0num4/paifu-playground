import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def main():
    readcsv()
    # x = np.linspace(0, 10, 100)
    # y = np.sin(x)
    # plt.plot(x, y)
    # plt.show()


def readcsv() -> pd.DataFrame | None:
    # CSVファイルの存在確認
    csv_file = "saka.csv"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, csv_file)
    if not os.path.isfile(csv_path):
        print(f"Error: {csv_file} does not exist.")
        return None

    # CSVファイルの読み込み
    df = pd.read_csv(csv_path)

    # 最初の列が10のもののみにフィルター
    filtered_df = df[df.iloc[:, 0] == 10]

    # フィルター後のデータフレームを表示
    print(filtered_df)
    return filtered_df


if __name__ == "__main__":
    main()
