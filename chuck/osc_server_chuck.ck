//Pretty much the same as ChucK’s example files.

OscRecv recv;
8008 => recv.port;
recv.listen();

recv.event( "/test/address, sfi" ) @=> OscEvent oe;

while ( true )
{
    oe => now;
    <<<"RX">>>;
    while ( oe.nextMsg() != 0 )
    { 
        oe.getString() => string test;
        <<< "got (via OSC):", test>>>;

        oe.getFloat() => float test1;
        <<< "got (via OSC):", test1>>>;

        oe.getInt() => int test2;
        <<< "got (via OSC):", test2>>>;


    }
}
