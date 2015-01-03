import math
import pandas as pd

# This is the combinatoric definition of my data set by the rules of Shadowrun 5th Edition
# the final if condition is a player may only have 1 attribute with 5 points in it at creation
# so an attribute spread with two or more 5's is possible, but the rules do not allow for this.

attr12 = [[i, j, k, l, m, n, o, p] for i in range(0, 6)
              for j in range(0, 6)
             for k in range(0, 6)
            for l in range(0, 6)
           for m in range(0, 6)
          for n in range(0, 6)
         for o in range(0, 6)
        for p in range(0, 6)
       if (i + j + k + l + m + n + o + p) == 12
          and ((i, j, k, l, m, n, o, p).count(5) <= 1)]

attr14 = [[i, j, k, l, m, n, o, p] for i in range(0, 6)
              for j in range(0, 6)
             for k in range(0, 6)
            for l in range(0, 6)
           for m in range(0, 6)
          for n in range(0, 6)
         for o in range(0, 6)
        for p in range(0, 6)
       if (i + j + k + l + m + n + o + p) == 14
          and ((i, j, k, l, m, n, o, p).count(5) <= 1)]

attr16 = [[i, j, k, l, m, n, o, p] for i in range(0, 6)
              for j in range(0, 6)
             for k in range(0, 6)
            for l in range(0, 6)
           for m in range(0, 6)
          for n in range(0, 6)
         for o in range(0, 6)
        for p in range(0, 6)
       if (i + j + k + l + m + n + o + p) == 16
          and ((i, j, k, l, m, n, o, p).count(5) <= 1)]

attr20 = [[i, j, k, l, m, n, o, p] for i in range(0, 6)
              for j in range(0, 6)
             for k in range(0, 6)
            for l in range(0, 6)
           for m in range(0, 6)
          for n in range(0, 6)
         for o in range(0, 6)
        for p in range(0, 6)
       if (i + j + k + l + m + n + o + p) == 20
          and ((i, j, k, l, m, n, o, p).count(5) <= 1)]

attr24 = [[i, j, k, l, m, n, o, p] for i in range(0, 6)
              for j in range(0, 6)
             for k in range(0, 6)
            for l in range(0, 6)
           for m in range(0, 6)
          for n in range(0, 6)
         for o in range(0, 6)
        for p in range(0, 6)
       if (i + j + k + l + m + n + o + p) == 24
          and ((i, j, k, l, m, n, o, p).count(5) <= 1)]

attr_list = []

attr_list.append(attr12)
attr_list.append(attr14)
attr_list.append(attr16)
attr_list.append(attr20)
attr_list.append(attr24)

essence = 6

def limit_maker(combination):
    '''pass an attribute set combination to find the limits and return the limits as a list'''
    global essence

    # the python interpreter expects float conversion BEFORE division
    # not declaring the float before taking the ceil led to all sorts of off by 1 errors before
    physical = math.ceil( float( (2 * (combination[3] + 1) ) + (combination[0] + 1) + (combination[2] + 1) ) / 3)
    mental =   math.ceil( float( (2 * (combination[5] + 1) ) + (combination[6] + 1) + (combination[4] + 1) ) / 3)
    social =   math.ceil( float( (2 * (combination[7] + 1) ) + (combination[4] + 1) +             essence  ) / 3)

    return [physical, mental, social]

#database append function
def Attribute_to_DataFrame(attributes):
    '''make DataFrame to append all data to, then write to a csv once'''

    # Lists  of values to be inserted into the dataFrame once appended below
    Bod = []
    Agi = []
    Rea = []
    Str = []
    Wil = []
    Log = []
    Int = []
    Cha = []
    Phy = []
    Men = []
    Soc = []
    Sum = []

    # iterate through my gigantic list of list comprehnsion made lists and append it to lists for the data frame
    for priority in attributes:
        for attr_set in priority:
            
            # pass the list to the above function perform the calculations for the limits
            limits = limit_maker(attr_set)

            # then append that the attr_set, limits, and the sum of the attributes to the dataframe lists
            Bod.append(attr_set[0])
            Agi.append(attr_set[1])
            Rea.append(attr_set[2])
            Str.append(attr_set[3])
            Wil.append(attr_set[4])
            Log.append(attr_set[5])
            Int.append(attr_set[6])
            Cha.append(attr_set[7])
            Phy.append(limits[0])
            Men.append(limits[1])
            Soc.append(limits[2])
            Sum.append(sum(attr_set))

    # Construct Key : Value pairs to their list of scores
    # I effectively pivoted the table for how the frame want it to be passed to write to a .csv
    AttributeFrame = pd.DataFrame({ 'Body' : Bod,
                                    'Agility' : Agi,
                                    'Reaction' : Rea,
                                    'Strength' : Str,
                                    'Willpower' : Wil,
                                    'Logic' : Log,
                                    'Intuition' : Int,
                                    'Charisma' : Cha,
                                    'Physical Limit' : Phy,
                                    'Mental Limit' : Men,
                                    'Social Limit' : Soc,
                                    'Attribute Sum' : Sum})

    # The extra arguments are needed due to how pandas auto alphabatizes my columns
    # Before that made the data much less human readable in csv form
    AttributeFrame.to_csv('Shadowrun_Attributes.csv',
                          index=False,
                          columns=['Body', 'Agility', 'Reaction', 'Strength',
                                   'Willpower', 'Logic', 'Intuition', 'Charisma',
                                   'Physical Limit', 'Mental Limit', 'Social Limit',
                                   'Attribute Sum'],
                          engine='python')

# Call the final function and we're done! :D       
Attribute_to_DataFrame(attr_list)
