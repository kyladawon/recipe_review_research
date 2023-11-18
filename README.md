# Investigating Recipe Reviews

### By Heidi Tam and Kyla Park

---

### Introduction

Our culinary experiences have become very intertwined with data over the years, whether it involves measuring the amount of an ingredient needed for a recipe or ensuring you cooked a dish for the proper amount of time. We wanted to consider the impact of data on a business setting. In this project, we are considering a website where people post reviews to recipes.

We have access to two DataFrames:

1. **Interactions**: This DataFrame (731,927 rows) describes how people
   _interacted_ with each recipe. The columns included in this DataFrame are the user_id, recipe_id, date, rating, and review.
2. **Recipes**: This DataFrame (83,782) contains important information about what is included in the recipes and how to make them. Some examples of the columns in this DataFrame include tags, nutrition, n_steps (the number of steps in the recipe), steps (how to create the recipe), and n_ingredients (the number of ingredients in the recipe).

Our goal is to determine an attribute that is most closely associated with the reviews columns. In other words, we are wondering whether the number of reviews for a particular recipe is influenced by a specific column more strongly than another.

This question intrigues us because in order for businesses to do well, they need to analyze the behavior of their customers and how that impacts their businesses. By analyzing what impacts the number of reviews a recipe receives, we can better understand how restaurants and other culinary-related businesses can boost their website engagement rate.

### Data Cleaning

For the data cleaning, we performed a left merge between the 'interactions'
and 'recipes' DataFrame. Then, we filled in all zeroes in the 'Rating' column with np.NaN since it does not make sense for a recipe to receive a rating of 0; in this context, ratings can only be on a scale from 1 to 5. Therefore, a recipe receiving a rating of 0 probably just means that a rating was not received for that particular recipe.

Next, we considered what columns to add for our DataFrame. Since we are inspecting the impact of other columns on reviews, we decided to make a column to make reviews more interpretable: we made a column that tells us the number of total reviews per recipe. To do so, we grouped the merged DataFrame by recipe ID, and counted the number of reviews per recipe.

We performed something similar for the tags list; in this project, we do not care about what the exact tags of each list are, so we created another column called 'tag_count', which contains the number of tags for each recipe. This way, we can use numbers to see how the number of tags a certain recipe has influences the number of reviews.

By taking these steps, we made our data more usable to answer our question.

### Univariate Analysis

<iframe src="assets/univariate_plot1.html" width=600 height=450 frameBorder=0></iframe>

For our univariate analysis, we chose to plot the distribution of the number of tags per recipe by creating a box-and-whisker plot. We discovered the number of tags per recipe were usually between 11 (the first quartile) and 21 (the third quartile). The median, 16, is a measure of central tendency that is not strongly affected by outliers. Since the mean, about 16.29, is pretty close to 16, we can say that the distribution of tags is approximately symmetric. This means that approximately half of our distribution has a number of tags that is less than 16 and half has a number of tags that is greater than 16.

<iframe src="assets/univariate_plot2.html" width=600 height=450 frameBorder=0></iframe>

The above is another univariate analysis we conducted, where we chose to plot the distribution of the number of reviews per recipe by creating a box-and-whisker plot. We discovered the number of reviews per recipe were usually between 1 (the first quartile) and 3 (the third quartile). The median, 2, is a measure of central tendency that is not strongly affected by outliers. Since the mean is about 2.797, it means that the plot is slightly skewed to the left.

### Bivariate Analysis

<iframe src="assets/bivariate_plot1.html" width=600 height=450 frameBorder=0></iframe>

For bivariate analysis, we created scatter plot with the number of tags on x-axis and the number of reviews on y-axis to see their relationships. The overall scatter plot looks like a bell curve. The middle of the bell curve shaped scatter plot seems to have higher scatter density with more data points. Moreover, the data point with high number of review counts seem to be outliers since they are apart from clusters.

<iframe src="assets/bivariate_plot2.html" width=600 height=450 frameBorder=0></iframe>

<<<<<<< HEAD
### Assessment of Missingness
#### NMAR Analysis
We believe the reviews column could be not missing at random (NMAR) if people
chose not to leave a review. This could be due to:
- **lack of time:** People may not have the time to write a review; additional
  columns we could study to investigate the lack of time include number of 
   hours worked a day, spent at school, or spent in extracurriculars.
- **assumed unimportance:** People may not consider leaving a review to be 
   important. Additional information we could gather is how people would
   rate the importance of answering surveys, but this information is also
   pretty useless, considering people who do not want to take the time to 
   leave a review probably also would not take the time to answer an extra question.
- **privacy concerns:** People may have privacy concerns and may not feel comfortable
  sharing their thoughts online. Similar to the last bullet point, we could
  obtain information where people rank how much they value privacy, but those
  who care a lot about privacy may just avoid the question. 


#### Missingness Dependency

Our null hypothesis is that the distribution of the tag count per recipe is 
the same whether or not the reviews are missing. Our alternative hypothesis 
is that the distribution of the tag count is different when the reviews are
missing compared to when it is not missing. Our observed statistic is a KS 
statistic comparing the tag counts and reviews per recipe for each 
distribution mentioned. 

<< embed graph here >>

We used a KS statistic since the shape of the 
distribution when the reviews are vs. are not missing are notably different.
When the reviews are missing, the distribution is fairly uniform, whereas 
when the reviews are not missing, the distribution appears generally normal.

Since our p-value is **0.245** > 0.05 (our significance level threshold), we 
fail to reject the null hypothesis, so the missingness of our data is 
**missing completely at random (MCAR)**. The missingness of the reviews has *no
correlation* with the distribution of tag counts per recipe.

We want to determine if there's a column that *does* affect the missingness 
of the reviews. We decided to investigate whether the missingness of the reviews
depends on the number of steps in a recipe.


Our new null hypothesis is that the distribution of the number of steps per 
recipe is the same whether or not the reviews are missing. Our alternative 
hypothesis is that the distribution of the number of steps is different 
when the reviews are missing compared to when it is not missing. Our 
observed statistic is a KS statistic comparing the number of steps and 
reviews per recipe for each distribution mentioned. 

< embed graph 2 here >

We used a KS statistic
since the shape of the distribution when the reviews are vs. are not 
missing are notably different. When the reviews are missing, the 
distribution is fairly uniform, whereas when the reviews are not missing,
the distribution appears generally normal. 

Since our p-value is **0.02** < 
0.05 (our significance level threshold), we reject the null hypothesis, 
so the missingness of our data is **missing at random (MAR)**. The missingness
of the reviews depends on the n-steps. A plausible explanation for this is
that the reviews are more likely to be missing when there are more steps 
in a recipe, less people are likely to follow the recipe since the dish 
will take more time to make and read, causing less people to ultimately 
leave a review.


=======
We also created different scatter plot with the number of steps on x-axis and the number of reviews on y-axis to see their relationships. The overall scatter plot is positively skewed and the data points are densely packed in the area where it represents less number of steps, which means that the recipe with more less steps have more reviews compared to the recipe with more steps.
>>>>>>> 26412b3a4b6769c1e4975e084506da210fe319bb

### Interesting Aggregates

We decided to take a closer look at which columns impact the missingness of reviews in the "reviews" column by creating a pivot table, where we grouped the data by the rating (from 1 to 5) and set the values to be the sum of the tag_count per recipe.

<<<<<<< HEAD
<< embed chart here >>

It seems as though recipes with a higher rating generally have 
more tags, whether a review is missing or not. However, we also noticed 
that recipes where the reviews were not missing also had significantly 
more tags than recipes with missing reviews. This is probably because 
certain recipes were more popular amongst chefs or food critics, meaning 
those recipes were more likely to receive a (higher) rating and review. 
When someone sees a recipe with positive ratings and reviews, they may be 
more inclined to try the recipe themselves, which results in significantly 
more people providing feedback for popular recipes, and therefore tagging 
recipes more often when the dish has a review(s) and a high rating.
=======
It seems as though recipes with a higher rating generally have
more tags, whether a review is missing or not. However, we also noticed
that recipes where the reviews were not missing also had significantly
more tags than recipes with missing reviews. This is probably because
certain recipes were more popular amongst chefs or food critics, meaning
those recipes were more likely to receive a (higher) rating and review.
When someone sees a recipe with positive ratings and reviews, they may be
more inclined to try the recipe themselves, which results in significantly
more people providing feedback for popular recipes, and therefore tagging
recipes more often when the dish has a review(s) and a high rating.

### Assessment of Missingness

#### NMAR Analysis

We believe the reviews column could be not missing at random (NMAR) if people chose not to leave a review. This could be due to:

- **lack of time:** People may not have the time to write a review; additional columns we could study to investigate the lack of time include number of hours worked a day, spent at school, or spent in extracurriculars.
- **assumed unimportance:** People may not consider leaving a review to be important. Additional information we could gather is how people would rate the importance of answering surveys, but this information is also pretty useless, considering people who do not want to take the time to leave a review probably also would not take the time to answer an extra question.
- **privacy concerns:** People may have privacy concerns and may not feel comfortable sharing their thoughts online. Similar to the last bullet point, we could obtain information where people rank how much they value privacy, but those who care a lot about privacy may just avoid the question.

#### Missingness Dependency

Our null hypothesis is that the distribution of the tag count per recipe is
the same whether or not the reviews are missing. Our alternative hypothesis
is that the distribution of the tag count is different when the reviews are
missing compared to when it is not missing. Our observed statistic is a KS
statistic comparing the tag counts and reviews per recipe for each
distribution mentioned.

<iframe src="assets/missing_depend_tag.html" width=600 height=450 frameBorder=0></iframe>

We used a KS statistic since the shape of the distribution when the reviews are vs. are not missing are notably different. When the reviews are missing, the distribution is fairly uniform, whereas when the reviews are not missing, the distribution appears generally normal.

Since our p-value is **0.245** > 0.05 (our significance level threshold), we fail to reject the null hypothesis, so the missingness of our data is
**missing completely at random (MCAR)**. The missingness of the reviews has _no correlation_ with the distribution of tag counts per recipe.

We want to determine if there's a column that _does_ affect the missingness of the reviews. We decided to investigate whether the missingness of the reviews depends on the number of steps in a recipe.

Our new null hypothesis is that the distribution of the number of steps per
recipe is the same whether or not the reviews are missing. Our alternative
hypothesis is that the distribution of the number of steps is different
when the reviews are missing compared to when it is not missing. Our
observed statistic is a KS statistic comparing the number of steps and
reviews per recipe for each distribution mentioned.

<iframe src="assets/missing_depend_nstep.html" width=600 height=450 frameBorder=0></iframe>

We used a KS statistic since the shape of the distribution when the reviews are vs. are not missing are notably different. When the reviews are missing, the distribution is fairly uniform, whereas when the reviews are not missing, the distribution appears generally normal.

Since our p-value is **0.02** < 0.05 (our significance level threshold), we reject the null hypothesis, so the missingness of our data is **missing at random (MAR)**. The missingness of the reviews depends on the n-steps. A plausible explanation for this is that the reviews are more likely to be missing when there are more steps in a recipe, less people are likely to follow the recipe since the dish will take more time to make and read, causing less people to ultimately leave a review.
>>>>>>> 26412b3a4b6769c1e4975e084506da210fe319bb
