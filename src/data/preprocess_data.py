from load_data import load_data


choc_df = load_data("data/processed/chocolate_cleaned.csv")

max_rating = choc_df["Rating"].max()
choc_df["Rating"] = choc_df["Rating"].apply(lambda x: x * (100 / max_rating))
choc_df.to_csv("data/processed/chocolate_preprocessed.csv", index=False)
