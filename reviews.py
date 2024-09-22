import pandas as pd

# Read the data from the zip file
data = pd.read_csv(r"C:\Users\william.ashby\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-WEAshby\data\winemag-data-130k-v2.csv.zip")

# Group by country and calculate the number of reviews and average points
summary = data.groupby('country').agg(
    number_of_reviews=('country', 'size'),
    average_points=('points', 'mean')
).reset_index()

summary=data.groupby('country').points.agg(['count',('points','mean')]).sort_values('count',ascending=False)

# Rename columns to match the example output
##summary.columns = ['country', 'count', 'points']

summary['points']=summary.points.round(1)
print(summary)

summary.to_csv(r'C:\Users\william.ashby\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-WEAshby\reviews_per_country.csv', index=False)

