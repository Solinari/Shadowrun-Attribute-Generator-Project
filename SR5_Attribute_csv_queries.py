import pandas as pd

# old crappy way. takes a long time to load..
#print(open('Shadowrun_Attributes.csv').read())


# The pandas way...

# really fast but truncates the list
print(type(pd.read_csv('Shadowrun_Attributes.csv')))
