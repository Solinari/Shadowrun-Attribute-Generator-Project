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

    # stacked type - this is colored*
    # The stack is somewhat hard to read..
    #plt.figure()
    DataFrame.plot(kind='hist',stacked=True,
                   bins=20)
    
    # indpendant Histograms
        
    DataFrame.hist(sharex=True,
                   sharey=True,
                   bins=20)
    
    plt.show()

    # again doing this just kinda shows the dataset sort of falls into a normal distribution
    
                
#Show_Histogram(df)


# Scatter Plot
def Show_ScatterPlot(DataFrame):
    '''Show a series of scatter plots when called'''

    # we don't need sums for this one
    DataFrame.pop('Attribute Sum')
    
    # create a 2-dimensional list
    attribute = ['Body', 'Agility','Reaction', 'Strength','Willpower', 'Logic','Intuition', 'Charisma']
    limit = ['Physical Limit', 'Mental Limit', 'Social Limit']

    # all 8 attributes on x plotted against all 3 limits on y, each in their own graph
    # takes a bit to load 24 scatter plots that do all these comparisons though.
    for i in range(len(attribute)):
        for j in range(len(limit)):
            DataFrame.plot(kind='scatter',x=attribute[i], y=limit[j])

    plt.show()

    # These will show form of the spread of min/max attributes needed for any such attribute..this was cool!

Show_ScatterPlot(df)
