#! /usr/bin/python3

'''
exponential backoff states that:
    Given a uniform distribution of backoff times, the expected backoff time is the mean of the possibilities.
    That is, after c collisions, the number of backoff slots is in 
        [0, 1, ..., N], where N = 2c - 1 
    and the expected backoff time (in slots) is:
    (1/(N+1))*(n∑i,i=0), where (n∑i,i=0) = ((n*(n+1))/2)
'''

import math

class EBSimulator:
    def __init__(self, collisions=0):
        self.COLLISIONS = collisions
        self.N_SLOTS = 0
        
    def calc_collision_slots(self):
        '''N = '''
        self.N_SLOTS = int(math.pow(2,self.COLLISIONS)) - 1
        print(self.COLLISIONS)
        print(self.N_SLOTS)
    
    def get_backoff(self, collisions=0):
        self.collisions = collisions
        self.calc_collision_slots()
        N = self.N_SLOTS
        E = (1/(N+1)) * ((N*(N+1))/2)
        print(E)
        
COLLISIONS = 3

EBS = EBSimulator(COLLISIONS)
EBS.get_backoff(COLLISIONS)
