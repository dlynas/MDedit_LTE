---
source: math.stackexchange.com
url: https://math.stackexchange.com/questions/267384/does-this-multiplayer-generalization-of-the-prisoners-dilemma-exist
---

While thinking some things over in my head, I came across the idea of trying to generalize the Prisoner's Dilemma to multiple participants, and trying to do it in the simplest way possible.

In essence, what I came up with is that between each ordered pair of players, there is the action of "take 1". Each player can either do it or not do it to another player. If the player does it, he gains one point, while the person whom he "took 1" from loses two points.

In the case of two players, each with the action "take 1" or "don't take 1", the payoff matrix looks like the traditional Prisoner's Dilemma \[transpose for player 2\]:

Player 1TakeDon'tTake−1+1Don't−20

(It's a nonpositive-sum game because people are usually more loss-averse than they are gain-prefering, so removing global gain as an option generally forces more psychological strain \[and often more irrational, destructive action\] on the players, which is part of the point of the Prisoner's Dilemma.)

It generalizes in the global behaviour of the Nash equilibrium - "take 1" is still the more locally beneficial ("personally rational") option, but leads to the worst global result.

My question is, does such a generalization (where the dilemma is split into multiple independent actions) already exist, and whether studies have been done on it. If so, where can I find it (and its analysis)? If not, how could I go analyzing such a multiplayer situation myself?
