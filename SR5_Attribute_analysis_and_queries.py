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

def Show_BoxPlot(DataFrame):
    ''' call this to show boxplots of my passed dataframe'''
    groupby = ['Physical Limit', 'Mental Limit', 'Social Limit', 'Attribute Sum']

    for i in range(len(groupby)):

        DataFrame.boxplot(column=['Body', 'Agility','Reaction', 'Strength',
                                  'Willpower', 'Logic','Intuition', 'Charisma'],
                          by=groupby[i],
                          notch=True,
                          showmeans=True)

    plt.show()


#Show_BoxPlot(df)

# Histogram plot

def Show_Histogram(DataFrame):
    '''Show a histograms when called'''

    # we don't need sums for this one
    DataFrame.pop('Attribute Sum')

    # stacked type
    plt.figure()
    DataFrame.plot(kind='hist',stacked=True,
                   bins=20)
    # indpendant type
    DataFrame.hist(sharex=True,
                   sharey=True,
                   bins=50,)
    
    plt.show()

    # again doing this just kinda shows the dataset sort of falls into a normal distribution
    
                
#Show_Histogram(df)


# Scatter Plot
def Show_ScatterPlot(DataFrame):
    '''Show an area plot when called'''

    # we don't need sums for this one
    DataFrame.pop('Attribute Sum')
    
    plt.figure()
    DataFrame.plot(kind='area', stacked=False)

    plt.show()

Show_AreaPlot(df)
