#!/usr/bin/env python
# coding: utf-8

# ## 1. Welcome!
# <p><img src="https://assets.datacamp.com/production/project_1170/img/office_cast.jpeg" alt="Markdown">.</p>
# <p><strong>The Office!</strong> What started as a British mockumentary series about office culture in 2001 has since spawned ten other variants across the world, including an Israeli version (2010-13), a Hindi version (2019-), and even a French Canadian variant (2006-2007). Of all these iterations (including the original), the American series has been the longest-running, spanning 201 episodes over nine seasons.</p>
# <p>In this notebook, we will take a look at a dataset of The Office episodes, and try to understand how the popularity and quality of the series varied over time. To do so, we will use the following dataset: <code>datasets/office_episodes.csv</code>, which was downloaded from Kaggle <a href="https://www.kaggle.com/nehaprabhavalkar/the-office-dataset">here</a>.</p>
# <p>This dataset contains information on a variety of characteristics of each episode. In detail, these are:
# <br></p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/office_episodes.csv</b></div>
# <ul>
#     <li><b>episode_number:</b> Canonical episode number.</li>
#     <li><b>season:</b> Season in which the episode appeared.</li>
#     <li><b>episode_title:</b> Title of the episode.</li>
#     <li><b>description:</b> Description of the episode.</li>
#     <li><b>ratings:</b> Average IMDB rating.</li>
#     <li><b>votes:</b> Number of votes.</li>
#     <li><b>viewership_mil:</b> Number of US viewers in millions.</li>
#     <li><b>duration:</b> Duration in number of minutes.</li>
#     <li><b>release_date:</b> Airdate.</li>
#     <li><b>guest_stars:</b> Guest stars in the episode (if any).</li>
#     <li><b>director:</b> Director of the episode.</li>
#     <li><b>writers:</b> Writers of the episode.</li>
#     <li><b>has_guests:</b> True/False column for whether the episode contained guest stars.</li>
#     <li><b>scaled_ratings:</b> The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).</li>
# </ul>
#     </div>

# In[2]:


# Read in the CSV as a DataFrame
import pandas as pd 
office_episodes = pd.read_csv("datasets/office_episodes.csv")

# Print the first ten rows of the DataFrame
office_episodes[:10]


# In[3]:


# Create a color_scheme list
colors = []

# Iterate over rows of office_episodes to input color name to the colors list
for lab, row in office_episodes.iterrows():
    if row['scaled_ratings'] < 0.25:
        colors.append("red")
    elif 0.25 <= row['scaled_ratings'] < 0.50:
        colors.append("orange")
    elif 0.50 <= row['scaled_ratings'] < 0.75:
        colors.append("lightgreen")
    else:
        colors.append("darkgreen")
        
# Inspect the first 10 values in the list

colors[:10]


# In[4]:


# Create a sizing system:
# episodes with guest appearances have a marker size of 250
# episodes without are sized 25

sizes = []

for lab, row in office_episodes.iterrows():
    if row['has_guests'] == True:
        sizes.append(250)
    else:
        sizes.append(25)

# Inspect the first 10 values in the list      
sizes[:10]


# In[5]:


# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(11,7))

# Create a scatter plot
plt.scatter(office_episodes["episode_number"], office_episodes["viewership_mil"], c = colors, s = sizes)

# Create a title
plt.title('Popularity, Quality, and Guest Appearances on the Office', size = 16)

# Create an x-axis and an y-axis
plt.xlabel('Episode Number', size = 14)
plt.ylabel('Viewership (Millions)', size = 14)

# Show the plot
plt.show()


# In[6]:


# The highest view
highest_view = max(office_episodes["viewership_mil"])

# Filter the Dataframe row that has the most watched episode
most_watched_dataframe = office_episodes.loc[office_episodes["viewership_mil"] == highest_view]

# Top guest stars that were in that episode
top_stars = most_watched_dataframe[["guest_stars"]]
top_stars 

