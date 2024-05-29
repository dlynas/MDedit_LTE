---
title: is_there_a_game_theory_term_for_a_repeated_game
url: https://www.reddit.com/r/GAMETHEORY/comments/1b3kj4k/is_there_a_game_theory_term_for_a_repeated_game/
source: reddit
subreddit: GAMETHEORY
media: no
---
**r/GAMETHEORY** | Posted by u/GoodReasonAndre ⬆️ 4 _(2024-02-29 22:42:44)_

## Is there a game theory term for a repeated game with resource accrual?

Original post: [https://www.reddit.com/r/GAMETHEORY/comments/1b3kj4k/is_there_a_game_theory_term_for_a_repeated_game/](https://www.reddit.com/r/GAMETHEORY/comments/1b3kj4k/is_there_a_game_theory_term_for_a_repeated_game/)

> I'm a game theory noob, so apologies if this is a dumb question. **I was wondering: is there a game theory name for a repeated game with resource accrual, where your resources change what strategies you have available?** For example, you could imagine a repeated version of [the ultimatum game](https://en.wikipedia.org/wiki/Ultimatum_game), where you have to pay a 'fee' to a third party to reject a split. In that way, the amount of money you have already - and the amount of money the other player has - changes what strategies both players have available. Which of course, would also change the strategies they pursue.
> 
> I assume that something similar must appear somewhere in game theory, but since I don't know the term for it, I can't find anything about it.

💬 ~ 4 replies

---

* 🟩 **[YuptheGup](https://www.reddit.com/user/YuptheGup)** ⬆️ 3 _(2024-02-29 23:50:44)_

	Look up stochastic games.

	What you're talking about is using some sort of state space to define each stage of the game. You'd need to define a transition matrix (or markov kernel if state space is continuous) that tells us how each state evolves from the previous. Then, typically you would restrict your strategies to only payoff relevant states (Markov strategies). Typical SPE would run into problems related to the folk theorem when it comes to infinite games.

	Try to clearly define your state space as well as your law of motion. It does get tricky though, so I wouldn't recommend it to someone with not that much game theory experience.

* 🟩 **[Background_Cat_9061](https://www.reddit.com/user/Background_Cat_9061)** ⬆️ 1 _(2024-03-29 02:14:22)_

	I see it has been 28 days but the scenario you describe fits into any setting where the strategy set is restricted to the resource set. Think of a poker game where the strategy is how much money you put on the table, third party is the dealer. given the payoff structure (the strength of your hand) and the information set (information about others' resources, that you interpret in the game, and your beliefs about the others' hands) you have in each round, you decide whether or not to enter and how much to put on the table. Also, the other comment is really helpful and mine is somehow an example of it. But sbe is kinda advanced shit and refers to an equilibrium concept. assuming you're an econ master's, I advise you to develop interest in different areas 😥

	* 🟨 **[GoodReasonAndre](https://www.reddit.com/user/GoodReasonAndre) (OP)** ⬆️ 1 _(2024-03-29 15:23:33)_

		Why assume I'm an econ masters? So specific! Is that common for this sub?

		* 🟧 **[Background_Cat_9061](https://www.reddit.com/user/Background_Cat_9061)** ⬆️ 1 _(2024-03-29 15:25:32)_

			I thought you had some political econ or experimental econ classes since you mentioned ultimatum games


