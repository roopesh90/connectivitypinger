# connectivitypinger - Check Internet Connectivity State

---

### Background

To explore how [Exponential backoff][exp_backoff] works, I wrote this script that helps check if the system is connected to the Internet of not. Another reason for making the script is, I was fed up with my ISP resetting my connection, since I'm on ssh, it kept timing out and the only way to find/notify disconnection was through Dropbox, and it takes forever.

Exponential back-off states that:

> Given a uniform distribution of backoff times, the expected backoff time is the mean of the possibilities.
    
That is, after `c` collisions, the number of backoff slots is in

    [0, 1, ..., N], where N = 2c - 1 
    
and the expected backoff time (in slots) is:

    (1/(N+1))*(n∑i,i=0), where (n∑i,i=0) = ((n*(n+1))/2)

### Working

The script checks if the system is connected, by getting www.google.com. If true, backs off for x seconds, if false backs out for y secs.

On a successful:
- connection-after-disconnection
- disconnection-after-connection

the script send a notification using notify-send.

> **PS:** Do remember, this will silently run in the background :)

### Requirements
- python3
- notify-send 
    - install using `sudo apt-get install notify-osd`

----

#### To Do:

- ~~check socket timeout issue and fix~~
- ~~clean and make code legible~~
- ~~Implement backoff of both disconnection and connection~~
- ~~make notifications audible~~
- back it as a shell callable
- Way to get kill the script form terminal, one command


I'm open to all suggestion and feedback.

Also, I have a very faint feeling I'm doing it wrong, if so, please do let me know

[exp_backoff]:https://en.wikipedia.org/wiki/Exponential_backoff
[summation]:https://en.wikipedia.org/wiki/Summation
