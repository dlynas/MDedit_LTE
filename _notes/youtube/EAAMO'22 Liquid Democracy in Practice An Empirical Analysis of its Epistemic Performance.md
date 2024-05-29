---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=ThXTZQN_m3E
---

# Video
EAAMO'22: Liquid Democracy in Practice: An Empirical Analysis of its Epistemic Performance
![](https://www.youtube.com/watch?v=ThXTZQN_m3E)

## Transcript:
okay hello welcome to our session on
computational social choice and
redrawing boundaries
um I'm excited to kick things off with
Daniel Halpern I'm going to talk about
liquid democracy so I will turn over the
floor to Daniel thank you thank you for
the introduction
um yeah my name is Daniel Halpern I'm a
PhD student at Harvard and today I'll be
talking about some joint work with Mano
Ravel Adam barinski and Elijah babai I'm
in particularly talking about some new
empirical results on liquid democracy
and I really want to give a lot of
credit to mano here we've done some
theoretical work on this before but she
was really the leader of these
experiments and fortunately couldn't
make it today
anyway so what is liquid democracy
um it's a voting Paradigm and I think
it's easiest to understand on a spectrum
of other paradigms we're familiar with
so on one side we have direct democracy
this is classic Athenian democracy where
everybody in a society votes and the way
you make a decision you just hold a vote
with everybody and you just take the
majority opinion say if you're deciding
on two things
on the other end is slightly more modern
take on this they're more familiar with
which is representative democracy so
here there's a small set of
Representatives
um that vote sort of on our behalf and
again we just take the majority of what
these Representatives say as the outcome
for a decision
and on the middle of the spectrum as we
is a liquid democracy so how does liquid
democracy work you have all your people
that want to make some decision
um and everyone has a choice they can
either directly vote just a just like uh
direct democracy or they can delegate
their vote very similar to
representative democracy but in
particular they can delegate to anybody
right and the idea is that the is these
uh delegations are transitive so you
know if this person here delays this
person
um although this person the the final
person on this chain of delegations
votes on behalf of all of them so then
they hold a vote and uh you just take
the majority weighted by these
delegations
and liquid democracy promises to be sort
of a Best of Both Worlds taking benefits
from both direct and representative
democracy
so on the direct side
um you sort of have this like legitimacy
participation aspect where everybody
feels like they're part of it they
actually have an impact on every vote
they're not just sort of handing it off
to this uh representative far away
um and you can delegate to anyone you're
not restricted on who you might delegate
to maybe you don't like any of the
representatives in your election
um but on the other hand you get some
benefits from representative democracy
you really get a more like large-scale
feasibility it might not be feasible to
ask every single person every question
for every single issue
um and you might not be knowledgeable in
every single issue you know you might
not want to vote on everything
um I trust that person more than myself
to make a good decision
um and the idea is that you're sort of
implicitly identifying the people that
might be knowledgeable in this issue
right you're not like explicitly
deciding who the representatives are but
sort of you know you delegate to people
you think are a little better off and
you end up at a better decision
okay um and we're going to focus a
little more on this today
um but before I jump into our results I
just want to say like this really is
something that's used in practice there
are several political parties around the
world especially in like Germany
Argentina Australia
um you know they're sort of small scale
but like it really is something being
used they sort of get represented in in
their associate parliaments and run this
and vote on just as liquid democracy
would have said
um it's also used a more company scale I
know like Google's run some experiments
and I think like corporate governance is
more like a feasible way we can
implement this more quickly
um and it seems like a cool application
and I'm not too familiar with it but I
think some like crypto people are also
interested for uh they're making
decisions in a decentralized way
um they like these kind of things
so
um
to understand this you know we're
implicitly finding more knowledgeable
people we sort of need some model of how
this works
um and we take inspiration from the
epistemic approach introduced by like
condorsay several hundred years ago uh
and this is this has some uh it's been
used before in some other theoretical
work the idea is that your end voters in
society are voting on one of two
outcomes
and there really is some notion of like
a better outcome that we want for
everybody and I think this is more
applicable in some situations than
others we can get back to that later but
I'll show you what I mean more in the
experiments in a bit
um and the idea is that you know people
are trying to figure out the right
answer and they might sometimes make a
mistake so with some probability they
they vote hopefully above a half well
some fix probability they're voting for
the correct thing and otherwise they
vote incorrectly
um and just to give you idea how this
works so let's say we have this Society
of seven people
um let's say these blue people are
voting correctly with probably 0.6 and
the purplish people is probably 0.8
um now if you just sort of run direct
democracy you let everyone vote uh I did
the math for you the probability that um
at least four of these seven people are
correct is about 82 percent
now let's instead assume that like these
two people these two blue people
delegate to the two purple people
um you can again rerun this math and
just ask you know what's the probability
majority now weighted by these
delegations the Purple People sort of
have two votes
um that they're correct and we've seen
it goes up a little bit
um we sort of you know probably we made
the correct answer is increased
um now what what else could happen maybe
a few more delegations happen these two
blue people again vote to the purple
person and now we have a not a great
situation actually if you count the
number of votes this purple person is uh
accounted for more than half the votes
the entire Society so they're almost
like a dictator
um so the probability were correct is
just the probability this purple person
got it right
um so 80 percent
and even worse this purple person may
delegate to this other blue person and
now we're even much worse off worse than
if we had just run the classic majority
direct democracy election
um because now we're just depending on
this one person here they only get it
right with probably 0.6
um and just to give you an idea of sort
of like when do things go well and might
they go wrong
um things look really bad if you uh
sorry things look really good if you
have like a bunch of maybe not too
knowledgeable people delegating to a
single middle person if you sort of let
the entire Society vote if they're
frequently getting it wrong then uh the
the overall decision is bad but if you
know you all delegate to this one person
the middle then things look good
um although conversely it can be a very
similar looking situation but now the
outside people are like getting it right
with a 60 probability and now when you
have lots of people they're actually
going to very frequently get the right
answer but if you do these delegations
you're only getting right eight percent
of the time so maybe not quite as good
and the key takeaway is like
um how well liquid actually performs
really depends on these delegation
behaviors really depends on the context
right
um
so uh there has been lots of theoretical
research on this but the talk today is
actually about some real world
experiments we ran
um and we did these in like small
classroom uh settings
um and the idea is we sort of asked
these people some questions right so
you're going to be asked a lot of
questions about uh you know the meaning
of some English idioms or some you know
about some movies some like trivia
knowledge and you have the option you
can either choose to vote directly on
this or delegate your vote to someone
else in the classroom that you might
think is better than you
um so here are some examples of my
questions it's we took it from this big
there's been lots of studies we didn't
make these questions ourselves this is
like big Corpus of uh questions used by
some like Stanford experiments that we
just copied their questions
um and they're all true false questions
they're either yes or no just two
options
um right so again similar thing with
movies
um and the nice thing about running
these experiments is that we not only
ask people to delegate even if you chose
to delegate you actually were forced to
answer the question as well so we have
an idea we can actually like compute
these counter factuals what would have
happened if fewer people delegated if
they just voted directly or what happens
when they do delegate how often are we
right
um and so we immediately get these these
delegation graphs right
um in the nodes we we have an estimate
of how
um good people are at answering these
questions maybe from like a different
set of questions and we can see what the
delegations look like so sometimes
things look good like over here uh we
have sort of some less competent people
delegating here it's actually someone
who who is really good at this category
it doesn't always work well we have
people here that these numbers are a
little small but this is a good number
this is a bad number so uh sometimes
people are delegating to people that
weren't quite as good as themselves and
it doesn't work quite as well but it's
it's just cool that we can immediately
look at and observe these delegation
graphs rather than just you know uh
um implicitly assuming them from some
theoretical model
um and using this information we can
also immediately compare how good
liquidmer actually does compared to the
counter factual of everyone just
directly voting
um so this is across our several
different categories of questions and
specific to different experiments we run
we write it in several classrooms
um and we see across all these the the
purple triangle represents the the
frequency that liquid democracy was
correct the blue dot direct democracy so
very consistently look at democracy is
outperforming direct democracy at least
a little bit
um
and we can also compute uh using these
like uh
um estimated expertise is how good we we
expect people to be at different
categories based on a few other
questions
um how these uh efficiences increase
among delegation do you tend to delegate
to people that are actually better at
the topic
um and we do see in in several
categories and pretty statistically
significant results in this people
actually are delegating but are people a
few categories we don't
um this one over here the spatial
reasoning is kind of an anomaly it looks
negative
um but uh really what's happening is
this is just like a very easy category
that sort of everyone is getting right
so it's not too interesting to look at
you know how a delegation changes so
clearly is context dependent but uh um
overall we're seeing very positive
results
um so these are very like direct high
level like did we do better off
um we're also interested in questions
sort of understanding
um delegation Behavior more exactly
um so not just the overall probably
correctness how are people actually
delegating
and and to do this we need sort of some
parameterized model that we can fit
um you know what what is a way we can
sort of classify Behavior and to do this
we're uh referencing our previous
theoretical paper that introduced this
model
and the idea is that uh we think there's
sort of two aspects to delegation
um so for a fixed uh set of expertises
first there's some probability that you
delegate in the first place and we think
there's something depend on your on your
expertise hopefully people that that are
more knowledgeable or less likely to
delegate maybe that doesn't happen maybe
it's actually other way maybe if you're
more more uh um knowledgeable on the
topic then you're maybe less confident
we did some other studies on this but
hopefully that's how it works and then
given this there's sort of some tendency
to delegate to someone of of different
companies maybe you you put a different
weight on different people depending on
how knowledgeable they are and it sort
of looks like uh you're you're
delegating randomly or maybe some you
know proportion to these different
people
um
and just to make this like a little more
concrete
um say again we have this very similar
situation here and we fit our functions
and we think uh these functions
accurately somehow describe delegation
Behavior so what what does this mean if
we think these are the way the functions
work if you're this voter so your your
expertise in the topic is three-fifths
um the probability you choose to
delegate is uh according to this one
minus three-fifths so maybe forty
percent of the time you tend to delegate
um and then condition on you delegating
you sort of place weight on every other
everyone else according to this and it
very conveniently chose these numbers
they add up to 100. um so maybe you know
nine percent of time you're delegating
to each of these blue people and 16 so
these people so you're not like
deterministically doing anything
necessarily better but maybe like on
average you're delegating to to better
people slightly more often
um yeah you choose someone according to
this and you do this for everybody
so some prior theoretical results from
our last paper is that as long as these
Behavior functions are sort of moving in
the right direction so if uh the more
knowledgeable you are the topic the less
likely you are to delegate and uh in
addition to this
um when you do decide to delegate you
slightly more frequently delegate to
people who are more knowledgeable not
determinants I mean sometimes you can
delegate downwards but uh at least on
average you tend to be doing something
slightly better
um this implies again according to these
other theoretical properties that liquid
oxy is performing well we expect it to
frequently outperform direct democracy
and so what do we see in the data
um so we can first fit this this Q
function this is the probability you
delegate
um so on the the bottom is your
estimated expertise how knowledgeable we
think you are and on the the right is
how frequently tend to delegate and we
really do see on average it is does seem
to be decreasing in a pretty
statistically significant way
um so this is encouraging it's sort of
matching our theoretical sufficient
conditions
and similarly for this this Phi function
where do people tend to delegate so on
the the bottom is the
estimated knowledge of the person doing
the delegation and on the the right is
the person they tend to delegate to so
we're sort of looking at this heat map
how often do people of one uh knowledge
or level of knowledge delegate to
someone else and what we really want to
see and what what very encouraging we do
see is that it's sort of increasing when
you move left to right you're more often
delegating to people that tend to be
more knowledgeable on the topic
um so again that's a very exciting it
sort of fits our sufficient conditions
and through a theoretical paper which
would imply things tend to work out
um overall and again we see that from
the other experiments
so just to wrap up with a few takeaways
so liquid Moxie really is I think it's a
very exciting new voting Paradigm um I'm
not as much you know at a national scale
maybe it's very hard to implement
there's other other drawbacks but I
think there's there's many places it
really could be used and has lots of
intangible benefits that I'm not
describing this work you know maybe you
feel more represented or for whatever
reason
um and there's been lots of back and
forth in the theory some theoretical
papers say like oh yes it looks like
it's doing really well another thing say
oh no it's not looking great you know
maybe sometimes we expect it to not work
too well
um but but our experiment suggests you
know at least in some cases in certain
contexts we really do expect it to work
well and our goal is just to identify
regimes where we would expect this to
happen
um and hopefully implement it at least
here
um but as for future work these
experiments truly are pretty preliminary
I think they're in pretty small scale
settings pretty specific and we just
really need more experiments in in
different different contexts bigger
situations different sort of social
connections but either way I think very
exciting results and I'm excited for the
future of liquid democracy thank you
very much

here we go
hey thanks for your talk
um do you think that in real world use
cases there could be a psychological
effect from knowing that many others
have delegated uh votes to you yes this
is a really good point and and something
that people think about a lot in
particular in in uh real world use cases
uh
um you sort of need a lot of this like
public information to be available like
even even if you're delegating you're
starting to know like what happened to
my vote where did it end up with you
know who's delegating to me
um you know which is sort of uh goes
against some other things we might want
in boating maybe like privacy type
concerns
um yeah and I think there there's some
evidence that maybe if you feel that
you've got a lot of delegations you're
going to put more effort and hopefully
make a better decision
um I think there's just you know there's
a lot a lot of features so this problem
it's really hard to model everything but
you know I think that's again really
exciting future work that we could
hopefully look into yeah
hi so thanks a lot for the great talk
and uh
paper so I'm not familiar with the
literature but I was very interested
about the question of how the network
structure if you have some prior
knowledge can you tell whether liquid
democracy would work so because I assume
that the problem with it can be if
there's a crazy cult like some person
with a network and can we make important
decisions yeah
so how will the network effect
sort of uh these sort of like super
voters that are getting lots of
delegations right yeah so this is
something that happens in practice I
think it is a pretty major worry
um so again like sort of where the
theory falls apart or where they would
say it doesn't work well is situations
like this where sort of one person's
getting so many votes that that you kind
of lose this like you know spreading
spreading the knowledge across the site
and like asking lots of people
um you know I think in some cases it can
work well if that one person who's
receiving lots of delegations really is
like a pretty informed person in some
cases it won't so again it's very
context dependent I think we just need
more experiments I mean this was hopeful
that like even in situations where
someone was receiving quite a few
delegations it tended to perform well
um so maybe we'd be hopeful of that but
again I I don't want to claim that
generalizes are is always true I think
just more experiments are needed yeah
thank you
a bunch of questions maybe we have time
for one or two more
I'm wondering in the experiment did you
click like demographic information
because you can imagine there might be
gaps based on like gender or like
religious affiliation
um so I don't think we did we did we did
do these in pretty small classroom
environments where I think the
demographics weren't weren't too mixed
um yeah I mean I think the again this is
we just need more experiments this
really is a small scale I sort of Hope
features we need to take into account I
think that's a really good point that is
something we definitely should be
looking into so thank you
huh
thanks so much really interesting work I
might have missed it but I was curious
like how agents learn their preferences
over the nodes in the network is is it a
learning process or is it just I mean in
the theory work it's probably just
random right but uh sorry what do you
mean by learning like how deciding how
to vote like the weights over the oh oh
yeah so uh the way it tends to actually
be implemented is is it's sort of all
public which is maybe not the best thing
but you know you can people can see the
whole graph they can see who delegated
to who they can they can see
um what delegations they received
actually in our experiments that's not
how it happened we sort of had people
vote and you know they were just filling
out their one little form they don't
know what other other people are doing
but I think in real world situations
that that does happen so you know you
are aware
um pretty freaking like how how many
people to delegate to you but like they
also know which of their friends have
some expertise like is it is it oh no so
that's just assumed to be you know you
you delegate however you want we we did
there are other mechanisms that sort of
take a more like Central planning type
approach you know maybe we we can
encourage people to delegate to better
people are going to make decisions we
were really hoping to keep this very uh
local like it's sort of it's your own
decision we're not going to make you do
anything and sort of Hope is that we
like implicitly get people uh moving the
right direction but they can delegate to
whoever they want to and whatever they
think expertise means to them you know
they it's their choice yeah
yeah okay uh let's thank the speaker
again



## Keywords:
