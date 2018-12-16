This program is an Agent-Based Model used to display a set of raster data (the environment) and a number of agents (x,y coordinates, also referred to as sheep) which are 
plotted in random locations within the environment. After the points are plotted, they move around the environment and eat the data. The path of movement of each agent is 
indicated by dark areas on the graph where the environment has been "eaten". The movement of the sheep is random and is determined by values produced using the random 
function in the agentframework.py module. Upon running the model it will display as an animation which shows the movement of agents around the environment and the 
environment gradually being eaten.


Instructions for running the program:

In order to run the program, 3 files should be saved. It is advised to save them in the same directory:

Model.py - 		the model/program

Agentframework.py - 	module which is used with model.py. This code is used to create the agents class and determines their behaviour within the environment.

In.txt - 		file containing the environment code in the form of raster data (a DEM). This program reads in this data and it is used to display the environment with which the agents will interact. This could be replaced with a different raster data csv file.


Before running the program, enter "%matplotlib qt" into the console in order to view the output as an animation in a pop-up window.
Open the model.py file and run the program. An output window will open which displays an animation of the environment and the agents moving within it.

The program will run until the specified number of movements has been met or the stopping condition is met. The current stopping condition will end the animation if any 
agent is generated a random.random value of less than 0.01 in the agent framework. Random.random generates values between 0 and 1. This value is specified on line 86 of 
model.py can be changed to any value between 0 and 1. A message will be printed in the console if the stopping condition has been met.

If the stopping condition is not met, the animation will carry on until the specified number of frames is reached. This value is given on line 99 of model.py and 
should be an integer. If changing this value, the value given on line 109 of model.py should also be changed in order for the text to be displayed in the console at the correct time.
A message will be displayed in the console once the animation is complete.
