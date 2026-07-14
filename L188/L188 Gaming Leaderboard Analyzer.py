import pandas as pd

#PART 1 - Create a Pands=as Series of top player scores
print("---PART 1: Pandas Series ---")
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=["NightWolf", "StarBlaze", "PixelKing", "cyberFox", "IronStorm"])

print(players)
print()

# PART 2 - Create a DataFrame of gaming stats
print("--- PART 2: Pandas Data Frame ---")
data = {
    "player": ["NightWolf", "StarBlaze", "PixelKing", "cyberFox", "IronStorm"],
    "Level":  [42, 38, 35, 30, 27],
    "score":  [98500, 87200, 76400, 65100, 54800],
    "Wins":   [210, 185, 162, 140, 118]
}

df = pd.DataFrame(data)
print(df)
print()

# PART 3 - Access rows using .loc
print("--- PART 3: Accessing Rows ---")
print("Row 0 (top player):")
print(df.loc[0])
print()

print("Rows 2 and 3:")
print(df.loc[2:3])
print()

# PART 4 - Load leadebord.csv and view the data
print("--- PART 4: Reading a CSV File ---")
full_df = pd.read_csv(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L188\leaderboard.csv")
print("First 5 rows (head):")
print(full_df.head())
print()

print("First 3 rows (tail):")
print(full_df.tail())
print()

print("dataset info:")
print(full_df.info())
print()

# PART 5 - Clean the data
print("---PART 5: Cleaning Data ---")
print("Rows with missing values removed (dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()

print("Missing values filled with 0 (fillna):")
filled_df = full_df.fillna(0)
print(filled_df.to_string())