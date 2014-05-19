PythOSC
=========
PythOSC is a partial imeplentation of OSC (Open Sound Control) for Python 2.7.

QUICKSTART: Getting something running with PythOsc
-------------------------------------
1. Navigate to the folder containing PythOSC
2. Fire up a terminal and type ```Python osc_tester.py``` (This launches the "client" sender)
3. In another terminal window, type ```Python osc_listener.py``` (This launches the "server" listener)

The above three steps launch a client and server. The ```osc_tester.py``` file includes the ```osc_sender.py``` module, sending its contents out once per second. The server, ```osc_listener.py``` receives, unpacks, and displays the transmitted message.


What PythOSC is (at the moment)
---------------
- A (partial) implementation of an OSC client (sender).
- A (partial) implementation of an OSC server (listener).
- A learning experience for me to get better at Python and gain a keener understanding of OSC (I'm a long-term MIDI user and abuser, so I thought I'd step into 2014 and see what's up).

What PythOSC isn't (yet)
------------------------
- It's not yet capable of dealing with OSC bundles
- It's not fully compliant with ancient OSC stuff lacking typetags: the server requires messages to have a typetag (all parsing is performed by examining the typetag).
- It doesn't know how to deal with more exotic types (e.g. MIDI over OSC, etc.).

PythOSC and ChucK
-----------------
Included in the ```ChucK``` directory are a couple of dead-simple ChucK programs to send and receive ints, strings, and floats. These are good "sanity tests" to see if any hacks you make to PythOSC have broken its ability to send and receive OSC. These are tested and work with ChucK's [MiniAudicle] IDE.

FAQ
---
* Q: "I'm looking for a robust Python OSC implementation."
* A: Try something like [python-osc]. PythOSC is both in its early stages and really intended as a learning project. That said, have a glance through its source. It might be simple enough that you can hack what you need out of PythOSC.
* Q: "I'm looking for a way to send and receive OSC and MIDI. Not necessarily Python."
* A: Try [ChucK]. One of its strong suits is dealing with OSC, and I personally use it all the time as a way to hack together OSC to MIDI scripts (and vice versa).
* Q: What's with this Twisted stuff in ```osc_listener.py```?
* A: I'm using [Twisted] to execute a callback upon receipt of a UDP datagram. Twisted is deep and powerful, and I'm just skimming the surface. Interested in what's going on? Have a look at [these] really nice tutorials.

License
----

MIT

[python-osc]:https://github.com/attwad/python-osc
[ChucK]:http://chuck.cs.princeton.edu/
[MiniAudicle]:http://audicle.cs.princeton.edu/mini/
[Twisted]:https://twistedmatrix.com/trac/
[These]:http://krondo.com/blog/?p=1333
