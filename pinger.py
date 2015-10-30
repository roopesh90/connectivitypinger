#! /usr/bin/python3

'''
exponential backoff states that:
    Given a uniform distribution of backoff times, the expected backoff time is the mean of the possibilities.
    That is, after c collisions, the number of backoff slots is in 
        [0, 1, ..., N], where N = 2c - 1 
    and the expected backoff time (in slots) is:
    (i/(N+1))*(n∑i,i=0), where (n∑i,i=0) = ((n*(n+1))/2)
'''
