import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# old crappy way. takes a long time to load..
#print(open('Shadowrun_Attributes.csv').read())


# The pandas way...
# print(pd.read_csv('Shadowrun_Attributes.csv'))
# really fast but truncates the list, which is okay

# print(type(pd.read_csv('Shadowrun_Attributes.csv')))
# The type on this is: <class 'pandas.core.frame.DataFrame'>
# Since I know it's a dataframe object I can do stuff to it

df = pd.read_csv('Shadowrun_Attributes.csv')

# Box plots

def Show_Boxplots(DataFrame):
    ''' call this to show boxplots of my passed dataframe'''
    groupby = ['Physical Limit', 'Mental Limit', 'Social Limit', 'Attribute Sum']

    for i in range(len(groupby)):

        DataFrame.boxplot(column=['Body', 'Agility','Reaction', 'Strength',
                                  'Willpower', 'Logic','Intuition', 'Charisma'],
                          by=groupby[i],
                          notch=True,
                          showmeans=True)

    plt.show()


Show_Boxplots(df)

