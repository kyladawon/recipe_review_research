import pandas as pd
import numpy as np
import os

import plotly.express as px
pd.options.plotting.backend = 'plotly'

recipes = pd.read_csv('food_data/RAW_recipes.csv')
interactions = pd.read_csv('food_data/RAW_interactions.csv')

raw_merged = recipes.merge(interactions, how = 'left', left_on = 'id', right_on = 'recipe_id')
nan_merged = raw_merged.replace(0, np.nan)

with_average_ratings = raw_merged.groupby('recipe_id').mean()['rating']
merged_w_average_ratings = nan_merged.merge(with_average_ratings, how = 'left', left_on = 'id', right_on = 'recipe_id').set_index('id')
cleaned_merged = (merged_w_average_ratings
                .rename({'rating_x': 'rating', 'rating_y': 'average_rating'}, axis=1)
               .fillna(np.nan))

# tag count
cleaned_merged['tags'] = cleaned_merged['tags'].str.strip("[]").str.replace("'", "").str.split(", ") 
cleaned_merged = cleaned_merged.assign(tag_count = cleaned_merged['tags'].apply(len))

# review count
final_merged = cleaned_merged.assign(review_count = cleaned_merged.groupby('recipe_id')['review'].count()).reset_index()
                               
final_merged