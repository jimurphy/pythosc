//Pretty much the same as ChucK’s example files.

"localhost" => string hostname;
8009 => int port;

if( me.args() ) me.arg(0) => hostname;
if( me.args() > 1 ) me.arg(1) => Std.atoi => port;

OscSend xmit;

xmit.setHost( hostname, port );

while( true )
{
        xmit.startMsg( "/test/message", "iiiiii");
        33 => int temp1 => xmit.addInt;
        666 => int temp2 => xmit.addInt;
        111 => int temp3 => xmit.addInt;
        222 => int temp4 => xmit.addInt;
        444 => int temp5 => xmit.addInt;
        555 => int temp6 => xmit.addInt;

        <<< "sent (via OSC):", temp1 >>>;
        1::second => now;
}
