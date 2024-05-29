---
source: www.classes.cs.uchicago.edu
url: https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node6.html
---

[![next](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/next_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node7.html) [![up](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/up_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/project_98.html) [![previous](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/previous_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node5.html)  
**Next:** [Extra Credit: The Three-Player](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node7.html) **Up:** [No Title](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/project_98.html) **Previous:** [The Two-Player Prisoner's Dilemma](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node5.html) **Subsections**

-   [Problem 5](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node6.html#SECTION00060010000000000000)
-   [Problem 6](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node6.html#SECTION00060020000000000000)
-   [Problem 7](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node6.html#SECTION00060030000000000000)
-   [Problem 8](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node6.html#SECTION00060040000000000000)

---

So far, all of our prisoner's dilemma examples have involved two players (and, indeed, most game-theory research on the prisoner's dilemma has focused on two-player games). But it is possible to create a prisoner's dilemma game involving three--or even more--players.

Strategies from the two-player game do not necessarily extend to a three-person game in a natural way. For example, what does tit-for-tat mean? Should the player defect if _either_ of the opponents defected on the previous round? Or only if _both_ opponents defected? And are either of these strategies nearly as effective in the three-player game as tit-for-tat is in the two-player game?

Before we analyze the three-player game more closely, we must introduce some notation for representing the payoffs. We use a notation similar to that used for the two-player game. For example, we let DCC represent the payoff to a defecting player if both opponents cooperate. Note that the first position represents the player under consideration. The second and third positions represent the opponents.

Another example: CCD represents the payoff to a cooperating player if one opponent cooperates and the other opponent defects. Since we assume a symmetric game matrix, CCD could be written as CDC. The choice is arbitrary.

Now we are ready to discuss the payoffs for the three-player game. We impose three rules:[<sup>3</sup>](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/footnode.html#foot177)

1) Defection should be the dominant choice for each player. In other words, it should always better for a player to defect, regardless what the opponents do. This rule gives three constraints:

<table><tbody><tr><td><em>DCC &gt; CCC</em></td><td>(both opponents cooperate)</td></tr><tr><td><em>DDD &gt; CDD</em></td><td>(both opponents defect)</td></tr><tr><td><em>DCD &gt; CCD</em></td><td>(one opponent cooperates, one defects)</td></tr></tbody></table>

2) A player should always be better off if more of his opponents choose to cooperate. This rule gives:

<table><tbody><tr><td><em>DCC &gt; DCD &gt; DDD</em></td></tr><tr><td><em>CCC &gt; CCD &gt; CDD</em></td></tr></tbody></table>

3) If one player's choice is fixed, the other two players should be left in a two-player prisoner's dilemma. This rule gives the following constraints:

<table><tbody><tr><td><em>CCD &gt; DDD</em></td></tr><tr><td><em>CCC &gt; DCD</em></td></tr><tr><td><em>CCD &gt; (CDD + DCD) / 2</em></td></tr><tr><td><em>CCC &gt; (CCD + DCC) / 2</em></td></tr></tbody></table>

  

<table><tbody><tr><td><em>CDD = 0</em></td></tr><tr><td><em>DDD = 1</em></td></tr><tr><td><em>CCD = 3</em></td></tr><tr><td><em>DCD = 5</em></td></tr><tr><td><em>CCC = 7</em></td></tr><tr><td><em>DCC = 9</em></td></tr></tbody></table>

#### Problem 5

Revise the Scheme code for the two-player game to make a three-player iterated game. The program should take three strategies as input, keep track of three histories, and print out results for three players. You need to change only three procedures: play-loop, print-out-results, and get-scores. Give your revised procedures the new names play3-loop, print-out-results3, and get-scores3 You also need to replace \*game-association-list\* by \*game3-association-list\* as follows:

```
(define *game3-association-list*
  '(((c c c) (7 7 7))
    ((c c d) (3 3 9))
    ((c d c) (3 9 3))
    ((d c c) (9 3 3))
    ((c d d) (0 5 5))
    ((d c d) (5 0 5))
    ((d d c) (5 5 0))
    ((d d d) (1 1 1))))
```

#### Problem 6

_a._ Write strategies poor-trusting-fool-3, all-defect-3, and random-strategy-3 that will work in a three-player game. Try them out to make sure your game-supervision code is working.

_b._ Write two new strategies: tough-tit-for-tat and soft-tit-for-tat. tough-tit-for-tat should defect if _either_ of the opponents defected on the previous round. soft-tit-for-tat should defect only if _both_ opponents defected on the previous round. Play some games using these two new strategies.

#### Problem 7

A natural idea in creating a prisoner's dilemma strategy is to try and deduce what kind of strategies the _other_ players might be using. In this problem, we will implement a simple version of this idea.

First, we need a procedure that takes three histories as arguments: call them hist-0, hist-1, and hist-2. The idea is that we wish to characterize the strategy of the player responsible for hist-0. Our procedure will return a list of three numbers: the probability that the hist-0 player cooperates given that the other two players cooperated on the previous round, the probability that the hist-0 player cooperates given that only one other player cooperated on the previous round, and the probability that the hist-0 player cooperates given that both others defected on the previous round. To fill out some details in this picture, let's look at a couple of examples. We will call our procedure get-probability-of-c; here are a couple of sample calls.

```
&gt; (get-probability-of-c '(c c c c) '(d d d c) '(d d c c))
(1 1 1)

&gt; (get-probability-of-c '(c c c d c) '(d c d d c) '(d c c c c))
(0.5 1 ())
```

In the top example, the returned list indicates that the first player cooperates with probability 1 no matter what the other two players do. In the bottom example, the first player cooperates with probability 0.5 when the other two players cooperate; the first player cooperates with probability 1 when one of the other two players defects; and since we have no data regarding what happens when both other players defect, our procedure returns () for that case.

Write the get-probability-of-c procedure. Using this procedure, you should be able to write some predicate procedures that help in deciphering another player's strategy. For instance, here are two possibilities:

```
(define (is-he-a-fool? hist0 hist1 hist2)
  (equal? '(1 1 1) (get-probability-of-c hist0 hist1 hist2)))

(define (could-he-be-a-fool? hist0 hist1 hist2)
  (equal? (list true true true)
          (map (lambda (elt) (or (null? elt) (= elt 1)))
               (get-probability-of-c hist0 hist1 hist2))))
```

Use the get-probability-of-c procedure to write a predicate that tests whether another player is using the soft-tit-for-tat strategy from Problem 7. Also, write a new strategy named dont-tolerate-fools. This strategy should cooperate for the first ten rounds; on subsequent rounds it checks (on each round) to see whether the other players might both be playing poor-trusting-fool. If our strategy finds that both other players seem to be cooperating uniformly, it defects; otherwise, it cooperates.

#### Problem 8

Write a procedure make-combined-strategies which takes as input two _two-player_ strategies and a \`\`combining'' procedure. Make-combined-strategies should return a _three-player_ strategy that plays one of the two-player strategies against one of the opponents, and the other two-player strategy against the other opponent, then calls the \`\`combining'' procedure on the two two-player results. Here's an example: this call to make-combined-strategies returns a strategy equivalent to tough-tit-for-tat in Problem 7.

```
(make-combined-strategies
  tit-for-tat tit-for-tat
  (lambda (r1 r2) (if (or (equal? r1 'd) (equal? r2 'd)) 'd 'c)))
```

The resulting strategy plays tit-for-tat against each opponent, and then calls the combining procedure on the two results. If either of the two two-player strategies has returned d, then the three-player strategy will also return d.

Here's another example. This call to make-combined-strategies returns a three-player strategy that plays tit-for-tat against one opponent, go-by-majority against another, and chooses randomly between the two results:

```
(make-combined-strategies
  tit-for-tat go-by-majority
  (lambda (r1 r2) (if (= (random 2) 0) r1 r2)))
```

---

[![next](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/next_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node7.html) [![up](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/up_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/project_98.html) [![previous](https://www.classes.cs.uchicago.edu/usr/lib/latex2html/icons.gif/previous_motif.gif)](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node5.html)  
**Next:** [Extra Credit: The Three-Player](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node7.html) **Up:** [No Title](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/project_98.html) **Previous:** [The Two-Player Prisoner's Dilemma](https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node5.html)

_Michael J. O'Donnell_  
_1998-11-22_
