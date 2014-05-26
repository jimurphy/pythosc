###PythOSC

PythOSC is a partial imeplentation of OSC (Open Sound Control) for Python 2.7.

#####QUICKSTART: Getting something running with PythOSC
Note: make sure the ```\pythosc``` folder goes into your PYTHONPATH (if you're not sure how to do this, see [pythonpath]).

1. Navigate to the folder containing PythOSC
2. Fire up a terminal and type ```Python osc_tester.py``` (This launches the "client" sender)
3. In another terminal window, navigate to the /examples folder.
4. Type ```Python basic_server_example.py``` (This launches the "server" listener on its own thread)

The above three steps launch a client and server. The ```osc_tester.py``` file includes the ```osc_sender.py``` module, sending its contents out once per second. The server, ```osc_listener.py``` receives, unpacks, and displays the transmitted message.

#####What PythOSC is (at the moment)

- A (partial) implementation of an OSC client (```osc_sender.py```).
- A (partial) implementation of an OSC server (```osc_listener.py```).
- A learning experience for me to get better at Python and gain a keener understanding of OSC (I'm a long-term MIDI user and abuser, so I thought I'd step into 2014 and see what's up).

#####What PythOSC isn't (yet)

- It's not yet capable of dealing with OSC bundles.
- It's not fully compliant with ancient OSC stuff lacking typetags: the server requires messages to have a typetag (all parsing is performed by examining the typetag).
- It doesn't know how to deal with more exotic types (e.g. MIDI over OSC, etc.).

#####PythOSC and ChucK

Included in the ```ChucK``` directory are a couple of dead-simple ChucK programs to send and receive ints, strings, and floats. These are good "sanity tests" to see if any hacks you make to PythOSC have broken its ability to send and receive OSC. These are tested and work with ChucK's [MiniAudicle] IDE.

######Sending OSC from ChucK to PythOSC
Note: This assumes you're using command line ChucK. This should work equally with MiniAudicle.
Another note: Make sure you've set up your typetags, port, and address patterns to match in ChucK and PythOSC.

1. In a terminal window, navigate to PythOSC's /chuck directory.
2. Type ```chuck osc_client_chuck.ck```. This will start ChucK sending OSC to the specified port.
3. In another terminal window, navigate to PythOSC's /examples folder.
4. Type ```Python basic_server_example.py``` (This launches the "server" listener, which starts printing out the messages.)

######Sending OSC from PythOSC to ChucK
Note: This assumes you're using command line ChucK. This should work equally with MiniAudicle.
Another note: Make sure you've set up your typetags, port, and address patterns to match in ChucK and PythOSC. If you don't, ChucK will ignore any non-matching messages.

1. In a terminal window, navigate to PythOSC's /chuck directory.
2. Type ```chuck osc_server_chuck.ck```. This will start ChucK listening for incoming OSC.
3. In another terminal window, navigate to the /pythosc folder.
4. Type ```Python osc_tester.py``` (This launches the an OSC client, which starts sends OSC messages.)


#####FAQ

* Q: "I'm looking for a robust Python OSC implementation and/or something for Python 3."
* A: Try something like [python-osc]. PythOSC is both in its early stages and really intended as a learning project. That said, have a glance through its source. It might be simple enough that you can hack what you need out of PythOSC.
* Q: "I'm just looking for a way to send and receive OSC and MIDI. Not necessarily Python."
* A: Try [ChucK]. One of its strong suits is dealing with OSC, and I personally use it all the time as a way to hack together OSC to MIDI scripts (and vice versa).

#####License
MIT

[python-osc]:https://github.com/attwad/python-osc
[ChucK]:http://chuck.cs.princeton.edu/
[MiniAudicle]:http://audicle.cs.princeton.edu/mini/
[Twisted]:https://twistedmatrix.com/trac/
[These]:http://krondo.com/blog/?p=1333
[pythonpath]:http://stackoverflow.com/questions/19917492/how-to-use-pythonpath
