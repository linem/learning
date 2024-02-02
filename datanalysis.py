# workflow

## 1. set objective
## 2. aquire data
## 3. clean data
## 4. analyze data
## 5. communicate findings


# objective
## relationship between rotten tomato rating and imdb rating?
## insights from analysis of movie length?
## relationship between no of killed enemies and the movie rating?

# aquire data
import pandas as pd
import random

file_path = "data/jamesbond_tutorial.csv"
james_bond_data = pd.read_csv(file_path).convert_dtypes()

#print(james_bond_data.head())
#print(james_bond_data.shape)  # nrows, ncols
#print(james_bond_data.info())

# clean data
new_column_names = {
    "Release": "release_date",
    "Movie": "movie_title",
    "Bond": "bond_actor",
    "Bond_Car_MFG": "car_manufacturer",
    "US_Gross": "income_usa",
    "World_Gross": "income_world",
    "Budget": "movie_budget",
    "Film_Length": "film_length",
    "Avg_User_IMDB": "imdb",
    "Avg_User_Rtn_Tom": "rotten_tomatoes",
    "Martinis": "martinis_consumed",
    "Kills_Bond": "bond_kills",
    }

data = james_bond_data.rename(columns = new_column_names).convert_dtypes()
data = data[list(new_column_names.values())]

#print(data.info())
## two columns have missing values and the Dtype is turned to Float64
pd.set_option('display.max_columns', 1000)
print(data.loc[data.isna().any(axis="columns")])

## missing values are 7.1 and 6.8

data = james_bond_data.rename(columns=new_column_names).combine_first(
    pd.DataFrame({"imdb": {10: 7.1}, "rotten_tomatoes": {10: 6.8}})
)