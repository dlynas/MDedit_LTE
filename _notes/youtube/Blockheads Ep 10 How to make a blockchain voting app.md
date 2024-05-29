---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=sm8w9tDnMZc
---

# Video
Blockheads Ep 10: How to make a blockchain voting app
![](https://www.youtube.com/watch?v=sm8w9tDnMZc)

## Transcript:
hey everyone my name is doran crutcher
welcome to an episode of blogheads where
in this video we'll be reworking and
updating at the original blockheads
voting application tutorial video
thanks to you guys your driver got a lot
of great organic viewership
but you know as time goes on libraries
get updated unfortunately applications
get outdated so now it's time to build
something new
functional and working so you guys can
have a working decentralized application
so grab your computers
sit tight and let's build a new version
of block vote
better it's not stopping

okay everyone let's get started so first
let me show you guys what we are
creating
we are creating block votes so i'm gonna
show you guys why i designed a figma to
show you out
the layout um so this is the home page
this would just be a simple list of
polls so
every existing poll that is currently
running on block boat
will appear here this is the actual
polling station the meet of the
application so you can see
the uh the two candidates which is
pikachu and kirby
the prompt here is like who's more
likely to win smash so i think it's
gonna be kirby because you know he's my
my favorite characters so you guys can
fight me on that well and literally it's
in smash brothers
um but you can have your own opinions
i'd love to hear them in the comments
uh we also have our two voting buttons
to vote for candidates and then the
results of the vote will appear
only when the vote has been cast so
we're going to
design a whole way to record the users
um to be able to actually like see
the results of the vote um and then here
is the actual uh new polling station so
here's the um
uh this is how users be able to enter in
and create
new polls for the blockchain or onto the
blockchain
and onto the application so other users
can get involved
so yeah we have a whole like we have a
whole project too to work out so we can
get started i'll show you guys extra
application too
so yeah this is the um
this is what the home page will look
like uh we'll be using react bootstrap
uh to kind of like circumvent most of
the css um
you know designing uh stuff or steps
um these are able to essentially see the
prompts here
be able to click on go to polls and then
you can see at the user um
that these two images will appear and
the user can vote on them and once they
vote
you can see the results here so two
votes for kirby zero votes for pikachu
if you want to create a new poll you can
go through this entire process by
entering in the candidate's name and
then entering in the
candidate's image url so you could
actually enter in
their pictures just like off the web or
something and then we're also going to
enter in the
prompt name it's like what's this vote
about and what's going on with it
and um we're gonna be using that as our
key for a lot of our smart contract code
um yeah so lots of fun stuff in store
for you guys so let's just get started
hey everyone so a few quick items you'll
need to get started on building your
cool decentralized applications so first
head over to node.js website
to download the recommended version of
node.js which comes with the npm packet
manager as well as the npx package
executor
which we're going to be using to kick
off our create new app project template
to get start with building our
application
after that over to yarn's website their
installation page kind of looks like
this
and follow their instructions to
download the yarn we have a lot we have
a bunch of scripts built into the
project template that will be used to
execute
and download our packages as well as
execute our project
so this will help us make sure things
run smoothly and we can down things
effectively
once you have that done install your
microsoft visual studio code ide by
googling that microsoft visual studio
code which we navigate to a page that
looks like this
it's our download page uh this button
automatically accommodates for whichever
os you are working with
but just in case you can hit this button
here and download from something free
download the
ide for windows for linux if you're on
mac i'm on mac so i'm going to so i have
everything ready for mac um and then
that's it
yeah on to the next step

so step two would be to actually run the
create new app command to create our
project template brought to you by near
to start off our cool decentralized
application
npx create new app dash dash front end
equals react the name of the project
which is block vote
that's what this whole like line here
looks like uh so essentially what's
happening here is you're saying npx
create new app that's the project
template
um you know starter dash jazz front is
equal to react if we don't put this here
it's going to build out the entire
template in vanilla javascript but i'm
gonna be using react if you guys do not
know
how to work with react i'll include a
crash course link in the video to one of
my favorite youtubers traversing media
so you guys get it you guys get a cool
quick ramp up on how to work with react
and then the name of the project which
is block vote
uh these smart contracts are written in
two languages on the ears so one is
assembly script which is a lot like
javascript
and then the other one also if you guys
do not know send me a script i also put
a crash course video
uh link in the description for sony
script also by traversing media it's a
great
great way to start writing an assembly
script um
and then the other language that near
writes their smart contracts in is rust
much more secure much more safe language
there's a little bit of a learning curve
to it but
again there also be another crash course
video by traversing media in the link
i'll also put in the description for
that
and if you guys would like me to make a
rust version of this block boat tutorial
video please let me know in the comments
below i still
make one anyway because it's good for
you guys to have one under your belt
um and then with that we can just jump
right into vs code and get our project
started

okay everyone open up your visual studio
code ide to start off
creating your project and then hit on
this file button and navigate to this
open button
to navigate into the directory of which
you want to actually create your project
so i'm in this tutorials folder here
this is where i want to create my
project so i'm just going to hit open
and just spit me out here so there's
nothing in this folder right now so this
is what it should look like
um hit command j if you're unmatched up
your uh terminal here
uh otherwise you just go over to this
like top bar here
navigate to the terminal button and
select new terminal to open up this
built-in terminal
that comes with the microsoft visual
studio code type in npx
that's that that was included with our
node.js download
it's nps create near app
dash dash front end as we discussed
earlier
if i can spell front end sql to react
and then the name of the project which
is block
vote and hit enter and we should be
underway
with our installation

yeah this is the done message we get the
happy hacking message it's really cool
really fun really lively
uh so that lets us know that the project
has been nice and created
so that's our project folder we can
navigate into it in our terminal so type
in cd
hit tab and then hit enter to navigate
to the block
vote folder just see this name switch
over to blog vote to know that you're in
the correct folder
type in yarn start
to create your project instance what's
going to do it's going to
use nodemon to run a local node.js
server to
kind of like show off school like little
like project template website that they
created
in the create new app template so just
give it a quick minute
so that account id where it says like
dev and all these numbers that's like a
development account or dev count uh
that's actually created on the new
network on the near test net
uh so anytime you run like yarndev
that actually creates a whole brand new
instance of a dev account
uh for you guys to play with so it comes
with cool fake new tokens it comes with
like
you know functional access it comes with
a bunch of cool stuff that i'll go get
i'll go into later it's also where your
um
where your smart contracts gets deployed
onto the test net
uh while you're developing here so i'm
gonna show you guys how to actually
customize that as well
if you guys do not want to use like a
dev camp you guys want to use your own
test net account
so once it says built it should just
kick you over to the
okay keep me over here that's fine
cool there we go let's put you up here
there oh okay there we are
so uh once you guys see this webpage
here you guys have know
you guys know that you guys have made
your first step into creating your cool
decentralized project
by running creating your app so good job
guys

so once you get to this page you see
that this entire like test application
is working
uh it's time for you guys to go ahead
and clear out all the template code
that comes with create new app uh some
of it i won't delete everything right
away because there's some stuff i want
to
show you guys and explain in terms of
the flow everything but
for now just follow my lead let's head
over to app.js and go after this first
curly brace and just to delete
everything um
replace the end curly brace uh make some
enter
enter some spaces there and just get rid
of that okay
uh and then type in return
parentheses div hello
world see hello world appear right here
uh go over to global.css and just hit
ctrl a
and delete everything type in body
margin zero
i think you see hello world appear like
this after that we're going to go ahead
and install react bootstrap
so go over to react bootstrap.com.io
go over to get started
and then copy this line here hit ctrl c
to stop your development server
hit ctrl command v to paste in that line
and start installing react bootstrap
okay so uh and then in terms of the css
we're going to
hit this line here
and go over to our app.js file
and simply import
our styling our style sheets after that
we're going to test that see if it
worked
by going over to search bar and typing
in navbar
to look for this component here
scroll down so you find the the dark nav
bar
and uh you guys don't have this but i'm
just going to delete this sass file this
scss folder i don't really need this
right now
um and then i'm going to paste
this in
surround this entire thing with
parentheses
uh just for the return statement uh of
course i have to actually import
everything we see here
so import
container
navbar nav nav
drop down all from
react bootstrap so you're going to hit
save
and uh yarn start that's right so we are
in start
to restart our development server
because that uh that out
uh and you should see this entire menu
here looks really cool right
it's perfectly reactive yeah it looks
pretty sweet so
we're going to actually uh remove a lot
of these links like we don't need
dank memes or more deets as much as i
love dank memes
um we don't actually need that uh so
i'm going to move on to the next step of
simply just getting rid of like these
lines and bringing what we want
so here where it says dink memes we're
going to just type in log in as a
placeholder
and then delete this href thing here
and this event key too
where it says more deets uh just simply
get rid of it
and get rid of this as well and type
in type in uh we're gonna do
they're called new poll
so new poll
uh this entire drop down section we
don't need such as get rid of it all
get rid of this uh pricing and features
page you can keep
this nav uh this like nav section here
so see what happens we have new poll and
login
looks pretty good so there should be
some spacing in between
um this like logo and these
these uh two these two buttons here so
let's see
what's going on here like why is it
spacing not happening
okay figure out what's going on here
it's some weird bug in the
in the css i guess they update things
maybe um but we're gonna replace this me
auto with mx auto
and add this class name uh actually
looks pretty good
yeah so we have mx auto which moves
everything to the side here
um and yeah looks pretty awesome
uh i'm gonna go ahead and like install
something else right off the bat
uh so that's gonna be um a react router
page
so if you guys aren't familiar with
react routers just wait like switch
between pages
um in react so it's a cool way of like
switching between between components
um it's react router
uh if you guys aren't familiar with
react router i would definitely
put a tutorial link in the description
so you guys can get started on it
uh just go over to the quick start
option
hit this installation or copy this
installation line
control c to kill your development
server command b to paste it in
and hit enter
and there we go okay so now we have
react router installed uh
this uh just copy literally everything
from this import statement down
to this colon and
place that let's place this right up
here
right right below our react bootstrap
stuff
surround this entire uh this entire line
these entire lines here
with this router tag
it's a router oh dang it i don't know
why this happens sometimes
okay there we are should
and then hit yarn start
so this router tag is going to allow us
to um it's going to bring in the react
router dom into our page so about um so
we can
um effectively use router and switch
between our pages so
it's really cool like you guys are
loving let's go ahead and change up some
of these uh
href links so let's delete this one put
slash here
uh for this link we're going to
type in href is equal to
forward slash new poll
and that's essentially it that's all
we're doing here
and cool so we have our like we have a
functioning um
functioning nav bar it's really cool i
think the next logical step is to make a
slogan button
work so let's go ahead and do that
so what i'm going to do is i'm going to
go over to this link set a link here and
type in on click
so on click
and put in a simple conditional
statement so it's conditional same is
essentially going to
check if the user is actually logged in
or not and if not they're going to run
this login function
and if they are they're going to it's
going to switch over to a logout
function but display the user's name
so we're going to type in window
window.account id
sql to empty string and there is
actually a
uh sign in uh function that comes with
near api js
but for some reason i just got into the
habit of doing it this way but there is
a sign in button feature so definitely
uh look for that just wanna make it make
that clear so
again what this is essentially saying is
um if window dot account is equal to
empty string
uh that means that the user is not
logged in so we want to run the login
function
uh if it if the window dot account id is
not equal to nepu string
then it is then the user is currently
logged in so we want to run the logout
function if this button is clicked again
i'm sure you guys are wondering where
window dot account is even defined and
really even comes from
so i'm going to go and explain that in a
minute all right for this
we're going to finish this login logout
feature
so window.account id
is equal to empty string question mark
we're going to display the word login if
we if we are logged in then we are going
to display the word window dot
account id in other words the user's
name
so now we save that this login event
should work now
so kicks this over to the wallet says do
you want to log in we'll say yes
and then it kicks us back into the
application you can see our username
appear right here
so where is this uh window data kind of
um you know
like thing get defined so let's go it's
actually defined here in details.js
so i'm going to make this as big as
possible so you guys can see
as much of it as you can
here we go so let's explain
everything that's happening here so
we're going to um so this first part
this first part of the
function is to initialize a contract and
set our global variables
uh this near equals awaits connect
line here is establishes where we're
going to store
our like our key pair so what this is
saying is that we're storing our key
pair in browser keys
in our browser key store uh which is
actually what you want to do for
front-end applications
so if we go over to uh application
go to local storage i'm not going to
expand this all the way up but you can
see like all these little near tags here
like all these like it says squish as
much as it possibly can okay here we go
see always like little near keys here so
that's literally the keys to our test
net application
near config is defined
services define is defined up here and
it's getting that function it's going to
be output this function called near
config and where's this function
coming from is coming from our config
folder as find up here so let's over to
our conflict folder and see what's in
there
uh in our config.js file you can see
this thing looks
massively insane right it looks kind of
scary but it's not too bad if you just
break out little chunks
so let's just focus on this little chunk
right here this is the chunk we're
working with right
now essentially um this is uh this
function just takes in
a parameter called environment right um
to see like what our environment is if
everybody
if our environment variable is equal to
the word production or mainnet
it's going to set our config to the
mainnet configuration
to connect our application to the
mainnet blockchain
set to developer testnet it's going to
set it to the testnet
rpc so that's going to says to the
testnet blockchain this is where we are
right now
so right now we're in again we're
defining this as development
and the environment variable even the
process the environment variable node m
is currently defined to development as
well or test net
uh so that's all the config files for
something too insane you can even follow
some of these where's the where's the
config file there we go
you can follow some of these links to um
actually you know uh
they're their legit website so you can
for example follow this explorer
you can see the test net explorer here
see what transactions taking place see
where the block height is get some
useful information here for development
um and so on and so forth yeah
definitely feel free to play with this
and check this out
um and just break up with little chunks
it's not this entire thing
so don't worry about that so let's get
out of here don't really care about that
right now
uh let's head back over to youtube and
continue on
so here we have window.contract this is
probably one of the more important
features
uh well it's all important it doesn't
work without any of this
um so for our window.contract
line here it's essentially making it's
actually establishing connection to our
contract
right it's also a place where you're
going to define your view methods and
your change methods
so what are view methods what are change
methods so view methods are read-only
and they only modify
they only they do not modify the state
of the blockchain
they only return some value and change
methods modify the state of the
blockchain
and they usually do not return a value
if they're called
so let me explain some keywords here so
state state
state is kind of like i'm like for thing
uh state is essentially like um when
you're modifying the state of the
blockchain you're adding information to
the blockchain or you're changing some
information to the blockchain
um so in other words like if i put mine
if there's a
contract call it says add name right uh
and i say and i call it i'm adding let's
just say my name dorian
to the blockchain to the blockchain
application uh that would be changing
the state of the blockchain
let's just say change that name from
during to bob that's also changing say
the blockchain
every time you change or add something
to the state of the blockchain you are
modifying the contract and you are also
going to incur a transaction fee if you
just do a view method
right so that's what this is like get
greetings you just get something
or retrieve something you're just
reading it so you're not really adding
anything
to the blockchain you're not changing
the state you're just reading it so that
does not
thankfully uh cost anything uh costing
anything in terms of transaction fee
that depends on how you write your smart
contract but
for most part it does not cost anything
to view information from the blockchain
and then of course we have our again uh
the reason we're here in the first place
uh window.accountid this is actually
where window
cut.account id is defined and simply
just returns
your account id so if i go here see i'm
logged in
right logged in blockheads.net open up
our inspection tool go over to
our console and type in window.account
id see blockhead.testnet um

and yeah so anyway uh yeah good job guys
you guys built out the nav bar and we
even got to go through a quick little
preview of what happens in the details
folder in the config folder
uh let's keep moving forward

next step is building out a front end if
you guys are interested in building up
the front end i'm going to
create repo for you guys uh where the
front end is already built out and
you can just focus on the contract side
of things uh but if you guys are
interested in like
building out from from the very
beginning which i do encourage you guys
to do so you can see how everything gets
plugged in
much more seamlessly um you know where
everything is
uh then yeah stick around and yeah let's
have some fun
um anyway i definitely encourage you
guys
to just build it from the start it's
pretty it's pretty good for you
uh so enter in the switch statement
uh and then type in the word route
and inside of route we're going to type
in this home tag here
and then after that i'm going to go down
create route again
if i can type route there we go
and we're going to create a tag called
pulling station
and then lastly oops uh end that tag
and lastly we're going to create another
route
and call this last tag new full
so these are three components we're
gonna essentially create for application
um so it's a scream at us right we're
gonna get a bunch of errors because we
have not defined any of this
so let's create a folder in our source
file
called components
inside that file we're going to a folder
we're going to create some files
one called home.js while i'm here before
you move on if you guys haven't
installed this yet i definitely
encourage you guys to install
uh react js snippets
oh go back there we go uh
react.js code snippets by charlampose
i'm sorry you can't say it last name i'm
going to butcher it um
uh if you guys do this it makes your
life a lot easier when creating new
components because you can just use
something like rcsp
hit enter and get this entire template
built out for you see that's right do
you type all this you guys do not want
to install it
feel free to copy this um get rid of
this props
type stuff let me just get back here
let's give
this like prop type stuff here we really
need that right now um
and get rid of that and just type in the
word
um home here is our placeholder
uh we're going to continue on add a new
file
called new poll dot js
rcsp get rid of this
new
new poll
new file
polling station dot js
rcsp enter same thing as before
care of that pulling station
care of this line we're good
so go go we're not going to go we're now
going to go back
that's all folks

is that that duck yeah whatever um
no porky pig that's what i sounded like
porky pig uh going back to our app.js
file
uh we're going to establish our links
so we're going to say exact essentially
exact is just
not there not there not home in route
exact
essentially exact saying um we want to
make sure that this path i'm writing
right now
is exactly a slash it's not it's like if
you don't write this essentially you're
just going to accept anything that has a
slash in it
as the home as a homelink it's not going
to work it's really interesting actually
um exact path equal to
slash pulling
hand cramp dude what's wrong carpal
tunnel
carpal tunnel oh jesus he's got it bad
quick we need ben gang

honey dude i've got as fast as i can
there we go
pulling station
and lastly same thing for here exact
up yeah yeah exactly
path equal to
new poll
so um again look at our links here so we
have let's see what's
wrong that's right and lastly uh we have
to import all of our new
brand new bouncing baby components
so import uh
i can't do that whatever home
from dot slash component slash home
and then after that import
new poll from
dot slash component slash new poll
that imports
polling station polling
station from dot slash components
slash pulling station hit save
should this be this should be working
again so let's see if this all
if this all works out right um so we can
hit
this button here hit go over to new poll
you should see new poll up here so you
know that works this button again
hit the home page see the home page
and if we go up here and type in
slash polling station should see the
polling station
uh i didn't create an explicit link to
this for a reason
uh because we're gonna build out a table
that's gonna actually um
govern this next and that's how you set
up react
router

okay the homepage we're gonna do is
we're going to
import a few things from react bootstrap
so we're gonna import a table top a
container uh and a button

from react bootstrap hit save
hit the home button here hello you know
what actually before we even go here
let's fix up this nap bar thing that's
going to bug me if you're not ready
um let's go back up to uh app
dot js
app.js let's delete this um
and what i'm actually going to do next
is show you show you guys this really
cool feature from figma
it's actually like it's actually it's
actually pretty fun uh so we're going to
put in an image text img
src equal to block
vote logo yeah but we have not imported
this yet so don't worry about
i'm not having this just yet uh it's a
black boat logo
we're actually gonna head back over to
figma let's see
figma
and let's see
so we're gonna go down here let's see if
we can just zoom in real quick
can i zoom in there we go so if you guys
um
so here's this really cool uh here's
this really cool feature by figma
so i made this logo um in figma for this
application especially for this
uh cool project um infigma so i made
this logo in figma
and what figma allows you to do is
actually export these files as different
file types you can export as a jpeg as a
png as an svg
um i like svgs because they're like
infinitely scalable
so i'm just kind of uh click on this
export group
group one button i'm gonna call this
block
boat logo and hit save
and i'm simply going to take this file
and toss it into our assets folder
and there it is
so don't worry guys i'll create a
download link for that logo in the
description
so you guys can download it that way um
and now we're going to just simply
import it so let's
import it right here so
images let's call this
components
images okay so what i call that called a
blockboard logo let's copy this let's
have to retype it
type in import
logo from dot slash
assets slash block vote
logo dot svg
hit save and there we go
so we have this awesome cool looking
custom block vote logo
uh it's much better than what i used to
do we should just type out the word
block vote
uh now let's continue on the home.js on
page
um okay so we have our table our
container and our button
so we're gonna do with all this so we're
going to
type in the parentheses here type in the
word container
type in the word table
yeah there we go that's um
straight from react bootstrap so yeah
don't worry too much about this right
now but
uh if you guys are curious you can just
go over to um
like react reach strap go to components
search up table and you can see how the
structure is typically laid out if
you're having a hard time following here
so you can just follow along with these
um table structures it's actually pretty
straightforward
so we have our um each of these like
table headers count determines like a
column
and tr's tr tag determines a row it's
actually not too bad pretty
straightforward you have your head
and you have your body it's pretty cool
let's keep going so we have um
t head say t head
tr uh
and then t h
and then this first column will be
the number sign so i'm going to save
this so you can see you guys can see
what i'm actually doing here
so you can see this like first column
being uh literally being a number sign
um we're also going to add some tags
here so add
tag striped
bordered and hover
and light spot right or stripped striped
stripped um and hovered so that's going
to be
a cool way of like you know you can see
actually these lines appear it actually
looks pretty nice now
like not too not too shank not too um
janky
let's add some spacing up between this
first row and then this uh this nav bar
that gets you out of the developers
table
so type in the word style
margin uh five vh is fine
hit save and hit enter so cool we could
see our table starting to form
let's keep going so we're going to have
th
a list of poles
and th go
to pull
uh then we're going to start to develop
our body
so type in t body
and uh this part's kind of the fun part
so
let's create this temporary array here
uh for now we're not gonna do this
forever
or use this forever but you know it's
pretty good now essentially we're gonna
have here is like a list of props
so uh i'm gonna say const
equal to sorry
prompt list and come back and change
this later
and the probably who would
win in smash bros
so in tbody uh we're gonna put in some
javascript so again this all this is all
here
jsx so inside this curly braces we want
some we're gonna actually enter in some
javascript
um i'm gonna type in prompt list
dot map el
index um
sorry about that message uh el index
so uh tr key is equal to
index
td um tr means row sorry table row
um putting in that key text so you don't
get this like error saying like um
essentially every time you use a map
function to kind of like iterate through
an array to print stuff onto a page it
will
um essentially want you to identify each
element you're printing out onto the
page with a key
and we're going to define each of those
keys as the index number
td is like a data column so td
and index one
i'm sorry index plus one
so why am i putting this plus one here
so let's say
uh let's save this see what happens
oh uh we have to also surround
everything here with return
uh inside return uh parentheses so type
in the word
return here oops
uh let's see
it doesn't like me
oh
let's see what's going on um
see return tag starts here
it ends where i think it's supposed to
be inside of here
there we go okay cool
okay so we have uh
one yeah listed one here
um and then uh
type in so you can actually see we're
printing out add a curly brace here
add the name of the array so prompt list
and add the index
actually we don't need to do this we're
typing the word element sorry
okay so you can see uh one who would win
smash bros
um and i'm going to do another prompt
uh let's see um
who is the
better actor
something like that so we have this one
and two if we get rid of this index plus
one
it's going to um start from zero which i
don't really think looks that good
so i want to start off from one so
that's simply why i put the plus one
there
uh we have we're missing obviously we're
missing one column
and that's going to be your button
column so we're going to use the word
button
from react bootstrap um
and type in go to poles
so that's actually going to be the way
we're going to navigate to the polls
um you know within uh
or from this home page uh we have to
surround this with a td tag as well
so td
there we go that looks pretty sweet
right uh
but yeah in terms of the front end
that's it that is our homepage
so good job guys
next on the list is the uh you know kind
of the meat of the application the
polling station
i think it'd be a lot of fun to build
out so let's go ahead and design our
polling station
so head over to the polling station.js
file
and we're going to import a few things
to start off
so we're going to import
a container
a row column and a button
from react bootstrap hit save
uh we're gonna our entire um our tire
like return statements can be filled
with first uh well first parenthesis and
then after that
container
inside this container we're going to uh
essentially we're going to um split this
up
into one giant row with three columns
right so i have these little lines these
little guidelines here
as you can see uh kind of detailing what
each columns you filled with so it's
gonna be called the pikachu picture
the button and then the result the
second column will be filled with this
prompt
there this uh it's not it's not going to
be here don't worry about that and the
third columns will be filled with the
second candidate the button and then
their vote count
so we're going to say row
column
uh and then essentially
each column will be filled uh with its
own let's see
with his own container yeah
so container uh
and that okay
uh before we even move on uh this is
gonna be a very common
thing where i do i'm going to type in
class name
is equal to justify
content center
uh and then d dash flex so that's
simply a way to justify the contents of
um
our application uh i'm sorry of the
column and rows
i'm gonna type in uh in your url type in
polling station
so we can get on this page and see
what's actually going on
uh underneath container you're gonna add
a row
i'm gonna start off with some uh styling
to the row so style
is equal to margin
top 5eh
with the background color
of hashtag c4
oops in a single closed c4
picking type before c4 c4
and it's going to scream me because i
forgot to put the hashtag in front of it
it's a hexadecimal
and why is this screaming at me
oh closing tag for the row
then within this row now so bear with me
uh we're going to create div and that
div will have a
style tag to it so add some style some
player
add to it and that style tag will have a
display of flex i'm just getting this
css out of the way not going to be not
going to focus too much on this
but just kind of follow along justify
content
add the word center here
add some padding 3vw
hit save um and then
inside of this div we're going to add in
our image tag
so this is where pikachu is actually
going to display uh
add some styling out of the way to get
this out of the way so we're going to
make these images all
on uniform on this page
so we have nothing that looks too out of
control
uh this may not be the best way of doing
this but
for now it is the way i want to do it
for this example add a width
of 20 vw
20 vw so we're using this we're using
this inline styling that's what's called
react so inline styling
uh and close the image tag
um and then the source for this image
will be a state variable
so source is equal to single quotes or
single curly braces
candidate one url
it's going to scream at me again because
i don't have that defined
but that's okay let's go up and actually
define that right now
so from react
we're going to import the
use state um
use state function

const uh call um
what's it called candidate one candidate
one url
and then change candidate one
and set that equal to use state okay so
if you guys have never seen this before
it's not too hard
uh it's not too scary um we're gonna
find some filler image and put in there
for now
um stretch
there we go uh so what's happening here
is that this is a state variable
this is a function it's a function uh
that's going to uh this is called the
solve cover react hook back
hooks by the way so if you guys get
confused with this just google react
hooks
um so this second uh parameter is like a
function that's
that's literally its purpose is to
change the value
that resides in this um candidate one
state variable okay
so this is the variable this is the
function that changes the value within
this variable
this use state function is going to be
um
the default value for this so uh default
value i'm just going to
look up um
uh let's look up like i don't know a
loading
screen for now uh just doing something
really quick and we can just
grab something like this again it's not
to be super fancy
uh copy image
um actually you know what i might i
can't
make my own but okay whatever uh open
image new tab that i'm looking for
so you can see this thing opening a new
tab uh i may make my own and like link
it in the description for you guys and
change that later on this video but for
now this is totally fine
uh and just set that as your default
value
yeah okay okay yeah i'm gonna be lazy
i'm just gonna do this real quick um
so i'm gonna add like three circles
make them black
there we go so copy paste
paste oops
perfect group
selection you guys don't have to do this
i'm gonna i'm gonna give you guys this
uh
this image
svg
loading circles hit save
toss this over here to assets go back to
our
polling station hit ctrl z to undo that
uh and then if you guys want to add
something for yourself that's like
totally cool too
i am going to import loading circles
dot slash asset slash loading
circles dot svg and then just
toss that in here so loading circles
um
yeah that looks fine uh
cool so let's see if you can actually
censor that right
so let's see display dot
flex justify
content and center
let's enter it oh maybe
nope that should have worked
uh oh you know what oh okay no actually
it's fine
no i forgot this the entire row is
what's that what is what's has that
background so this is actually okay so
we don't even need you
need this ignore that step anyway sorry
about that quick detour
let's let's keep going um
okay so now bear with me for a minute
we're actually going to uh set up our
logic separate logic
for um but first we actually need the
button right so the voting button
okay so it's fine let me find a button
here
okay so we have this container we have a
few rows here
underneath our image is going to be our
button
oh sorry a row uh and actually make two
rows here
so this is gonna be kind of cool another
row here
uh inside this first row that's going to
be where the actual results are going to
be
for the for the vote uh we're going to
set that
to display as a conditional statement so
i'm going to put three here for now
um and around this three
i'm actually going to create div
yeah okay so then around this three is a
div inside this div we're gonna add some
styling right away so style
is equal to uh display
flex
justify content
center font size
font size um
8 vw in single braces 8w
padding 10px
background color
uh i think it's hashtag a4c4 yes
so hashtag c
check c4 c4 c4
okay uh yeah so let's keep going um so
we're gonna then we're gonna clean it up
and in a quick minute
um actually yeah right now let's just do
this real quick
uh so in this row we're also gonna add
some styling
so style
is equal to margin top
5vh
and then uh last
name oops not inside sorry not inside
these curly braces so
even before that so class name is equal
to
justify
dash content
dash center
and d dash flex
i need to spell content so content there
we go
um so cool yeah
so we have our very first uh we have
very first score
um and we're gonna add some conditional
uh code here to actually
uh determine when this gets um shown or
not right
so because we don't want this we don't
want this information being shown
before the user made their makes their
vote so we're gonna do
is we're going to take this entire row
and
um we're going to add some curly braces
around it
and before the curly braces i'm going to
type this thing called show
results we haven't created that variable
yet but we will in a minute
then at the end of this uh at the end of
this conditional statement we're just
going to type in the word null
so up by our state variables we're going
to add a new line
i'm going to make this a little smaller
so you guys can see more
uh const
actually squish that okay
show results change
we change results
uh change results yeah results display
able to use state we set that equal to
true for now hit save
and if this is false watch what happens
just goes away
right so hit true it comes back
so uh we're gonna keep that there for
now
and under row you only have one more
thing to add here
so we're almost almost done with this
this section this parts
this part is kind of the weird bulky
part of the front end
so in a row we're going to create this
um we're going to create button class
inside the button we're going to say
vote hit save
let's see the vote here of course we're
dealing with um react bootstrap so we're
going to add
the tag class name is equal to
justify content dash center
d dash flex
censored there as well it's kind of cool
right
um so let's keep it up let's keep going
uh so by this button
nice button um we had some functionality
a little bit later
uh okay so don't worry about that right
now so now
next step is to add another column
let's see add another column
so column same thing so
class name is equal to you guessed it
literally this so it's probably going to
be one of our most used
statements here probably find a way to
make that even a little
a little easier to write someone to keep
typing up the entire thing
um inside here inside here we're going
to create div
so dave add some styling
so style is equal to
display flex
justify content wow cannot see any of
that
content what is going on
okay uh center
background color
um it's going to be hashtag c4
c4 stuff dang it hashtag
c4 c4 c4 hands cramping
height is going to be 20
vh 20vh
align items
center padding
it's going to be 2vw
text align
center and it's going to be where the
actual like message prompt is gonna be
so we're gonna say um who
would win in smash
right um
let's see i have anything wrong here uh
center c4 c420
uh center to vw i feel like i'm missing
something oh
because i'm missing something
yeah okay so here uh also add um align
items center
and there we go so if our prompt moved
and shifted towards the center
so displays reflect justify content
align items
uh oh okay because i misspelled the word
align
cool okay so we have our prompt we have
our image
we have a results button uh and we also
have
like
we also have our sorry i also have our
physical button down here
um and actually to that button
yeah tab button i want to add so i want
to add some a quick margin
to can't give it to spacing so i'm going
to do a quick style
is equal to margin
top 5
vh just to add some extra spacing there
okay so um next part is a little bit
easier so
you know we literally just take
everything we have here for his first
column so let's copy
all of this
um and paste it under
here
we want to change a few little things
here
so i'm going to do we type in the number
one so
um we can see we have to add
candidate two here right so you have to
wait make one for
candidate one and make another one for
candid too hit save
let's keep going
okay um
yes so essentially where it says i feel
like i'm missing a candidate too yeah
right here where it says source is equal
to canada uh one url we're gonna we're
gonna add
canada to url here
um yeah so hopefully this is all looking
you know fairly familiar
uh if i expand this out more you can see
these pages are reactive thanks react
bootstrap yeah i mean essentially yeah
that's it
so that is kind of that is the front end
for our um
for our polling booth uh component
uh yeah so i know there's a lot so keep
it up keep going push through it you
guys are doing great
um we're gonna so next step we're gonna
create the new poll form
uh but then after that we get to
actually work with some cool smart
contract stuff
let's get over and uh create the polling
booth so separate new poll
um then go into newpol.js
and we're gonna import some fun stuff
from react bootstrap so
do there we go
so import

container form button that's all we need
from react
bootstrap hit save go here
into return statement it's around
everything inside of container
oh first parenthesis and then container
hit save again hit enter
type in the word form

hit save we'll go kind of fast here
so um i apologize uh so
style is equal to let's get the sounding
out of the way
some margin top test i'm saying between
the navbar and the container
uh that be 10px
and then after that okay so after that
we're gonna go into our form
type in form dot group
uh add a class name so class name is
equal to
mb-3 uh that's a react bootstrap class
for spacing or uh
yeah class yeah uh classroom spacing um
css class you're facing contro i don't
need that okay
um inside this group we're gonna add a
label so
form dot label
candidate one oh my gosh
candy date

just my computer there we go candidate
one name hit save see that name p
right there which is kind of cool uh
sorry you can ignore this my
styling sh my styling is kind of weird
my editor
uh after that type in form dot control
and add a placeholder tag inside the
first
opening tag so type in placeholder here
enter candidate name can candidate
name hit save and there we go we have
our first like input field
uh with every input field it comes with
the ref right so we're going to want to
reference what's inside that field so
let's just get that out of the way right
now
so ref first curly brace candid
date name one
can to date name one cool
hit save uh it's gonna scream at me
saying like this does not exist
uh so we wanna do is actually go over to
react type curly brace type in use
ref uh hit enter
that's good okay save um
that's okay oh add a comma between the
react in this thing
so now inside of here we're going to
type in const
candidate
name one is equal to use ref parentheses
and that's it see not so bad right
so let's keep going form
dot group form group
class name is equal to mb-3
um form.label
it's going to be candidate fun
image url hit save
go one line below that type in form dot
control
and of course you can see what all this
form.control form label stuff
um is on the react bootstrap website uh
so type in oh my other light's not on
uh type in ref
equal to candidate name one
url and then
sorry put that in curly braces
and add a placeholder holder
equal to uh enter
image url url and make these capitalized
hit save if you can error again it's
totally fine
because you have to add a reference here
so two lines
const equal to that equal to use ref
parentheses uh you can just duplicate
this first line down
and add it and switch this over to two
because we need that anyway
deplete this line as well and switch
this over to two
uh so candidate name two url kind of
name one url can name one candidate name
two hit save the next part
is uh you know fairly really easy so
we're just going to copy all of this
and simply go up go two lines below and
hit spam
paste change this one to a two
change this one to a two change this one
to a two
and change this one to a two so i have
everything filled out for our second
candidate
uh last form group will be for our
prompt
so i'm going to type in word form dot
group
class name is equal to
mb dash three
form dot label
it's prompt
form dot control
ref is equal to prompt
ref the placeholder
of add prompt
uh conclude that hit save gonna get an
error
because we haven't created this prop ref
yet so i'm gonna go down here
add two lines hit const
paste that in set the angle to use ref
to parentheses
there we go we only have one more thing
guys one more thing for this front end
and then
literally our front end is essentially
done after this uh so button
also forgetting something should
probably have let's see
submit uh button submit
uh and variant signal to
primary
uh and then that is essentially our form
yeah i mean great job guys you know this
was a lot of information
a lot of stuff let's just let's just
like circle back and navigate through
everything
so we have our um our home page which is
a list of polls here
so we can see um who went who would win
in the smash bros who's the best actor
uh we haven't set this link yet i will
in a minute
but we can go to our polling station by
typing in
polling station uh we can see our polls
here
so we have picture one picture two the
prompt the results
and the vote uh we should actually set
these results to um
default so we don't that so by default
we do not want that to be seen so we're
gonna set it to false
and then after that uh we can go over to
our new pull button
and get our entire form here yeah so i
mean yeah great job guys it's all
responsive
you can see that like this all like
resizes pretty nicely you can log in we
can log out
um so next up is the fun part where we
are actually
creating the smart contracts this is a
cool part guys so
sit tight and i'll also upload upload
this part to github so
uh users that don't want to go through
the process of making the front end this
is where you guys are going to
um well appear and start working on the
contract side of things
so yeah fun stuff

for those of you who are um jumping to
the contract side of things
uh head on over to my github page and
you know go to the blog for tutorial 2
repo and select the branch front end
complete
to essentially start from the front end
and start working the contract to start
seeing how that side of things is
implemented into the project
so with that uh first i'm going to check
out the main branch again so
hit checkout i mean
um with that let's just keep going
okay so the contract code contract stuff
this is the cool
this is the fun stuff so head on over to
contract uh
assembly and then go to index index.ts
and i'm gonna
make this screen super small and go over
everything that's here so um yeah this
all may look scary definitely read
through all these comments if you can
uh just to get a sense of what's going
on with the default code um like i said
right through everything
but essentially i'm just gonna tell you
guys what's going on so
we have uh two sections of code defined
here
so we have our view methods of view
methods
right here and our change method so
earlier i said
change methods
so changes state of
block chain
costs a transaction
b to do so
for view methods uh
this does not change state
of the block chain where you guys do
have these notes
for review uh and then um does
not incur a fee
polls and reads information
from blockchain
uh sorry about that okay um
ads ads or modifies
information to blockchain

uh let's give these default functions
before we get rid of them uh so get
greeting as it
um as it sounds it's getting a greeting
from the blockchain so you're just the
raw storage i get which is a
way to interact with the on-chain simple
contracts um
in other words it's just reading uh
this value this the this message that
the user
has inputted into the blockchain uh
let's start with sec reading right so we
have our message
our message here that the user which um
the user which is being defined as
variable account id or context.sender
is saying to uh so it's like a key value
pair for storage here so
keep being the user's name and the
message being the value and then that's
setting the value for the message and
this is simply retrieving
that value um so
i'm going to show you guys the the
essential pattern i do from
for all my like you know get and set
methods
so let's delete these uh let's delete
this thing i need that and let's delete
all these comments up here
um let's hit save um and then i'm also
going to show you guys essentially the
workflow
that's involved with setting up these
things
actually i'm going to bring back a few
of those items here
okay there you go
okay so we can see that this function
structure
it essentially goes like this we have
export that makes the function public
to the contract um export function
get greeting right get greeting this is
all written
in assembly script which is a lot like
typescript if you guys do not know
simuscript i'll put a link in the
description to crash course video
uh for you but anyway uh so um in
semiscript you have to define
you have to define that you're the
variable types for each of your
variables
so you have a couch we have account
which in which we're expecting a string
to be implemented here um we're
expecting this function that's what
colon mark is saying
essentially says we're expecting this
function to return
either a string or a null value string
or null
value um so get the function get
greeting will accept a string
named i'm sorry a string and put it in
the variable account id
uh do stuff with it so in other words uh
you know send that to the
send that to the blockchain as the um uh
key to read
and then it'll spit out this function is
going to return a string or null value
so it's going to return either something
or nothing
right for the set greeting we're
accepting a string
storing in the variable message
returning nothing that's avoided so
returning nothing
um where we're defining this variable is
the context.sender which is the user
itself so it's going to be the person
that's currently logged in
this logging log is kind of like
console.log
so it's essentially printing these
messages out to
via console and then it's setting
the key account id which is the user's
name
um with the value of this message which
is a string
after you create these functions get
greeting and set grading
we're going to go down to utils.js and
you can see that
get greeting and set greeting are set in
this view methods and change methods
uh array uh you know accordingly so
if you're if you're defining a new view
method you put it in the speed methods
right you're finding a new
change method you put in this change
methods array it's pretty
straightforward
um and that's essentially the flow after
every single change
you uh create you make to your smart
contract in the index.ts
file you're going to recompile that
smart contract and get a new wasm script
out of it
so you can find your wasm script here in
the build slash debug folder
so um to build it just type in yarn
build
and see you can go over to your
package.json up down
down here see what that build script
does
so you can see npm run build contract
npm run build web
um so when every time we could change to
your index.ts value to run yarn build
to recompile the smart contract
and then you can after that you can test
it out in your front end application
uh anyway so that was a lot of stuff i'm
gonna go back to
where we were so this is all we have in
our fault in our file right now
so just this import statement and then
all this stuff here
um
once this is done building can get this
message here so built in 16.25 seconds
saying everything worked out and it's
done
it'll let you know if there's any uh
compilation errors in your in your
index.ts file as well
uh so just keep that in mind um so we're
gonna write out our entire contract in
one single go
be pretty fun so um
up here we're going to import
this thing called a persistent map it's
a persistent map
let's actually get rid of storage
and context we don't actually need those
so i'm going to hit save
um so
a persistent map is near is a probably
near sdk as
uh library it's essentially a storage
wrapper that
makes this makes this uh or makes your
data structure act like a map
so mapping any other language which is a
key value pair
python ski value pair and uh in like
um i forgot what other language it is uh
in javascript it's something like an
object but you essentially have a key
value pair
uh it's pretty cool i'll show you guys
all cool things you can do with it so
const um
const candidate url
is equal to new persistent map
string
string
candidate url
so what's happening here with this
persistent map is we're saying that
we're defining the variable to a new
instance of a persistent map
in which the key is a string and the
value is going to be also a strike
this prefix here is simply just to
prevent data collisions on the
blockchain so that's all this is for
i'll just give it a unique name inside
these parentheses
our next persistent map will be const
candidate pair so this will be a way for
us to store
the pair of candidates for every single
polling session
probably make more sense if you actually
see it so
the key will be a string the value will
be a string
array and i'm going to
give the prefix name candidate
pair
let's get rid of that second d here okay
const prompt
array is equal to new persistent map
string string bracket
okay then array
of props so uh again
this string and bracket notation just
means it can be an array of strings so
it'll be like
you know this would be like uh so this
is like an array of numbers right so
this is going to be
um like a number uh array
right or this can also be like a
like an i 32 array
um an array of strings to be like
dorian was
here and this is a
string array so hopefully that daytime
makes sense um
again i'll look at the crash course uh
link in the description for you guys you
guys can
have some uh you know basis to start off
if you're not used to
some descriptor typescript next
persistent map would be a vote array
so the place actually store our votes
so vote
vote array is equal to new
persistent map oops
persistent map string
i32 array
uh stores
votes
so next step after that is the user
participation
so this one is simply just to um make
sure that or to check if the
uh user has participated in certain
polls so they can no longer participate
in that poll afterwards
because we don't want a user submitting
like 30 votes if they've already voted
so const user participation
is equal to new persistent map
string string array
user participation
record
um so these are our entire set of
persistent maps that we're going to be
relying on
uh and a misspelled candidate pair so
candid date
pair there we go um
i have this add-on to check spelling
it's actually really cool
uh so let's go down to our change
methods so i'm going to show you the
flow for changing methods they're all
they're
kind of fun so let's start for the url
so export
function add url
uh so name is a string url will also be
a string
we're going to be turning void so this
function's gonna be turning nothing
candidate url uh
there we go um
dot set so that's set method we'll set a
new key value pair in this
persistent maps and name comma url
and logging log so that's going to be
our way of notifying the developer
um that a url so added url was added
it's your edit url for
name okay
so if we run um so i'm going to show you
guys what happens if we don't do it if
we don't uh complete the flow so i'm
going to type in yarn build
to build up this contract because we
made a change to index.ts
so we need to rebuild it uh
let's keep it going
okay it's done uh type in yarn to start
let's build it let's build it let's
really really build it there we go
um you can open up your terminal
and watch this if i type in a
window dot
contract dot add
url we get this undefined notice right
because the functions exist
because we have not completed our flow
so you have to take this name
add url go down to utils.gs
js js sorry uh we're adding
something to the blockchains we are
changing the state of the blockchain
so add url and hit save now we can do
await window dot contract so to do away
because
uh wait the awake keyword is important
so we have to do a wait because
um all your contra calls all your
function calls
they are asynchronous so you have to um
you know
talk to the rpc and then get some
response right
so that takes some asynchronous time so
wait
window.contract dots add url
then i forgot what the parameters were
already
oh name and url uh to actually um
to actually like call this function
you're gonna type in the word name
you're gonna make you're gonna create an
object instant inside uh of your
of your arguments um section of your
function uh so make an object instance
here
as your parameter type in name
then you know dorian comma url
colon test
and object instance and function
parentheses
hit enter
you get this cool receipt from the
blockchain and get this message from our
um contract saying added url for dorian
and that's so you know it worked so yeah
i'm a great job guys that's the very
first
change method um so let's keep this
going
uh we also want a way to actually read
that function right so
um let's see
so we're gonna call this function get
url so export
function get url
url name string
and oh it's going to return a string
and honestly here's my flow for most um
for most you know for most uh
get a view method sorry few methods
first i have to first
check if that

if the um name is even in the persistent
map
registry right so i'm going to type in
uh
contains it's kind of a cool method that
comes with the persistent maps so you
can even see if a key exists within that
persistent map
that key is our name i'm going to hit um
colin there so uh curly braces there so
if the canon name
does exist then i'm just going to return
turn candidateurl.getsum
and then name right i'm turning a string
so it's kind of cool is that it's um
looking
uh okay
so it's kind of cool that this
function's looking for a string right
it's saying like is this a string
are you returning a string if you are
awesome if not you got to fix something
else uh return
nothing right so um
now what's kind of cool is like if i
were to change this to i 32
i'll get an error here right because
it's returning a string it's not
returning an i32 variable
so let's change that back if i were to
say
i32 here right we get that same error
letting us know that this is returning a
string not i32
so it checks the types for which is kind
of cool
um so let's keep going
uh so i'm sure you can
rebuild this we could test this out in a
minute um
obviously if we don't return anything
type in logging
log can't
can't find
find that user
uh so let's keep going so we have a
little bit of quite a bit functions to
get through
so let's out of all of our change
methods
so next step will be export
function add candidate pair and you guys
know the flow now so that's essentially
the flow of adding the sum of
adding like functions adding view and
changing methods to your smart contract
so these last two we're just going to
fly through so prompt
string uh
name one what's happening here oh
name one is a string name two is a
string we're gonna
um essentially we're going to store
these candid pairs underneath
the uh
underneath the key of a prompt so our
prop is going to be a key for a lot of
these
uh so that's going to return void
and then candidate pair
dot set under prompt
uh name one name two
so that's our array of strings right
have a candidate pair up here
wave strings totally cool next up
will be adding your votes right a place
actually store our votes
export function add vote
prompt string
index i32
void um so if
the vote array dot contains the prompt
then we're going to create a temporary
array so temp array
equal to vote array so if this value
exists we're simply just going to
get the current values which should be
an array of two numbers
and then i'm going to say let temp val
retrieve
one of those values so rate temp valve
is equal to
temp array um retrieve that from the
index
and then add one to that value so new
val so new valve is equal to
temp val plus one
and then we're going to replace that um
the index with that new value so we're
going to say
temp array index
is equal to new vowel right so
essentially the vote is going to look
something like this
it's going to look like see
so i'll just say pikachu has three
and kirby has five right kirby gets one
more vote
i add one to five so i get six so that's
essentially what's happening here
um oh yeah and then after that we have
to actually save that to the blockchain
so vote
array.set prompt
dot view array that's it
um or no
temporary sorry temporary
there we go
else let new array
equal to zero comma zero
so we're creating a new ray uh in which
both users
have no votes right if the prompt does
not exist then we're
creating a new a new instance of this
prompt right where
both um users start off with uh zero
new array index
is equal to one right so
whoever this vote is for gets the first
vote
vote array dot set prompt
dot new array
hit save keep going
uh so next step is to record the user so
we can see if the user has participated
in the voting process so export
function new record
user
prompt string user string
returning voice must change methods
return void
if user participation does not contain
or does contain the prompt
then we're going to let a temporary
array so temporary
equal to um or store the
uh the user's
name right or sorry temporary restore um
like all the users that participate in
this vote so
this use this like user array is going
to turn is going to um
essentially list out each and every user
that has ever voted
in this in this poll so get some
prompt
temp array.push user
so we're adding a new user to that
existing list of users
user participation dot set
prompt temp array
so now we're setting that new update
array to the blockchain after we added
the latest user else if this is the very
first
user we're just going to set that first
user
to the prompt uh by instantiating a new
array
and that's record user and that's all of
our change methods actually
so now let's go and create some view
methods
so view methods fun stuff that's where
we actually get all the information
so this part's a little bit for most
part simpler for the most part
so export function
did participate did any let's see
participate
so did the user in question that the
user that's currently logged in
participate in the vote that's what
we're asking here so prompt
string user string
turn a boolean if user participation
dot contains prompt
let get array equal to user
participation
dot get sum prompt so
we're again restoring the temporary
we're storing uh
the um sorry we're storing the list of
all the users into our temporary array
called getarray
return getarray dot includes
user does this array even include user
because
this is um did this user um make it make
its way into list meaning like they ever
vote before
else uh
yeah else
logging log
prompt not found the prompt is probably
not gonna be found right
uh it's the only other uh other
situation so then if you have to return
something so
you're going to return false
next step
export function get all
prompts i'm gonna get the entire list of
every prompt that was ever created
all the prompts were stored in a string
array uh
so we're going to check if the prompt
array
that contains the key that we're saying
by default which is going to be all
arrays
i think i'm going to be missing a change
function but let's just see
return prompt array
get some i'll erase
uh if
if no prompt has ever been created in
the history of this application
we're gonna just return the message
logging log no prompts
found right and we're going to we're
going to return
an empty array because typescripts don't
want something
next step uh we have do we have to get
url
we have get url uh next up is get votes
so export function get votes
prompt string we're returning
an i 32 array right remember the whole
like
pikachu gets three votes thing
three votes and kirby gets five right so
we're getting this array here
rave two um
so if boats array dot contains
um prompt
oh my god prom pot
there we go prompt yeah
vote array
dot get some prompt
right we're just getting all the votes
otherwise
return zero zero with the message saying
logging log
prompts prompt
not found for his
vote um
i think that's everything so get all
prompts
set new prompt i set a new prompt
oh yeah i have to add a prompt array uh
i think i missed one yes we did miss one
okay
last function guys export
export function
function add to prompt
array prompt
string
void logging log
added to prompt array
if
uh if prompt array dot contains i want
to keep misspelling prompt
that's prompt prom that's cool let's go
to prom
um contains
all arrays right so making sure that
variable is the same
yeah all arrays so cool
let temp array equal to
prompt array
dot get sum all
arrays
temp array.push the latest prompt
so this is just all this fanciness is
just to create a list of props
they're just having one fixed key for it
that's why we have this one fixed key of
all arrays
so it's not dynamic key right um
there we go
so otherwise
we're adding our first key adding a very
first prompt if there know the prompt
saver exists we're adding our first one
so prompt oh no prompt array
dot set all
i'll erase
prompt hit save
so now after all of that this is our
entire smart contract
uh after all of that got to actually add
all
each of these individual names to the
utils.js file
so we're going to start off with all the
view methods
if you hit um on mac it's alt double
click
to select multiple lines or select
multiple on strings
and then
sorry and then uh head over to utah.js
and just place them all into your v
methods
and then add strings around them add a
comma
surround it with a string add a comma
add some strings
and uh what's happened what's happened
here
oh add a comma up here as well
um now we're going to add all of our
change methods
so
again that's uh for me it's um i'm sorry
i think i think for mac
i say alt i mean option i have two
different keyboards here so it's kind of
confusing
uh so option double click is how i can
select multiple things
add a comma here paste all these in
let's run
oops surround all of these with quotes
and then add a comma add a comma add
comma
add a comma and hit save
we're still not done right because if we
um
oops twice
so uh if i define these without
rebuilding the contract let's see what
happens we get window
or wait window dot contract dot
no no add vote
right it's gonna say it's gonna wait
it's
like it's gonna check the blockchain as
you say contract methods not found
because we have not
rebuilt the contract it's gonna rebuild
a contract
there we go hit yarn start
so now we can do i don't know i think
we're missing one
oh
yeah you're missing get url uh add
get url it's definitely better to like
add these functions as you're building
them out
um so you don't forget anything but huh
it's okay
uh so let's do await window
dot contract dot ooh contract dot
get url uh and then
name so name
name dorian
and there we go yeah so i added test
earlier
so that all comes back full circle so
great job guys
you guys just built out your very first
smart contract
or maybe you're doing this again who

knows
you guys are champions i know the smart
contract part was long
uh but guys we're almost done all that's
left is to implement
all these functions into actual
application
so let's start with the form the form is
gonna be a little bit yeah
gonna be kind of bulky but that's okay
um
so let me just get my notes up
so new poll so we're gonna navigate over
to newpol.js
and start at the very very top okay
so we have all these like used refs
right all these like references pointing
to different sections of our form uh
that's going to be our means of actually
getting the information that's written
within each form so
to kind of kick things off we're going
to create a function that collects all
this information
and sends off to the blockchain so i'm
going to say let's call this function
const
send to blockchain
it's a bit on those but you know it
works
async okay so this has to be an
asynchronous function because like i
said
uh all smart contracts are what all
smart
are i cannot say that word
all smart contract function calls are
what they're asynchronous
um so that means that we have to uh
essentially wait for the response to
return to each value
each time we make a contract call
so i'm going to type in await then
window.contract
dot dot
add url
um and then i'm going to pass in the
name
of first an object instance so then
first
property will be the name the name will
be
candidate name one
dot current value
oops dot current uh i am betraying this
okay the name will be can
the date name one dot current
dot value so that's going to pull
whatever i type in here so if i type in
uh dorian i should get the value door in
um so
there you go uh then
the url itself so url uh
candidate
let's copy this put this here okay
candidate name one url
dot current dot value
uh and then that's essentially it here
um
well not for the entire function but for
this part of it right
so we have to make this whole thing
again so we're just going to duplicate
this line
let's hit alt d there we go
and switch these numbers from one to two
so two
there we go i think misspelled async
there we go
think uh look at all that things aren't
screaming anymore
to
and i think i may have deleted a
parenthesis so
there we go i swear i know what's going
on sometimes
okay so uh next line will be to add the
candid pair
so wait dot contract
dot add candidate
pair
so we're going to need the prompt
which is going to come from prompt ref
uh prop ref.current.value
comma and then name one and name two
which is just going to come from these
so i'm going to copy
this value here create the name
one property paste that in
and then grab uh oh yeah then just type
in
name two paste that in and then switch
this first one to from two to one
this first name uh this first candidate
name
current value from name one two that's
from name two
to name one uh this should be await
window dot contract dot add candidate
pair it's gonna save
all of this um and then we have one more
function to go we're almost done here
await window.contract dot add
to oh i forgot what this one's called
i think it's add to prompt array so add
to prompt
array yeah so copy this
um we have one our parameter here so
it's just the prompt
let's paste that in call prompt

and that's it uh well that's not it
i keep saying that's it i have to stop
saying that we start to actually make
this uh
you know this function work it's like
actually call this function so let's go
down to our button
and say on click
and this is called add
to blockchain or send to blockchain
send to blockchain there we go
save everything here we can test this
out
so i'm going to refresh this page i
think it disconnected
um i'm going to pull this window over
here
open up the inspection tool and then
let's see what we do what we have here
so let's just say um
i don't know enter candidate name dorian
it's our url
test one name two uh
bob then test two
who is the better bob
and hit submit
okay so add url's not a function
is it not
it's not i misspelled it okay
it should be uh lowercase r and l

okay one more time dorian test
one bob test two
uh who is the
better bab
baby there we go hit submit okay so
added url for dorian
added url for bob

it looks like parameter prompt with type
string is required but missing
uh so we know the euros are working so
perhaps
oh yeah okay
forgot to actually complete this line so
at the add to prompt array
type in prompt prompt
and then essentially just this line here
right
so snag this
and paste this right here
hit save i'm going to do one more test
hopefully it shall work
dorian test
one pikachu
test two who
will catch who
or who will be
the trainer right we'll probably pick it
to a better chance of
you know catching me i'm gonna hit
submit
edit url for dorian edit url for pikachu
added to prompt array so cool okay
awesome
no that's good uh yeah and that's
essentially it for our form
okay so this part's gonna be a little
bit um interesting i probably said it
before every section
uh but we have to um actually
so we have to find a way to pass in
information to
the polling page before we can actually
go and you know cast our vote
um so right now we have these like
buttons and they're kind of useless
right they can't really do anything
just add shout out to that so we're
actually gonna head over to app.js page
and do something kind of fancy um
so fancy's always fun so we are going to
uh create a function called change
candidates
function it's going to be an
asynchronous function uh
so async it'll accept a prompt
we're gonna say uh name pair so we're
gonna achieve the name pair
it's equal to await
window dot contract dot
get candidate pair so we're going to
what i'm going to essentially do oh
sorry
wow let's keep doing that candidate
pair uh so i want to do is like pass in
uh use use the prompt to retrieve the
name pair
for the polls that um that the user is
interested in
pass the names into that into the actual
like
you know um uh into
the polling uh what's called
pollingstation.js file
uh so that i can use those to query the
blockchain to get the urls to copy the
images to retrieve the vote counts
um to add votes to uh their you know
respective names
um this function is fairly important for
passing in all the information i'm going
to show you guys how we're going to
accomplish that
so we're going to retrieve the candidate
pair using the prompt key
so the prompts themselves are the keys
so prompt.prompt
and then after that we're going to save
all the information retreat from that so
we're going to say
uh we're going to set the local storage
so local storage set item
candidate one that's gonna be fixed
value in your local storage
name pair we're going to save the first
name
to the key candidate one in local
storage
uh and then copy that down it's going to
retype it
and just replace this to a 2 and replace
the 0
to a 1. so this is going to get pikachu
this one will get kirby and save them to
local storage
after that we're going to do local
storage dot
set item
prompt and save the prompt name as well
so prompt

uh then after that we need to actually
redirect ourselves to the polling page
right
so we're going to call window dot
location
dot replace

parenthesis window dot location
dot href uh plus
polling polling
uh station so this is gonna redirect us
to
uh the polling station um section of our
application
oh my god excuse me
sorry about that um oh my god
so my sneezes sound like screams
bloody screams oh my god
uh so we're going to take this function
name
and pass it into our home component
under the name change candidates
is equal to this
it's making a reference to the function
if you save all of that save all of that
um and we're gonna go back into our home
page
our home dot js button and we are going
to attach that
as an on click
to these buttons here so we're going to
call props
props dot i refresh the name of the
function
change canned i'll probably go
dates yeah
um and then we're going to
what's our argument so arguments is is a
prompt that's right
so which means you have to pass in
element and i got this
l from this um map function here
that l contains the name of the prompt
so if i click this button it should
uh set the element to oh who went in
smash
um in fact we can like even just like
test if this works
uh so let's go back to our app.js file
and call contu
okay it didn't like the way it typed on
click i think
uh uh make sure you add a callback
function here or else or else if you
um wrote the way i wrote it uh this
function just automatically call as soon
as the um as soon as the
component loads so put a callback
function on this on click inside of the
home.js file
and that will that will get rid of that
error uh so we're gonna add a
console.log
add prompt here make sure it gets called
so we're going to say uh yeah who wins
who will win in smash right
who won smash and get candid pair is not
a function
it's not i might have also missed that
add candid pear pear pear
oh we just never made it whoa
ah we were so close i thought we had all
these brain out
um okay that's okay so export function
get candidate pair
yeah prompt
string return a
uh string array
and yeah so if
if uh what's that thing called
okay if candid pair if candidate pair
dot contains
prompt
then we will get a temporary array
actually we're just going to return
um
return candidate pair dot
get some prompt
else logging log
prompt not
found return
empty array hit save
copy this name go down to utils.js
and it's a view method
kill the server do yarn
build yarn start
almost done gang we're almost done
okay open up our inspection tool
uh who when smash go to pole
oh no

it's saying i'm missing a parameter
somewhere
let's go to home go to
app.js
prompt
ah there we go perfect okay so now we're
gonna see
if um i'm gonna go to application
go to local storage and you should see
candidate two
kirby candidate one pikachu prompt who
will win in smash
uh yeah so we can see candid candidate
one kirby candidate two
pikachu and then again uh prompt who
will win in smash
um but yeah i mean that's yeah super
awesome
yeah we have our we have our local
storage uh working so that's good
um so now uh is the fun part
so we go to um let's go to
let's see polling station let's create a
use effect
uh use effect
and this function oh wow sorry
i did not want all that help from vs
code right now
uh so create callback function create
the empty array
we're going to create a function inside
of it called const
get info so is it equal to an async
function
and this is going to do a bunch of stuff
for us
so we're going to first create a
variable called vote count
let vote count
vote count equal to await
window dot contract dot
get votes so that's this is going to
retrieve and store
all the current votes so prompt
um is going to be equal to a weight
uh local storage actually
wait for that so we're gonna do local
storage
dot get item
prompt it's gonna retrieve the prompt um
and use a prompt as a key
to get our vote count the vote count
return and array we're going to use that
array to populate
the number of votes for each contender
um what's next
next up is actually updating the vote
count so
uh let's see we have to create more
state variables
right so we're going to
um create a state variable for the votes
let's see sorry give me a second here
look at my notes here
shirts on short cells there we go
uh so we're gonna have yeah
const candidate one votes
change vote one
use state
um we're gonna put in some dashes here
for now
some dashes so dashes would be our
placeholder for that
uh and we're gonna switch this value to
number two
that's value number two uh so if the
votes aren't loaded yet we're just going
to display some dashes
um we're going to call changevote1
and under vote count we're going to say
change but one
parentheses vote count
zero so we're getting the first
indexed value of vote count because it
because remember
that window.contract.getvote returns an
array of two elements
uh first one is the count for the first
connect contender and the second one is
the account for the second contender
uh after that so
vote count stuff
okay next up we have
image stuff
so i'm going to call um the
change candidate url uh functions well
first i'm going to save this copy
um and paste it here
so inside of this change function we're
going to call await
window dot contract dot get
u r l um
make an object instance where the
instance will contain a name
and name will be window sorry just be
local
storage dot get item
and our key is candidate
one uh as you can expect we're going to
take all this
and duplicate it
and switch all these ones to twos so one
two two and one to two and that's our
image and those are images
um then after that change
participation so we need to uh record if
the user participated or not
right uh we're gonna do anything like
check for that and update these
functions and see if that's true
so change results display for example
uh could be our function so change
results
display and say did
user well
um so did user vote right so
let's see we're going to create a new
variable called
first we make a section called um vote
checking stuff
so create a variable called a did user
vote set that to a weight
window.contract dot
did participate
now writing a lot of stuff here so i'm
assuming we're going to get some sort of
error
that's okay
prompt so local storage
dot get item
prompt
add a comma and then user which is just
going to be
this is just going to be the window dot
account
id then after that we simply
chuck that variable into here
now we're going to save all of this
and before we even even say we're gonna
have to we have to call this function
still right
so call get info um inside of use effect
so this should light up there we go
so save see what's screaming at me
what's screaming at me uh i don't
remember where my return statement went
oh that's weird there you go oh
uh wow yeah i put this entire function
inside of the
the return statement do not do that move
that above the return statement
hit save let's see what's screaming at
me now

effect is not a function because i
forgot to import it
use effect hit save
oh wow that actually worked i mean of
course it worked what are you saying
huh so there we go i mean we have
pikachu we have kirby appearing
um you know all this fsc is to see like
what happens we actually vote right
uh so actually in making these vote
buttons actually work
so these buttons do nothing they're just
for show
so let's add some functionality to our
vote buttons so you have to um create
this function
create another function
called add vote
sounds a bit easier async index
um so i'm going to say await
window.contract
dot add vote
prompt local storage
dot get item prompt
so that's going to the prompt is going
to be the key that like
the um votes be stored under
uh index the index is going to be which
um the index for the candidate that
we're voting for
is index and then we're not done we stop
so once we do that with text record the
user right
so await window
dot contract dot record
record user
um object instance
then essentially it's going to be
the exact same thing as this layout here
but zip index we're going to type in
our key which is going to be user and
instead of index again
we're going to type in window.account
id
now we have to go down to buttons so do
command f look for button
and on click right so
on click there we go
we're going to create a callback
function that's going to reference the
add
vote function which is going to uh
let's see which one is this okay
so this first index will be zero
there we go
now search for the word vote do the same
thing here
so on click
then add vote oops sorry
callback function add
vote one hit save
um and while we're actually working with
these buttons
here let's do
something else let's do something else
let's add a disable tag disabled
to these buttons and
where it says uh
where it says
yeah i did use your vote right or change
results display
where it says show results we're going
to take advantage of that and do like
show results
which is returning a value of false
right now right
so which means that like this button
will not be disabled
um
and then i'm going to add that to here
as well
so again disabled right now is set
to false which means that these bones
will remain active
um until the vote has been placed
uh then if the user did vote but the um
results will display
and then true will cause these buttons
to be disabled
and in fact we're going to take this
change results display
and just toss it at the end of add vote
and that
we're going to put in the word true here
so that's going to change this value
from false to true
once we click on this button so i'm
going to vote for kirby
says see if this all works right you
know
i have no idea what happened there
okay so i'm going to vote for kirby
let's see did scream
prompt not found oh perfect
awesome so see uh we can see our results
we can see that both value are both um
pikachu and kirby somehow three votes
actually don't know how it's even
possible
uh hmm
why do you have three votes
oh because i was playing with this
earlier in this application it might be
it might still be referencing that um
yeah it's actually let's try different
account
so log out log in
i have a bunch of accounts
blah blah blah blah blah test net
uh so i'm gonna vote for kirby again
wait so kirby should have four
if this is correct ooh something is
definitely not right
okay so let's go up here and see what's
wrong
why is this returning a three well first
you want
actually i don't know if there's
anything wrong with that it might
be something as simple as

as i think i might know what it is i
think it might know it is
there it is okay
thank goodness i thought something scary
okay
literally i have not um i had i had no
effect just playing this
so where it says three right
in the code in the test code we created
earlier replace that with the
state variables candidate one votes
and

candidate two votes so kirby should
actually have two and pikachu should
have
zero uh what is going
on
i vote one uh
oh
this should be two change vote two
there we go ah yay okay there we go so
yeah
so kirby has two votes pikachu has uh
zero votes
um i love pikachu but pikachu's
definitely not my main
in smash uh and let's yeah let's try
this whole flow again so
here we go we are at our homepage you
know we want to participate in this poll
but first i'm going to switch my user
out so we log in
go to um blah blah blah dot test net
blah blah blah blah blah blah
who wouldn't smash this looks
interesting let's go to the poll let's
see pikachu and kirby load we have our
cool loading dots
we have a cool prompt right here um
and then after that uh we just say i
don't know let's go for pikachu let's
get pikachu vote
we wait
probably disable the button before while
it's loading uh
oh let's refresh the page here
there we go okay so not sure why i
didn't like update right away there
but that's okay pikachu has one vote
and kirby has two votes as we refresh
the page
uh yeah so i mean other than that weird
little bug which
which would you know it's not too big a
deal um we have a functioning
upgraded version of block vote much more
streamlined the custom logo and
everything
hey everyone thank you so much for
watching this episode of blockheads if
you guys had fun creating your version
of block vote guys if there's anything i
can do to improve this video or any
others please let me know in the
comments below
of course you guys get stuck and you
have any questions you guys can refine
me on our near discord channel i'll also
include that information in the
description below
and we'll be trying to do a better job
of keeping these videos updated as our
technology changes so you guys know the
most up-to-date version of these
projects
for your portfolios and whatnot again
you can find me on our discord channel
so reach out to me if you guys have a
question
and guys thank you so much for your time
and have a great day

oh my god
that's all folks


## Keywords:
