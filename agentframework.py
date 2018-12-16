import random
#The class for the agents/sheep:
class Agent():
    def __init__ (self, environment, neighbourhood, agents):
#defining the agents and environment:        
        self.environment = environment
        self.store = 0
        #making the labels "self._x" and "self._y", assigning them the value "random.randint(0,299)":
        #this makes the agent coordinates a random integer between and including 0 and 299:
        self._x = random.randint(0, 299)
        self._y = random.randint(0, 299)
        self.neighbourhood = neighbourhood
        self.agents = agents


    def __str__(self):
        return " x " + str(self._x) + " y " + str(self._y)

       
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

#moves the agents +/-1 space depending on the value of random.random().
#The "% 300" creates a torus environment, creating a boundary to prevent agents leaving the space.
#If an agent leaves the space on one edge of the graph it will re-enter on the opposite edge. 
    def move(self): 
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300

#conditions for sharing with neighbours (although this is not used in this version of the program)
    def share_with_neighbours(self, neighbourhood):
            for agent in self.agents:
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    print("sharing " + str(dist) + " " + str(ave))

#phythagoras func for calculating distance between 2 agents (also not used in this version):
    def distance_between(self, agent):
            return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5