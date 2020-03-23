# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:02:12 2020

@author: sydne
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#the ACC bracket data
tournament_bracket_path = "path\\to\\tournaments\\spreadsheet"
acc_brack = pd.read_excel(tournament_bracket_path, sheetname = "ACC")
#the SEC bracket data
sec_brack = pd.read_excel(tournament_bracket_path, sheetname = "SEC")


def roundone_tourney(tourney_bracket, seas_df):
    wins1 = []
    zero = tourney_bracket[tourney_bracket['Round'] == 0]
    zero = pd.DataFrame(zero)
    for index, row in zero.iterrows():
        x = bracket(row['Team 1'], row['Team 2'], seas_df)
        s1 = np.random.binomial(1, x[0],1)
        if s1 == 1:
            a = row['Team 1']
        if s1 == 0: 
            a = row['Team 2']
        y = bracket(row['Match 1'], a, seas_df)
        s2 = np.random.binomial(1, y[0],1)
        if s2 == 1:
            b = row['Match 1']
        if s2 == 0: 
            b = a
        w = bracket(row['Match 2'], b,seas_df)
        s3 = np.random.binomial(1, w[0],1)
        if s3 == 1:
            c = row['Match 2']
        if s3 == 0: 
            c = b 
        wins1.append(c)
        print(wins1)
    wins2 = []
    one = tourney_bracket[tourney_bracket['Round'] == 1]
    one = pd.DataFrame(one)
    for index, row in one.iterrows():
       x = bracket(row['Team 1'], row['Team 2'], seas_df)
       s4 = np.random.binomial(1, x[0],1)
       if s4 == 1:
            d = row['Team 1']
       if s4 == 0: 
            d = row['Team 2']
       y = bracket(row['Match 1'], d, seas_df)
       s5 = np.random.binomial(1, y[0],1)
       if s5 == 1:
            e = row['Match 1']
       if s5 == 0: 
            e = d
       wins2.append(e)
       print(wins2)
    last4 = list([wins2[0] ,wins1[0], wins2[1], wins1[1]])
    print(last4)
    return(last4)

cols = seas_2020.columns.drop('School') 

first = roundone_tourney(acc_brack, seas_2020)


def roundtwo_tourney(roundone, seas_df):
    wins3 = []
    for i in range(0,3,2):
        w = bracket(roundone[i], roundone[i+1], seas_df)
        s = np.random.binomial(1, w[0], 1)
        if s == 1:
            wins3.append(roundone[i])
        if s == 0: 
            wins3.append(roundone[i+1])
    return(wins3)

second = roundtwo_tourney(first, seas_2020)

def tourney_champ(roundtwo, seas_df):
    w = bracket(roundtwo[0], roundtwo[1], seas_df)
    s = np.random.binomial(1,w[0], 1)
    if s == 1: 
        champ = roundtwo[0]
    if s == 0: 
        champ = roundtwo[1]
    return(champ)

tourney_champ(second, seas_2020)

def tourney_sim(tourney, sdf, n):
    column_names =  tourney['Team 1'].append(tourney['Team 2'], ignore_index = True).append(tourney['Match 1'], ignore_index = True).append(tourney['Match 2'], ignore_index = True)
    column_names = list(column_names)[: -2]
    for elem in column_names: 
        if elem == 'drop':
            column_names.remove(elem)
    sim_round1 = pd.DataFrame(0, range(0,n), columns=column_names)
    sim_round2 = pd.DataFrame(0, range(0,n), columns = column_names)
    champ = pd.DataFrame(0, range(0,n), columns = column_names)
    for i in range(0,n):
        first = roundone_tourney(tourney_bracket = tourney, seas_df = sdf)
        for elem in first: 
            sim_round1.loc[i,elem] = 1
        second = roundtwo_tourney(first, seas_df = sdf)
        for elem2 in second: 
            sim_round2.loc[i,elem2] = 1
        champion = tourney_champ(second, seas_df = sdf)
        champ.loc[i,champion]= 1
        print(i)
    mean4 = pd.DataFrame(np.mean(sim_round1), columns = ['Final 4'])
    mean5 = pd.DataFrame(np.mean(sim_round2), columns = ['Championship'])
    mean6 = pd.DataFrame(np.mean(champ), columns = ['Champ'])
    means = []
    means = [mean4, mean5, mean6]
    all_rounds = pd.concat(means, axis = 1).reset_index()    
    all_rounds['School'] = all_rounds['index']
    return all_rounds.drop(columns = ['index'])
 
#you can change n here! the more simulation the more accurate, but also the longer it takes to run        
probs_acc_2020 = tourney_sim(acc_brack, seas_2020, n = 10000)

#you can also play around here if you want to see probabilities of:
#teams winning the tournament - y="Champ"
#teams playing in the championship game - y="Championship"
#teams making it to semi finals of tournament - y="Final 4" 

plt.figure(figsize=(10,10))
chart = sns.barplot(data = probs_acc_2020, x = 'School', y= 'Champ')
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
chart.set_title("Probability of Teams Winning ACC Tournament")


probs_sec_2020 = tourney_sim(sec_brack, seas_2020, 10000)
plt.figure(figsize=(10,10))
chart = sns.barplot(data = probs_sec_2020, x = 'School', y= 'Champ')
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
chart.set_title("Probability of Teams Winning SEC Tournament")
