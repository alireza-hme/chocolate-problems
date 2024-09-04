from load_data import load_data


choc_df = load_data("data/raw/chocolate.csv")


def rename_columns(df, column_mapping):
    df.rename(columns=column_mapping, inplace=True)
    return df


modified_columns = {
    "Specific Bean\nOrigin": "Specific Bean Origin",
    "Review\nDate": "Review Date",
    "Cocoa\nPercent": "Cocoa Percent",
    "Company\nLocation": "Company Location",
    "Bean\nType": "Bean Type",
    "Broad Bean\nOrigin": "Broad Bean Origin",
}


res = rename_columns(choc_df, modified_columns)

print(res)
