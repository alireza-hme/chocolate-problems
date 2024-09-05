import re

from load_data import load_data


choc_df = load_data("data/raw/chocolate.csv")


def normalize_columns(df, column_mapping):
    df.rename(columns=column_mapping, inplace=True)  # rename all columns
    df = df.astype(
        {col: "string" for col in df.select_dtypes(include="object").columns}
    )  # convert object type to str

    df["Cocoa Percent"] = (
        df["Cocoa Percent"].apply(lambda x: re.sub(r"%$", "", x)).astype(float)
    )  # remove % from Cocoa columns

    return df


modified_columns = {
    "Specific Bean\nOrigin": "Specific Bean Origin",
    "Review\nDate": "Review Date",
    "Cocoa\nPercent": "Cocoa Percent",
    "Company\nLocation": "Company Location",
    "Bean\nType": "Bean Type",
    "Broad Bean\nOrigin": "Broad Bean Origin",
}


processed_df = normalize_columns(choc_df, modified_columns)
processed_df.to_csv("data/processed/cleaned_chocolate_data.csv", index=False)

processed_df.info()
