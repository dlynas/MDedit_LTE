---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=pkT0g7utr70
---

# Video
The Rational Speech Acts Model | Stanford CS224U Natural Language Understanding | Spring 2021
![](https://www.youtube.com/watch?v=pkT0g7utr70)

## Transcript:
hello everyone welcome to part five in
our series on grounded language
understanding we're going to be talking
about the rational speech x model or rsa
this is an exciting model that was
developed by stanford researchers mike
frank and noah goodman and it's a chance
for us to connect ideas from cognitive
and psychology and linguistics with
large scale problems in machine learning
now what i'm going to do for this
screencast is kind of cue up the high
level concepts and the core model
structure as a way of leading into the
next screencast which is going to show
you how to incorporate pieces of this
model into standard machine learning
models
if you would like a deeper dive on the
conceptual origins of this model and how
it works in a kind of mathematical way i
would encourage you to check out these
resources here so this first paper
goodman and frank from the developers of
rsa is a nice overview that shows not
only all the technical model details
with real rigor but also connects the
ideas with decision theory game theory
cognitive psychology and bayesian
cognitive science and also linguistics
from there you could watch this
technical screencast that i did this is
on youtube and here are the associated
slides for that if you want to follow
along and from there i have this python
reference implementation of the core rsa
model and that would be a great way to
get hands-on with the model and begin to
think about how you could incorporate it
into your own project or original system
without further ado though let's dive
into the model and i'm going to begin
with what i've called pragmatic
listeners and we can also as you'll see
later take a speaker perspective
so the model begins with what's called a
literal listener this is a probabilistic
agent and you can see that it conditions
on a message that is it hears or
observes a message and makes a guess
about the state of the world on that
basis
and the way it does that is by reasoning
essentially entirely about the truth
conditions of the language here i've got
these double brackets indicating that we
have a semantic lexicon mapping words
and phrases to their truth values
uh this agent also takes the prior into
account but that's the only way in which
it's pragmatic otherwise it's kind of a
fundamentally semantic agent
from there we build the pragmatic
speaker
speakers in this model observe states of
the world things they want to
communicate about and then they choose
messages on that basis
and the core thing to observe here is
that the pragmatic speaker reasons not
about the semantics of the language as
the literal listener does but rather
about the literal listener who reasons
about the semantics of the language and
for this pragmatic speaker here it does
that taking costs of messages into
account
and it also has this temperature
parameter alpha which will help us
control how aggressively it reasons
about this lower agent the literal
listener
other than that you can probably see
that this model is a kind of soft max
decision rule uh where we're combining
the literal listener with message costs
and then finally we have the pragmatic
listener which has essentially the same
form as the literal listener it observes
a message and makes a guess about the
state of the world on that basis
and it has the same overall form as
literal listener except it's reasoning
not about the truth conditions but
rather about the pragmatic speaker
who is reasoning about the literal
listener who is finally reasoning about
the semantic grammar so you can see that
there's a kind of recursive back and
forth in this model you might think of
this as reasoning about other minds and
it's in that recursion that we get
pragmatic language use
here's a kind of shorthand for the core
model components a little literal
listener is reasoning about the lexicon
and the prior overstates
the pragmatic speaker reasons about the
literal listener taking message costs
into account and finally the pragmatic
listener reasons about the pragmatic
speaker taking the state prior into
account and then you can see nicely this
point of indirection down to the
semantic lexicon and as i said it's in
that recursion that we get interesting
pragmatic language use let me show you
how that happens with a with a small
example here so along the rows in this i
have the messages we're imagining a very
simple language in which there are just
three messages you can think of them as
shorthand for like um the person i'm
referring for referring to has a beard
the person i'm referring to has glasses
and so forth and we have just three
reference and i'll tell you that this is
david lewis
one of the originators of signaling
systems which is an important precursor
to rsa
this is the philosopher and linguist
paul greis who did foundational work in
pragmatics and this is claude shannon
who of course is the developer of
information theory
and in this table here we have the
semantic grammar the truth conditions of
the language you can see that lewis has
this wonderful beard
uh but neither grice nor shannon have
beards
glasses is true of lewis and grice and
tie is true of grice and shannon
the literal listener assuming we have
flat friars simply row normalizes those
truth conditions so we go from all these
ones to an even distribution and you can
see that already beard is unambiguous
for this listener but glasses and tie
present what looks like an
insurmountable ambiguity on hearing
glasses the speedness listener just has
to guess about whether the reference was
lewis or grice and same thing for tie
when we move to the pragmatic speaker we
already see that the system starts to
become more efficient so we take the
speaker perspective along the rows now
and we because we're going to assume
zero message costs we can again just row
normalize in this case from the previous
matrix having transposed it
and now you can see that on trying to
communicate about lewis the speaker
should just choose beard there's an
overwhelming bias for that
and down here on observing shannon or
wanting to talk about shannon the
speaker should say thai that's
completely unambiguous but we still have
a problem if we want to refer to grice
we have kind of no bias about whether we
should choose glasses or todd but
already we have a more efficient system
than we did for the literal listener
and then finally when we move to the
pragmatic listener we have what you
might think of as a completely
separating linguistic system
uh on hearing beard infer lewis on
hearing glasses your best bet is grice
and on hearing tie your best bet is
shannon and in this way you can see that
we started with a system that looked
hopelessly ambiguous and now in the back
and forth rsa reasoning we have arrived
at a system that is probabilistically
completely unambiguous and that's the
sense in which we can do pragmatic
language use
and end up with more efficient languages
as a result of this reasoning
now for natural language generation
problems it's often useful to take a
speaker perspective as we've discussed
before and i just want to point out to
you that it's straightforward to
formulate this model starting from the
speaker we would do that down here at
the bottom this has the same form as the
previous speakers
we're going to subtract out message
costs and we have this softmax decision
rule overall but now the speaker of
course will reason directly about the
truth conditions of the language
then we have our pragmatic listener
there's just one for this perspective
and it looks like just those other
listeners accepted reasons not about the
truth conditions but rather about that
literal speaker
and then finally for our pragmatic
speaker which is the one that you might
focus on for generation tasks it has the
same form as before except now we're
reasoning about the pragmatic listener
who is reasoning about the literal
speaker so we have that same kind of
indirection
and once again here's a kind of
shorthand way of thinking about the
speaker perspective so the literal
speaker reasons about the lexicon
subtracting out costs the pragmatic
listener reasons about that literal
speaker and the state prior and then
finally the pragmatic speaker reasons
about the pragmatic listener
taking message costs into account and
again you see that recursion down into
the lexicon
now i've given you a glimpse of why this
model might be powerful but let's close
with some limitations that we might
address in the context of doing modern
nlp and machine learning
so first we had to hand specify that
lexicon in cognitive psychology and
linguistics this is often fine we're
going to run a controlled experiment and
specifying the lexicon is not really an
obstacle but if we would like to work in
open domains with large corpora this is
probably a deal breaker
a related problem arises if you look
more closely at the way the speaker
agents are formulated in their
denominator they have this implicit
summation over all possible messages
where we do this computation here but in
the context of a natural language what
does it mean to sum over all messages
that might be an infinite set
and even if it's finite because we make
some approximations it's still going to
be so large as to make this calculation
intractable so for computational
applications we will have to address
this potential shortcoming
it's also rsa what you might think of as
a very high bias model we have
relatively few chances to learn from
data it hardwires in a particular
reasoning mechanism as it is inflexible
about how that mechanism is applied
relatedly we might then run up against
things like it's difficult to be a
speaker and speakers even the pragmatic
ones are not always perfectly rational
in the way the model might portray them
to be and we might want to capture that
if only to do well with actual usage
data
and relatedly even setting aside the
pressures on speakers to be rational
they just might have preferences for
certain word choices and other things
that the model is simply not even trying
to capture and we might hope in the
context of a large-scale machine
learning model that we would have
mechanisms for bringing those in
and finally it's just not scalable you
can see that in the first two bullet
points and there are many other senses
in which rsa as i've presented it just
won't scale to the kind of big ambitious
problems that we're trying to tackle in
this class
the next screencast is going to attempt
to address all of these limitations by
bringing rsa into large scale machine
learning models


## Keywords:
