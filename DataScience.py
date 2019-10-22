Sep 28

DATA EXPLORATION METHODS

# Describing a series of object

revs = f500["revenues"]
summary_stats = revs.describe()

# unique values counts for a column

country_freqs = f500['country'].value_counts()


ASSIGNMENT WITH PANDAS

# Creating a new column:
df["new column"] = 0

# Replacing a specific value in a database:

df.loc["name1", "ceo"] = "name2"

BOOLEAN INDEXING IN PANDAS

#Filtering a dataframe down on a specific value in a column:

any_bool = df["country"] == "USA"
result = df[any_bool].head()

# updating values using Boolean filtering

df.loc[df["column of values"] == 0, "column of values"] = np.nan
column_after = df["column of values"].values_count(dropna=False).head()



---------
Sep 29

USING ILOC[] TO SELECT BY INTEGER POSITION

# Selecting a value:
third_row_first_col = df.iloc[2,0]
# Selecting a row:
second_row = df.iloc[1]

CREATING BOOLEAN MASKS USING PANDAS METHOD

# selecting only null values in a column
rev_is_null = f500["revenue_change"].isnull()
# Filtering using Boolean series object:
rev_change_null = f500[rev_is_null]
# Selecting only the non-null values in a column:
f500[f500["previous_rank"].notnull()]

BOOLEAN OPERATORS

#Multiple required filtering criteria:
filter_big_rev_neg_profit = (f500["revenues"]>100000) & (f500["profits"]<0)
#Multiple optional filtering criteria:
filter_big_rev_neg_profit = (f500["revenues"]>100000) | (f500["profits"],0)

CONCEPTS

# To select values by axis labels, use loc[]. To select values by 
# integer locations, use iloc[]   When the label for an axis is 
# just its integer positions, these methods can be used intercahngeable

# Because using a loop doesn't take advantage of vectorization, it's 
# important to avoid doing so unless you absolutely have to. Boolean 
# operators are a powerful technique to take advantage of vectorization
# when filtering for expressing more granular filters


------
Oct.01

# READING A CSV FILE USING A SPECIFIC ENCODING
# using latin encoding

laptops = pd.read_csv('laptops.csv',encoding='Latin-1')

# READING IN A CSV FILE USING UTF-8:

laptops = pd.read_csv('laptops.csv',encoding='UTF-8')

# READING IN A CSV FILE USING WINDOWS-1251:

laptops = pd.read_csv('laptops.csv',encoding='Windows-1251')




# MODIFYING COLUMNS IN A DATAFRAME

# Renaming an existing column

laptops.rename(columns={'MANUfacture':'manufacture'},inplace=True)

# Converting a string column to float

laptops['screen_size'] = laptops['screen_size'].size.replace('"','').astype(float)

# Converting a string column to integer

laptops['ram'] = laptops['ram'].str.replace('GB','').astype(int)



#STRING COLUMN OPERATIONS

# extracting values from strings:

laptops['gpu_manufacturer'] = (laptops['gpu'].str.split().str[0])


#FIXING VALUES
# replaceing Values using a mapping dictionary


mapping_dict = {
    'Android':'Android',
    'Chrome OS':'Chrome OS',
    'Linux': 'Linux'
    'Mac OS': 'macOS'
    'No OS' : 'No OS'
    'windows' : 'Windiws'
    'macOS' : 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)

# dropping missing values:
laptops_no_null_rows = laptops.dropna(axis=0)

#ExPLORING CLEANED DATA
# exporting cleaned data:

df.to_csv('laptops_cleaned.csv',index=False)




-----------
October 5th

LINE CHARTS
# Importing the pyplot module:
import matplotlib.pyplot as plt

# Displaying the plot in a Jupyter Notebook cell:
%matplotlib inline

# Generating and displaying the plot:
plt.plot()
plt.show()

# Generating a line chart:

plt.plot(first_twelve['Date'], first_twelve['VALUE'])

# To rotate axis ticks:

plt.xticks(rotation=90)

# To add axis labels:

plt.xlabel('Month')
plt.ylabel('Unemployment Rate')

# To add a plot label:

plt.title('Monthly Unemployment Trends, 1948')





Oct 6th

# Creating a figure using the pyplot module

fig = plt.figure()

# Adding a subplot to an existing figure with 2 plots and 1 column, one 
aboev other

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# Generating a line chart within an Axes object

ax1.plot(unrate['DATE'][:12],unrate['VALUE'][:12])
ax2.plot(unrate['DATE'][12:24],unrate['VALUE'][12:24])

# Changing the dimensions of the figure with figsize parameter

fig = plt.figure(figsize=(12,5))

# Specifying the color for a certain line using the c parameter

plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],c='red')

# Creating a legend using the pyplot module and specifying its location

plt.legend(loc='upper left')

setting the title for an Axes object:

ax.set_title('Unemployment Trend, 1948')



Oct 7th

BAR PLOTS AND SCATTER PLOTS

# Generating a vertical bar plot:

pyplot.bar(bar_positions, bar_heights, width)

# or

Axes.bar(bar_positions, bar_heights, width)

# Using arange to return evenly seperated values

bar_positions = arange(5)+0.75

# Using Axes.set_ticks(), which takes in a list of tick locations

ax.set_ticks([1,2,3,4,5])

# Using Axes.set_xticklabel(), which takes in a list of labels

ax_set_xticklabels(['RT_user_nrom','Metacritic_user_nom','IMDB_norm'])

# Rotating the labels

ax_set_xticklabels(['RT_user_nrom','Metacritic_user_nom','IMDB_norm'], rotation = 90)

# Using Axes.scatter() to create a scatter plot

ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])


Oct 13 

IMPROVING PLOT AESTHETICS

# Turning ticks off
ax.tick_params(bottom='off',left='off',top='off',right='off')

# Removing spines for the right axis
ax.spines['right'].set_visible(False)

# Removing Spines for all axes
for key, spine in ax.spines.items():
    spine.set_visible(False)





Oct 14

PROJECT VISUALIZING THE GENDER GAPS IN COLLEGE DEGREES

fig = plt.figure(figsize=(16, 16))

## Generate first column of line charts. STEM degrees.
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    ax.axhline(50,c=(171/255,171/255,171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom='on')

## Generate second column of line charts. Liberal arts degrees.
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    ax.axhline(50,c=(171/255,171/255,171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif cat_index == 4:
        ax.tick_params(labelbottom='on')

## Generate third column of line charts. Other degrees.
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    ax.axhline(50,c=(171/255,171/255,171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        ax.tick_params(labelbottom='on')
    
#Export file before calling pyplot.show()    
fig.savefig('gender_degrees.png')
plt.show()







VISUALIZING GEOGRAPHICS DATA

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, ax = plt.subplots(figsize=(15,20))
plt.title("Scaled Up Earth With Coastlines")
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon = -180, urcrnrlon=180)
longitudes = airports['longitude'].tolist()
latitudes = airports['latitude'].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s = 1)
m.drawcoastlines()

def create_great_circles(df):
    for index, row in df.iterrows():
        end_lat, start_lat = row['end_lat'], row['start_lat']
        end_lon, start_lon = row['end_lon'], row['start_lon']
        if abs(end_lat - start_lat) < 180:
            if abs(end_lon - start_lon) < 180:
                m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)

dfw = geo_routes[geo_routes['source'] == 'DFW']
create_great_circles(dfw)
plt.show()




OCT 16

COMBINING DATA WITH PANDAS TAKEAWAYS

# CONCAT() FUNCTION

#Concatenate dataframes vertically (axis = 0)

pd.concat([df1, df2])

#Concatenate dataframes horizontally (axis = 1)

pd.concat([df1, df2], axis = 1)

#Concatenate dataframes with an inner join

pd.concat([df1, df2], join = 'inner')

# MERGE() FUNCTION

#join dataframes on index

pd.merge(left=df1, right=df2, left_index=True, right_index=True)

#Customize the suffix of columns contained in both dataframes

pd.merge(left=df1, right=df2, left_index = True, right_index = True, suffixes = ('left_df_suffix','right_df_suffix'))

#change the join type to left, right, or outer

pd.merge(left=df1, right=df2, how='join_type', left_index=True, right_index=True)

#join dataframes on a specific column:

pd.merge(left=df1, right=df2, on='Column_Name')

'''
Concept:
A key or join key is a shared index or column that is used to combine datframes together,

There are 4 kinds of joins:
    Inner: Returns the intersection of keys, or common values
    Outer: Returns the union of keys, or all values from each dataframe
    Left: Includes all of the rows from the left dataframe, along with any rows from the right dataframe with a common key. The result retains all
    columns from both of the original dataframes.
    Right: Includes all of the rows from the right dataframe, along with any rows from the left dataframe with a common key. The result retains all
    columns from both of the original dataframes

The pd.concat() function can combine multiple dataframes at once and is commonly used to 'stack' dataframes, or combine them vertically (axis = 0).
The pd.merge() function uses keys to perform database-style joins. It can only combine two dataframes at a time and can only merge dataframes horitzontally (axis=1)
'''



DATA AGGREGATION: TAKEAWAYS

# GROUPBY OBJECTS

#create a groupby object

df.groupby('col_to_groupby')

#select one column from a groupby object

df.groupby('col_to_groupby')['cols_selected']

#select multiple columns from a groupby object

df.groupby('col_to_groupby')[['col_selected1','col_selected2']]


#COMMON AGGREAGATION METHODS

mean(), sum(), size() calculate the size of groups, count() calculate the count of values in groups, min(), max()

#GROUPY.AGG() METHOD

# Apply one function to a GroupBy object

df.groupby('col_to_groupby').agg(function name)

# Apply multiple functions to a GroupBy object

df.groupby('col_to_groupby').agg([function_name1,function_name2,function_name3])

# Apply a custom function to a GroupBy object

df.groupby('col_to_groupby').agg(custom_function)


#AGGREGATION WITH THE DATAFRAME.PIVOT_TABLE METHOD

# apply only one function

df.pivot_table(value='col_to_aggregate', index='col_to_groupby', aggfunc=function_name)

# apply multiple functions

df.pivot_table(value='col_to_aggregate', index='col_to_groupby',aggfunc=[function_name1, function_name2, function_name3])

# aggregate multiple columns

df.pivot_table(['col_to_aggregate1','col_to_aggregate2'], 'col_to_groupby', aggfunc=function_name)

# calculate the grand total for the aggregation column:

df.pivot_table(['col_to_aggregate1, col_to_aggregate2'],'col_to_groupby',aggfunc=function_name, margins = True)

'''
Concepts

Aggregation is aplying a statistical operation to groups of data. It reduces dimensionality so that the dataframe returned will contain just one value
for each group. The aggregation process can be broken down into three steps:
    split the dataframe into groups
    apply a function to each group
    combine the results into one data structure

The groupby operation optimizes the split-apply-combine process. It can be broken down into two steps:
    create a groupby object
    call an aggregation functioin

Creating the groupby object is an intermediate step that allows us to optimize our work. It contains information on how to group the dataframe, 
but nothing is actually computed until a function is called
'''


OCT 21ST

WORKING WITH STRINGS IN PANDAS

#REGULAR EXPRESSIONS
# To match multiple characters, specify the characters between "[]"

pattern = r"[Nn]ational accounts"

# To match a range of characters or numbers, use:

pattern = r"[0-9]"

# To create a capturing group, or indicate that only the character pattern match
# should be extracted, specify the characters between "()"

pattern = r"([1-2][0-9][0-9][0-9])"

# To repeat characters, use "{}" to repeat pattern "[0-9]" three times

pattern = r"[1-2][0-9]{3}"

#VECTORIZED STRING METHODS

# Find specific strings or substrings in a column

df[col_name].str.contains(pattern)

# Extract specific strings or substrings in a column

df[col_name].str.extract(pattern)

# Extract more than one group of patterns from a column

df[col_name].str.extractall(pattern)

# Replace a regex or string in a column with another string

df[col_name].str.replace(pattern, replacement_string)

'''Concepts: Pandas has built in a number of vectorized methods that perform the
same operations for strings in Series as Python string methods
A regular expression is a sequence of characters that describes a search pattern.
In pandas, regular expression is integrated with vectorized string methods to make
finding and extracting patterns of characters easier.
'''

