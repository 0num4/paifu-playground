import matplotlib.pyplot
import pandas as pd
import os
import random


def main():
    df = readcsv(10)
    if df is not None:
        plt = simulate_games(df, num_games=2000)
        plt.legend()
        plt.show()


def readcsv(filter: int = 10) -> pd.DataFrame | None:
    # CSVファイルの存在確認
    csv_file = "saka.csv"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, csv_file)
    if not os.path.isfile(csv_path):
        print(f"Error: {csv_file} does not exist.")
        return None

    # CSVファイルの読み込み
    df = pd.read_csv(csv_path)

    filtered_df = df[df.iloc[:, 0] == filter]

    # フィルター後のデータフレームを表示
    print(filtered_df)
    return filtered_df


def simulate_games(df, num_games: int = 1000, max_score: int = 20000):
    results = {}

    for _, row in df.iterrows():
        place = row["place"]
        win_score = row["win"]
        lose_score = row["lose"]
        draw_score = row["draw"]
        win_rate = row["win_rate"]
        lose_rate = row["lose_rate"]
        draw_rate = row["draw_rate"]
        init_score = row["init_score"]

        scores = [init_score]
        for _ in range(num_games):
            result = random.choices([1, 2, 3], weights=[win_rate, lose_rate, draw_rate])[0]
            if result == 1:
                scores.append(scores[-1] + win_score)
            elif result == 2:
                scores.append(scores[-1] + lose_score)
            else:
                scores.append(scores[-1] + draw_score)

        results[place] = scores

    matplotlib.pyplot.figure(figsize=(10, 6))
    for place, scores in results.items():
        matplotlib.pyplot.plot(range(num_games + 1), scores, label=place)
    matplotlib.pyplot.axhline(y=df.iloc[0]["init_score"], color="black", linestyle="--", label="initial score")
    matplotlib.pyplot.axhline(y=df.iloc[0]["rank_up_score"], color="red", linestyle="--", label="goal")
    matplotlib.pyplot.xlabel("Game")
    matplotlib.pyplot.ylabel("Score")
    matplotlib.pyplot.ylim(0, max_score)
    matplotlib.pyplot.title("Score Transition")
    return matplotlib.pyplot


if __name__ == "__main__":
    main()
