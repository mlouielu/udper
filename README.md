UDP Tester
==========

Testing Wi-Fi fairness by UDP


HOWTO-USE
=========

serv.py (your stations)
-----------------------

This should use it at your stations, It will open a UDP socket at port 6600, and will report the result to 
`BACKTO` (default is 192.168.231.234:9000)

```
$ python serv.py
```

client.py (your master)
-----------------------

client will send UDP packet to the server. default will send 160 bytes packet 50 times in 60 rounds, repeat 10 
times. You should also change the dest ip for the test.

It will report the recv result, and report with the data, diff from stations, cumulative and average diff.

```
$ python client.py
RECV Counter({16: 2046, 0: 2012}) 34 34 34.0
RECV Counter({0: 1606, 16: 1600}) -6 28 14.0
RECV Counter({0: 2788, 16: 2759}) -29 -1 -0.3333333333333333
RECV Counter({16: 3000, 0: 2999}) 1 0 0.0
RECV Counter({0: 2956, 16: 2786}) -170 -170 -34.0
RECV Counter({16: 2920, 0: 2865}) 55 -115 -19.166666666666668
RECV Counter({16: 3000, 0: 3000}) 0 -115 -16.428571428571427
RECV Counter({0: 2878, 16: 2872}) -6 -121 -15.125
RECV Counter({0: 2921, 16: 2740}) -181 -302 -33.55555555555556
RECV Counter({16: 3000, 0: 3000}) 0 -302 -30.2
```
