from load_data import load_data


choc_df = load_data("data/processed/chocolate_cleaned.csv")


def normalize_rating_col():
    max_rating = choc_df["Rating"].max()
    choc_df["Rating"] = choc_df["Rating"].apply(lambda x: x * (100 / max_rating))


def calc_price_100g(cocoa_percent, rating):
    return cocoa_percent * rating * 25


def calc_price_col():
    choc_df["price(100g)"] = choc_df.apply(
        lambda x: calc_price_100g(x["Cocoa Percent"], x["Rating"]), axis=1
    )


normalize_rating_col()
calc_price_col()


# Save the processed data
choc_df.to_csv("data/processed/chocolate_price.csv", index=False)
