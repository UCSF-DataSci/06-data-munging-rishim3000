
# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 entries
- **Columns**: income_groups, age, gender, year, population

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
[income_groups]| [object] | [119412]       |  [9 vals]     |[N/A]   |
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [age]       | [float64] | [119495]       |  [102 vals]   | [50.00]|
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [gender]    | [float64] | [119811]       | [4 vals]      | [1.578]|
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [year]      | [float64] | [119516]       | [170 vals]    | [2025] |
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
|[population] | [float64] | [119378]       | [114926 vals] |[11298303]|
| ...         | ...       | ...            | ...           | ...    |




### Identified Issues

1. **[Missing Values]**
   - Description: I checked for the number of missing values across each column, and totaled them up
   - Affected Column(s): income_groups, age, gender, year, population
   - Example: when running the code df.isnull().sum(), I found that the age column has 6223 missing values.
   - Potential Impact: if we wanted to calculate any metrics of interest, such as mean or median, we wouldn't be able to apply those equations to the dataset, since missing values are present.

2. **[Duplicated values]**
   - Description: I checked for the number of duplicated values and totaled them up
   - Affected Column(s): There are no duplicated columns
   -Affected Row(s): When going across rows, I found that there were 5844 instances of a duplicated row
   - Potential Impact: Duplicated data is going to throw off the accuracy of any metric we try and measure, so getting rid of them is crucial to data cleaning.

3. **[Abnormal Distribution of Values]**
   - Description: I went across columns to check if the distribution of values matches what we'd expect to see in real life.
   -Affected column(s): 
      -Age: looking at the age column, the distribution is perfectly evenly spread across a range of 0-100 years, with Q1, mean, and Q3 at 25, 50, and 75, which is not accurate to real life
      -Year: the 'year' column also has many future years, which is impossible. For example, the Q3 and max values for this column are 2063 and 2119.
      -Gender - there are values of '3' scattered throughout the gender column, which does not line up with standard convention, with just 1 and 2 being the values for gender
   -Potential Impact: If we are dealing with synthetic data, there is no way to draw meaningful conclusions from it, so it should either be fixed or not used at all.

4. **[Typos in income_groups values]**
   - Description: I found that the income_group values sometimes had the string "_typo" attached to them
   -Affected column: income_groups
   -Potential Impact: This would make categorization of income group levels difficult, since the values aren't consistent. For example, if we wanted to get a simple frequency count of this column, the typo would make that needlessly difficult.

## 2. Data Cleaning Process

### Issue 1: [Missing Values]
- **Cleaning Method**: [I started by using dropna() to filter out rows with NAs]
- **Implementation**:
  ```df.dropna()
  # Include relevant code snippet
  ```
- **Justification**: [I found that the dropna() method was most effective in removing a lot of NA values.]
- **Impact**: 
  - Rows affected: [28077]
  - Data distribution change: [other than rows getting dropped, no significant changes in summary statistics of variables]

### Issue 2: [Duplicated Values]
- **Cleaning Method**: [I used the df.drop_duplicates() function to drop any duplicates found in the dataset]
- **Implementation**:
  ```df.drop_duplicates()
  # Include relevant code snippet
  ```
- **Justification**: [This is the most straightforward method to remove duplicates]
- **Impact**: 
  - Rows affected: [2215]
  - Data distribution change: [Again, other than the 2215 rows getting dropped, the summary stats remained virtually the same]
### Issue 3: [Abnormal Distribution of Values]
- **Cleaning Method**: [For age, I filtered out ages below 18, I also randomly distributed the age values throughout the dataset. For gender, I removed any rows with values of 3.0, converting all possible values to just 1 or 2. For years, I removed any values at or above 2025]
- **Implementation**: [Here, I have shown an example of what i did with the age column]
  ```
    age_vals_to_drop = df[df['year'] < 18.0].index #indexed any value under 18
    df.drop(age_vals_to_drop, inplace = True) #dropped unwanted year rows
    df['age'] = df['age'].astype(int)

    df['age'] = np.random.permutation(df['age'])
  # Include relevant code snippet
  ```
- **Justification**: [For age, I reasoned that adults would be more likely to take part in a survey such as the one this data is drawn from. Additionally, the previous distribution was perfectly evenly spread across values of 0 to 100. This is essentially meaningless in describing actual age patterns. Since this data has no integrity, I figured I can at least make it look more real, so i randomized the values. For gender, 3.0 as a vlue is not a standard value, so i removed those instances. I also didn't want any future year rows, since that is an impossibility]
- **Impact**: 
  - Rows affected: [16791 for age, 4220 for gender, 37453 for year]
  - Data distribution change: [The mean, std, and max values of gender changed due to 3.0 being removed. The statistics for age all increased, since values below 18 were deleted. The year statistics decreased significantly across all values except the min value, since all values past 2024 were removed.]
### Issue 4: [Typos in income_groups column]
- **Cleaning Method**: [I implemented a regex function to look for any income_groups column value ending with "_typo" and replace it with nothing.]
- **Implementation**:
  ```df['income_groups'] = df['income_groups'].str.replace('_typo$', '', regex = True)
  # Include relevant code snippet
  ```
- **Justification**: [Using regex expressions is the best and most efficient way to remove a typo that is consistent through the column]
- **Impact**: 
  - Rows affected: [1923]
  - Data distribution change: [No changes in the distribution of data, only changed the name of column value.]
## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [36782]
- **Columns**: [income_groups, age, gender, year, population]

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
[income_groups]| [object] | [36781]        |  [4 vals]     |[N/A]   |
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [age]       | [int64]   | [36781]        |  [101 vals]   | [59.15]|
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [gender]    | [int64]   | [36781]        | [2 vals]      | [1.501]|
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
| [year]      | [int64]   | [36781]        | [75 vals]     | [1987] |
| ...         | ...       | ...            | ...           | ...    |
|-------------|-----------|----------------|---------------|--------|
|[population] | [float64] | [36781]        | [36249 vals]  |[6.300164e+07]
| ...         | ...       | ...            | ...           | ...    |
### Summary of Changes
- [NAs and nans were dropped across all columns. The 3.0 value in gender was removed, as well as any years past 2024. Gender and year were also converetd to integer for convention standards. The income_groups column had any values with "_typo" at the end removed to fit the naming standard. As for age, I limited my age to those above 18 up to 100. I also redistributed the values randomly back into the dataset.]
- [The year, age, and gender metrics all changed significantly. Since all years above 2024 were removed, the mean, std, 25%, 50%, 75%, and max values all decreased as a result. As for gender, the max value changed from 3 to 2. Because of this, the mean and std decreased. The ages above 18 were the only ones kept, so the metrics increased.]

