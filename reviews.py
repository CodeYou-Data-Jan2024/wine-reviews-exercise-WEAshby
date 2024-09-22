import pandas as pd

reviews=pd.read_csv(r"C:\Users\william.ashby\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-WEAshby\data\winemag-data-130k-v2.csv.zip",compression='zip')

summary=reviews.groupby('country').points.agg(['count',('points','mean')]).sort_values('count',ascending=False)

summary['points']=summary.points.round(1)
print(summary)

summary.to_csv(r'C:\Users\william.ashby\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-WEAshby\wine_reviews_per_country.csv', index=False)

