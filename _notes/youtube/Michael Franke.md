---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=VEc0z6sZTTw
---

# Video
Michael Franke
![](https://www.youtube.com/watch?v=VEc0z6sZTTw)

## Transcript:
hi everyone
i'm greg scontris associate professor of
language science at the university of
california irvine
where i direct the meaning lab we're
here today for aberlin avivo
linguists online hi everyone an
initiative of the brazilian linguistics
association
of california irvine and somewhere i'm
hearing myself
online an initiative of the brazilian
linguistics association
and somewhere i'm hearing myself
okay let me try that again and see if
anyone is playing this back
sounds better okay so aberlin is
designed to give students and
researchers free access to
state-of-the-art discussions on diverse
topics related to the study of human
language
we have a great talk lined up and it's a
true pleasure to introduce today's
speaker
professor mikhail franca of the
university of osnabruck
mihal is a professor of at oslonbrook's
institute for cognitive science
where he heads the cognitive modeling
group with degrees in cognitive science
logic and philosophy and a habilitation
in linguistics
mikhail is a true polymath and an
authentic
intellectual broadly mikhail's research
applies
computational cognitive and evolutionary
modeling
to questions of language use with a
particular focus on pragmatics and
semantics or
issues of meaning when i think of
mikhail's extensive contributions to the
scientific study of linguistic meaning
i think of someone who uses and often
develops
state-of-the-art methods applying them
to foundational
theoretical issues this approach will be
very much on view in today's talk
where mikhail will tell us about
theory-driven statistical modeling
for semantics and pragmatics i know
you'll all join me in welcoming
professor mikhail franca
keep in mind that you can use the chat
function to submit questions as they
arise
i'll moderate the discussion at the
close of the talk
and now michal thank you for being here
and please
feel free to take it away
thank you so much greg for the very kind
introduction
thank you very much to all the
organizers from aberlene it's a
great pleasure to be here i hope you can
now
see my slides if that is not the case
maybe greg
tell me otherwise i'll jump right in
um into theo driven statistical modeling
so this talk is like greg mentioned
heavily methodological
so i would like to start out with a few
general remarks
on the distinction between
theory driven models and theory neutral
models
if we think of the standard logic of a
test-based approach to empirical
research
we probably have something in mind like
the following we have a
verbal theory and with verbal theory i
mean
not entirely specified as either
a mathematical framework or a computer
program
but it's not necessarily meant to be
something worse than that it's a theory
that's spelt out
in language in ideas
you look at this line this theory and
you um
ask yourself which distinguishing
features does it have
what predictions of relevance does it
make
that are surprising that set that theory
of
from other theories out there in the
market
you think about an experimental design
that you could set up that specifically
targets this distinguishing feature
often these distinguishing features are
predictions about a particular
difference
the drought has an effect and you
compare a control group
to a treatment group you
collect the data and you apply a
statistical test
for instance of difference is there
really
a difference in the measured effect
between the control group and the
treatment group
and then you interpret the outcome of
that statistical test as evidence for
against um the hypothesized difference
and then
in yet another step you reflect back on
what that means
for or against your verbal theory
now there's nothing wrong with this
approach absolutely
however it is probably not the only way
in which you can do
empirical research one thing to notice
about this
kind of approach is that it um
assumes or it often assumes that the
statistics that we're using
are off the shelf and with that i mean
that they can equally be applied
in psycholinguistics in biology
in physics and also in psychology for
instance
and in this sense the standard tests
that we use regression modeling t-tests
and over
and what you have are theory neutral
they are meant to be generally
applicable but therefore
they don't necessarily directly maybe
could
but usually they don't connect to the
kind of
special domain theory that you are
trying to test
however if you take a model-centric
approach to statistics
which is basically nothing new
any um statistical tests that you learn
in your stats 101 has
an underlying model theoretic or
formulation you could say
you can start to play around much more
freely
with integrating theory into statistical
mods
so more concretely a statistical model
often has
very broadly speaking the following
structure you have
some parameters if it's a parametric
test otherwise maybe not
which feed into some kind of predicted
value what you would expect on average
to happen from which you derive
a likelihood function over potential
outcomes
and you link that to the data so
the first parts in this model-centric
approach here the parameters in the
predictor you could say
are our the analysts assumptions about
the data generating process
and this could be for instance just some
linear predictor like in linear
regression model
but it could also um be
any kind of linguistic theory that
drives the likelihood and that drives
um the explanation of your data all the
way from
theory to data and so this talk is going
to be
about exploring this symbiosis of
statistical and cognitive modeling
from the point of view of linguistic
theory
i should say that what i'm saying here
about model-centric statistics and doing
more
theory driven statistical model modeling
is not new
many people are arguing for similar
things in other disciplines
however i think that in particular if
you look at
the recent empirical terms so to speak
in semantics and pragmatics where
we have a very strong established
linguistic theory
interesting homes terminology
and established theories um
we now turn to experiments and we want
to test
these established theoretical ideas so
we are in a position in a sense where
it is particularly prominent or maybe
even pressing to try to link directly
what we think of our interesting
theoretical constructs to
what we can observe in an experiment
so my agenda for this talk today is to
introduce ideas of probabilistic
modeling
as a kind of scaffolding to test
establish theoretical ideas
from linguistics in particular from
semantics and pragmatics
based on experimental data
and in order to do that i want to take
you
rather swiftly through three case
studies
first one on grammatically generated
implicature readings
second one on gradients and locality and
natural language quantification and then
the last one
is an outlook on task type link
functions and
what is actually measured by um
experimental task a word of caution
all of these case studies could be dealt
with in a one hour talk or even longer
so i will have to cut many corners i
would like this talk to be generally
interesting
also to people who are not familiar with
let's say probabilistic modeling
and even some of the semantic slash
pragmatic theory that i'll be touching
so please keep in mind i will first of
all
skip some very interesting detail
because we don't have time for it
and second of all just try to keep track
of the overall
red thread through this talk which is
how you can use
explicit mathematical slash
computational modeling
to link theory statistics and data
let's go first case study
this case study is based on joint work
from a recent paper that appeared in
language last year with leon bergen
and it deals with grammatically
generated implicature readings let me
first
illustrate what the topic of the case
study is
so i'm assuming as linguists you are
reasonably familiar with
scalar inferences usually we say that
from an
utterance of a sentence like 1a i own
jono some of johnny cash's albums
we're inclined to infer 1b that i own
some but not all of them
the standard explanation is because
otherwise i could probably have said
1c my own johnny cash
now a traditional
explanation of these kinds of scalar
implicatures
is that they fall out of a
rationalization of the speaker's
utterance in a context just like i did
just now i said
speaker didn't say that they owned all
of
johnny cash's album so probably
it's not the case that they do
however um already from the start of
original
griezian ideas of pragmatic reasoning
people have noted
that this picture has some problems
explaining certain
inferences that seem to occur in
embedded positions
and so very recently a very interesting
research program which i'll he'll call
grammaticalism has been proposed
which basically um suggests that a
grammatical mechanism
in the semantics is responsible for
generating
candidate scala implicature readings
so let's have a closer look at what that
would mean
so here are complex sentences um or
actually it's just one complex sentence
we'll see more
of those in a moment and it's potential
readings group take the sentence like 2a
all of the aliens drank some of their
water
on a literal reading key term to look
for is
obviously called fire sum um this
sentence just means that all of the
aliens strength
some and maybe all of their water it's
just literal reading
however we can by standard gricean
reasoning
contrast this sentence the 2a
with a stronger sentence like all of the
aliens drank all of their water
and say okay the speaker didn't say that
stronger sentence so
we'll read this first sentence to as2c
the global reading all of the aliens
drank some of their water
and it's not the case that i'll drink
all of it
however it is also plausible that there
is
another stronger sentence than 2a that
or a reading of a 2a
which is the one in 2d the so-called
local reading
all of the aliens drank some but not all
of their water where
could say that pragmatics so to speak
the enrichment of some
happens inside the scope of a logical
operator like all
and we could say that what
grammaticalism does
it supplies this reading so to speak
and we'll see um how it does that in a
moment an empirical question is
obviously
do we need it and
this is the part of what i would like to
contribute to today so if we think about
grammatically generated implicature
readings
of sentences of the following kind um
how to quantify of the aliens drank in a
quantifier of their water
with an alleged very simplified
syntactic structure of the
following variety then
grammaticalism would tell us that there
are different
parses slash readings supplied by
grammar syntax semantics interface in
such a way that an
exhaust operator an exhaustive operator
whose meaning is roughly equivalent
to that of an overt only can apply
at matrix position the whole sentence
level
it can apply at the inner quantifier and
it can also apply
or not apply at the outer quantifier
so if an exhaustive video operator would
for instance apply locally to
a noun phrase some of their water it
would get enriched to mean
some but not all of their water
and so on at the matrix level the
exhaustive operator would be
give or take equivalent to standard
globalist
and reasoning negating stronger
sentences
complete sentences so
this may already be quite a lot of
detail let's take a step back what does
that mean we have a theory
that is empirically well motivated that
suggests
that hidden operators that generate
candidate pragmatic readings
can apply at different scope sites for
simple sentences like the ones
i suggest here with two potentiological
quantifiers
there are then eight possible parses or
eight possible readings that you can
obtain by
inserting or not inserting these
exhaustive operators at
these three different scope sites we get
a
literal parse where no exhaustive
operator applies
um we get a reading where only
um we we have only one at the outer
position
um i'm sorry only at the matrix position
only at the outer position only at the
inner position and maybe
at several scope sides uh
conjointly a traditional griezian
approach
would only acknowledge in a sense the
literal
reading without any exhaust like it's
just a semantic reading
or the one that you can obtain by global
griezing reasoning which we
um here can approximate by saying
okay apply exhaustive exhaustification
at the matrix level
whereas a grammatical approach would
in principle allow for all of those
potential readings to be
derivable to be available for the
interpreter
now of course depending on what these
quantifiers are and also depending on
what
version of exhaust you might use
some of these readings might be
equivalent to other readings
but we'll see that in a moment okay
the question that i'm interested in here
is again
to ask how much of that ambiguity so to
speak
do we actually have empirical evidence
for and as you can guess by the whole
introduction to the to the top we'll you
will use probabilistic pragmatic
modeling
to try to answer that question or to try
to get a partial answer to that question
so let's first have a look at
experimental data that we can work with
the experimental data from the paper
that i'm presenting here
um looked at nine sentences
and i'll call them nested errors to
tellings because they are basically of
the structure that we just looked at
how the quantifier of the aliens drank
in a quantifier of their water
where the quantifiers are all the
aristotelian
lexicalized quantifiers also not with
all possible
combinations the abbreviations i'll use
in some of the figures that you will see
are
for instance a n for all a
of the alien string none of the water n
and so on
based on the standard logical meaning of
these sentences
we can distinguish seven world states
um also including potential pragmatic
enrichment so there's only seven
distinct states of the world that we can
distinguish with this
miniature language
these are stimuli from our experiment
and these are the states the world
states that we'll
use to probe participants interpretation
and production behavior
so you see a bunch of heavy aliens here
and
each one has a jar of water
and they have either not drawn anything
like these guys
or they emptied all of their jars like
these guys or some
drank nothing some drank half of it
and some drank all of it so we can
represent those seven world states if
you're interested but you don't
necessarily have to follow that notation
for instance with this miniature
icon here that says there is no in this
situation there is no
alien that drank all of the water there
are aliens that drank
half and there's no alien that drank
nothing
just to use these um icons
succinctly in visual representations of
the results for instance but i'll talk
you through the critical ones and it's
not going to be important
so with this material we recruited 100
participants using amazon's mechanical
turk only
self-reported native speakers of english
for allowed we presented them with a
cover story about scientific research
on obviously friendly scientific
research with friendly aliens who came
to earth and were just interested in
what they like to drink
the materials as i said consisted of
these nine nested aristotelians and we
presented
the seven possible world states with
pictures like the ones you just saw and
here again
the experiment had two parts each
participant
first went through
a task series that i will refer to as
production
proviso will be coming in a moment
whether it's true production or not and
a comprehension task
okay let's have a look at the production
trials in what i will call production
trial somewhat sloppily
participants were presented with a
display of a world state
and get the instruction please describe
the situation for the scientist as best
as you can
and the production consisted in
selecting from two drop down menus
an aristotelian quantifier at each
position so that is
in a sense and a very confined way of
asking how would you describe this
picture
given the nine hour strategies
in what i call comprehension trials um
participants were shown a similar
picture or actually
shown all uh seven pictures or of world
stays
um together with a given statement like
none of the monsters trunks um drank
some of their water
um and the question um how likely do you
think that someone else
had this situation in mind when they
uttered
this sentence and they had to rate this
with a slider for each of the seven
possible
world states so what is
the data that came out of you i'm just
going to throw it at you
the production data and the
interpretation data
don't worry we're not going to dig too
deeply into this
um we'll just use the data on block for
for modeling purposes i just want to
show you once
for once that there is data and how it
roughly looked like
so in production for each situation you
see here let's say
along the vertical line um we'll get
some
proportion of times that people to
chose so to speak an aristotelian a
nested arrow strategy
so here's a situation where um all of
the avians
actually drank half of their water and
the preferred way of
saying this or expressing this
describing this world state
is by choosing the nested aristotelian
all of the aliens drank some of their
water unsurprisingly
reversely if in interpretation um
uh participants heard
the sentence all of the alien strength
some of their water they rate it with
sliders for each of these situations how
likely they thought we normalized
their ratings for all seven sliders and
then averaged
and this is what you see here so the
according to this measure the most
likely
interpretation um according to our
participants
is again this state where all aliens
drank some but not all of their words
you could say
a local reading is the most preferred
reading according to this mesh
but what does that mean
for any other type of reading that could
be generated by
inserting hidden exhaustive operators
for all of the other sentences
in place and that is the question that
i'm
trying to address here now with
pragmatic modeling probabilistic
pragmatic model
we will use a particular way of
probabilistic pragmatic modeling
in the following so i'll take a step
back here now and introduce this once
for all of the
three case studies that we're going to
look at um
essentially what i'm endorsing here is a
theory roughly like the rational speech
act model
introduced by nora goodman michael frank
um take the position of a pragmatic
interpreter what's the job of a
pragmatic interpreter
a pragmatic interpreter hears an actual
speaker
uttering some observable message let's
say they
simply just bike that speaker
has in his mind some kind of meaning
that they would like to
convey but that pragmatic interpreter
cannot observe
the meaning they can only observe
an extensive signal like bike so their
job
you could say or what they might have to
do is come up
with interpretation hypotheses what
could the speaker have meant with bike
was it a motorbike was it a race bike or
was it a
regular bike and weigh those
interpretation alternatives according to
how plausible they think
these are and according to the framework
i'm adopting here
the way in which these alternative
hypotheses are
ranked or weighted against each other is
by
simulating a model of the speaker's
behavior
essentially asking if the speaker had
wanted to express let's say
motorbike what would the speaker have
said how likely is it that he would have
said bike
would he not have used an alternative
expression
doing this all probabilistically then
we'll arrive at something like an
abductive
inference or a rationalization of the
speaker's
um utterance by reasoning towards the
best explanation so the
the most likely state that would have
triggered
the message that we have observed
in full-fledged models that apply this
kind of
reasoning framework we would also like
to look at the pragmatic
interpreters knowledge of language but
also the reasoning about
knowledge of language of the speaker
which is important for our first
application
in other applications we might also want
to include reasoning about general
shared world knowledge on the side of
the interpreter or
over what the interpreter thinks
this speaker has in mind and finally
obviously also
about more specific parameters of the
concrete context
that we are engaged in however these
last two bits
do not play a major role for the case
studies that i'm looking at
in order to formalize these
ideas um the vanilla rational speech act
model
formulates essentially two conditional
probabilities which i'll
call a speaker rule and a listener rule
so a speaker rule is a conditional
probability distribution that assigns a
probability to an
utterance given a state and
a listener rule is in essence the
reverse
given an utterance how likely is it that
i'm
that the speaker had a particular state
interpretation in mind
the model assumes that the
speaker rule is grounded out in literal
interpretation so to speak
so an utterance comes with a semantic
meaning indicated here by these double
denotation brackets
and a speaker is trying to choose
an utterance for a given world state
such that under
a literal interpretation this this year
conditional on a literal interpretation
the probability of inferring the world
state
is as high as possible modulo some
parameter that
can be tweaked to model more or less
informative speakers
the idea behind this formulation is that
the speaker is trying to
make assumed literal interpreter who
interprets
literally infer the true state
with as high a probability as possible
under some defensible assumptions
this formulation can also be rewritten
in a more standard way
recognizable to um people familiar with
christ
in pre excuse me rice in pragmatics
namely that the speaker is trying to
adhere to
truth of what they say and also trying
to optimize
the informativity of a message
which is just maybe measured in terms of
the numbers of
states relevant world states that are
true
so the grycin
interpreter on the other hand basically
like i said previously would reverse
this whole process
and preferred prefer an interpretation
that makes it likely that the speaker
would
choose the utterance that they had
actually um observed
so that is the general um
probabilistic pragmatics modeling scheme
that i'll be
um endorsing for actually all of the
three case studies
with some variations um that are going
to follow
back to the concrete one that we looked
at
so far in this vanilla rsa model
there was no mentioning of the semantic
ambiguity
introduced by the grammatical approach
and so there's very little we can say
about
um the data that we just looked at from
our little experiment
in a way you could look at it in this
way that we have the
potential parses suggested by
grammaticalism
and the vanilla rational speech act
model if we don't do anything
to it would only assume
that the semantics of a
an expression is its logical its literal
semantics
however we can start

giving up this assumption we can give up
this assumption and just include
more of the semantically generated
ambiguity
into our mind a first attempt of doing
this
has been given by chris spotson
colleagues in
what they and i call the lexical
uncertainty model
without going into detail the lexical
uncertainty model assumes that
there are literal readings available for
our necessities
and that some can also mean some but not
all
but a speaker who has a lexical meaning
incorporated in the head that some means
some but not all
will use some always to mean somewhat
not all
so the only second the the only parse
that's also available
to these speakers is a parse where we
have a
local exhaustification at both embedded
scope sites
we can generalize this slightly more and
we could say okay now maybe we want to
have more flexible speakers
that can use some once in a sentence to
mean somewhat not all
and use another occurrence of some to
mean some and maybe all
so these speakers would have two more
potential readings
available to them and they could use
them in some sense
and we call that the lexical intentions
model intentions because
the way it is formalized in these models
is that the speaker actually
chooses a sentence with a specific
meaning of each occurrence of each
quantifier in mind
we can even generalize this further and
look at a global intentions model which
is
similar to the lexical intentions model
but allows for the full variety
of parses made available by
grammaticalism
okay that's a lot to take in
last slide on these formalisms just to
give you an idea
of how this global intentions model
would look like
essentially it looks very much like the
vanilla rational speech act model that
i've just introduced
but it adds one parameter p
and p is a parse one of the eight parses
that we just saw in the rows on the
table before
so the speaker is now assumed for a
given meaning that they want to express
to choose an utterance and also
to choose a parse what that means is
let's say i say all of the aliens drank
some of that water
and in the back of my mind which you
can't see i
intend that sentence to be read as the
meaning that comes out if you apply the
parse p
and you as a speaker as an as a listener
you don't know that p you only heard the
utterance u
but you can jointly reason about which
pair of
actual world state and speaker intended
reading of the sentence
best rationalizes the fact that the
speaker just said all of the aliens
drink some of their water
okay so with these models in place
we can turn back to our experimental
data
and now of course we have to skip a few
technical details but basically what we
do is we use bayesian model comparison
to ask the question of a rational
scientist
how credible is each model given the
data
i'll give you a brief overview of how
this would look like
the basic architecture of all of the
four models that we just saw
is roughly this we have two parameters
there's this alpha that you actually saw
the rationality parameter in the actual
modeling in this paper there's another
parameter that means the cost of
negative utterances but let's put that
aside
these are three parameters of the model
just like you have three parameters
let's say in a regression model
both of these parameters influence
the predictions of the speaker rule and
the listener
they feed into both the speaker rule the
probability of an utterance given a
state is
directly what explains or could explain
the data from the production layer
it provides a likelihood function for
the data from this production task that
we had
similarly the listener rule almost
directly provides
a likelihood function for the
interpretation part of the data
so the likelihood for all of the data
combined
production and interpretation at the
same time is just the product of those
two
and we can say for each model given
an average over all possible parameter
values
which we'll just set as an interval over
in principal plausible ranges
how likely is the observed data given
that model
and when we have such a likelihood term
which is really simple
to compute we can turn that around
and ask the question that we're really
interested in namely
given the data how likely relative to
all the other models
is a particular model from the set of
these four
that's easy to compute actually really
rather straightforward to compute given
that we have rather simple models with
just two free parameters
and the resulting numbers are extremely
intuitive
to interpret so the posterior
probability
of models given the data on the
assumption that
all of our modeling that there are
really only those four models so it's
always
relative to the very narrow focus on the
models that we look at
we'll find that the global intentions
model
is leaks more likely than the second
best model leaks means here 27 times
more likely than this and that's quite a
lot
which in turn is more than 30 more
likely than the lexical
uncertainty model and the vanilla rsa
model is
comparatively completely negligible
so what that means is
first of all we have used probabilistic
pragmatic modeling
to squeeze quantitative predictions from
grammaticalism
grammaticalism as i introduced it there
are papers who try to constrain the set
of potential readings more further
that's that's for granted but
grammaticalism as
i introduced it just said there are many
available readings
couching grammaticalism inside of
probabilistic pragmatics however allowed
us to derive
quantitative predictions for a model
that contained
so and so many grammatical
readings so to speak the result of this
exercise was that
it seems that we need the full range of
implicature readings that are generated
by grammaticalism which
is a directly interpretable
theoretically meaningful result
that is not derived by deriving
a let's say point hypothesis about
a comparison between groups or something
like that but taking the whole data into
account
both from production and from
comprehension
all right let's see if we can still
stomach a second case study
this one is joint work with
bob fantille and uli zoland in a paper
from this year and it's dealing with
gradients and focality in natural
language quantification
we've already talked about quantific
quantifiers a lot
just for um setting the scene again now
we're going to talk about
more quantifiers than just the
aristotelian ones
that's a relief probably stuff like some
of billy pilgrim's memories are pleasant
so some reoccurs probably gideon's
backhand smashed exactly three skeletons
or simo
spotted many banana fish all of the
orange ones being quantifiers that we
now
possibly care about
semantic theory tells us
one prominent semantic theory tells us
that the truth conditions that for the
meaning of a sentence like
q quantifier of the s some property
rp another property is a function of the
intersection set size so the cardinality
of the intersection between
those um predicates and questions right
for instance
a sentence like some of the srp just
means that the
iss is bigger than zero and this also
can work for context variable
quantifiers like many then you just have
to say that there is some threshold
that is supplied by the context against
which you
compare the intersection set size for
instance this is a really good and
powerful
theory because it offers very
interesting
um theoretic formerly precise notions
such as monotonicity
which can then help explain a lot of
puzzling observations from several
domains like
the cognitive complexity of quantity
concepts stages in the acquisition of
quantity words
um the amount of errors that people make
in certain reasoning tasks
and also for theoretical purposes the
distribution of polarity items at least
has been suggested to also be influenced
by monotonicity
however if we look at empirical data
from quantifiers in use we'll see a
slightly different picture from what
generalized quantifier theory would
suggest
data that is already rather old from the
70s
for instance has shown that if you ask
people for their preferred
interpretations for
various quantity words like a few cereal
and some
that seems to deviate quite from the
logical meaning let's
zoom in again on the word sum just
because
it's so familiar for us um then
according to
generalized quantifier theory the
logical meaning in light green is
something like well
just more than zero at least one or
maybe at least two depending if you
want to say from plural presupposition
or something like that
it's not important for us but anything
um bigger than two is certainly true
however if you look at the
typical ranges of interpretation that's
the dark greens one
they are much more narrowly confined and
that is
the kind of focality and as you will see
in a moment also the gradients
that i would like to address in this
talk
so again let's look at a something an
experiment that gives us something to
work with
here we're looking not at interpretation
but at production
and now in a more open-ended set
um a simple experiment um
invited in total 800 participants
600 of which considered consistent the
training center gave us the training
data
and 200 of which gave us a test data to
perform an online experiments
at amazon's mechanical turk they saw
pictures with
432 dots like this one here
the varying proportions of which were
red
the rest black and they saw this
in trial so trial like that and could
freely type
a quantifying expressions to complete
this
sentence of the circles are read
participants were kindly asked not to
produce
numeric like explicitly numeric
expressions like
uh 30 for instance um they still did
so we um filtered that out um but for
the most part
uh this elicited
quantify quantifier expressions just
like many moles
about half etc in particular
we now look at just the 15
most frequently produced types not
tokens so after classifying certain near
equivalents and
some spelling errors into the same
categories
we are left with

15 most frequent quantifiers and we also
look at
all and on all or none weren't produced
very often
uh but that is just an artifact of
um the situations in which they would be
true not being shown
very often so in order to have those
edge cases
included for modeling we also include
all or not and what we see here along
the
x-axis is the number of red circles that
participants saw an artist
in our experiment together um with
a smoothed out density and estimation
of how likely particular quantifiers
would be used
in these cases to describe that scene
and again what we see is let's say not
what you would expect from generalized
quantifier theory
which assumes that there is some
threshold and after that
that expression might be true or up to
that the expression might be true
but maybe rather something if you just
eyeball
this data that is accountable by
some kind of prototype based theory
where we would say
like um very very prominently here
half half has a prototype that is
exactly in the middle it actually isn't
here at least not the
top one but it has some kind of
prototype
and the um region of use or the use of
this quantifiers is maybe
described by something that has a
prototype and some
distance function from the prototype
according to which that is still
um this expression is still applicable
and indeed some people have
argued for prototype based semantics
of quantifiers but that is
tricky because how do you actually test
for
which semantics is best okay again we
could maybe
try to devise an experiment that sets up
a particular condition
in which um generalized quantifier
theory
would predict this and prototype theory
would predict that
but let's take the data as we have it
and try to infer
backwards what that data means about the
contrast between
a classical binary generalized
quantified theoretic semantics
and a potential prototype based
semantics and this is what we do with
probabilistic models of quantifier use
here i'll skip a lot of the details
actually so
i'll just keep it at the basic
architecture of the models in question
we have the data from the production
study that i just mentioned
we um wanted to derive similarly as to
what we had before
um a speaker rule which i'll call you
the production probably of the speaker
choosing a quantifying expression given
a world state which is here labeled
t in particular t prime
the hidden moving parts the
parameters so to speak that affect
this production probability or again
speaker's rationality parameter
um not a cost this time but rather a
salience there's a subtle difference
between costs and salines
something you might ask for in the q a
otherwise think of it as roughly the
same as the cost that we have before
but then two additional components
namely the lexicon
and the ans component so the lexicon
is depending on the type of model we
have
of which we have four either generalized
quantify theory or prototype theory
and we are using the data to backwards
infer
through this pragmatic link function
what a likely
semantic meaning could be for a given
quantifier but we do it in the way that
one model
exclusively assumes generalized
quantifier theoretic
semantics and another model assumes
exclusively proto-prototype theoretic

semantic meaning we'll also distinguish
pragmatic speakers from just literal
speakers
because prototype theoretic
semantics in a sense already
could be said to incorporate
pragmatic reasoning excluding
other states that could better be
expressed
by a different quantifier
so in order to be fair we also look at
just literal
language users because that might be
fairer to a
prototype theoretic semantic explanation
lastly this model also has an ans
component ans for approximate number
system
and the general idea is that
given a true state t
the true number of red dots for instance
in a display might not be
uh known to this to the participants who
were also instructed to
not try to count all those 432 dots
but they might just have a vague percept
of the actual
state so we'll define a noisy
probabilistic function from true state
to perceived state
and we'll say that what the speaker
actually chooses a quantifier too
is there possibly noisy percept of the
true world state
details have to be skipped for the
purpose of this talk unfortunately
so i'll skip those so for those four
models that we just had we can again do
um bayesian model comparison asking the
same question which model should we
believe in
we do it slightly different here for
technical reasons so we're not using
posterior probabilities we'll use um
we look at posterior predictive
distributions
and we'll on the next slide look at
cross validation results if you're
interested in the differences
bring it up in the q a so once more we
had for this
experiment in the training data so the
same data as we saw before but in a
different

format of representation and we had test
data
so what we do similarly to what you
often see in computational linguistics
so in machine learning
is we use this training data to
basically
train our models in this case to compute
posterior values over credible
parameters because there's a lot of
parameters in these
models because we have um one or
sometimes
two parameters for each of these
quantifiers for instance and we have a
salience
value once for um almost all
of these quantity expressions
and what you see down here is
the predictions a trained model of a
particular kind
would make based on this data
and what you can see for instance is
that a literal speaker who uses
generalized quantifier theory
is perceptibly different from all the
other ones for instance in the case
of most which is this
piglet's pink kind of color here
they would continue so to speak to use
most rather prominently as the number of
red dots for instance would grow towards
the total
number of 432 whereas
pragmatic speakers and also literal
speakers using a prototype theoretic
semantics
would decrease the frequency with which
they produce

most however not particularly clear
how to distinguish those with the naked
eye so that's why we now turn to the
test data set and we'll ask
for those trained models how likely is
the test data the whole out data set
and the log likelihood of the test data
is plotted here
so we meant the higher the better so how
likely is the holdout data set given the
trained models
the neighbor pragmatic generalized
quantifier theory
provides the best score

on this account by a margin
to test this even further very briefly
we also looked at
empirical model comparison that is we
invited another 200 experiments
into um our virtual lab via amter so to
speak
and we showed them the same displays and
we
randomly sampled a prediction so to
speak from
one of the four models and also
we sampled what other participants had
actually said
in the data for that picture
and then we had them rate with a slider
whether that
particular description was good or bad
and so we can compare
the posterior predictions from an
empirical point of view also against
the actual data the results are that
a literal speaker with generalized
quantified theoretic semantics
is really worse than everyone else
but there's no statistically significant
difference between these empirical
measures
for all of the other three models so
um here the pragmatic model which uses
generalized quantifier theory is not
necessarily the best one it's also not
worse
but we can't say which is okay for us
because what we would like to conclude
from this
is rather that first of all
gradients and focality that we see in
the data
seems to be consistent with generalized
quantifier theory generalized quantifier
theory is
not necessarily ruled out by just seeing
focal areas that flow into one another
so to speak but the more important
methodological point i would like to
make here is that
we can test semantic theories through
the lens of a pragmatic link model
so we can use the pragmatic model to
draw in theoretically interesting um
conclusions about latent moving parts
that we cannot
directly observe that we ca that we can
only study through their reflexes
and the pragmatic link model makes those
reflexes this stream that we imagine of
going from the latent structure to the
data
maximally explicit and that's a good
thing
last one shorter case study three
task types link functions and what is
measured
let's start with the experiment
immediately so
suppose you see this some of the circles
are black
you see i um display
one black circle and you are asked is
the sentence true or false in this
picture
the experiment only lets you press on
one button
make up your mind whatever you would
want to say
now imagine different type of tasks
different experiments
same picture same sentence but the
question is
not about truth and falsity but how well
does the sentence describe the picture
and you can choose from seven categories
on a liquid scale from bad to good
what would you do
and we ran this kind of experiment
based on a particular variation so first
of all
um i varied the type of task
seven point rating scale with the
question how well does the senate
describe the picture
and binary truth value judgment is the
sentence true or false in this picture
just as shown
then there's a cross-classification
in half of the experiments
between participants manipulation
there were filler sentences with most
and
many and in the other half they were not
they just
these participants never saw most of men
um the specific theoretical reasons for
doing this
are not so important i want to make a
methodological point
here's the data from this experiment
on the x-axis you see the condition how
many of the balls are actually black
0-10 and for the liquid scale
you see here um the mean
ratings rescaled to lie between zero
um and one for comparability once for
the
case where many and most were absent in
gray
and for when they were present and for
the binary truth value judgment task
what you see here is the proportion of
truth judgments for all of these cases
so you see here
similarly for absent and present
alternatives
now i want to introduce a straw man
interpreter here which i'm going to bash
on
and that person would reason as follows
obviously the
binary measure we ask for truth
conditions
measures the truth conditions of the
sentence
obviously if you ask for how well does
the sentence describe the picture and
you give the seven point rating scale
you're measuring something else you're
measuring pragmatic felicity
and you can see that in the data because
truth conditions are unaffected by
adding alternatives many and most
obviously because truth
but pragmatic felicity is affected by
adding
other alternatives now this is a straw
man
position and it's over exaggerating this
but maybe if you have read
experimental semantics in grammatics
papers you sometimes have felt that
hmm aren't we over interpreting
subtleties in the results
with respect to how
they relate to theoretical notions such
as truth conditions and pragmatic
felicity
so i think again here explicit
probabilistic modeling
can help and here the model is not
broken down that's the full
representation of the full model but
don't despair i'll talk you through it
what i want to do here is i want to look
at the data
the data from the liquid scale on the
one side
the data from the truth conditional
binary truth condition
uh truth or judgement task on the other
side
we'll have two variants of all of that
ones
with the alternatives and ones without
but that's not so very important
more important is that the data is
obviously
explained by a latent structure the last
layer of which is again the likelihood
function the choice probabilities of
choosing
one of the degrees on the liquid scale
or choosing true or false and
the task for everything else like with
or without
many and most present in the experiment
how do we generate those choice
probabilities
well for the binary judgments we'll
just look at standard logistic
regression models and use
their logistic linking function
for ordinal data you could scale rating
data we also just use
what you would use in ordinal regression
here in particular a probit linking
function
and the input and that's the important
bit
to those standard linking function for
the
type of data that we collected is a
theoretically
informed notion of pragmatic felicity so
we are assuming that's the most
important thing we're assuming that
both tasks measure pragmatic felicity
pragmatic felicity has a formal
derivation in terms of
rsa in terms of probabilistic pragmatics
but for our purposes we can just take it
as it measures how good
the description sum is as a description
of the given picture
and then we can look this is just one
model remember all the other
case studies so far different models and
we compared them this is just one model
and the model assumes the tasks measure
the very same thing
so we train the model so to speak on the
data and then we compare what the
what the trained model would predict
about any future
data that's so-called posterior
predictive check in particular here
a visual posterior predictive check and
the logic behind that is
is the trained model surprised by the
data it was trained on
right and it's not you see that by the
model predictions in red
and 95 um credible ranges over these
posterior predictors
um always including the data that was
um c what that means
is that a seven-point felicity task in a
binary truthful adjustment test
may actually measure the same thing
so it's a it's it's like an existence
argument look here
is a model that assumes they measure the
same thing and it's doing completely all
right
the main methodological point which is
even more important than the specific
one of course is
that using a fully spelled out
probabilistic model of this kind
has the potential of pointing out to us
exactly what we as modelers believe a
particular task measures
pragmatic felicity it was an ingredient
in this tree-like
description of the model so we can make
very explicit what we believe
is measured by a task and i think that's
a very good thing so i'm concluding here
in general that i think there is added
value to
mole centric in particular theory driven
statistical modeling and maybe now it's
also more clear why i
contrasted earlier on the
regression coefficient like the
regression predictor
to one of linguistic theory because
that's exactly what we did in the last
case study where we did not derive the
input
to an ordinal or logistic link function
as we would normally do from a
linear predictor in a regression model
but from a linguistic
theoretically informed concept
all right thank you very much for your
attention i'm looking forward to your
questions
thank you so much mikhail so now we'll
transition into the discussion and let
me remind those of you out there
watching that you can
use the chat function to ask any
questions and i'll monitor
the chat and read those
aloud okay so as you think of your
questions
i have a couple of questions for you
mikhail that i thought we could start
off with
one is a more practical one
so assuming that you're a linguist who
wants to be able to apply
these methods um most
linguistic training doesn't teach you
these things
and there are only so many hours in a
day
what sort of training or background
do you need how can you go about
acquiring it
and this is an excellent question um so
first of all i don't think
that's very important that um
everybody should do this or has to do
this that should be very clear right so
there should be no shame in not doing it
um ideally however um we are
we are all aware that there is this
approach
and that we um see its advantages not so
its disadvantages
um if you want to
learn this kind of modeling i think
let's say from this from from scratch i
think
learning statistics in general in a
model
based fashion is the best thing to do
anyway
so maybe that's not what you might have
expected but if you take a statistics
class as an undergraduate linguistics
student
organization student or something in
this vicinity
and you have a chance to take a course
that focuses
models and not tests i recommend
going for the model based course because
it tells you
that statistical methods are more
flexible than just applying
the appropriate test from some arcane
decision tree that tells you what test
you might need
and once you are comfortable with let's
say standard
statistical models like a linear
regression model maybe then a
generalized linear regression model
and you know how they are trained and
how they applied how different models
are compared
it's not much further to

changing crucial things in the model
that make them
theory specific of course then the
question is
how do you implement that but also there
i would say
if you are familiar with a standard
programming language like
python or r or julia there are very good
packages
that make slight changes to particular
models already
rather doable and other than that i
think there's
really great also textbooks and courses
that could bring you
into let's say probabilistic cognitive
modeling i would like to mention a
textbook by
michael d lee and jane eric marcus
eric mongerson sorry which i think is
very excellent takes you step by step
through exercises into building your own
data analytic models in later cognitive
models
okay great thank you for that um
another question that i had about
linking hypotheses so i think you've
convinced us that we need
linking hypotheses to map between the
data that we're observing the behavior
that we're observing and the cognitive
processes that we think are generating
those data and i think most linguists
whether they acknowledge it or not
tacitly assume
linking hypotheses what i'm wondering is
whether we need
computational models for those linking
hypotheses
is it ever the case that some
prose level description of that
hypothesis is going to be enough
can we get away with qualitative
predictions
um yes i think that's an excellent
question and i think the answer is
always positive i think
um it is being explicit about your
assumptions is always
good but it's always it's it has to be
being as
explicit as you can and sometimes we
might just want to be able to
do something and that is completely fine
without being able to spell out
everything and this is then a shame to
do no it's
i i really don't think it is i think for
instance if you look at
interpretation of neurological data eeg
data
we are coming to a better and better
understanding of
what the n400 component for instance
tells us in language understanding
there are models there's also control
controversy about which model is correct
and they're specific
um and these these models are partly
fully formalized but not to the extent i
think that they would
at least not according to my current
knowledge that they would derive a very
concrete likelihood function to apply
directly to the raw data or the
pre-processed data
is that bad no no no not at all not at
all and
the the moment where you might need
everything to be spelled out including
your link function is
presumably when you want to start
comparing the whole data and not just
the chunk that you have carved out
because it's small
according to to the modeler's intuition
or good arguments
it's the most relevant one so suppose i
look again at the nested aristotelians
i could just focus on the predictions
for one sentence or two
because that's where i'm assuming the
local reading all of the aliens
strengths someone not all of them
water shows its face most
clearly and that's fine but
if you stick with this kind of case
study the first one and this modeling
then
um there are potential pragmatic
readings for all other or
many other kinds of sentences and your
theory should somehow also say something
about all of these cases
and then it gets very tricky to do that
in a
not fully formalized or computational
way
so as soon as you have excuse me if you
want to compare
an idea based on its predictions for
more than one to
three clear-cut cases
but let's say all the data from the big
experiment i think
going computational is just necessary
because of the otherwise implied
complexity and also for being able to
weigh
house let's say in one condition one
condition the data speaks for that
model in another condition it speaks for
the other and
so on how do you weigh that in and that
is where full-fledged statistical
modeling can help
it often of course can give you a quite
different picture from
just focusing on one condition basically
integrate
over all the data that you have but i
think that's really where i would say
from the top of my head that's the
clearest case where you want to go
computational
okay thank you yeah so i i i totally
agree on the
so it seems like there are two points
one there could be
so much data so many predictions or
there it's just so complex that
you're going to start spinning in
circles if you don't have a more
powerful way of specifying the
predictions
but also it forces you to be maximally
explicit about the assumptions that
you're making
in specifying a computational model and
i i think those of us who have done that
have often come
across cases where we're surprised by
the assumptions that we had been making
or
seeing them in front of us it can be
more illuminating
i'm wondering though why probabilistic
do these things need to be probabilistic
is the are the processes are the
cognitive processes
probabilistic is it the methods that's
introducing
the gradients you touched on this a
little bit in the
last case study but i was hoping you
could say a little bit more
yeah um
if not probably i mean if not
probabilistic then what
um you could ask cheekily uh back right
um but i think um the strongest argument
and the one that i would actually
really like to um defend is um that it's
uh instrumental it's an instrumental
choice it's the best we have
um however i want to be i want to be
clear um these models that
i introduce are probabilistic are at
many levels
they are probabilistic at the level of
the likelihood with some noise and
so that way you could say this is
statistics this is objective
noise or you could say something like
that but then there's also the
subjective part of the cognitively
allegedly cognitively real probabilistic
part where we say
the choice rules the speaker rule and
the listener were also probabilistic
so yeah i think you have to keep these
separate
however for both cases i think it's fine
to say
um there is a clear asset for using
probabilities
there's they're actually rather simple
um
we know a lot about them we know how to
compute with them
um they are they have a lot of uh
um nice mathematical properties
maybe not so nice mathematical
properties but um
we know how to integrate the
probabilistic cognitive models with the
not with a with a probabilistic link
function
um and we can write them down in the
same software package and it works
like more or less and so i think that's
a strong instrumentalist point for
instance
if you think about representations of
uncertainty
in humans like higher level uncertainty
or actually
reasoning with uncertainty there's a lot
of evidence that suggests that
um human reasoners are not actually very
good at applying
base rule or applying general uh
probabilistic reasoning
although we can always look more
carefully and look at why they
might not be so good at this but there
might be reasons for at least in certain
cases assuming
um some more elaborate structure for
representing
uncertainty of an agent like themselves
hefner functions
but how do you calculate with them how
do you integrate them into your
cognitive model and like you just said
in your or mentioned in your first
question also the probabilistic modeling
is already quite
um quite a step maybe for linguists when
they for undergraduate linguists
and so i think sticking with
probabilities and using tools
in your favorite programming language
that allows you to compute with
probabilities
is a good advice um
but that doesn't it doesn't necessarily
mean that one has to
not be critical about using probability
i think especially
in the cognitive modeling part
so if i have a probabilistic cognitive
model does that necessarily mean that
i'm hypothesizing that there are aspects
of the grammar that are probabilistic
it seemed like you you dug into this a
little bit with
the case study inferring quantifier
meaning looking at
gqt versus prototype theory
you know it seems like whether or not
this is a
good thing linguists are generally
resistant
to or at least some linguists are
resistant to assuming that
aspects of grammar are probabilistic
what is your view on the role of
probabilities in grammar when we're
assuming them in the cognitive models
um that's again
in grammar can mean a lot of things in
the
quantifier study if i may stick first to
what i feel more confident about
semantic meanings although this
model that was presented here looked at
prototype theoretic
meanings these are not necessarily
probabilistic
they are gradient in a sense
right and they allow for truth values in
between zero and one
but the truth values don't have to sum
up to one so they're not necessarily
probability you could say they're not
normalized probabilities actually if you
normalize them it works exactly the same
in these models
but that's not that's a quirk of the
models because the normalization will be
happening anyway
um so there i i think it is very natural
to us to assume especially in
in the context of these models in the
context also of recent developments in
nlp
that semantic meanings are not
necessarily binary
and bound to zero and one they can be
so what that means um will have to
bring the philosophy squad into the
picture i think
how to correctly interpret um
truth values in between a zero and one
for a particular
model and the way i would like to do
that is not in general
but always to ask what is the functional
role that this
numeric value in between zero and one or
zero and one place
in the mechanism of this whole model
and that gives you constraints on how
you can interpret it
or should interpret it depending on the
mechanic role it plays
in this model so for instance in this uh
um quantifier mode i don't think that
there is any
um anything that would
pin us down to a specific interpretation
that these
prototype theoretic semantics are
probabilities of
any sense so what that means for other
types of the grammar
i would actually not like to commit
myself to
speaking about syntax right
i do believe that at least
certain pragmatic rules are also not
carved in stone
so to speak i do believe that we see
quite quick
adaptation to pragmatically aberrant
behavior like
over-informative speaker
under-informative speakers in
psycholinguistics experiments
so that a
so at least a flexible representation of
pragmatic
expectations how my interlocutor will
behave is i think very important
i think that's true we have to model and
we have to assume that people are
flexible
in what they expect others to do with
language
so at some point i think i like it's not
enough to just
assume one grammar and that's it
with er without any way of changing it
and weighing
other potential grammars that are close
to it but whether that is probabilistic
and at what level that is
depends on i think the case study would
like to look at okay thank you miguel
i'm going to turn now to a couple
questions from the chat
so first alina jacheva asks what the
psychological assumptions
are for probabilistic pragmatic models
the ones you're talking about
so specifically she's wondering whether
we assume that these multiple recursions
are happening
every time a listener hears an utterance
or that most of it happens during
learning
and different meanings are then cached
and retrieved depending on the
context how much of this is happening
online in the moment
excellent question alina thank you for
bringing it up um i
don't think i um okay i don't think that
in general conversation if we are
behaving pragmatically
on a on a normal level they say inform
like enriching a message to
uh it's more informative content or it's
more it's relative content that we go
through any type of
deep um theory of mind like
uh reasoning i think that the standard
processes when we are not dealing with
um intentionally misleading or
potentially misleading and uncooperative
speakers etc
are to a certain extent automatized
so my favorite way um
of thinking about the rsa modeling
framework that i have
introduced is that for instance although
we make records to the
literal interpreter when we describe
the speaker rule as being truthful
and um informative
i don't think that we have to
be committed to that being an actual
process
of imagining that the person i'm talking
to is a literal interpreter
it's more something like
a rationalization of probably a choice
heuristic
that we have learned that we have um
acquired and that makes good sense
unless we are faced with aberrant
speakers with malignant malignant
speakers
um etc and then similarly for
um the speaker for the listeners as well
so um there are good arguments for not
thinking
that listeners can do very complex um
joint inferences over 27 contextual
parameters
by fully executing bayesian reasoning on
that
high-dimensional space nevertheless
these computational level and abstract
descriptions
that assume this rationalistic framework
that i've sketched out here i think
are explanatory because
even if the actual computations are in
some sense amortized or learned
or evolved it still
is explanatory to describe their
functional rationale so um
i don't think that um you have to be
committed
to these processes being cognitively
online and real um when you do this kind
of let's say
rationalistic back and forth modeling at
the computational level
thank you uh next question from the chat
from
keo bach they ask i'm curious what kinds
of assumptions have been used for
defining the alpha parameter
the rational one you use in your
hierarchical model can you talk a little
bit more about that parameter
i would love to not to have to talk
about the alpha parameter but f
parameter is
really nasty in some sense so um i'm now
speaking loosely um
here um okay it's a soft max parameter
it's a
a standard mathematical formulation that
is used very frequently i could tell you
how you can actually derive it for
instance from stochastic choice theory
but it is problematic for many different
reasons
um so one value of alpha alpha equals to
5
can mean something completely different
from one model to the next
because it all depends on how the
overall structure of your utilities
is this is looking like so what do we do
with these alpha parameters
so normally in bayesian inference
i would like to not fix them
i would like to keep them free model
parameters and put
loosely informative priors on plausible
values for instance
that alpha is zero or even negative is
very unlikely
but whether it should be five or five
point five
um it's almost impossible to distinguish
or
to to settle beforehand so that's also
why all the
models that i've looked at here um
basically had
um rather loose priors over the alpha
parameters
the last one actually didn't have any
alpha parameter because of the way
pragmatic felicity was
formalized but i'm sure i hope that
settles your question somewhat short
answer it's tricky
yeah there's also some recent work out
of mit
noga zlasky who's been looking at the
behavior of
alpha in in some of these models uh
if anyone is interested in some more of
the gory details although it does get
quite gory
um okay so mikhail i wanted to ask you
a little bit uh specifically about the
nested aristotelian
case study and specifically the role of
alternatives so
we know that the alternatives
available can lead to
very different predictions from some of
these models
so it seems like what about what
alternatives one has available
can change the behavior that we might
expect to observe
and i'm wondering whether artificially
constraining the
set of alternatives to those nine
nested aristotelians could lead to
some of the observed grammatically
pragmatic behavior
so if i don't have a perfect way of
expressing a meaning and i have to
spread these meanings around across the
possibilities that i do have
could that be driving some of this
behavior you
you mean in particular that the fact
that the global intentions model was
preferred you think that this could have
been an artifact of
the fact that we only looked at seven
world states
in these nine sentences yeah it's not an
accusation it really is no no no no no
no no
good it's of course be critical so i'm
not so sure
actually um if anything
i would say is um
i would i would rather accept that
criticism like the other way around
if the vanilla rsa model had come up
the best then i would much rather
uh be inclined to say okay maybe that's
just an artifact of
just looking at this very constrained uh
set
so the fact that but okay if we look
more closely at this model
and the reason why the global intentions
model um was better
um we actually see that for some of the
cases it's actually not the
all of the aliens drink some of the
water case that is maximally
driving this result but it's the sum of
the alien strength some of the water
case
which if for which there are multiple
readings made available by the
grammatical model
including one that uses a top-level
parse
which gives that sentence a rather
specific reading
and it's and in indeed for that reading
seems to be used
so to speak by um participants
so um yeah i'm not sure what that means
about this this line of criticism uh
whether this
i think i have to throw my hands in the
air uh um greg and say it's fair
criticism
it's criticism that should be voiced and
it's absolutely clear
that this is a toy experiment like with
a with an artificially
uh restricted domain and i do completely
agree that follow-up research should
look at
more complex cases but this
question of potential alternatives that
figure into pragmatic interpretation is
also very nasty
and the bigger you go the more
naturalistic you go the more that
problem looms so i can say a bit of what
i already
know and did beyond what i just
presented
there are also of course different
versions of exhaustivity operators
and the differences hinge on which
alternatives you take into account
and so there are actually in the in a
model like this and i presented here two
types of alternatives there are the
let's say the the rsa style the the
pragmatic alternatives and there are the
grammatical alternatives
and they don't need to be the same
and then when you think about back and
forth reasoning
the alternatives that a speaker has in
mind
in one world state don't need to be the
same as the alternatives that a speaker
has to have in mind in another world
state
and then it just completely blo explodes
in terms of computational
complexity also what proper reasoning
about alternatives could be
i hope that the experimental theoretical
pragmatics community
will find a way of harnessing this
problem of
alternative states and or alternative
forms and my best guess is that
potentially also computational
linguistic applications could help like
maybe looking at embedding spaces or
something like that but i think that's
an open
very important and very pressing open
problem
thank you so related to that then
in terms of the actual theory
specification for that nested
aristotelian study
again so given that the
it seems like the global intentions
model is
outperforming the other models because
of specific
interpretations maybe not the full range
that it's generating
have you considered looking at
yet more intermediate models that might
selectively target those interpretations
where that model is outperforming the
others
um no i or we haven't
because uh first of all um
well i think the the way we went about
this is we
we just wanted to put a new idea out
there
um it's at least at the time we did this
it felt already bold enough to say
um look we're gonna put pragmatics back
on top
of the grammatical generation of
readings uh because the
the like the development so far was
and there was pragmatics and then we
realized oh no there's
much more that we need maybe we need a
grammatical mechanism that
generates these readings but then they
are not selected for and then this paper
is not saying okay
let's use pragmatics again on top to try
to
sort this out and that's already um
quite
i'm not sure it was it was in all of a
step i say minimally publish a
unit or something like that so that have
to think about what that means
etc but in in carving out those four
models specifically
um we were also guided by conceptual
concerns
so i don't think that
i think that not any subset from those
eight parses that you could think of
makes for a plausible model more
concretely
the lexical uncertainty model that i
introduced which is or that was
introduced by chris parts and colleagues
and the lexical intentions model which
are minimally different because the one
allows two more parses
they're conceptually quite different in
the one case the speaker is
ambiguity aware and chooses the intended
reading and the other the speaker at
least in terms of the model just
has this one fixed mental lexical entry
and that's it so there's also conceptual
so in other words
it's not just specifying which subset of
readings are available
but also giving them a good and
plausible conceptual role in the in the
pragmatics model then
so that's also why i i cannot think of i
mean
i couldn't think of any other
intermediate model that is conceptually
plausible
and has a good mechanistic realization
in the framework that we adopted
at the risk of getting too far into the
weeds with that is it the case i don't
remember with the global model
that you have the option of the matrix
exhaust and that's what's doing the work
with the
sum for you yeah interesting so this
could be a case where
in addition to these methods helping to
adjudicate between
theories that already exist maybe then
feeding back into the
the development of theory and exploring
that possibility space even more
again with these conceptual
considerations that you mentioned
constraining that yeah
um i'm wondering kind of shifting gears
a little bit and looking more toward the
future
what you think the next questions
are that might be ripe for this sort of
theory-driven
statistical modeling are there things
that come to mind as
um particularly well-suited or
in need of an approach like this
um other people are doing this right
it's not just me and i think that's
happening at many in the phone so i can
just maybe
um topic drop and maybe name drop a few
things but i think that
in in general um work that looks
at the use of language to
to communicate generalizations is like
generics habituals causal structures so
therefore also conditionals
is very important also
and the reason i feel that is because i
think that is where
a lot of knowledge is transferred
and because having a better grasp of
also the pragmatics of let's say causal
explanation or causal
you know transmission of cholera
information for instance
can be also helpful in applied domains
obviously
yet another area where i think
much more could be done is in terms of

pragmatics of questions and the
pragmatics of
answers to explicit or implicit
questions so generally reasoning about
in what way um a statement was uh
relevant which qd it might have
um address but yeah but it branches out
of course
um and uh i think maybe that's
one final thing to say i think that this
computational
driven work is particularly useful
potentially useful because
especially if you use probabilities it's
also easy to
it's not as if it's just plug and play
but it's easier
to combine with modern nlp applications
that also use uh numeric representations
sometimes even probably
depending on where you look
great so i think that's our our time for
today so i want to thank you
mikhail on behalf of aberlin and thanks
to
all of you out there watching either now
or asynchronously
and mikhail if you have any parting
words for us
please share them uh
um yeah i might just want to wrap up and
say
once more i think enlarging
a methodological toolbox is
a potentially good idea that explicit
theory driven statistical modeling can
particularly help
experimental semantics and pragmatics
and other maybe other fields
in theoretical linguistics to achieve
more clarity on what we are measuring
to be able to actually specify what we
are measuring to compare
different theoretically interesting
approaches really directly on large data
sets
so i'm not just focusing on one or two
choice
selections of data points and
i think that this is not necessarily
something

that goes against uh doing theoretical
work or doing experimental work in
another way
because if you look at psychology you
have
mathematical psychology as an
established
branch you have within psycholinguistics
you have established research in
computational
psycholinguistics which similarly tries
to make rather concrete
models eye gaze hand movements et cetera
so i would hope that also theoretically
minded linguists
would help set up a sub-community
with some fruitful exchange between
let's say standard experimental methods
theoretical work and maybe as a third
component this computational
theory driven statistical modeling
thank you very much for
your


## Keywords:
