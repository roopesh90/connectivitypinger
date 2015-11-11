#! /usr/bin/python3
# -*- coding: utf-8 -*-

import math, os, subprocess, inspect
import urllib.request
import time
from socket import timeout

class EBSimulator:
    '''
    generate backoff-time/timeout based on Exponential backoff
    '''
    def __init__(self, collisions=0):
        self.COLLISIONS = collisions
        self.N_SLOTS = 0
        
    def calc_collision_slots(self):
        '''N = '''
        self.N_SLOTS = int(math.pow(2,self.COLLISIONS)) - 1
    
    def get_backoff(self, collisions=0):
        self.COLLISIONS = collisions
        self.calc_collision_slots()
        N = self.N_SLOTS
        E = (1/(N+1)) * ((N*(N+1))/2)
        return E
        
    def get_backoff_msecs(self,collisions=0):
        return int(self.get_backoff(collisions)*1000)
        

def sendmessage(timeout, logo, heading, message):
    '''
    makes notification
    '''
    URGENCY = "critical"
    script_name = inspect.getfile(inspect.currentframe())
    script_path = os.path.realpath(__file__)
    logo_path = script_path.replace(script_name, logo)
    subprocess.Popen(['notify-send', '-u', URGENCY, '-i', logo_path, '-t', timeout, heading, message])
    return


class ConnectionState:
    '''
    check and set connection state
    '''
    def __init__(self, collisions=1, state=1,):
        self.connection_state = state
        self.collisions = state
    
    def get_state(self):
        return self.connection_state
        
    def set_state(self, state):
        self.connection_state = state
    
    def make_message(self):
        state = NOTIF['state'][self.connection_state]
        sendmessage(NOTIF[state]['timeout'], NOTIF[state]['icon'], NOTIF[state]['heading'], NOTIF[state]['message'])
    
    def check_connectivity(self, reference):
        try:
            urllib.request.urlopen(reference, timeout=1)
            self.connection_state = 1
            
        except (urllib.request.URLError, timeout):
            self.connection_state = 0
            
    def check_state(self, url):
        self.check_connectivity(url)

WEB = {}
WEB['protocol'] = "http"
WEB['reference'] = "www.google.com"
WEB['url'] = "%s://%s" % (WEB['protocol'], WEB['reference'])
NOTIF={}
NOTIF['state']={}
NOTIF['state'][1]='con'
NOTIF['state'][0]='discon'
NOTIF['discon']={}
NOTIF['discon']['icon']="disconnected.png"
NOTIF['discon']['timeout']="3000"
NOTIF['discon']['message']="Will let you know when its back, ASAP!"
NOTIF['discon']['heading']="The Internet went CAPUT"
NOTIF['con']={}
NOTIF['con']['icon']="connected.png"
NOTIF['con']['timeout']="4500"
NOTIF['con']['message']="Its back, ITS BACK!!!\n HUSTLE, we're back in action"
NOTIF['con']['heading']="The Internet back"

COLLISIONS = 1

EBS = EBSimulator(COLLISIONS)
con_state = ConnectionState(COLLISIONS)

con_state.check_state(WEB['url'])
PREV_STATE = con_state.get_state()
CURRENT_STATE = con_state.get_state()

def do_the_needful(state=1,show_msg=True):
    '''
    checks state and sends notification message
    '''
    global COLLISIONS
    # print(NOTIF['state'][state])
    if show_msg:
        con_state.make_message()
    secs = EBS.get_backoff(COLLISIONS)
    if state ==1:
        COLLISIONS=0
    else:
        COLLISIONS+=1
    # print(secs)
    time.sleep(secs)

while True:
    CURRENT_STATE = con_state.get_state()
    con_state.check_state(WEB['url'])
    if CURRENT_STATE != PREV_STATE:
        PREV_STATE = CURRENT_STATE
        do_the_needful(CURRENT_STATE) 
    else:
        do_the_needful(CURRENT_STATE,0)
        
