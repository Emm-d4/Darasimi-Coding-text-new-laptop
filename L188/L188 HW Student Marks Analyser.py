import pandas as pd

#PART 1 - Create a Pands=as Series of top player scores
print("---PART 1: Pandas Series ---")
scores = [92, 91, 87, 99, 95]
students = pd.Series(scores, index=["Samuel", "Roman", "Michael", "Tywin", "Darasimi"])

print(students)
print()

# PART 2 - Create a DataFrame of gaming stats
print("--- PART 2: Pandas Data Frame ---")
data = {
    "player": ["Samuel", "Roman", "Michael", "Emmanuel", "Darasimi"],
    "grade":  [6, 6, 6, 6, 6],
    "score":  [92, 91, 87, 99, 95],
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