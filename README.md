# recipe_review_research

### By Heidi Tam and Kyla Park

---

### Introduction

Our culinary experiences have become very intertwined with data over the years,
whether it involves measuring the amount of an ingredient needed for
a recipe or ensuring you cooked a dish for the proper amount of time. We wanted
to consider the impact of data on a business setting. In this project, we are
considering a website where people post reviews to recipes.

We have access to two DataFrames:

1. **Interactions**: This DataFrame (731,927 rows) describes how people
   _interacted_ with each recipe. The columns included in this DataFrame are
   the user_id, recipe_id, date, rating, and review.
2. **Recipes**: This DataFrame (83,782) contains important information about what is
   included in the recipes and how to make them. Some examples of the columns
   in this DataFrame include tags, nutrition, n_steps (the number of steps in
   the recipe), steps (how to create the recipe), and n_ingredients (the number
   of ingredients in the recipe).

Our goal is to determine an attribute that is most closely associated with the
reviews columns. In other words, we are wondering whether the number of reviews
for a particular recipe is influenced by a specific column more strongly than
another.

This question intrigues us because in order for businesses to do well, they need
to analyze the behavior of their customers and how that impacts their businesses.
By analyzing what impacts the number of reviews a recipe receives, we can better
understand how restaurants and other culinary-related businesses can boost their
website engagement rate.

### Data Cleaning

For the data cleaning, we performed a left merge between the 'interactions'
and 'recipes' DataFrame. Then, we filled in all zeroes in the 'Rating' column
with np.NaN since it does not make sense for a recipe to receive a rating of
0; in this context, ratings can only be on a scale from 1 to 5. Therefore, a recipe
receiving a rating of 0 probably just means that a rating was not received for
that particular recipe.

Next, we considered what columns to add for our DataFrame. Since we are inspecting
the impact of other columns on reviews, we decided to make a column to make
reviews more interpretable: we made a column that tells us the number of total
reviews per recipe. To do so, we grouped the merged DataFrame by recipe ID,
and counted the number of reviews per recipe.

We performed something similar for the tags list; in this project, we do not
care about what the exact tags of each list are, so we created another column
called 'tag_count', which contains the number of tags for each recipe. This
way, we can use numbers to see how the number of tags a certain recipe has
influences the number of reviews.

By taking these steps, we make our data more usable to answer our question.

### Univariate Analysis

<iframe src="assets/univariate_plot1.html" width=800 height=600 frameBorder=0></iframe>

For our univariate analysis, we chose to plot the distribution of the number
of tags per recipe by creating a box-and-whisker plot. We discovered the number
of tags per recipe were usually between 11 (the first quartile) and 21 (the
third quartile). The median, 16, is a measure of central tendency that is not
strongly affected by outliers. Since the mean, about 16.29, is pretty close to
16, we can say that the distribution of tags is approximately symmetric. This
means that approximately half of our distribution has a number of tags that is
less than 16 and half has a number of tags that is greater than 16.

<iframe src="assets/univariate_plot2.html" width=800 height=600 frameBorder=0></iframe>

### Bivariate Analysis

<iframe src="assets/bivariate_plot1.html" width=800 height=600 frameBorder=0></iframe>

<iframe src="assets/bivariate_plot2.html" width=800 height=600 frameBorder=0></iframe>
