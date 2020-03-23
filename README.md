# TournamentSimulation
2020 ACC and SEC tournament simulation 

Since all of our favorite sporting events have been cancelled this year, including the ACC and SEC basketball championships, I decided to simulate what those tournaments would have looked like! 

This project was born out of my building a program that would simulate a march madness bracket. However, since that bracket was never released, I decided to apply the same logic to the ACC and SEC tournaments because we did get to see those brackets! 

The images attached show the results of 10,000 simulations for the ACC and SEC tournament bracket. It is showing the proportion of times that each team was the champion within those 10,000 simulations. If you play around with the program, you can also see the proportion of times teams make it to the finals or semi-finals!

The files I have attached are:
  
  Programs:
  - BracketModelandFunctions.py : this is the file that builds the logistic regression that this entire simulation is built off of. It       also contains the function called "bracket" that gives the predicted probability of the outcome of any given game. 
  - tourney_sim_deploy.py : this uses the logistic regression and the bracket function from the program above to simulate the tournament      and produce visualizations. It also contains the functions that will simulate each round individually. 
  
  Data: 
  - 2020_stats.csv : the stats for each team for 2020 
  - model_data.csv : stats and game results from the past 10 years that the logistic regression is built off of
  - Tournaments_2020.xlsx : contains 2 sheets ACC and SEC that are basically the tournament brackets in spreasheet form 
  
  Images:
  - Results of 10,000 simulations for ACC champion and SEC champion
