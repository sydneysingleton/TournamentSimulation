# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:08:03 2020

@author: sydne
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from functools import reduce
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import numpy as np

stats_2020_path = "path\\to\\2020\\stats"
model_data_path = "path\\to\\model\\data"
seas_2020 = pd.read_csv(stats_2020_path)
cols = seas_2020.columns.drop('School')
seas_2020[cols] = seas_2020[cols].apply(pd.to_numeric, errors='coerce')
full_data = pd.read_csv(model_data_path)

full_data = full_data[~full_data['srsd'].isnull()] #take out random NAs
X = full_data.drop(columns = ['Home_win', 'Unnamed: 0.1', 'Unnamed: 0']) #same steps as in bracket_build.py just creating the model 
y  = full_data['Home_win']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
y_probs = logistic_regression.predict_proba(X_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
confusion_matrix

def bracket(home, away, df): #same function as in bracket_build.py
    home_df = df[df['School'] == home].reset_index()
    
    away_df = df[df['School'] == away].reset_index()
    
    full_df = pd.merge(home_df, away_df, right_index = True, left_index = True)
    full_df['ngd'] = full_df['NumGames_x'] - full_df['NumGames_y']
    full_df['owd'] = full_df['OverallW_x'] - full_df['OverallW_y']
    full_df['old'] = full_df['OverallL_x'] - full_df['OverallL_y']
    full_df['srsd'] = full_df['SRS_x'] - full_df['SRS_y']
    full_df['sosd'] = full_df['SOS_x'] - full_df['SOS_y']
    full_df['tpd'] = full_df['Team Points_x'] - full_df['Team Points_y']
    full_df['opd'] = full_df['OppPoints_x'] - full_df['OppPoints_y']
    full_df['mpd'] = full_df['MP_x'] - full_df['MP_y']
    full_df['fgpd'] = full_df['FG%_x'] - full_df['FG%_y']
    full_df['orbd'] = full_df['ORB_x'] - full_df['ORB_y']
    full_df['tppd'] = full_df['3P%_x'] - full_df['3P%_y']
    full_df['trbd'] = full_df['TRB_x']-full_df['TRB_y']
    full_df['ad'] = full_df['AST_x'] - full_df['AST_y']
    full_df['sd'] = full_df['STL_x'] - full_df['STL_y']
    full_df['bd'] = full_df['BLK_x'] - full_df['BLK_y']
    full_df['td'] = full_df['TOV_x'] - full_df['TOV_y']
    X = full_df[['ngd','owd','old','srsd','sosd','tpd','opd','mpd','fgpd','orbd','tppd','trbd','ad','sd','bd','td']]

    win = logistic_regression.predict(X)
    if win == 1: 
        winner = home
    if win == 0: 
        winner = away
    prob_win = np.array(logistic_regression.predict_proba(X))
    return([prob_win[0][1], winner])

#you can play around here and see the probability of the outcomes of specific games in 2020 for example: 

bracket("Duke", "North Carolina", seas_2020)



