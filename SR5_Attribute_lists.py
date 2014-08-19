import random
import math

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

limit_list = [[], [], [], [], []]

essence = 6

# How long each list is

##for unit in range(len(attr_list)):
##    print("{} is {} items long.\n".format(str(unit), str(len(attr_list[unit]))))

def limit_maker(l):
    '''makes my list of limits in the same order
    of my list of attributes'''
    #It is to be noted that you MUST call float() on LHS before dividing*
    for priority in attr_list:
        for combination in priority:
            physical = math.ceil( float( (2 * (combination[3] + 1) ) + (combination[0] + 1) + (combination[1] + 1) ) / 3)
            mental =   math.ceil( float( (2 * (combination[5] + 1) ) + (combination[6] + 1) + (combination[4] + 1) ) / 3)
            social =   math.ceil( float( (2 * (combination[7] + 1) ) + (combination[4] + 1) +             essence  ) / 3)
            combination_limit = [physical, mental, social]
            l[attr_list.index(priority)].append(combination_limit)

    return l


limit_maker(limit_list)

#this function will gives a print out for a random set of attributes and its corresponding limit

def limit_printer(a, x):
    '''for any given attribute set, and its corresponding limit
    take them and print'''

    chosen_attr = attr_list[a][x]
    chosen_lim = limit_list[a][x]


    your_attr = "Your attributes are:\n\n Bod: {} Agi: {} Rea: {} Str: {} Will: {} Log: {} Int: {} Cha: {}\n".format((attr_list[a][x][0] + 1),
                                                                                                                     (attr_list[a][x][1] + 1),
                                                                                                                     (attr_list[a][x][2] + 1),
                                                                                                                     (attr_list[a][x][3] + 1),
                                                                                                                     (attr_list[a][x][4] + 1),
                                                                                                                     (attr_list[a][x][5] + 1),
                                                                                                                     (attr_list[a][x][6] + 1),
                                                                                                                     (attr_list[a][x][7] + 1))
    your_lim = "Your limits:\n\n Physical: {} Mental: {} Social: {}".format(limit_list[a][x][0],
                                                                            limit_list[a][x][1],
                                                                            limit_list[a][x][2],)

    print("{}\n\n{}\n".format(chosen_attr, chosen_lim))

    print("{}\n\n{}\n".format(your_attr, your_lim))

## sample of this working

##a = random.randint(0, len(attr_list) - 1)
##x = random.randint(0, len(attr_list[a]) - 1)
##
##limit_printer(a, x)
   
# now let's fine the max's

def attr_lim_max(attributes):
    '''if an attribute sets limit sums to the max, add it to the list of max's, call lim_printer(a, x), else nothing'''

    themax = 0
    attrlimmax = [[], [], [], [], []]

    # max just won't work for this because there is more than one sum that equals a max
    # as the loop continues you have to delete the sums less than the new max.
    # the o(n) gets big terrible because of this
    # would probabably be a good idea to think of a data structure to make this faster

    for priority in range(len(attributes)):
        for attri_set in range(len(attributes[priority])):
            if sum(attributes[priority][attri_set]) >= themax:
                themax = sum(attributes[priority][attri_set])
                attrlimmax[priority].append(attributes[priority][attri_set])
                #limit_printer(priority, attri_set)
                for attribute in attrlimmax:
                    for priorities in attribute:
                        if sum(priorities) < themax:
                            attrlimmax.remove(priorities)

                

attr_lim_max(attr_list)
