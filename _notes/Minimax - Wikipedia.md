---
source: en.m.wikipedia.org
url: https://en.m.wikipedia.org/wiki/Minimax
---

**Minmax** (sometimes **Minimax**, **MM**<sup id="cite_ref-1"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-1">[1]</a></sup> or **saddle point**<sup id="cite_ref-2"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-2">[2]</a></sup>) is a decision rule used in [artificial intelligence](https://en.m.wikipedia.org/wiki/Artificial_intelligence "Artificial intelligence"), [decision theory](https://en.m.wikipedia.org/wiki/Decision_theory "Decision theory"), [game theory](https://en.m.wikipedia.org/wiki/Game_theory "Game theory"), [statistics](https://en.m.wikipedia.org/wiki/Statistics "Statistics"), and [philosophy](https://en.m.wikipedia.org/wiki/Philosophy "Philosophy") for _minimizing_ the possible [loss](https://en.m.wikipedia.org/wiki/Loss_function "Loss function") for a [worst case (_max_imum loss) scenario](https://en.m.wikipedia.org/wiki/Worst-case_scenario "Worst-case scenario"). When dealing with gains, it is referred to as "maximin" – to maximize the minimum gain. Originally formulated for several-player [zero-sum](https://en.m.wikipedia.org/wiki/Zero-sum "Zero-sum") [game theory](https://en.m.wikipedia.org/wiki/Game_theory "Game theory"), covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.

## Game theory [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=1 "Edit section: Game theory")

### In general games [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=2 "Edit section: In general games")

The **maximin value** is the highest value that the player can be sure to get without knowing the actions of the other players; equivalently, it is the lowest value the other players can force the player to receive when they know the player's action. Its formal definition is:<sup id="cite_ref-ZMS2013_3-0"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-ZMS2013-3">[3]</a></sup>

![{\displaystyle {\underline {v_{i}}}=\max _{a_{i}}\min _{a_{-i}}{v_{i}(a_{i},a_{-i})}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/76d2fe8fe2fc328093c7b0c19e83a0197004a5d3)

Where:

Calculating the maximin value of a player is done in a worst-case approach: for each possible action of the player, we check all possible actions of the other players and determine the worst possible combination of actions – the one that gives player i the smallest value. Then, we determine which action player i can take in order to make sure that this smallest value is the highest possible.

For example, consider the following game for two players, where the first player ("row player") may choose any of three moves, labelled T, M, or B, and the second player ("column player") may choose either of two moves, L or R. The result of the combination of both moves is expressed in a payoff table:

![{\displaystyle {\begin{array}{c|cc}\hline &L&R\\\hline T&3,1&2,-20\\M&5,0&-10,1\\B&-100,2&4,4\\\hline \end{array}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c94218d6211047370d9243ce80081b8860b90c33)

(where the first number in each of the cell is the pay-out of the row player and the second number is the pay-out of the column player).

For the sake of example, we consider only [pure strategies](https://en.m.wikipedia.org/wiki/Strategy_(game_theory)#Pure_and_mixed_strategies "Strategy (game theory)"). Check each player in turn:

If both players play their respective maximin strategies ![{\displaystyle (T,L)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/20493aa06e4ba84a0057e0fc6a261dc87667ca8e), the payoff vector is ![{\displaystyle (3,1)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a8933db1c87b5fefc8d54c6e2d157e4b343bb8b8).

The **minimax value** of a player is the smallest value that the other players can force the player to receive, without knowing the player's actions; equivalently, it is the largest value the player can be sure to get when they _know_ the actions of the other players. Its formal definition is:<sup id="cite_ref-ZMS2013_3-1"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-ZMS2013-3">[3]</a></sup>

The definition is very similar to that of the maximin value – only the order of the maximum and minimum operators is inverse. In the above example:

-   The row player can get a maximum value of 4 (if the other player plays R) or 5 (if the other player plays L), so:  
-   The column player can get a maximum value of 1 (if the other player plays T), 1 (if M) or 4 (if B). Hence:  

For every player i, the maximin is at most the minimax:

Intuitively, in maximin the maximization comes after the minimization, so player i tries to maximize their value before knowing what the others will do; in minimax the maximization comes before the minimization, so player i is in a much better position – they maximize their value knowing what the others did.

Another way to understand the _notation_ is by reading from right to left: When we write

the initial set of outcomes   depends on both   and   We first _marginalize away_   from  , by maximizing over   (for every possible value of  ) to yield a set of marginal outcomes   which depends only on   We then minimize over   over these outcomes. (Conversely for maximin.)

Although it is always the case that   and   the payoff vector resulting from both players playing their minimax strategies,   in the case of   or   in the case of   cannot similarly be ranked against the payoff vector   resulting from both players playing their maximin strategy.

### In zero-sum games [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=3 "Edit section: In zero-sum games")

In two-player [zero-sum games](https://en.m.wikipedia.org/wiki/Zero-sum_game "Zero-sum game"), the minimax solution is the same as the [Nash equilibrium](https://en.m.wikipedia.org/wiki/Nash_equilibrium "Nash equilibrium").

In the context of zero-sum games, the [minimax theorem](https://en.m.wikipedia.org/wiki/Minimax_theorem "Minimax theorem") is equivalent to:<sup id="cite_ref-Osborne_4-0"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-Osborne-4">[4]</a></sup><sup>[<i><a href="https://en.m.wikipedia.org/wiki/Wikipedia:Verifiability" title="Wikipedia:Verifiability"><span title="The material near this tag failed verification of its source citation(s). (February 2015)">failed verification</span></a></i>]</sup>

> For every two-person, [zero-sum](https://en.m.wikipedia.org/wiki/Zero-sum "Zero-sum") game with finitely many strategies, there exists a value V and a mixed strategy for each player, such that
> 
> (a) Given Player 2's strategy, the best payoff possible for Player 1 is V, and
> 
> (b) Given Player 1's strategy, the best payoff possible for Player 2 is −V.

Equivalently, Player 1's strategy guarantees them a payoff of V regardless of Player 2's strategy, and similarly Player 2 can guarantee themselves a payoff of −V. The name _minimax_ arises because each player minimizes the maximum payoff possible for the other – since the game is zero-sum, they also minimize their own maximum loss (i.e., maximize their minimum payoff). See also [example of a game without a value](https://en.m.wikipedia.org/wiki/Example_of_a_game_without_a_value "Example of a game without a value").

### Example [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=4 "Edit section: Example")

<table><caption>Payoff matrix for player A</caption><tbody><tr><th></th><th>B chooses B1</th><th>B chooses B2</th><th>B chooses B3</th></tr><tr><th>A chooses A1</th><td>+3</td><td>−2</td><td>+2</td></tr><tr><th>A chooses A2</th><td>−1</td><td>0</td><td>+4</td></tr><tr><th>A chooses A3</th><td>−4</td><td>−3</td><td>+1</td></tr></tbody></table>

The following example of a zero-sum game, where **A** and **B** make simultaneous moves, illustrates _maximin_ solutions. Suppose each player has three choices and consider the [payoff matrix](https://en.m.wikipedia.org/wiki/Payoff_matrix "Payoff matrix") for **A** displayed on the table ("Payoff matrix for player A"). Assume the payoff matrix for **B** is the same matrix with the signs reversed (i.e., if the choices are A1 and B1 then **B** pays 3 to **A**). Then, the maximin choice for **A** is A2 since the worst possible result is then having to pay 1, while the simple maximin choice for **B** is B2 since the worst possible result is then no payment. However, this solution is not stable, since if **B** believes **A** will choose A2 then **B** will choose B1 to gain 1; then if **A** believes **B** will choose B1 then **A** will choose A1 to gain 3; and then **B** will choose B2; and eventually both players will realize the difficulty of making a choice. So a more stable strategy is needed.

Some choices are _dominated_ by others and can be eliminated: **A** will not choose A3 since either A1 or A2 will produce a better result, no matter what **B** chooses; **B** will not choose B3 since some mixtures of B1 and B2 will produce a better result, no matter what **A** chooses.

Player **A** can avoid having to make an expected payment of more than 1/ 3  by choosing A1 with probability 1/ 6  and A2 with probability 5/ 6 : The expected payoff for **A** would be   3 × 1/ 6  − 1 × 5/ 6  = −+1/ 3    in case **B** chose B1 and   −2 × 1/6  + 0 × 5/ 6  = −+1/ 3    in case **B** chose B2. Similarly, **B** can ensure an expected gain of at least 1/ 3 , no matter what **A** chooses, by using a randomized strategy of choosing B1 with probability 1/ 3  and B2 with probability 2/ 3 . These [mixed](https://en.m.wikipedia.org/wiki/Mixed_strategy "Mixed strategy") minimax strategies cannot be improved and are now stable.

### Maximin [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=5 "Edit section: Maximin")

Frequently, in game theory, **maximin** is distinct from minimax. Minimax is used in zero-sum games to denote minimizing the opponent's maximum payoff. In a [zero-sum game](https://en.m.wikipedia.org/wiki/Zero-sum_game "Zero-sum game"), this is identical to minimizing one's own maximum loss, and to maximizing one's own minimum gain.

"Maximin" is a term commonly used for non-zero-sum games to describe the strategy which maximizes one's own minimum payoff. In non-zero-sum games, this is not generally the same as minimizing the opponent's maximum gain, nor the same as the [Nash equilibrium](https://en.m.wikipedia.org/wiki/Nash_equilibrium "Nash equilibrium") strategy.

### In repeated games [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=6 "Edit section: In repeated games")

The minimax values are very important in the theory of [repeated games](https://en.m.wikipedia.org/wiki/Repeated_games "Repeated games"). One of the central theorems in this theory, the [folk theorem](https://en.m.wikipedia.org/wiki/Folk_theorem_(game_theory) "Folk theorem (game theory)"), relies on the minimax values.

## Combinatorial game theory [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=7 "Edit section: Combinatorial game theory")

In [combinatorial game theory](https://en.m.wikipedia.org/wiki/Combinatorial_game_theory "Combinatorial game theory"), there is a minimax algorithm for game solutions.

A **simple** version of the minimax _algorithm_, stated below, deals with games such as [tic-tac-toe](https://en.m.wikipedia.org/wiki/Tic-tac-toe "Tic-tac-toe"), where each player can win, lose, or draw. If player A _can_ win in one move, their best move is that winning move. If player B knows that one move will lead to the situation where player A _can_ win in one move, while another move will lead to the situation where player A can, at best, draw, then player B's best move is the one leading to a draw. Late in the game, it's easy to see what the "best" move is. The minimax algorithm helps find the best move, by working backwards from the end of the game. At each step it assumes that player A is trying to **maximize** the chances of A winning, while on the next turn player B is trying to **minimize** the chances of A winning (i.e., to maximize B's own chances of winning).

### Minimax algorithm with alternate moves [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=8 "Edit section: Minimax algorithm with alternate moves")

A **minimax algorithm**<sup id="cite_ref-5"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-5">[5]</a></sup> is a recursive [algorithm](https://en.m.wikipedia.org/wiki/Algorithm "Algorithm") for choosing the next move in an n-player [game](https://en.m.wikipedia.org/wiki/Game_theory "Game theory"), usually a two-player game. A value is associated with each position or state of the game. This value is computed by means of a [position evaluation function](https://en.m.wikipedia.org/wiki/Evaluation_function "Evaluation function") and it indicates how good it would be for a player to reach that position. The player then makes the move that maximizes the minimum value of the position resulting from the opponent's possible following moves. If it is **A**'s turn to move, **A** gives a value to each of their legal moves.

A possible allocation method consists in assigning a certain win for **A** as +1 and for **B** as −1. This leads to [combinatorial game theory](https://en.m.wikipedia.org/wiki/Combinatorial_game_theory "Combinatorial game theory") as developed by [John H. Conway](https://en.m.wikipedia.org/wiki/John_Horton_Conway "John Horton Conway"). An alternative is using a rule that if the result of a move is an immediate win for **A**, it is assigned positive infinity and if it is an immediate win for **B**, negative infinity. The value to **A** of any other move is the maximum of the values resulting from each of **B**'s possible replies. For this reason, **A** is called the _maximizing player_ and **B** is called the _minimizing player_, hence the name _minimax algorithm_. The above algorithm will assign a value of positive or negative infinity to any position since the value of every position will be the value of some final winning or losing position. Often this is generally only possible at the very end of complicated games such as [chess](https://en.m.wikipedia.org/wiki/Chess "Chess") or [go](https://en.m.wikipedia.org/wiki/Go_(board_game) "Go (board game)"), since it is not computationally feasible to look ahead as far as the completion of the game, except towards the end, and instead, positions are given finite values as estimates of the degree of belief that they will lead to a win for one player or another.

This can be extended if we can supply a [heuristic](https://en.m.wikipedia.org/wiki/Heuristic "Heuristic") evaluation function which gives values to non-final game states without considering all possible following complete sequences. We can then limit the minimax algorithm to look only at a certain number of moves ahead. This number is called the "look-ahead", measured in "[plies](https://en.m.wikipedia.org/wiki/Ply_(chess) "Ply (chess)")". For example, the chess computer [Deep Blue](https://en.m.wikipedia.org/wiki/IBM_Deep_Blue "IBM Deep Blue") (the first one to beat a reigning world champion, [Garry Kasparov](https://en.m.wikipedia.org/wiki/Garry_Kasparov "Garry Kasparov") at that time) looked ahead at least 12 plies, then applied a heuristic evaluation function.<sup id="cite_ref-6"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-6">[6]</a></sup>

The algorithm can be thought of as exploring the [nodes](https://en.m.wikipedia.org/wiki/Node_(computer_science) "Node (computer science)") of a _[game tree](https://en.m.wikipedia.org/wiki/Game_tree "Game tree")_. The _effective [branching factor](https://en.m.wikipedia.org/wiki/Branching_factor "Branching factor")_ of the tree is the average number of [children](https://en.m.wikipedia.org/wiki/Child_node "Child node") of each node (i.e., the average number of legal moves in a position). The number of nodes to be explored usually [increases exponentially](https://en.m.wikipedia.org/wiki/Exponential_growth "Exponential growth") with the number of plies (it is less than exponential if evaluating [forced moves](https://en.m.wikipedia.org/wiki/Forced_move "Forced move") or repeated positions). The number of nodes to be explored for the analysis of a game is therefore approximately the branching factor raised to the power of the number of plies. It is therefore [impractical](https://en.m.wikipedia.org/wiki/Computational_complexity_theory#Intractability "Computational complexity theory") to completely analyze games such as chess using the minimax algorithm.

The performance of the naïve minimax algorithm may be improved dramatically, without affecting the result, by the use of [alpha–beta pruning](https://en.m.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning "Alpha–beta pruning"). Other heuristic pruning methods can also be used, but not all of them are guaranteed to give the same result as the unpruned search.

A naïve minimax algorithm may be trivially modified to additionally return an entire [Principal Variation](https://en.m.wikipedia.org/wiki/Variation_(game_tree)#Principal_variation "Variation (game tree)") along with a minimax score.

### Pseudocode [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=9 "Edit section: Pseudocode")

The [pseudocode](https://en.m.wikipedia.org/wiki/Pseudocode "Pseudocode") for the depth-limited minimax algorithm is given below.

```
<b>function</b> minimax(node, depth, maximizingPlayer) <b>is</b>
    <b>if</b> depth = 0 <b>or</b> node is a terminal node <b>then</b>
        <b>return</b> the heuristic value of node
    <b>if</b> maximizingPlayer <b>then</b>
        value&nbsp;:= −∞
        <b>for each</b> child of node <b>do</b>
            value&nbsp;:= max(value, minimax(child, depth − 1, FALSE))
        <b>return</b> value
    <b>else</b> <i>(* minimizing player *)</i>
        value&nbsp;:= +∞
        <b>for each</b> child of node <b>do</b>
            value&nbsp;:= min(value, minimax(child, depth − 1, TRUE))
        <b>return</b> value
```

```
<i>(* Initial call *)</i>
minimax(origin, depth, TRUE)
```

The minimax function returns a heuristic value for [leaf nodes](https://en.m.wikipedia.org/wiki/Leaf_nodes "Leaf nodes") (terminal nodes and nodes at the maximum search depth). Non-leaf nodes inherit their value from a descendant leaf node. The heuristic value is a score measuring the favorability of the node for the maximizing player. Hence nodes resulting in a favorable outcome, such as a win, for the maximizing player have higher scores than nodes more favorable for the minimizing player. The heuristic value for terminal (game ending) leaf nodes are scores corresponding to win, loss, or draw, for the maximizing player. For non terminal leaf nodes at the maximum search depth, an evaluation function estimates a heuristic value for the node. The quality of this estimate and the search depth determine the quality and accuracy of the final minimax result.

Minimax treats the two players (the maximizing player and the minimizing player) separately in its code. Based on the observation that   minimax may often be simplified into the [negamax](https://en.m.wikipedia.org/wiki/Negamax "Negamax") algorithm.

### Example [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=10 "Edit section: Example")

 [](https://en.m.wikipedia.org/wiki/File:Minimax.svg)

A minimax tree example

 [](https://en.m.wikipedia.org/wiki/File:Plminmax.gif)

An animated pedagogical example that attempts to be human-friendly by substituting initial infinite (or arbitrarily large) values for emptiness and by avoiding using the [negamax](https://en.m.wikipedia.org/wiki/Negamax "Negamax") coding simplifications.

Suppose the game being played only has a maximum of two possible moves per player each turn. The algorithm generates the [tree](https://en.m.wikipedia.org/wiki/Game_tree "Game tree") on the right, where the circles represent the moves of the player running the algorithm (_maximizing player_), and squares represent the moves of the opponent (_minimizing player_). Because of the limitation of computation resources, as explained above, the tree is limited to a _look-ahead_ of 4 moves.

The algorithm evaluates each _[leaf node](https://en.m.wikipedia.org/wiki/Leaf_node "Leaf node")_ using a heuristic evaluation function, obtaining the values shown. The moves where the _maximizing player_ wins are assigned with positive infinity, while the moves that lead to a win of the _minimizing player_ are assigned with negative infinity. At level 3, the algorithm will choose, for each node, the **smallest** of the _[child node](https://en.m.wikipedia.org/wiki/Child_node "Child node")_ values, and assign it to that same node (e.g. the node on the left will choose the minimum between "10" and "+∞", therefore assigning the value "10" to itself). The next step, in level 2, consists of choosing for each node the **largest** of the _child node_ values. Once again, the values are assigned to each _[parent node](https://en.m.wikipedia.org/wiki/Parent_node "Parent node")_. The algorithm continues evaluating the maximum and minimum values of the child nodes alternately until it reaches the _[root node](https://en.m.wikipedia.org/wiki/Root_node "Root node")_, where it chooses the move with the largest value (represented in the figure with a blue arrow). This is the move that the player should make in order to _minimize_ the _maximum_ possible [loss](https://en.m.wikipedia.org/wiki/Loss_function "Loss function").

## Minimax for individual decisions [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=11 "Edit section: Minimax for individual decisions")

### Minimax in the face of uncertainty [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=12 "Edit section: Minimax in the face of uncertainty")

Minimax theory has been extended to decisions where there is no other player, but where the consequences of decisions depend on unknown facts. For example, deciding to prospect for minerals entails a cost, which will be wasted if the minerals are not present, but will bring major rewards if they are. One approach is to treat this as a game against _nature_ (see [move by nature](https://en.m.wikipedia.org/wiki/Move_by_nature "Move by nature")), and using a similar mindset as [Murphy's law](https://en.m.wikipedia.org/wiki/Murphy%27s_law "Murphy's law") or [resistentialism](https://en.m.wikipedia.org/wiki/Resistentialism "Resistentialism"), take an approach which minimizes the maximum expected loss, using the same techniques as in the two-person zero-sum games.

In addition, [expectiminimax trees](https://en.m.wikipedia.org/wiki/Expectiminimax_tree "Expectiminimax tree") have been developed, for two-player games in which chance (for example, dice) is a factor.

### Minimax criterion in statistical decision theory [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=13 "Edit section: Minimax criterion in statistical decision theory")

In classical statistical [decision theory](https://en.m.wikipedia.org/wiki/Decision_theory "Decision theory"), we have an [estimator](https://en.m.wikipedia.org/wiki/Estimator "Estimator")   that is used to estimate a [parameter](https://en.m.wikipedia.org/wiki/Parameter "Parameter")   We also assume a [risk function](https://en.m.wikipedia.org/wiki/Risk_function "Risk function")   usually specified as the integral of a [loss function](https://en.m.wikipedia.org/wiki/Loss_function "Loss function"). In this framework,   is called **minimax** if it satisfies

An alternative criterion in the decision theoretic framework is the [Bayes estimator](https://en.m.wikipedia.org/wiki/Bayes_estimator "Bayes estimator") in the presence of a [prior distribution](https://en.m.wikipedia.org/wiki/Prior_distribution "Prior distribution")   An estimator is Bayes if it minimizes the _[average](https://en.m.wikipedia.org/wiki/Average "Average")_ risk

### Non-probabilistic decision theory [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=14 "Edit section: Non-probabilistic decision theory")

A key feature of minimax decision making is being non-probabilistic: in contrast to decisions using [expected value](https://en.m.wikipedia.org/wiki/Expected_value "Expected value") or [expected utility](https://en.m.wikipedia.org/wiki/Expected_utility "Expected utility"), it makes no assumptions about the probabilities of various outcomes, just [scenario analysis](https://en.m.wikipedia.org/wiki/Scenario_analysis "Scenario analysis") of what the possible outcomes are. It is thus [robust](https://en.wiktionary.org/wiki/robust "wikt:robust") to changes in the assumptions, in contrast to these other decision techniques. Various extensions of this non-probabilistic approach exist, notably [minimax regret](https://en.m.wikipedia.org/wiki/Minimax_regret "Minimax regret") and [Info-gap decision theory](https://en.m.wikipedia.org/wiki/Info-gap_decision_theory "Info-gap decision theory").

Further, minimax only requires [ordinal measurement](https://en.m.wikipedia.org/wiki/Ordinal_measurement "Ordinal measurement") (that outcomes be compared and ranked), not _interval_ measurements (that outcomes include "how much better or worse"), and returns ordinal data, using only the modeled outcomes: the conclusion of a minimax analysis is: "this strategy is minimax, as the worst case is (outcome), which is less bad than any other strategy". Compare to expected value analysis, whose conclusion is of the form: "This strategy yields ℰ(X) = n ." Minimax thus can be used on ordinal data, and can be more transparent.

## Minimax in politics [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=15 "Edit section: Minimax in politics")

The concept of "[lesser evil](https://en.m.wikipedia.org/wiki/Lesser_evil "Lesser evil")" voting (LEV) can be seen as a form of the minimax strategy where voters, when faced with two or more candidates, choose the one they perceive as the least harmful or the "lesser evil." To do so, "voting should not be viewed as a form of personal self-expression or moral judgement directed in retaliation towards major party candidates who fail to reflect our values, or of a corrupt system designed to limit choices to those acceptable to corporate elites," but rather as an opportunity to reduce harm or loss.<sup id="cite_ref-7"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-7">[7]</a></sup>

## Maximin in philosophy [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=16 "Edit section: Maximin in philosophy")

In philosophy, the term "maximin" is often used in the context of [John Rawls](https://en.m.wikipedia.org/wiki/John_Rawls "John Rawls")'s _[A Theory of Justice](https://en.m.wikipedia.org/wiki/A_Theory_of_Justice "A Theory of Justice"),_ where he refers to it in the context of The [Difference Principle](https://en.m.wikipedia.org/wiki/Difference_Principle "Difference Principle").<sup id="cite_ref-Rawls-1971_8-0"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-Rawls-1971-8">[8]</a></sup> Rawls defined this principle as the rule which states that social and economic inequalities should be arranged so that "they are to be of the greatest benefit to the least-advantaged members of society".<sup id="cite_ref-9"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-9">[9]</a></sup><sup id="cite_ref-10"><a href="https://en.m.wikipedia.org/wiki/Minimax#cite_note-10">[10]</a></sup>

## See also [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=17 "Edit section: See also")

-   [Alpha–beta pruning](https://en.m.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning "Alpha–beta pruning")
-   [Expectiminimax](https://en.m.wikipedia.org/wiki/Expectiminimax "Expectiminimax")
-   [Computer chess](https://en.m.wikipedia.org/wiki/Computer_chess "Computer chess")
-   [Horizon effect](https://en.m.wikipedia.org/wiki/Horizon_effect "Horizon effect")
-   [Lesser of two evils principle](https://en.m.wikipedia.org/wiki/Lesser_of_two_evils_principle "Lesser of two evils principle")
-   [Minimax Condorcet](https://en.m.wikipedia.org/wiki/Minimax_Condorcet "Minimax Condorcet")
-   [Minimax regret](https://en.m.wikipedia.org/wiki/Regret_(decision_theory)#Minimax_regret "Regret (decision theory)")
-   [Monte Carlo tree search](https://en.m.wikipedia.org/wiki/Monte_Carlo_tree_search "Monte Carlo tree search")
-   [Negamax](https://en.m.wikipedia.org/wiki/Negamax "Negamax")
-   [Negascout](https://en.m.wikipedia.org/wiki/Negascout "Negascout")
-   [Sion's minimax theorem](https://en.m.wikipedia.org/wiki/Sion%27s_minimax_theorem "Sion's minimax theorem")
-   [Tit for Tat](https://en.m.wikipedia.org/wiki/Tit_for_Tat "Tit for Tat")
-   [Transposition table](https://en.m.wikipedia.org/wiki/Transposition_table "Transposition table")
-   [Wald's maximin model](https://en.m.wikipedia.org/wiki/Wald%27s_maximin_model "Wald's maximin model")

## References [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=18 "Edit section: References")

1.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-1 "Jump up")** Bacchus, Barua (January 2013). [Provincial Healthcare Index 2013](http://www.fraserinstitute.org/uploadedFiles/fraser-ca/Content/research-news/research/publications/provincial-healthcare-index-2013.pdf) (PDF) (Report). Fraser Institute. p. 25.
2.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-2 "Jump up")** Professor Raymond Flood. [_Turing and von Neumann_](https://www.youtube.com/watch?v=fJltiCjPeMA&t=12m0s) (video). [Gresham College](https://en.m.wikipedia.org/wiki/Gresham_College "Gresham College") – via [YouTube](https://en.m.wikipedia.org/wiki/YouTube "YouTube").
3.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-ZMS2013_3-0) [<sup><i><b>b</b></i></sup>](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-ZMS2013_3-1) Maschler, Michael; [Solan, Eilon](https://en.m.wikipedia.org/wiki/Eilon_Solan "Eilon Solan"); Zamir, Shmuel (2013). _Game Theory_. [Cambridge University Press](https://en.m.wikipedia.org/wiki/Cambridge_University_Press "Cambridge University Press"). pp. 176–180. [ISBN](https://en.m.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [9781107005488](https://en.m.wikipedia.org/wiki/Special:BookSources/9781107005488 "Special:BookSources/9781107005488").
4.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-Osborne_4-0 "Jump up")** Osborne, Martin J.; [Rubinstein, A.](https://en.m.wikipedia.org/wiki/Ariel_Rubinstein "Ariel Rubinstein") (1994). _A Course in Game Theory_ (print ed.). Cambridge, MA: MIT Press. [ISBN](https://en.m.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [9780262150415](https://en.m.wikipedia.org/wiki/Special:BookSources/9780262150415 "Special:BookSources/9780262150415").
5.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-5 "Jump up")** [Russell, Stuart J.](https://en.m.wikipedia.org/wiki/Stuart_J._Russell "Stuart J. Russell"); [Norvig, Peter.](https://en.m.wikipedia.org/wiki/Peter_Norvig "Peter Norvig") (2021). _[Artificial Intelligence: A Modern Approach](https://en.m.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach "Artificial Intelligence: A Modern Approach")_ (4th ed.). Hoboken: Pearson. pp. 149–150. [ISBN](https://en.m.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [9780134610993](https://en.m.wikipedia.org/wiki/Special:BookSources/9780134610993 "Special:BookSources/9780134610993"). [LCCN](https://en.m.wikipedia.org/wiki/LCCN_(identifier) "LCCN (identifier)") [20190474](https://lccn.loc.gov/20190474).
6.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-6 "Jump up")** Hsu, Feng-Hsiung (1999). "IBM's Deep Blue chess grandmaster chips". _IEEE Micro_. **19** (2). Los Alamitos, CA, USA: IEEE Computer Society: 70–81. [doi](https://en.m.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/40.755469](https://doi.org/10.1109%2F40.755469). During the 1997 match, the software search extended the search to about 40 plies along the forcing lines, even though the non-extended search reached only about 12 plies.
7.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-7 "Jump up")** [Noam Chomsky](https://en.m.wikipedia.org/wiki/Noam_Chomsky "Noam Chomsky") and John Halle, "[An Eight Point Brief for LEV (Lesser Evil Voting)](https://newpol.org/eight-point-brief-lev-lesser-evil-voting/)," _[New Politics](https://newpol.org/about/),_ June 15, 2016.
8.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-Rawls-1971_8-0 "Jump up")** [Rawls, J.](https://en.m.wikipedia.org/wiki/John_Rawls "John Rawls") (1971). [_A Theory of Justice_](https://en.m.wikipedia.org/wiki/A_Theory_of_Justice "A Theory of Justice"). p. 152.
9.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-9 "Jump up")** [Arrow, K.](https://en.m.wikipedia.org/wiki/Kenneth_Arrow "Kenneth Arrow") (May 1973). ["Some ordinalist-utilitarian notes on Rawls's _Theory of Justice_"](https://www.pdcnet.org/jphil/content/jphil_1973_0070_0009_0245_0263). _Journal of Philosophy_. **70** (9): 245–263. [doi](https://en.m.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.2307/2025006](https://doi.org/10.2307%2F2025006). [JSTOR](https://en.m.wikipedia.org/wiki/JSTOR_(identifier) "JSTOR (identifier)") [2025006](https://www.jstor.org/stable/2025006).
10.  **[^](https://en.m.wikipedia.org/wiki/Minimax#cite_ref-10 "Jump up")** [Harsanyi, J.](https://en.m.wikipedia.org/wiki/John_Harsanyi "John Harsanyi") (June 1975). ["Can the maximin principle serve as a basis for morality? a critique of John Rawls's theory"](http://piketty.pse.ens.fr/files/Harsanyi1975.pdf) (PDF). _American Political Science Review_. **69** (2): 594–606. [doi](https://en.m.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.2307/1959090](https://doi.org/10.2307%2F1959090). [JSTOR](https://en.m.wikipedia.org/wiki/JSTOR_(identifier) "JSTOR (identifier)") [1959090](https://www.jstor.org/stable/1959090). [S2CID](https://en.m.wikipedia.org/wiki/S2CID_(identifier) "S2CID (identifier)") [118261543](https://api.semanticscholar.org/CorpusID:118261543).

## External links [edit](https://en.m.wikipedia.org/w/index.php?title=Minimax&action=edit&section=19 "Edit section: External links")

Look up _**[minimax](https://en.wiktionary.org/wiki/Special:Search/minimax "wiktionary:Special:Search/minimax")**_ in Wiktionary, the free dictionary.

Wikiquote has quotations related to _**[Minimax](https://en.wikiquote.org/wiki/Special:Search/Minimax "q:Special:Search/Minimax")**_.

-   ["Minimax principle"](https://www.encyclopediaofmath.org/index.php?title=Minimax_principle), _[Encyclopedia of Mathematics](https://en.m.wikipedia.org/wiki/Encyclopedia_of_Mathematics "Encyclopedia of Mathematics")_, [EMS Press](https://en.m.wikipedia.org/wiki/European_Mathematical_Society "European Mathematical Society"), 2001 \[1994\]
-   ["Mixed strategies"](http://www.cut-the-knot.org/Curriculum/Games/MixedStrategies.shtml). _cut-the-knot.org_. Curriculum: Games. — A visualization applet
-   ["Maximin principle"](https://web.archive.org/web/20060307183023/http://www.swif.uniba.it/lei/foldop/foldoc.cgi?maximin+principle). _Dictionary of Philosophical Terms and Names_. Archived from [the original](http://www.swif.uniba.it/lei/foldop/foldoc.cgi?maximin+principle) on 2006-03-07.
-   ["Minimax"](https://xlinux.nist.gov/dads/HTML/minimax.html). _[Dictionary of Algorithms and Data Structures](https://en.m.wikipedia.org/wiki/Dictionary_of_Algorithms_and_Data_Structures "Dictionary of Algorithms and Data Structures")_. US [NIST](https://en.m.wikipedia.org/wiki/NIST "NIST").
