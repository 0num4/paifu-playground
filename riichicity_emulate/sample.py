import matplotlib.pyplot as plt
import pandas as pd
import os
import random


def main():
    df = readcsv()
    if df is not None:
        simulate_games(df, num_games=2000, initial_score=3800)


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


def simulate_games(df, num_games, initial_score):
    results = {}

    for _, row in df.iterrows():
        place = row["place"]
        win_score = row["win"]
        lose_score = row["lose"]
        draw_score = row["draw"]
        win_rate = row["win_rate"]
        lose_rate = row["lose_rate"]
        draw_rate = row["draw_rate"]

        scores = [initial_score]
        for _ in range(num_games):
            result = random.choices([1, 2, 3], weights=[win_rate, lose_rate, draw_rate])[0]
            if result == 1:
                scores.append(scores[-1] + win_score)
            elif result == 2:
                scores.append(scores[-1] + lose_score)
            else:
                scores.append(scores[-1] + draw_score)

        results[place] = scores

    plt.figure(figsize=(10, 6))
    for place, scores in results.items():
        plt.plot(range(num_games + 1), scores, label=place)
    plt.axhline(y=initial_score, color="black", linestyle="--", label="initial score")
    plt.axhline(y=7600, color="red", linestyle="--", label="goal")
    plt.xlabel("Game")
    plt.ylabel("Score")
    plt.ylim(0, 20000)
    plt.title("Score Transition")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
