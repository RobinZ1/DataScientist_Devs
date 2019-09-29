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

