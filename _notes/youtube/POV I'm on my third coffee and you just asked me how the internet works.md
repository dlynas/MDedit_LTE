---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=jjKFXlFNR4E
---

# Video
POV: I'm on my third coffee and you just asked me how the internet works
![](https://www.youtube.com/watch?v=jjKFXlFNR4E)

## Transcript:
this video is sponsored by brilliant.org
I was born within the brief window where
operating your own website was both
normal to want and possible to
achieve everywhere I went I kept hearing
about this great new thing called the
worldwide web it's going to change the
way we get information they said change
the way we relate to each other it's
going to change
everything turns out when you do an
internet you don't have a passive
consumer role assigned to you just as
you establish connections to the Google
server so can others establish
connections Onto You amen etcp
connection is just two machines agreeing
they're having a conversation by sending
packets to each other over a vast
interconnected Network that involves
under cables so Discovery one for
childhood me there's nothing saying that
this needs to happen in that direction
you can flip it around and it's still
works at least it did when I started
using the internet with dialup you'd
plug the phone line into a modem that
looked like this the modem into a port
that looked like this and
one later you're online well one
computer's online at that point you
could give your IP address to a e Budd
and your two computers could talk
directly that is assuming the internet
is working that day in both directions
in October 2021 Facebook did an oopsie
as a result their servers could reach
the outside world but couldn't receive
anything in response that day a lot of
people learned that the Internet isn't
Direct lines to one another it's packet
switching with Dynamic routing that's
supposed to be resilient to attacks
because well arpanet Department of
Defense Etc but that also means that
connection can be half broken just in
One Direction and I bring this up
because for a lot of us who have home
internet connections we run into a
problem when we want to expose something
to the internet a problem that didn't
really exist in the days of
dialup because dialup bandwidth was so
limited it didn't really make sense to
share it between multiple devices
also using it took up the phone line you
can make calls at the same time it was
something you turn on when you needed it
and off when you didn't and that you
paid per minute just like phone
calls DSL is a game changer it too uses
existing phone lines but this time
internet traffic is encoded on a
separate frequency Bend thanks to
Digital Signal processors that used to
be very expensive to make but that are
in the late '90s starting to get
affordable thanks to advances in the
manufacturing process of integrated
circuits in the DSP processing P that's
that's that's in your average ad L modem
was unimaginable you know 20 years ago
that you would just be throwing it at
this problem suddenly the internet is
always on a lot more bandwidth is
available and it starts making sense for
multiple devices to share the same
connection either via ethernet cables to
a router or over WiFi through an access
point which are also becoming affordable
around that same
time now sharing the water supply line I
can imagine sharing electricity sure
just don't forget fuses but sharing the
internet how does that work well it's
kind of a long
story let's talk about IP addresses if
you're making a website and you give a
friend this link they're not going to
see your website this address tells
their computer to connect to itself
through the loop back device instead of
going out to some router the packets are
going to loop back inside the computer
here's that same address as a diagram
it's 4 bytes 32 bits total that's what
ipv4 addresses look like
but this is more than one address it's a
subnet sl8 means the first eight bits
are for the network part shown in blue
the rest is the host part all 16 plus
million of these addresses are reserved
for loop back as per RFC 5735 and on
Linux we can use all of them we can
ping. two for example but we don't have
to use ping to know that we can use IP
to show us the route this gives us the
destination IP and the source IP that
means that when connecting to a program
that listens on do two it sees a
connection from IP do1 something that's
easy to demonstrate with a bit of rust
our loop back interface also supports
IPv6 this is a SL1 128 so it has a
single address normally we'd write all
eight segments as hexadecimal separated
by colons but since this addresses
mostly zeros we can express that with a
double colon making it much
shorter it makes sense that our friends
can't use those addresses to visit our
website the loop back interface is
virtual it's different for every
computer if we want them to be able to
reach us we must give them the address
of a network interface that is connected
to the internet but how do we find that
out well let's think of an example
website like example.org I can visit in
my browser so I know it's a real website
but this isn't an IP address this is a
domain name and we only know how to
route IP addresses how do we turn one
into the
other
oh look it's DNS DNS for domain name
system if we ask for a records we get an
ipv4 address and if we ask for Quad a
records we get an IPv6
address let's start with IPv6 since
believe it or not it is the simplest of
the two we can ping that address so we
know that we have connectivity to it and
the latency is high enough that I
suspect we're crossing an ocean there
can we find that out for sure well the
who is command is able to query various
databas here we find out that this
address is part of a sl32 block assigned
to edgecast it says edgecast is
headquartered in Los Angeles and gives
us three different as numbers which is
kind of vague as means autonomous
systems the smaller networks that
assemble to make up the internet we care
about these because the global routing
rules Define how to get packets from one
autonomous system to the next is the
right level of detail for us right now
another thing we can query is Max min's
Gip database unfortunately the city
field is missing and the coordinates
point to the middle of the USA so yeah
that's that's the problem with databases
they can be inaccurate imprecise and or
out of date plus they don't tell us
where the traffic actually flows to find
that out we can perform each race route
IP packets have a TTL field for time to
live every hop decreases that TTL by one
and if it reaches zero the packet is
sent back letting the sender know
something went wrong icmp trace route
uses this it sets low ttls on purpose to
get messages back from every node on the
path a TTL of one will result in a Time
exceeded message from next door neighbor
a TTL of two will let us know who their
neighbor is and we can keep going until
we get an echo Rec which means we've
traced the full route here's the path
from my computer to example.org over
IPv6 we see packet loss of up to 100% in
the middle but 0% for the destination
this is common it just means some middle
boxes are not sending back icmp time
exceeded messages they're refusing to
play with us unfortunately it also means
we can't tell what's happening between
hops 4 and six thanks to reverse DNS
we're able to turn IP addresses into
into domain name so we can see traffic
transiting through cogent and then
entering edgecast I am ready to bet that
this means Paris this means London and
this means Boston and so we are crossing
an ocean between hops 8 and 9 where the
latency jumps from 14 to 77
milliseconds we've seen two techniques
so far trace route which gives us only
one of the possible paths with some
nodes missing and the Hoist database
which is purely informative it is not
the actual source of Truth used by
routers to send packets around bdp is
the Border Gateway protocol
sdv lets you generate cute little graphs
that show pass from their autonomous
system to an arbitrary address using
their view of bgb rules this is
important not everyone has the same
vision of bgb rules there's as many
versions of the truth as there are
participants their best path is the same
one as the one we saw in my Trace rout
but we also see Alternatives through
yellow and Hurricane Electric or through
F Telecom open transit and NTT so you
see the internet is such a big organic
living network that it takes an
empirical approach to study it we make
experiments and measurements and try to
reconcile those with publicly available
data sets note that we didn't even find
out which undc cable our traffic was
going through this is the topic of a
fascinating paper I've Linked In the
description and which you should go read
right now go oh wait this video is
sponsored by brilliant.org brainstorming
ideas for the sponsored segment I
realized I can't sound excited for the
whole video and then sound even more
excited for the sponsored segments the
only way to make this segment Stand Out
is for me to chill and take a minute
with all of you to
relax breathe
in and breathe out 1 minute that's all
it takes to keep your streak going on
b.org now I've met some people who are
skeptical of the whole gamification
thing shouldn't learning be tur and
difficult and occur in sem circle with
some bearded guy rehashing the same
class has been giving out for over 15
years hell no that's just gatekeeping
there has never been a better time to
teach yourself something and you do want
to teach yourself something don't
you
no Jim jimy got another
one I don't know how they keep finding
me well what do you want to do with them
they're just they're just sitting there
waiting for the segment to end
okay all right right I figured something
out
no you hang up if you or someone you
know wants a fun and interactive way to
teach themselves something go to
brilliant.org faster thanan I'm now for
a free 30-day trial of everything
brilliant has to offer in addition the
first 200 of your friends who actually
want to learn something I am Cal well
they at the course list online they're
not that's okay it's your point but the
deal was 90 seconds so I don't know what
you expect me to do about it now oh
you're back um so we know I can reach
the IPv6 address from this computer but
how this route shows a next hub that's
part of a sl10 reserved by RFC 4291 for
link local addresses the link here being
this white ethernet cable hence the
interface name and it's an address I can
ping from my MacBook for example but not
from one of my servers which is in a
different country altogether The Source
address for this route is associated to
the correct network interface and is a
public address we can have a static file
server listen on it and make requests to
it from across the globe
who is confirms this IP block is owned
by proide it's a sl26 that's that's a
lot of addresses and go gives us a very
rough location for it it's in the right
region of friends finally our computer
is clever enough to Route packets
through the loop back interface instead
of to the router and back because you
know it's our address and that's where
the story ends for IPv6 we get one loop
back address for development one link
local address one temporary address for
privacy reasons one stable address for
serious hosting and that's it
it's simple it's straightforward and it

works that's what IPv6 sounds like to
Americans who still don't have access to
it it's hard to explain the difference
in scale between the ipv4 and IPv6
address spaces so I made you a sketch to
scale the yellow dot is IPv6 and the
blue dot is invisible because ipv4 may
have 4 billion addresses but IPv6 has
340 billion billion billion billion
addresses that
many when Rand a server they tend to
throw in an ipb 6/64 but you have to pay
two bucks a month for a single ipv4
address even fly who stuck piled them
like Atomic Warheads has started
charging for them in
2024 and yet all the devices in my home
are able to breach the internet over
ipv4 I think let's check to turn
example.org into an ipv4 address we ask
for DNS records of type A we can ping
that address and we have a route for it
so I guess just like before uh that's
the router and that's the address of my
computer and so we can just listen on it
right okay that works and we can access
that from the Macbook so far so good but
we can't access it from one of my
servers this is suspicious what is this
address
I think it's time for packet
(Laughter)

sniffing myio shark is an excellent tool
for this I will use it to find out what
happens as I physically plug in my
ethernet cable into the
computer right now not much is happening
because the cable is physically
unplugged so I'm going to plug it in if
the guardian lets me
through okay here's the cable
and I want to plug it in here and keep
an eye on the screen as I do this
because you're going to see a flood of
packets come
through
now hold on hold on we just missed it it
happened between those two frames let me
show you what I'm talking about so a
device that is entirely new to the
network would send a DHCP discover
message but this one already had an
address so it's just asking for it back
with the DHCP request message DHCP is
built on top of UDP which is built on
top of I which is built on top of
ethernet ethernet lets you send frames
to any device you have the MAC address
for but we're new to this network we
don't even know the MAC address of the
router so what do we do we send it to
the broadcast address that way anyone on
the network will hear about R dhtp
requests does this have security
implications absolutely anyone on the
network could just reply to our request
and pretend they're the router luckily
no one in this household except for the
cat is trying to attack me right now so
only the router responds saying yes you
can have this IP address for 12 hours
please use these servers for DNS
requests also here's my address if you
need it and here's the subet mask for
this network that's another way of
saying it's a sl24 and at that point we
are sure that this is not a public ipv4
address why because the sl24 only has
256 hosts minus one for broadcast and
there's a little more than 256 devices
on the Internet isn't there and yet yet
we are able to make requests to www.
msftconnecttest.com over ipv4 what the
heck is going
on
it is time for me to do the only thing I
can think of to do which is to run this
R program that we wrote earlier on a
fresh new header Cloud Server that has a
dedicated ip4 address I'm paying this
amount per hour to have and see which
address is printed in the logs when I
access it from my home let's effing go
so hey I am on the server mining my own
business it has a single public ipv for
address and as promised it's a sl32 I've
modified the program to to listen on all
public network inter faes and if we try
and connect it with netc count from my
computer we're going to see that it
succeeds three times in a row let's
check back the logs from our server and
we see finally finally my public ipv4
address quick point of order did I just
docks myself let's find out if we do a
who is on this IP address we find out
that it is owned by free and the diip
database shows that it's in the general
vicinity of Leon in France which is what
I have on my GitHub profile so no it did
not give you any additional information
as to where I actually live but if you
do find out where I live and you want to
come for a visit please let me know
about 15 minutes in advance because I
like to make fresh orange juice and
pancakes for all my guests back to our
little experiments I want to note
something important here on the client
side we always connect to the same ports
on the server but on the server side we
see connections come from different
ports from the clients and this is
important because this is how the client
can tell apart different connections
going to the same address and Port
combination when a establishing an
outgoing TCP connection it picks a port
at random from the ephemeral Port range
and then that's the port this connection
has now because the port field in the
TCP protocol is only a u16 there's only
60,000 ports GE take so what do you
think happens if you try to establish
more than 65,000 connections well let's
find out okay so we've got everything
ready the server is on the right it is
listening on this port I'm going to run
the client and we'll see how many
connections it successfully establishes
before something goes
wrong
so far so good I get a feeling it's
going to fail way before we actually run
out of the ports yeah Dr not available
oh well thanks for playing I originally
thought something else must have gone
wrong during this demonstration because
300 ports seemed like too little but
actually that is the range configure on
this Linux install on wl2 we all agreed
the router is definitely doing some sort
of network address
translation there's something weird
about our experiment though all the
ports that that we see on the client
side are the exact same that we see on
the server side for the pier address not
the local address but then what would
happen if two of the computers on my
local network establish connections to
the same address with the same Source
Port forcing the operating system to
pick a specific Source Port is a bit
awkward but the next best thing we can
do is to have two computers open
thousands and thousands of connections
to my server and keep track of the exact
moment my internet box is forced to
switch to port address translation also
called IP masquerade in that scenario my
box itself picked the source port and it
remembered that it's meant for that
different Source port on that local IP
address that way both directions work
from the laptop to the server and from
the server back to the laptop because
the Box remembers the mapping and that
is the route of all the root it's the
root of all evil this scheme only works
if my computer is the one initiating the
connection to the outside world not the
other way around if my computer was just
waiting for connections on Port 443 for
example it wouldn't work because it
would reach my internet box would just
say I'm not expecting anyone and just
hang up this would prevent peer-to-peer
applications like voice calls from
working but the human race is ever so
resourceful and so we thought if we have
two half functioning connections that
work in opposite directions can we use
those to make one fully functioning
connection the answer is yes and it's
called nat hole punching the idea is you
have both ends connect to a third party
server and that server takes note of
what the actual IP addresses in Port are
and it sends that information to both
peers which they can now use to actually
connect to each other because there is a
hole that was punched the buck remembers
this mapping is now expecting traffic on
this port everything works as expected
sometimes also most internet boxes can
be configured you can just tell the Box
you know if you get a call or you get a
connection on Port 443 just send it to
me I'll take care of it and that way you
can buy a domain name and set up DNS
records that point to your home IP
address and then you can host something
from home Tada no need to rent someone
else's server in the cloud
unless your internet service provider is
also doing
that that's right there's nothing saying
that your internet box actually needs a
public ipv4 address it could have
another private ipv4 address in the
network of your internet service
provider and at this point you have two
translation layers going on across three
different addressing domains and if you
want to host anything from your home
you're out of luck you know this
isn't the video I wanted to make all
right I don't like explaining things for
the sake of explaining things well I am
a man but the video I did want to make
was about hosting your own stuff and the
first question I wanted to answer was
why do you not want to host these things
from home and part of the answer is not
there's also some privacy concerns it's
not like your IP address automatically
you sumone your house address but it can
lead them there if they're trying to
find you for example if one of your
devices has configured your router
through UPnP to actually open some port
and they are able to scan your IP
address and find that open port and talk
to that device and it's an old device
and it's vulnerable and they gain access
to the local network and they can scan
it and by doing that they find the MAC
address of your Wi-Fi access point and
then they look up your house address in
the database from Mac addresses to
geolocation that M
maintains you know it's hard to predict
exactly how you're going to get pawned
but I did do a bit of homework to make
sure this video was safe to put out and
uh if I got it wrong I always have the
cide pill in this

tooth

for

fore

the


## Keywords:
