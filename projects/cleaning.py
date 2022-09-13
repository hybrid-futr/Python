#The meat of this is from: https://realpython.com/python-data-cleaning-numpy-pandas/
#io - core tools for working with streams: https://docs.python.org/3/library/io.html
import pandas as pd
import requests
import io 

#CSV import code HELP: https://medium.com/towards-entrepreneurship/importing-a-csv-file-from-github-in-a-jupyter-notebook-e2c28e7e74a5
#Download the raw csv file from GitHub
url = "https://raw.githubusercontent.com/realpython/python-data-cleaning/master/Datasets/BL-Flickr-Images-Book.csv"
download = requests.get(url).content

#Read the content and turn it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Print out the first 5 rows of the dataframe
print (df.head, '\n')

#Drop dataframe columns
to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)
print (df.head(), '\n')

#Change the dataframe index
#df['Identifier'].is_unique. 
#note: I can set this index to anything!!! 
df = df.set_index('Place of Publication')
print (df.head(), '\n')

#Access individual record
print(df.loc[0], '\n') #position-based indexing
print(df.iloc[0], '\n') #label of the index

#Tidying up fields
#get_dtypes_counts has been depracated: https://stackoverflow.com/questions/62858271/attributeerror-dataframe-object-has-no-attribute-get-dtype-counts
print(df.dtypes.value_counts(), '\n')

#Clean date of publication info to have only one numeric value for the date
print(df.loc[1905:, 'Date of Publication'].head(10), '\n')

#Run the regex = r'^(\d{4})' expression on our dataset to find any four digits at the beginning of a string
extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(extr.head, '\n')

#Convert dtype to numeric and compute on the remaining valid values
df['Date of Publication'] = pd.to_numeric(extr)
print(df['Date of Publication'].dtype, '\n')
print(df['Date of Publication'].isnull().sum() / len(df), '\n')

#Place of publication
print(df['Place of Publication'].head(10), '\n')

#Two entries that were published in the same place, but have different naming conventions
print(df.loc[4157862], '\n')
print(df.loc[4159587], '\n')

#We use str.contains() to clean the 'London' entries in this column
pub = df['Place of Publication'] 
london = pub.str.contains('Tyne')
print(london[:10], '\n')