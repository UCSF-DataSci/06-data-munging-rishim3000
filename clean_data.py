import pandas as pd
import numpy as np


def cleanup_csv(filename, output):
    #Reading in the CSV file:

    df = pd.read_csv(filename)

    #Issue 1: Handling Missing Values
    ##Removing all na values using dropna() - from Part 1, we know that total number of missing vals is 30978
    ##below step has decreased number of rows by this amount, we know that we are left with a dataset with no missing values
    df = df.dropna()

    #Issue 2: Duplicated values
    ##This step automatically removes all duplicates that aren't the first occurrence, across all columns
    df = df.drop_duplicates()
    
    #Issue 3: Inconsistent values across multiple columns
    ##Age
    ###Analysis of age values in part 1 show an exactly even distribution of ages from 0-100, with a mean of 50, Q1 of 25, and Q3 of 75
    ###This is obviously very incorrect
    ###In order to filter this, I kept upper bound of age at 100, since humans have lived to that age before
    ###For lower bound, I set ages above 18, for adults 
    
    df['age'] = df['age'].astype(int)
    age_vals_to_drop = df[df['age'] < 18].index #indexed any value under 18
    df.drop(age_vals_to_drop, inplace = True) #dropped unwanted year rows

    df['age'] = np.random.permutation(df['age']) #randomized values of age and re-inserted them back into age column for more real look

    ##Gender
    ###There are values of 3.0 for gender, so I chose to drop those rows, leaving us with just values of 1 or 2.
    gender_vals_to_drop = df[df['gender'] == 3.0].index
    df.drop(gender_vals_to_drop, inplace = True)

    ##Future years
    year_vals_to_drop = df[df['year'] >= 2025.0].index #indexed any year value at or above 2025
    df.drop(year_vals_to_drop, inplace = True) #dropped unwanted year rows
    df['year'] = df['year'].astype(int)

    #Issue 4: income_group values
    
    #getting rid of '_typo' attached to end of value

    df['income_groups'] = df['income_groups'].str.replace('_typo$', '', regex = True)

    #Saving cleaned dataset as a csv file
    df.to_csv(output, index = False)

    print(f"Clean CSV saved as {output}")

#function takes messy dataset and returns cleaned dataset
cleanup_csv('messy_population_data.csv', 'cleaned_population_data.csv')  