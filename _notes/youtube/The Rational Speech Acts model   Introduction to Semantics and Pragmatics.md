---
note_type: metamedia
mm_source: youtube
mm_url: https://www.youtube.com/watch?v=bPd6CNy5UqA
---

# Video
The Rational Speech Acts model  | Introduction to Semantics and Pragmatics
![](https://www.youtube.com/watch?v=bPd6CNy5UqA)

## Transcript:
Hi, I'm Chris Potts.
This screencast provides a technical introduction
to the Rational Speech Acts model, or "RSA".
I intend this to be a technical companion
to Noah Goodman and Michael Frank's 2016 paper
'Pragmatic language interpretation as probabilistic
inference'.
I'll start with some high-level motivation
for RSA, but the screencast is mostly devoted
to example calculations.
My goal is to expose the technical inner-workings
of the model and convey how it makes predictions
about pragmatic language use.
This should give you a feel for RSA, and then
you can start to rely on computational simulations
to gain a deeper understanding.
And I'll point you to some code for doing
that at the end.
To start, let's consider the theory of pragmatics
that Grice developed in his classic paper
'Logic and conversation'.
The backbone of that theory is the cooperative
principle, which enjoins the speaker to "Make
your contribution as is required, when it
is required, by the conversation in which
you are engaged".
This is meant to define linguistic interactions
as cooperative affairs in which the listener
is seeking to understand the speaker's intentions
for their utterances, and speakers are supposed
to do their best to make that job easy for
the listener.
Grice also defined a set of maxims, which
fall under the cooperative principle and seek
to flesh out at least major parts of it.
So, quality says you should speak truthfully
and say only things for which you have evidence.
Quantity says you should be informative, but
not overly informative.
Relevance says that you should make sure your
linguistic contributions serve the current
goals of the conversational interaction.
And manner places pressure on the forms you
use the convey information, asking you as
a speaker to be clear and concise.
And there might be other maxims.
Now, these are certainly intuitive and useful
principles, but they will not admit of easy
formalization, which means that they are also
hard to empirically test in a rigorous fashion.
So this raises the question of whether we
might be able to let these specific maxims
fade into the background, to serve simply
as broad, intuitive motivation.
And this what I take the fundamental thesis
of RSA to be: from the assumption that speaker
and listeners are truly trying to communicate,
and some core mathematical concepts that embody
aspects of the maxims, we can achieve a robust
and precise pragmatic theory.
We can also motivate RSA using Grice's notion
of a conversational implicature.
I have a separate screencast on implicature
that covers that idea in detail, so I won't
go into too much depth here.
But, informally, suppose we have this speaker
on the left, and this listener on the right.
And imagine they're in a context containing
these two salient individuals.
Now the speaker would like to refer to the
friend on the left.
To do this, she says, "My friend has glasses".
In the background, the definition of implicature
says that the speaker will reason like this:
"My listener knows I'm cooperative in the
Gricean sense.
So they'll be able to work out that I mean
'not hat' as well."
From the listener's perspective, we have the
core tension that the definition of implicature
sets up: the speaker's utterance seems ambiguous
or under-informative given their referential
goal.
But the listener thinks, "I was assuming this
speaker was cooperative in the Gricean sense".
So there's a tension here.
And then the reconciliation: if the listener
assumes that the speaker meant also to convey
"not hat", then all's well: the speaker is
still basically cooperative, and the referential
goal succeeds.
In a deep sense, this "filling in" of the
proposition "not hat" is what RSA formalizes.
So let's move to the model itself to see how
that happens.
To start, we need to formalize the sort of
reference game that I just used.
So first we have a set of referents, and we
assume it's common knowledge that these are
the set of referents.
The semantics provides a core set of conventions
for the conversational participants to work
with.
It's a traditional semantics, in that it maps
words to the sets of things those words are
true of.
So this interpretation function matches the
picture in the way that you'd expect.
The version of RSA that I present here is
restricted by these truth conditions, in that
it can strengthen these meanings, but it can't
stray outside of them.
This can be seen as reflecting the maxim of
quality.
Now, it's noteworthy that variants of RSA
that don't adhere to truth conditions in this
way have been explored, and for phenomena
that Grice too took to fall outside of quality.
I'm thinking especially of metaphor.
We also have a prior probability distribution
over referents.
We can think of this in lots of ways -- for
example, as the relative likelihood that one
would want to refer to each referent, or as
measuring each referent's salience.
The best view of this is still an open area
of investigation, but we won't need to worry
about the conceptual details.
We also have real-valued costs for messages.
This is our main gesture to the maxim of manner.
The interpretation is that large negative
costs correspond to messages that the speaker
would prefer to avoid.
The final ingredient is the alpha parameter.
I'll say a lot more about what it does later.
For this screencast, I'm going to depict reference
games in this compact way that you see at
the bottom of the screen here.
In the middle we have the truth conditions
-- the semantics.
The prior over referents is in the bottom
row.
The costs are given in the final column.
And the alpha value stashed up here in the
corner.
The final thing I'll say about this reference
game is that it has the potential for the
implicature we just walked through informally.
Right, the speaker should choose 'glasses'
for r1 and 'hat' for r2, and the listener
should make corresponding inferences.
This isn't encoded in the truth conditions,
which make 'glasses' equally true of both
referents, but we'll see that it emerges from
pragmatic reasoning.
Okay, let's do a first calculation.
I'll introduce the model incrementally as
part of this calculation, and I'm going to
start with just a basic version of the model,
so that we get a feel for the rhythms of the
calculations.
Up here is the reference game I'll be working
with.
But when alpha is 1, the prior is flat, and
the costs are 0, we can simplify the reference
game to just its truth conditions, like this.
This is the literal listener.
It defines a conditional probability distribution
of referents given messages.
As you can see here, this distribution is
defined entirely in terms of the semantics,
as the truth value of message m for referent
r divided by the sum of all the truth values
of message m over all referents r-prime.
Just to make this a bit more concrete, let's
walk through the calculation of this value
here: the probability of r1 given the message
'hat'.
So the definition gives us the expression
in the orange box.
From there, we just look up the values in
the truth conditions.
After substitution, we get 0 divided by 0
plus 1, which of course resolves to 0.
Let's do one more.
We'll do r2 given 'glasses'.
Again, using P-Lit, we get the expression
in the orange box.
We look up the values in the truth conditions,
and then we just do a simple calculation.
Later on, we'll see that the full RSA model
incorporates the referent prior into this
calculation, but what we just saw is really
the core of it.
And calculating these values for all messages
m and referents r gives us the full that you
see here.
And I just want highlight that this basic
listener has a maximal interpretive bias for
'hat', but not for 'glasses', since both referents
have glasses.
This is the sense in which this listener is
not pragmatic.
The pragmatic speaker is next.
To calculate those values, we first need to
transpose the literal listener matrix, which
just means swapping rows and columns like
this.
It's then this equation here that defines
the full pragmatic speaker.
The speaker in this model is a conditional
distribution over messages given referents,
the reverse of the listener.
I like to think that the speaker wants to
refer to a specific individual -- that's taken
as given -- and this model equation here characterizes
how the speaker will achieve that.
So this speaker is very similar to P-Lit,
except that it reasons about the literal listener,
rather than about the truth conditions, and
it chooses messages given referents, rather
than the reverse.
Let's walk through another calculation.
So using the model definition we get the expression
in the orange box.
And then, crucially, we look up the values,
not in the truth conditions, but rather in
P-Lit.
Simple substitution and calculation then gives
us the final value.
So that's how that kind of calculation goes.
Notice that this pragmatic speaker has broken
the tie that the literal listener had for
'glasses'.
This comes from the fact that, while the 'glasses'
row is even for the listener, if we think
column-wise like the speaker in effect does,
then things are more imbalanced.
This is, I'd say, the speaker version of the
scalar implicature that we're targeting.
Okay, the final agent is the pragmatic listener.
To derive it, we again transpose, so that
the messages are back on the rows and the
referents on the columns.
This agent is completely parallel to the literal
listener.
The crucial difference is that it uses the
values from the pragmatic speaker rather than
the truth conditions.
The effect is that this recursion that we
see is two or three levels deep, depending
on how you count.
So we go from here, to the speaker, and then
to the literal listener, and finally to the
semantics.
Let's walk through the full calculation one
more time to help convey the rhythm of the
calculations.
So we start with the semantics.
We normalize to get the literal listener.
Then we transpose to start the speaker calculation.
We normalize the rows again to get the pragmatic
speaker.
Then we transpose to begin the pragmatic listener
calculation.
And then finally we normalize.
And what we get reflects our desired implicature,
which is a strong bias for r1 given 'glasses'.
Okay, that's RSA in its most basic form.
We've so far ignored costs, alpha, and the
priors.
For this next set of calculations, we'll bring
in costs.
That's the component that seems to introduce
the most complexity, but it's not actually
all that complex.
We just need to deal with some mathematical
niceties.
So we'll use this simple reference game here.
It's the same as before, except 'hat' now
has a very large cost associated with it.
This will mean that the speaker avoids this
form.
The speaker's avoidance of this form is going
to diminish the implicature we saw before
because now the listener can't tell whether
avoidance of 'hat' is because the speaker's
referent is r1, or because the speaker just
doesn't want to say 'hat'.
The literal listener calculation is unchanged.
Here's the full speaker matrix with its corresponding
definition.
And let's unpack the definition a little bit.
At its core, this is what we saw before: the
numerator has P-Lit, and the denominator is
summing over those P-Lit values.
We'll ignore the alpha parameter for now.
If you assume it's 1, then it can be left
out.
Okay, and the rest of this derives from the
fact that we want to incorporate the real-valued
scores, but we need this whole thing to be
something we can turn into a probability distribution.
So the log transform here moves the P-Lit
probabilities into the same sort of space
as the costs, which then get added in.
And then exponentiating with exp returns us
to a space we can normalize, by compressing
these log-P-Lit-plus-cost values back into
a positive space.
Now, what I've written as exp here is often
given with an italic e and a superscript,
where e is the base of the natural logarithm.
And note that taking the log of x, and then
exponentiating the result of that, just takes
you back to x again.
This is why we could leave these expressions
out before, when we had all-0 costs and alpha
was 1.
In that situation, this whole expression reduces
to P-Lit of r given m.
So to derive the probability of 'hat' given
r2 in this game, we create this expression
here in the orange box.
As before, we look up the core P-Lit values,
but now we also fetch the costs.
And then those get wrapped in the math that
we just walked through, with exp and log.
After that, you should let your calculator
take over to derive the final value.
From there, the pragmatic listener calculation
is identical to the one we did before with
the simpler speaker.
So I'll leave that aside.
And just to round out the above, let's walk
through the full calculation here.
In outline, it's what we did before, but with
a bit more math.
So we start with the semantics.
Wew normalize to get the literal listener.
Then you transpose to start the speaker calculation.
Okay, and now the only new bit: add the costs,
take the log of the the P-Lit values, and
exponentiate the whole thing.
Then you normalize as usual.
And from there it's the same pragmatic listener
calculation: transpose and then normalize.
What's noteworthy here is that, as predicted,
we've basically lost the pragmatic listener
bias for r1 given 'glasses'.
The high cost of 'hat' results in avoidance
of that form in general.
Okay, there are two more technical pieces
to review: the alpha parameter and the role
of referent priors.
Let's look at the alpha parameter now.
The core of this is that the alpha parameter
can be seen as controlling how much pragmatics
we see.
Larger alphas result in stronger pragmatic
inferences, and smaller alphas correspond
to weaker pragmatic inferences.
The literal listener, as you see here, isn't
affected, since it's lower down than alpha
in the computation.
But here's the definition of the speaker without
the costs -- that is, just with alpha.
And we saw before that, with alpha set to
1, we get this speaker bias.
Compare that to when alpha is set at 4.
The bias for using 'hat' to refer to r2 is
much greater now.
This happens because of the scaling effect
of alpha in this exponential space.
To get a feel for this, consider the fact
that if we compare .75 and .25 in our model
with alpha equals 1, then .75 is merely three
times larger than .25.
In contrast, with alpha set to 4, .75, once
scaled, is about 81 times larger than .25,
once scaled!
So this is how we end up with the generalization
that larger alpha means stronger pragmatic
inferences -- all these contrasts get amplified.
We have one more component to review.
That's the referent priors.
We'll stick with our usual referent game,
but now we've created a strong bias in favor
of referring to r2.
And this too will reduce our implicature that
'glasses' refers to r1.
Now, when the listener hears 'glasses', they
can't be sure whether this is steering them
towards r1 or just reflects the speaker's
eagerness to refer to r2 with any language
With priors, the literal listener is changed,
in that we now reason both about the truth
conditions and about this referent prior.
The prior is just multiplied in.
To make this concrete, suppose we want to
calculate the probability of r2 given 'glasses'.
Then the P-Lit calculation unpacks as in the
orange box.
We look up the truth conditions as before,
and now we also look up the prior values.
And the calculations after that are simple.
Notice that this means that the entire pragmatic
process starts with a strong bias in favor
of referring to r2, no matter what the message.
As a result, the usual speaker bias for associating
r2 and 'hat' is smaller -- recall that this
used to be .67.
We also bring in the prior in the pragmatic
listener calculation, and notice that, instead
of having .75 probability of choosing r1 given
'hat', it's now down to around fifty percent.
That's as we predicted given the strong bias
in favor of referring to r2.
Just to round this out, let's go through the
whole calculation.
So we start with the semantics.
We incorporate the priors -- that's the new
piece.
Then we normalize as usual.
Then we transpose and normalize for the speaker
calculation.
Then we transpose to begin the pragmatic listener
calculation.
Then we bring in the priors again.
And then finally normalize.
And now you have the final pragmatic speaker.
And as I said, the bias away from r1 has weakened
the pragmatic association between 'glasses'
and r1.
Okay, that's it!
Here's the full model, with priors, costs,
and alpha.
If you're feeling comfortable with the the
model now, then I'd suggest downloading this
simple implementation of RSA, which is available
from the Linguist 130a website, and trying
out different calculations on your own, seeking
to find new predictions that you can test
empirically.


## Keywords:
