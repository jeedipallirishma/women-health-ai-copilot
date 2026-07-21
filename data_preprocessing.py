import pandas as pd
import numpy as np



## load a dataset
survey_df=pd.read_csv(r"C:\Users\ramla\Downloads\Health– Women’s Health Survey .csv\survey_data.csv")

print("\nDataset Shape:")
print(survey_df.shape)

print("\nColumn Names:")
print(survey_df.columns.tolist())


survey_df.columns=survey_df.columns.str.strip()
print(survey_df.columns.to_list())

print("\nData Types:")
print(survey_df.dtypes)

print("\nFirst 5 Rows:")
print(survey_df.head())

# find missing values
missing_values=survey_df.isnull().sum()
print(missing_values)

print("Unique Height Values:")
print(survey_df["Height (cm)"].unique())

print("\nUnique Weight Values:")
print(survey_df["Weight (kg)"].unique())


survey_df["Height (cm)"]=pd.to_numeric(survey_df["Height (cm)"],errors="coerce")
survey_df["Weight (kg)"]=pd.to_numeric(survey_df["Weight (kg)"],errors="coerce")


height_median=survey_df["Height (cm)"].median()
survey_df["Height (cm)"] = survey_df["Height (cm)"].fillna(height_median)
weight_median=survey_df["Weight (kg)"].median()
survey_df["Weight (kg)"] = survey_df["Weight (kg)"].fillna(weight_median)

print(survey_df.isnull().sum())
print(survey_df["Height (cm)"].unique())
print(survey_df["Weight (kg)"].unique())

survey_df["Which symptoms do you experience?"] = survey_df["Which symptoms do you experience?"].fillna("No Symptoms Reported")
survey_df["Have you been diagnosed by a doctor with any of the following?"] = survey_df["Have you been diagnosed by a doctor with any of the following?"].fillna("Not Diagnosed")

print(survey_df.isnull().sum())


print(
    survey_df["Height (cm)"]
    .sort_values()
    .unique()
)

def convert_height(height):
    if height < 10:
        return height * 30.48
    else:
        return height
    

survey_df["Height (cm)"] = survey_df["Height (cm)"].apply(convert_height)

print(
    survey_df["Height (cm)"]
    .sort_values()
    .unique()
)



##Data Validation RuleLet's remove invalid heights.
survey_df = survey_df[
    (survey_df["Height (cm)"] >= 120)
    & (survey_df["Height (cm)"] <= 220)
]


###bmi
Height_in_meters = survey_df["Height (cm)"] / 100

survey_df["BMI"] = (
    survey_df["Weight (kg)"] /
    (Height_in_meters ** 2)
)

print("BMI column created")
print(survey_df[["Height (cm)", "Weight (kg)", "BMI"]].head())


print(
    survey_df[
        survey_df["BMI"] > 60
    ][["Height (cm)", "Weight (kg)", "BMI"]]
)

print(survey_df["BMI"].describe())
