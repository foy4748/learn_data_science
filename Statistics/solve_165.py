import pandas as pd
import os

data_file_path = os.path.abspath("./data/data_165.json")

df = pd.read_json(data_file_path)

# Creating midpoint column
# df.assign(midpoint=lambda dfa: (dfa["lower_limit"] + dfa["upper_limit"]) / 2)

df["midpoint"] = (df["lower_limit"] + df["upper_limit"]) / 2

df["male_fx_i"] = df["male_occurance"] * df["midpoint"]
df["female_fx_i"] = df["female_occurance"] * df["midpoint"]

sample_size_of_male = df["male_occurance"].sum()
sample_size_of_female = df["female_occurance"].sum()

average_age_of_male = df["male_fx_i"].sum() / sample_size_of_male
average_age_of_female = df["female_fx_i"].sum() / sample_size_of_female

combined_average_age = (
    sample_size_of_male * average_age_of_male
    + sample_size_of_female * average_age_of_female
) / (sample_size_of_male + sample_size_of_female)

print(
    f"""
average_age_of_male: {average_age_of_male}
average_age_of_female: {average_age_of_female}
combined_average_age: {combined_average_age}
        """
)
