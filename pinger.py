#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
exponential backoff states that:
    Given a uniform distribution of backoff times, the expected backoff time is the mean of the possibilities.
    That is, after c collisions, the number of backoff slots is in 
        [0, 1, ..., N], where N = 2c - 1 
    and the expected backoff time (in slots) is:
    (1/(N+1))*(n∑i,i=0), where (n∑i,i=0) = ((n*(n+1))/2)
'''

import math, os, subprocess, inspect
import urllib.request

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
        
def check_connectivity(reference):
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False


def sendmessage(timeout, logo, heading, message):
    URGENCY = "critical"
    script_name = inspect.getfile(inspect.currentframe())
    script_path = os.path.realpath(__file__)
    logo_path = script_path.replace(script_name, logo)
    subprocess.Popen(['notify-send', '-u', URGENCY, '-i', logo_path, '-t', timeout, heading, message])
    return
    
WEB = {}
WEB['protocol'] = "http"
WEB['reference'] = "www.google.com"
WEB['url'] = "%s://%s" % (WEB['protocol'], WEB['reference'])
NOTIF={}
NOTIF['discon_icon']="disconnected.png"
NOTIF['con_icon']="connected.png"
NOTIF['discon_timeout']="3000"
NOTIF['con_timeout']="4500"

# for disconnection
sendmessage(NOTIF['discon_timeout'] , NOTIF['discon_icon'], "The Internet went CAPUT", "Will let you know when its back, ASAP!")
# for connection
sendmessage(NOTIF['con_timeout'], NOTIF['con_icon'], "The Internet back", "Its back, ITS BACK!!!\n HUSTLE, we're back in action")
# While
print( )
COLLISIONS = 7

EBS = EBSimulator(COLLISIONS)
# EBS.get_backoff(COLLISIONS)
