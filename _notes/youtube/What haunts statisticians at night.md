---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=SGGLkrJa9_w
---

# Video
What haunts statisticians at night
![](https://www.youtube.com/watch?v=SGGLkrJa9_w)

## Transcript:
this video is sponsored by brilliant
more on that later hey this is Christian
and you're watching very normal a
channel for teaching and talking about
statistics the one topic where you could
be 95% confident about something and
still be wrong correlation does not
equal causation even if you're not in
statistics you've probably heard this
phrase before it's a reminder that our
pattern-seeking primate brains are not
always correct two things can look
related but this can be an illusion
created purely out of Randomness and in
other words we tend to see patterns in
terms of cause and effect when I take a
painkiller I expect my headache to go
away when I lift weights at the gym I
expect some gains when you watch a video
I make you click the Subscribe button
causes make effects but when you stop to
really think about it it can be really
hard to Define what a cause is what does
it mean for one event to cause another
to happen furthermore how can you
formalize this in terms of a statistical
model luckily for us people much smarter
than me have thought about this question
a lot and turned it into its own
subfield of Statistics causal inference
if you've been with this channel for a
while you might recognize that causal
inference was named one of the most
influential ideas and statistics in the
past 50 years and for good reason both
Pharma companies and tech companies have
a massive interest in distinguishing
between causes and correlations the aim
of causal inference is to take this idea
of correlation does not equal causation
and figure out when they are equal and
what needs to be done or assume to make
them equal but as we'll see this is no
easy task in this video I'm going to
tell you about what haunts statisticians
at night in everyday speech the saying
correlation does not equal causation
refers to the idea of seeing cause and
effect between two events when in fact
there isn't any but what is correlation
and for that matter what's causation the
first thing I'll do is distinguish
between these two from a statistical
lens broadly speaking correlations can
refer to any association between two
random variables an association is a
tendency we see between two random
variables I'll focus on the type of
correlation that most people know about
Pearson's correlation coefficient and
I'll denote it with the Greek letter row
this type of correlation focuses on the
linear association between two random
variables let's say that I'm a
statistics Professor very unlikely that
that'll happen but bear with me I've
given my class a homework assignment and
I collect some data on them one of these
variables is the amount of time a
student works on the homework and the
other variable is the score they
actually get on the assignment one
tendency I might see is that people who
spend more time on the assignment will
tend to have higher scores likewise
people who barely work on it will tend
to score lower this is what's called a
positive Association I've only noticed
that higher work duration is usually
paired with high scores and lower
duration with lower scores this
relationship is symmetric I can also say
that higher scores are associated with
longer work times once I've collected
this data I can use this equation to
calculate the correlation between these
two random variables in this case X will
refer to the time spent on homework and
Y will be the score they got in the
numerator we have an expectation which
is kind of like an average within this
expectation we have a product this part
here describes how far a single student
deviates from the average work time and
this part describes how far student
score deviates from the average score so
this is the product of these two
deviations to show this I'll mark the
averages in the middle of our scatter
plot we can divide the plot into
quadrants points in this region will
produce positive products while points
in these quadrants will make negative
products by taking the average of all
the products of all these points we can
get a sense of these two variables tend
to vary more positively together or
negatively likewise if we have a similar
number of products with similar
magnitudes in all of the quadrants
taking their average cancels everything
out visually we can see that the second
variable y doesn't vary in any
particular direction no matter the value
of the first value X giving us this
diffuse plot this expectation in the
numerator has a name the covariance and
like it same suggests it tells us how
much two variables will vary from their
respective means together this
denominator contains the product of the
standard deviations of the two random
variables by dividing by this product we
standardize the covariance to be between
1 and positive 1 this helps us control
for the variances and puts correlation
onto a common scale correlation says
nothing about how one variable affects
the other only that they tend to vary
from the mean in the same or opposite
way on the other hand causation marks a
clear distinction between the two
variables a change to one variable the
cause creates a change in the other
variable the effect unlike correl
you can't flip the relationship between
the two variables the effect depends on
the cause not the other way around
causality is a complicated subject and
it only gets more complicated in the
world of Statistics where we have to
deal with Randomness as well the
framework that we'll use to understand
causality is the counterfactual
framework a counterfactual is something
that happens counter to what actually
happened statisticians didn't want to
call it a what if scenario so they gave
it a fancy name instead let's go back to
my previous example causal inference
gets really hairy when the cause
variable is continuous so I'll simplify
my example a bit instead of letting
students work on the homework however
long they want they can only work on it
for either one or 2 hours no more and no
less one group will opt in for 1 hour
and the rest will opt in for 2 hours
like before they'll do the homework and
get some score each student has a
counterfactual for the students in the
1hour group their counterfactuals are
the scho score they would have gotten if
they were in the 2-hour group and vice
versa for the 2-hour group let's zoom in
on an individual student to get a
glimpse of what a cause is given a
student and their counterfactual the
only thing that's different between what
actually happened and the counterfactual
is that the student studied for an
additional hour this means that any
difference between the actual and the
counterfactual must be due to that one
extra hour of studying therefore this
difference in the outcomes is the hyp
thetical causal effect of studying an
additional hour on this student score in
reality we never see the counterfactual
scores but these ideas help set up how
statisticians and causal inference think
of causes with this impossible to
observe causal effect in mind there are
other strategies to get around this and
still estimate other types of causal
effects one strategy is to calculate an
average causal effect rather than an
individual causal effect this is what AB
tests and randomized clinical trials do
but here's the catch the data from an AB
test doesn't look much different from
the data I might collect from my
hypothetical homework experiment in fact
they can be analyzed with the same
statistical model like a linear
regression but one experiment gives us
causal evidence and the other one only
tells us about associations just having
data and a statistical model won't let
you estimate causal effects you need
control or you need assumptions if you
don't have these you have to deal with
something much worse
confounders from here on out I'll be
using directed asyc graphs also known as
dags to visualize statistical
relationships in a dag random variables
are denoted by nodes the variable X will
denote the independent variable the
thing that we as experimenters can
change I'll call this variable the
exposure likewise y will represent the
outcome that we're interested in an edge
between these two variables indicates
that there's an actual relationship
between them the arrow indicates which
variable affects the other if x points
to Y it indicates that Y is a function
of X for Simplicity we'll say that each
Edge represents the presence of a linear
relationship between the two variables
so here's our problem I've gathered data
on my students about the amount of time
they spent on homework and the resulting
score they got I want to know if there's
a significant relationship between X and
Y
in other words I want to know if an edge
exists here but I know that there are
other factors that can influence both
the time a student can spend on homework
and the score that they'll get these
third wheels are called confounders
confounders are variables that have an
association with both the exposure and
the outcome we'll denote the confounder
as C and for Simplicity we'll make it a
binary variable for our example our
confounder will be whether or not a
student has friends having friends can
negatively affect how much time you
spend on homework but at the same time
having friends can also help increase
your score if you happen to be friends
with someone who actually knows what
they're doing the specific reasons don't
matter here I'm just pointing out that
the presence of friends influences both
the exposure and the outcome confounders
introduced two major problems the first
problem is when there's actually no
relationship between the exposure and
outcome since the confounder is
associated with both of them changes in
the confounder can create illusions of
association between them let's say that
having friends reduces your study time
but increases your score so the linear
relationships might look like this
within a class there's going to be a mix
of people who have friends and who don't
I've mocked up some code to simulate
this situation in my class of 50
students half have no friends and the
others have friends you can see that
study time has a negative association
with having friends and score has a
positive Association note in the
simulation that there's no relationship
between study time and score here so
theoretically if I try to analyze it
it's more likely that I won't detect one
in the form of a statistically
significant P value but look what
happens if I try to look at the
relationship between study time and
score here I'll plot both the raw data
using a scatter plot and a plot of the
linear regression if I didn't know any
better I might be tricked into thinking
there's a small but negative relation
ship between these two variables and if
I actually run the analysis and ignore
the confounder I'll see a significant
effect and I'll be checked into thinking
I have a publication on my hand but what
happens when we actually do account for
the confounder in the analysis you'll
see that the significant result
disappears which is what I should see
the second problem of confounders is
from when there actually is a true
relationship between study time and
score in the same way that confounders
can create illusions of association
between between two variables that
aren't related confounders can also
pollute a relationship that's actually
there if we see an increase in the
outcome was it because of a change in
the exposure or was it because of the
confounder here's the same simulation
again with small modification score
actually does have a relationship with
study time if you look at the
relationship between them we can see
that there's a more clear linear
relationship between them if I were to
analyze this relationship I would see
that study time has an extremely
significant relation ship with score but
look at the estimated regression
coefficient I get it's in the right
direction but it's smaller than what it
actually should be it's correct but not
the complete picture now look what
happens when I account for the
confounder in the analysis the estimated
effect is much more accurate and it
still maintains its statistical
significance it's clear from these two
examples that the solution to
confounding is to include them in your
analyses with linear regression
including confounders in the model
changes how we interpret the regression
coefficient for the exposure instead of
just being an average change in the
outcome for a unit increase in the
exposure the coefficient gains an added
interpretation of holding other
variables constant in the model this is
often phrased as controlling for other
variables controlling for confounders
allows us to isolate the relationship
between the exposure and the outcome so
if that's the solution then what stops
someone from just collecting all the
data they can and sticking it all in the
model to isolate the association there's
actually a lot of problems with that but
I'll just focus on one here it sounds
like the obvious solution to just stick
all the confounders into the model but
this makes the assumption that you know
all the confounders in the first place
as a famous philosopher once said well
what I'm saying is that they are known
knowns and that they are known unknowns
but there's also unknown unknowns things
we don't know that we don't
know no matter how much data you collect
the Spectre of unobserved confounders
will always haunt your analysis we make
a lot of assumptions in statistics but
the assumption that you have all the
confounders is a pretty strong one so
much so that no self-respecting
statistician will declare that a
significant Association is causal in a
manuscript unless they know that the
data was gathered in a specific way
we've already seen that confounders
cause problems whether or not there is a
relationship between the exposure and
the outcome so one that you haven't
measured or don't even know about is an
even bigger problem the problem of
unobserved confounders has been known
for a while at one point in history lung
cancer was a rare disease and then
cigarettes became a thing several famous
studies started to show an association
between smoking and lung cancer but the
smoking industry was quick to hire some
intellectual big guns to convince people
that it was all just a funny coincidence
one of those big brains was Ronald fiser
one of the granddaddies of modern
statistics the spite several converging
lines of evidence fer did his best to
poke holes into statistical findings one
of the holes he used was the unobserved
confounder in this case a gene fer
proposed that there was some Gene that
made people more likely to smoke not
only that but it also increased their
odds of getting lung cancer but just
like how Einstein didn't get it quite
right with quantum physics Fisher was on
the wrong side of history with smoking
so where does that leave us how do we
account for something that we haven't
observed and might not even know that we
need to observe are we doomed to just
have spous relationships and polluted
associations if we were we wouldn't be
able to get new medicines to people who
need them unobserved confounders will
always be a problem for statisticians
and analysts but knowing that they exist
is a first step in figuring out how to
overcome them in this video we learned
about the problem of confounders and saw
how they could get in the way of
statisticians trying to estimate causal
effects correlation does not equal
causation but that's not the whole story
at least in statistics if an exposure
causes a change in an outcome then
they're also correlated as well
causation implies correlation just not
the other way around instead a
correlation is a hint to causation that
could be researched further or leveraged
for prediction if you like this video
then consider subscribing to the channel
if you'd like to get video straight to
your inbox then subscribe to the
newsletter too I don't just talk about
statistics there I've also been
chronicling my YouTube Journey there and
things I've learned along the way to
create a successful video I need to
synthesize multiple skills together but
I don't always know these skills ahead
of time as a solo Creator I need to take
the initiative and learn these skills
myself I could do it the slow way
through trial and error or I can speed
things up with an organized platform
like brilliant statistical programming
requires a lot of knowledge about
computers but I don't know a lot about
how they work I've been taking the
computer science courses on brilliant to
learn more about this field from first
principles I'm the type of person who
learns the fastest when I can interact
directly with the concepts I'm learning
and Brilliant is great for this if
you're interested in learning from
brilliant you can get started for free
for 30 days and the first 200 people who
sign up at brilliant.org very normal can
get 20% off an annual plan thanks again
to brilliant for sponsoring this video
thanks for watching I'll see you in the
next

one

n


## Keywords:
