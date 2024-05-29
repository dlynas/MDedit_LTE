---
source: benoitessiambre.com
url: https://benoitessiambre.com/simcb.html
---

## Sim Central Bank, The Explanation

It's your turn to have ultimate control over one of society’s most powerful element, _all_ of its money. You get to decide how much is available and how costly it is to borrow. Can you do a better job of controlling inflation than Christine Lagarde or Jay Powell? Can you limit unemployment and help your economy grow production? [Play SimCB here](https://benoitessiambre.com/macro.html).

You've played the game, you did the fun part. Now time to dive into the tedious wonkish details.

Understanding something means being able to explain it, ideally with a level of detail that allows you to simulate its essential parts. This is sometimes called a "model". They say all models are wrong but some are useful. Economic models tend to be particularly wrong. Experts often produce disagreeing and contradictory models. The rest of us get to witness the high profile quarrels that ensue as they encounter each other being wrong on the internet.

I am not an economist so the model behind SimCB is even more wrong than usual.

SimCB was made after following some of this quarreling for some time and deciding I needed to try to put a toy model down, something to convince myself that I had understood something after squinting at the hazy arguments. The other, more serious reason that made this game worth building is that, I like toys. This is the post that describes the model behind the game. The mechanics revealed might help you hit those high GDP scores.

A lot of real economic models involve advanced math and differential equations. The goal here was to keep this type of mumbo jumbo to a minimum to make it more easily understandable for those who like to **right click ➤ view source** (and more importantly to make it less work for me to build).

I started this project years ago as a way to learn about macroeconomics. After doing some reading and going down a certain number of rabbit holes that led to more questions than answers, I gave up.

Economics is a complex, controversial and politicized subject. A surprising amount of it is rooted in relatively immaterial stuff: promises, expectations, laws, IOUs, a lot of things which only have value through some kind of (often tenuous) human convention. How these conventions form and propagate and move through societies is sometimes rooted in crowd psychology based on convoluted game theoretic moves of not-so-rational actors that are very hard to model. This has never been more obvious than in the current world of crypto tokens.

Macroeconomic models are complex. There are many economic schools, saltwater, freshwater, monetarist, keynesians, austrians, MMTers and more.

Despite all this, I recently decided to give it another go. It's probably still useful to model some economic phenomena in terms of simpler things like offer and demand and production and consumption of concrete physical goods and services. These things play a role especially if you can assume people eventually want to get some products or services out of their wealth and not just hold virtual tokens or get high scores in their bank accounts.

Even if you simplify homo economicus to its simplest dumbest version (like the agents in SimCB who only ever work in orchards and only ever consume apples), macroeconomics remains very counterintuitive. There are concepts that are difficult to wrap your head around.

Economics at the macro, aggregate level often works inversely to economics of smaller parts of the economy in seemingly paradoxical ways. For example, when someone says there is too much debt in the economy, they necessarily imply that there is also too much savings as one person’s debt is always another person’s saving, the person that the debt is owed to.

![](https://benoitessiambre.com/img/docbrown.png)

(Hints for resolving the paradox include making a distinction between financial savings like contracts, IOUs, stocks, cash, coupons, tokens etc. and the more physically real capital investment type of savings such as factories, inventory, production capacity, knowhow, etc that are (and it makes me anxious to say this) kinda maybe supposed to at least indirectly underly the intangible financial paper or electronic types of savings.)

Another apparent paradox is that at the macroeconomic level, money can’t be “spent” by people purchasing things. A purchase only moves money around from one party to another party without changing the level of money out there. The amount of money out there has a lot more to do with loans than with spending.

![](https://benoitessiambre.com/img/gru.png)

This is one reason it's so crucial for central banks to do a good job putting the right amount of money in circulation. When they don't put enough, the markets tie themselves into knots, production and employment drops as everyone gets busy hoarding the scarce tokens instead of producing real things to buy with these tokens. On the flip side, when they print too much, you get destabilizing inflation.

Now the goal in this game was to simulate an economy following strict accounting constraints. No money comes out of thin air, or disappears on a whim. Money isn’t created or destroyed unless the central bank makes loans. The balance sheets of individuals and businesses always add up.

I’m a believer in the pedagogical powers of simplified cartoon models. The economy of SimCB contains only people, apples, coins, orchards, an apple market and a central bank. People are all apple farmers, businesses are all orchards, there are no commercial banks, the central bank is responsible for making all loans. There is no government other than the central bank and the imposed rules.

The orchards can be thought of as coops owned equally by everyone. This means every time a company makes a profit, these profits are distributed equally as dividends to everyone. If an orchard goes bankrupt, since there are no commercial banks and you can’t default on the central bank, everybody has to pitch in to pay the outstanding debt in a kind of reverse dividend (in a real economy people might do this indirectly through ownership in commercial banks).

When the central bank lends money at positive interest rates, the interest profits or “seigniorage” are distributed to everyone like dividends (they would in the real world go to the government which would spend or distribute them). If seigniorage was not distributed, at the end of each loan, the money supply would shrink a little bit as the central bank would be gradually absorbing money from the economy as interest. Seigniorage serves to neutralize this.

The inverse happens with negative interest rates. If the central bank makes a loss on a loan, people are taxed to make the central bank whole in a kind of reverse seigniorage. Now in the real world this doesn’t tend to happen.

I could have let the central bank take the loss. Apparently for reasons of popular perception, central banks tend to be reluctant to have a negative balance sheet even though they can’t go bankrupt since they can just print more money. This reluctance is probably undue awkwardness from central banks not being used to it. Apparently up to now most central banks with negative rates have managed to keep positive revenues by diversifying into riskier higher returns assets.

Now I could still have allowed central bank losses in SimCB's model. This might have made sense especially given that SimCB doesn't have a government to amplify central bank moves by borrowing. Central banks taking a loss, instead of taxing reverse seigniorage, might have simulated government stimulus, allowing the negative interests to act as little helicopter drops of money. Real world governments often borrow and spend during conditions that warrant very low rates (or under any other conditions really) to help put money into circulation. Something to try in a future version.

SimCB has no government to help stimulate, so the effect of central bank interest rate changes are subdued. They rely solely on stimulating borrowing from orchards and spending from consumers.

SimCB only allows negative interest rates down to -0.5%. This is similar to real world constraints. People would borrow huge sums and stash money under their mattresses to reap the benefits of negative interests. Central banks can't go much lower than zero.

SimCBs economy operates on a monthly basis. Every month people work, orchards produce, apples go to a market, people take a share of their coins to buy a share of the apples at the market.

Orchards follow a life cycle. They are in a planning phase for 6 months, they are in a cultivating/growing phase for 24 months and in a producing/harvesting phase for 30 months. After that they (may) start again.

Now when I first implemented the game, orchards were stopped and launched randomly when rates and wages were favorable. They also had a random number of employees. Since the game has only 10 orchards, each time one of these orchards restarted, 10% of the economy stopped or started, which was creating a lot of pretty large, hard to manage shocks.

In order to make the SimCB economy with only 10 businesses act more like a large economy having many more businesses and where a single business stopping doesn't create that large of a shock, I used a dirty trick. I made it so that businesses can only start once every 6 month period and only a single business can do so per period which results in lifecycles being staggered. This means that when the economy is at full employment, all orchards are operating, the moment one finishes, one restarts so that there is no downtime. One of the 10 orchards is always in its preparation phase which means it doesn't employ anyone so the natural unemployment rate is one out of ten or 10%. Of course orchards can go bankrupt or fail to start. It will then take a while for them to start again, until it's their turn in the staggered scheme.

So the player controls the interest rate. This has two main effects, one on orchards and one on people.

Orchards are continuously estimating their potential profitability given the going rates, wages and apple prices. They have a model in the model, extrapolating prices to take into account the effect of inflation.

Every month each orchard calculates what is the maximum wage they could afford without going bankrupt. If the orchard is currently running and the max wage is below what was negotiated before, it goes bankrupt (wages are negotiated at the beginning of the lifecycle and fixed for the 60 month period).

To estimate the going wage for a newly starting orchard, the lowest of the maximum wage each orchard could afford is calculated. A scheme called [marginal revenue productivity of wages](https://en.wikipedia.org/wiki/Marginal_revenue_productivity_theory_of_wages). The going wage can't be higher than that otherwise some orchards couldn't survive and some people would always be without a job and starve. Starvation is a good motivator to accept lower wages.

The wages aren't higher than that because if some workers have to accept it to prevent bankruptcies, why would other businesses pay other identical workers more than that accepted rate? Statisticians might say people are considered [_exchangeable_](https://stats.stackexchange.com/questions/3520/can-someone-explain-the-concept-of-exchangeability). In reality, more productive businesses that can afford to pay more might pay more depending on negotiations, but this is just a toy model.

Another constraint present in the model is that wages are sticky, they can't go up or down much more than previous average wages. If an orchard would require wages too far below recent wages to be worth starting given prices and interest rates, it fails to launch and people go unemployed.

This is why adjusting interest rates is crucial. Eventually the going wage or prices will adjust but the player can make the transition smoother avoiding bankruptcies by varying interest rates.

SimCB gives you some hints. An approximate maximum interest rate that the least profitable orchard can tolerate before going bankrupt is displayed as the "natural rate" (this is not quite the textbook definition of natural rate but it hints at it). If you set the interest rate higher than that, orchards risk going bankrupt, unemployment going up.

Lowering interest rates makes businesses able to afford higher wages, which will make wages slowly adjust higher, the extra borrowing to pay those wages will put more money in circulation and prices will also go a bit higher in a kind of wage price spiral. This is one of the effects of varying rates.

Note that this effect is maybe weaker than you might expect. The borrowing may only get slightly higher since orchards also sell apples and pay as they go, even if the wages are significantly higher, remember that lower interest rates means less seigniorage and maybe less profits and part of the higher pay is offset by the lower received dividends. Only the actual extra borrowing puts more money in circulation in a way that raises prices possibly after a long and variable lag.

I find it interesting that even though higher wages leading to higher prices seems like a pretty intuitive causal mechanism, it doesn't really work that way since people on average don't necessarily end up with that much more money when you account for the lowered investment income.

The other thing that is affected by interest rates is people's propensity to spend. The model is pretty simple here. People every month pay X% of their coins to buy Y% of the apples the market has. Y is fixed. When interest rates are higher, X goes proportionately lower and vice versa. This calculation is made with an inflation adjusted rate. This means higher inflation will make people spend more.

This effect on spending is more immediate after the player changes the interest rate. It seems, at first, stronger than the effect on investment and wages in orchards, though things can normalize pretty quickly as wages and apple prices adjust. If the investment part leads to changes in unemployment, the effect eventually gets very large on that side too.

Note that before I implemented sticky wages, things tended to adjust very quickly and changes in interest rates did not have much of an effect on employment. It mostly just changed the nominal prices of things and the share of people's revenue being received through wages vs through seigniorage and dividends.

I suspect in a real economy having commercial banks and governments, the effect on borrowing and credit would be greater than in this model so the economy might be more impacted by borrowing, seigniorage distribution having relatively less importance.

It's difficult to create hyperinflation in SimCB (unless in the aftermath of high unemployment leading to low market inventory), when you lower interest rates, even to negative rates, the central bank takes a loss and you get reverse seigniorage, people's money is automatically taxed away, which offsets the inflationary effects of low interest rates and the system self stabilizes. This is partially due to there not being government debt to help fuel high inflation. I don't know how well this reflects real world economics.

The other aspect that is missing from SimCB which could cause hyperinflation is the option for people in an economy to switch to another currency. Basically, in SimCB, if money gets too unstable and impractical, it's tough luck for the villagers. They still have to use it if they want to buy apples. There are no alternatives. This forces a sustained demand for money even when it is poorly managed money.

I suspect in the real world, hyperinflation is more likely to happen when people have the option to leave a currency for another one. Almost like a run on the currency where people try to redeem it for something else (people might need to keep a minimum amount for paying taxes and such).

Hyperinflation could also have happened more easily in SimCB if I had allowed the central bank to incur loss, like mentioned previously.

You'll notice that shocks cause prices to move in a direction but they often rebound in the opposite direction as things adjust and as inflation expectations and employment moves with a lag and skews profitability estimates and investment and spending decisions from people and orchards.

Large moves or shocks seem to create oscillations before things settle. These oscillations can be hard to counter and can lead to bankruptcies. Players might have to move interest rates somewhat aggressively in both directions after a shock. I'm not sure how much this reflects real economies.

If there is a production disruption long enough for the apple market to lose most of its inventory, things can get really hard to stabilize because orchards resuming production lead to large inventory swings and thus large price swings. You get a kind of [bullwhip effect](https://en.wikipedia.org/wiki/Bullwhip_effect).

The player might avoid this fate by slowly creeping interest rates up when the economy is going well which gives space for aggresively lowering them during shocks to the village economy.

Also note that when prices are changing too much, "menu costs" go up. SimCB simulates this by penalizing production from orchards. This happens in a real economy when resources are diverted to renegotiations and price updates because of unstable prices.

I hope this provides some insights on how this all works. I left out some of the finer details such as how orchards estimate their profitability (try "view source" if interested). There are definitely knobs I adjusted to make the game behave like what subjectively seemed reasonable to me. I hope you find the experience interesting and maybe even fun.

Addendum: [followup post](https://benoitessiambre.com/simcb2.html)
