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


