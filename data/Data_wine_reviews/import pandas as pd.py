import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("C:\Users\william.ashby\github-classroom\CodeYou-Data-Jan2024\wine-reviews-exercise-WEAshby\data\winemag-data-130k-v2.csv.zip, index_col=0")

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()


