---
source: benoitessiambre.com
url: https://benoitessiambre.com/simcb2.html
---

## Sim Central Bank Reflexions and Something About AI and Empathy

[Sim Central Bank](https://benoitessiambre.com/macro.html) has been online for more than a month, generating almost 200k hits to this website. I received some good feedback that made me think about ways to improve the model and also made me wonder about the broader implications for simulating worlds and what it implies for things like AGI.

First the feedback and observations.

1\. I noticed that the model didn't always quite follow what you would expect from mainstream Keynesian/Monetarist descriptions of economics and I was wondering if this meant there were flaws or bugs that led to unrealistic outcomes.

One thing that emerged in the simulation was what some economists call Neo-Fisherite dynamics which seem to be caused by seigniorage profits cycling through the model. Now I think the limited possibilities for lending and borrowing in SimCB's model under-emphasizes the keynesian/monetarist dynamics you would see in a real economy. However, Noah Smith pointed to me that the Neo-Fisherite dynamics I observed are in line with some known theories:

![](https://benoitessiambre.com/img/ns.png)

So this aspect might not be completely wrong!

2\. One common experience for new players is they start the game, prices creep down, one orchard goes bankrupt, then the other ones quickly fall like dominoes and unemployment goes to 100%. This dynamic is exaggerated in SimCB. What happens is that when an orchard goes bankrupt, that's ten percent of the economy going offline. Not only that but if that business had loans, those loans get reversed with a kind of negative dividend being imposed on people to pay for the bankruptcy. In a real economy, this would happen through banks or other lenders who would be forced to take the hit (since you can't default on the central bank). In any case, this results in an instant shrinking of the money supply. The negative dividends act like a one time tax, people have less money in their bank accounts, spend less on apples, prices drop which makes the other businesses less profitable and in turn go bankrupt.

This is maybe the biggest flaw in SimCB's model and was the result of simulating too small an economy. This choice was made to keep the UI simple, to be able to click on each household, each business and see their data. I might have to revisit.

I'm not sure what the implications are for the real world. Too small a number of agents create a highly unstable monetary system. Central banks might never be able to operate effectively under small village-like economies.

3\. An aspect that makes the simulation difficult and that is annoyingly hard to simulate or get around is the role of expectations. Prices and the value of money has a lot to do with how people think others value things. There is an almost tautological nature to value. Money is worth what people think it's worth. Or rather it is worth what people think other people will exchange for it in the future which also depends on what these future people will think other future people will exchange and so on. While there are some more tangible anchors for the value of money, there are also these recursive expectations which are difficult to model.

Now SimCB does model expectations. Orchards make decisions based on an embedded simple model of prices. Their inner model is basically just an extrapolation of apple prices into the future allowing them to decide if it's worth paying employees to operate the orchard, implemented as a simple linear regression, a kind of [adaptive expectations](https://en.wikipedia.org/wiki/Adaptive_expectations).

I asked myself how I could improve this aspect of SimCB's model and the answer seems to be that it's very difficult!

It might be possible to improve the model by getting the orchards to better guess what others will do. I believe this is in line with the idea of [rational expectations.](https://en.wikipedia.org/wiki/Rational_expectations) This would require orchards having their own more complex sub model of the economy with its own sub agents. And for these sub agent models to be complete, they would potentially in turn have to have a model of the other agents.

This is obviously a considerable challenge. Even if I could implement such a scheme, it would surely be very difficult to simulate in a reasonable amount of time since the recursive possibility space could be very large.

Still, let's speculate on what an implementation might look like. One strategy would be to reuse the exact same model for the children simulations than the main simulation, true model recursion. This looks appealing in terms of saving complexity in specifying the sub model but in order to run such model, sub agents in the sub models would also have to run the full model, simulating their peer agents who might also need to run the full model and so on again. So while using true recursion might solve memory complexity, it might be at the cost of very high time complexity. We get potentially too much recursion and never finish the simulation.

I can think of a rough implementation where at every decision point for an agent, we would pause and save the state of the main simulation, do a few limited timespan runs of the simulation, starting from the saved state for different potential decision scenarios (a kind of simulated A/B test), then rewind back in time and let the agent pick the best path. This would work if it was not for the fact that the sub simulations might encounter other decision points for other agents which might recusively trigger more sub simulations resulting in that time complexity explosion.

So orchards using simplified adaptive models makes the simulation much more tractable or at least easier to implement. I'm not sure how rational expectations are simulated by economists, if they found some closed form differential equations that make some idealized models tractable but with a complex numerical simulation, it seems very difficult.

Still, if you choose to use some kind of sub model, child models reusing parts of the parent model for information theoretic efficiency and simplification still seems like a powerful concept.

You could call this idea a kind of algorithmic empathy. Make the agents in your model have a model for their peers that is similar to their own, basically putting their own model, their own reasoning, in other agent's shoes.

There is a research field called artificial empathy that is about reflecting human emotions. This is not what is meant here. We are talking about something more related to the algorithmic aspects of [social cognition](https://en.wikipedia.org/wiki/Social_cognition) (also see these [algorithmic examples](https://probmods.org/chapters/social-cognition.html)) or [social metacognition.](https://www.lesswrong.com/posts/K4eDzqS2rbcBDsCLZ/unrolling-social-metacognition-three-levels-of-meta-are-not)

To conclude, I'll make some wild speculative comments about AI that occurred to me while thinking about simulations. My impression is that for an AI to be considered fully general, it would need to be able to sort out the kinds of scenarios that require algorithmic empathy and there may be hard limits on what is possible here. If you asked me to give an argument against the possibility of a technological singularity, theoretical limits on doing recursive simulations of simulations of simulations might be the best I can find.

It's one of the most impressive feat of the evolution of human intellect that a lot of people seem to be able to do, at least aproximate, recursive empathic reasoning fairly instinctively and effortlessly, as far as I know, something that even the most advanced AIs barely even try to do. It's possible that the human race is already pushing the limits of what's possible in this area.
