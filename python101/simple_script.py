import os
# in order to use a package, you have to import it
# adding `as pd` lets us refer to it with a shorter name
import pandas as pd

# load a data file
input_file = "/Users/peterhawthorne/Projects/RST/ki-tutorials/python101/data.csv"
df = pd.read_csv(input_file)
print()
print("Original Table:")
print(df.head())  # head selects just the first few rows
print()

# group the data by state, and compute the sum (this will drop the 
# non-numeric "county" column)
state_sums = df.groupby(by='state').sum()

# in the summed table, the summed column is still called "value", but
# it will make more sense for us to give it a distinguishable name
state_sums = state_sums.rename(columns={'value': 'state_total'})

# merge the sums back to the original table
df = pd.merge(df, state_sums, on='state')
print("After merge:")
print(df.head())
print()

# Calculate some additional statistics
df['county_fraction'] = df['value'] / df['state_total']
print("With county fraction:")
print(df.head())

output_file = os.path.join(os.path.dirname(input_file), "output.csv")
df.to_csv(output_file, index=False)
