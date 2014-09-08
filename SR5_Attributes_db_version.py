import random
import math
import sqlite3

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

    physical = math.ceil( float( (2 * (combination[3] + 1) ) + (combination[0] + 1) + (combination[1] + 1) ) / 3)
    mental =   math.ceil( float( (2 * (combination[5] + 1) ) + (combination[6] + 1) + (combination[4] + 1) ) / 3)
    social =   math.ceil( float( (2 * (combination[7] + 1) ) + (combination[4] + 1) +             essence  ) / 3)

    return [physical, mental, social]

#database append function
def Attribute_DB(attributes):
    '''make database to append above combinations'''

    # make database, point cursor, create table 
    con = sqlite3.connect('Attributes.db')

    cur = con.cursor()

    cur.execute("""CREATE TABLE AttributeData(Body integer, Agility integer, Reaction integer, Strength integer,
                                              Willpower integer, Logic integer, Intuition integer, Charisma integer,
                                              Physical_limit float, Mental_limit float, Social_limit float)""")

    # iterate through my gigantic list of list comprehnsion made lists and append it to the database
    for priority in attributes:
        for attr_set in priority:
            
            # pass the list as a set with the calculation from the limit
            limits = limit_maker(attr_set)

            # then append that and the attr_set to a new set
            attr_and_limits = (attr_set[0], attr_set[1] , attr_set[2], attr_set[3],
                               attr_set[4], attr_set[5], attr_set[6], attr_set[7],
                               limits[0], limits[1], limits[2])

            # then that into the database! :D
            cur.execute("INSERT INTO AttributeData VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", attr_and_limits)
            
    # Testing this on my system, the .db file is about 7.75 MB

    con.commit()
    con.close()

Attribute_DB(attr_list)
