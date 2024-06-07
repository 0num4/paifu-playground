import matplotlib.pyplot
import pandas as pd
import os
import random


def main():
    df = readcsv("gou3")
    if df is not None and df.empty is False:
        plt = simulate_games(df, num_games=2000)
        plt.show()


def readcsv() -> pd.DataFrame | None:
    # CSVファイルの存在確認
    csv_file = "majsoul_sanma.csv"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, csv_file)
    if not os.path.isfile(csv_path):
        print(f"Error: {csv_file} does not exist.")
        return None

    # CSVファイルの読み込み
    df = pd.read_csv(csv_path)

    # filtered_df = df[df.iloc[:, 0] == dan_filter]

    # フィルター後のデータフレームを表示
    print(df)
    return df


def simulate_games(df, num_games: int = 1000, max_score: int = 20000):
    results = {}
    matplotlib.pyplot.figure(figsize=(10, 6))
    for index, row in df.iterrows():
        dan = row["dan"]
        # place = row["place"]
        win_score = row["win"]
        lose_score = row["lose"]
        draw_score = row["draw"]
        win_rate = row["win_rate"]
        lose_rate = row["lose_rate"]
        draw_rate = row["draw_rate"]
        init_score = row["init_score"]
        rank_up_score = row["rank_up_score"]
        matplotlib.pyplot.axhline(y=init_score, color="black", linestyle="--", label=f"{dan} initial score")
        matplotlib.pyplot.axhline(y=rank_up_score, color="red", linestyle="--", label=f"{dan} goal")
        scores = [init_score]
        for _ in range(num_games):
            result = random.choices([1, 2, 3], weights=[win_rate, lose_rate, draw_rate])[0]
            if result == 1:
                scores.append(scores[-1] + win_score)
            elif result == 2:
                scores.append(scores[-1] + lose_score)
            else:
                scores.append(scores[-1] + draw_score)

        results[dan] = scores
        df.at[index, "reached_goal"] = any([score >= row["rank_up_score"] for score in scores])
        df.at[index, "rank_down"] = any([score <= 0 for score in scores])


    for dan, scores in results.items():
        matplotlib.pyplot.plot(range(num_games + 1), scores, label=dan)

    matplotlib.pyplot.xlabel("Game")
    matplotlib.pyplot.ylabel("Score")
    matplotlib.pyplot.ylim(0, max_score)
    matplotlib.pyplot.title("Score Transition")
    matplotlib.pyplot.legend()
    return matplotlib.pyplot


if __name__ == "__main__":
    main()
