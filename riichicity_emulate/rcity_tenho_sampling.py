import matplotlib.pyplot
import pandas as pd
import os
import random
import enum
import pydantic


def main():
    df = readcsv(10)
    if df is not None:
        plt = simulate_games(df, num_games=2000)
        plt.show()


class Platform(enum.IntEnum):
    rcity = 1
    tenhou = 2
    majsoul = 3


def readcsv(
    filter: int = 10,
    platform: Platform = Platform.rcity,
) -> pd.DataFrame | None:
    # CSVファイルの存在確認
    if platform == Platform.rcity:
        csv_file = "rcity_sanma.csv"
    elif platform == Platform.tenhou:
        csv_file = "tenho_sanma.csv"
    # majsoulは根本的に処理が違うので別ファイルで処理している

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


def simulate_games(
    df,
    num_games: int = 1000,
    max_score: int = 20000,
    custom_rates: None | list[int, int, int] = None,
):
    results = {}

    for index, row in df.iterrows():
        place = row["place"]
        win_score = row["win"]
        lose_score = row["lose"]
        draw_score = row["draw"]
        win_rate = row["win_rate"]
        lose_rate = row["lose_rate"]
        draw_rate = row["draw_rate"]
        init_score = row["init_score"]
        if custom_rates is not None:
            win_rate, lose_rate, draw_rate = custom_rates
        scores = [init_score]
        for _ in range(num_games):
            result = random.choices(
                [1, 2, 3], weights=[win_rate, lose_rate, draw_rate]
            )[0]
            if result == 1:
                scores.append(scores[-1] + win_score)
            elif result == 2:
                scores.append(scores[-1] + lose_score)
            else:
                scores.append(scores[-1] + draw_score)

        results[place] = scores
        df.at[index, "reached_goal"] = any(
            [score >= row["rank_up_score"] for score in scores]
        )
        df.at[index, "rank_down"] = any([score <= 0 for score in scores])

    matplotlib.pyplot.figure(figsize=(10, 6))
    for place, scores in results.items():
        matplotlib.pyplot.plot(range(num_games + 1), scores, label=place)
    matplotlib.pyplot.axhline(
        y=df.iloc[0]["init_score"], color="black", linestyle="--", label="initial score"
    )
    matplotlib.pyplot.axhline(
        y=df.iloc[0]["rank_up_score"], color="red", linestyle="--", label="goal"
    )
    matplotlib.pyplot.xlabel("Game")
    matplotlib.pyplot.ylabel("Score")
    matplotlib.pyplot.ylim(0, max_score)
    matplotlib.pyplot.title("Score Transition")
    matplotlib.pyplot.legend()
    return matplotlib.pyplot


class Result(pydantic.BaseModel):
    place: str
    is_reached_goal: bool
    is_koudan: bool


def simulate_games_core(
    df,
    num_games: int = 1000,
    custom_rates: None | list[int, int, int] = None,
) -> list[Result]:
    results = []

    for _, row in df.iterrows():
        place = row["place"]
        win_score = row["win"]
        lose_score = row["lose"]
        draw_score = row["draw"]
        win_rate = row["win_rate"]
        lose_rate = row["lose_rate"]
        draw_rate = row["draw_rate"]
        init_score = row["init_score"]
        rank_up_score = row["rank_up_score"]

        if custom_rates is not None:
            win_rate, lose_rate, draw_rate = custom_rates

        score = init_score
        is_reached_goal = False
        is_koudan = False

        for _ in range(num_games):
            result = random.choices(
                [1, 2, 3], weights=[win_rate, lose_rate, draw_rate]
            )[0]
            if result == 1:
                score += win_score
            elif result == 2:
                score += lose_score
            else:
                score += draw_score

            if score >= rank_up_score:
                is_reached_goal = True
                break
            if score <= 0:
                is_koudan = True
                break

        results.append(
            {"place": place, "is_reached_goal": is_reached_goal, "is_koudan": is_koudan}
        )

    return results


def testing(num: int = 20):
    """
    simulate_gamesをn回回して、結果を表示する
    """
    df = readcsv(10)

    if df is not None:
        place_stats = {}

        for _ in range(num):
            results = simulate_games_core(df, num_games=2000)
            for res in results:
                place = res["place"]
                if place not in place_stats:
                    place_stats[place] = {"promotions": [], "demotions": []}
                place_stats[place]["promotions"].append(res["is_reached_goal"])
                place_stats[place]["demotions"].append(res["is_koudan"])

        for place, stats in place_stats.items():
            print("-----")
            print(f"place: {place}")
            print(f"回した回数: {num}")
            print(f"昇段: {stats['promotions']}")
            print(f"後段: {stats['demotions']}")
            print(f"合計昇段回数: {sum(stats['promotions'])}")
            print(f"合計後段回数: {sum(stats['demotions'])}")


if __name__ == "__main__":
    testing()
