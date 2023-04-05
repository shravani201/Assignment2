import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(filename):
    df = pd.read_csv(filename, skiprows=4)
    df_years = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis=1).set_index(df['Country Name']).T
    df_countries = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis=1).set_index(df['Country Name'])
    df_main=df
    return df_years, df_countries

def clean_dataframe(df):
    df_cleaned = df.dropna(axis=1, thresh=int(0.5 * len(df))) # Drop columns with more than 50% missing values
    df_cleaned = df_cleaned.fillna(df_cleaned.mean()) # Fill missing values with mean of the respective column
    return df_cleaned

# Read and clean data
filename = "API_19_DS2_en_csv_v2_5312862.csv" # Replace with the dataset of your choice
df_years, df_countries = read_data(filename)
df_years_cleaned = clean_dataframe(df_years)
df_countries_cleaned = clean_dataframe(df_countries)

#df_main=clean_dataframe(df_main)
df_years_cleaned
df_countries_cleaned.head()
df_countries_cleaned.columns

# Summary statistics
summary_stats = df_countries_cleaned.describe()
print(summary_stats.T)

# Correlations between countries
correlations = df_countries_cleaned.corr()
#correlations
#latest_year
# Top 10 highest CO2 emitting countries in the most recent year
# Find the latest year with available data
# Top 10 highest CO2 emitting countries in the most recent year
latest_year = df_countries_cleaned.columns[-1]
top_10_emitters = df_countries_cleaned[latest_year].nlargest(10)


# Line plot: CO2 emissions for top 10 emitters over time
plt.figure()
import matplotlib.pyplot as plt

plt.figure()
sns.barplot(x=top_10_emitters.index, y=top_10_emitters.values)
plt.xticks(rotation=45)
plt.xlabel('Country Name')
plt.ylabel('CO2 emissions (kt)')
plt.title('Top 10 CO2 emitters in {}'.format(top_10_emitters.name))
plt.show()

# Scatter plot: Comparing two countries
country1 = 'United States'
country2 = 'China'
plt.figure()
plt.scatter(df_years_cleaned[country1], df_years_cleaned[country2])
plt.xlabel('{} CO2 emissions (kt)'.format(country1))
plt.ylabel('{} CO2 emissions (kt)'.format(country2))
plt.title('CO2 emissions: {} vs {}'.format(country1, country2))
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate total CO2 emissions by year
total_emissions_by_year = df_countries_cleaned.sum(axis=0)

# Plot the data
plt.figure(figsize=(20, 25))
sns.lineplot(x=total_emissions_by_year.index, y=total_emissions_by_year.values)
plt.title("Total CO2 Emissions by Year (1990-2015)")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.show()

# Plot the data
plt.figure(figsize=(10, 5))
sns.histplot(df_countries_cleaned['2015'], bins=50, kde=True)
plt.title("CO2 Emissions Distribution Across Countries in 2015")
plt.xlabel("CO2 Emissions")
plt.ylabel("Frequency")
plt.show()


