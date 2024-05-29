---
source: electowiki.org
url: https://electowiki.org/wiki/COWPEA
---

**COWPEA (Candidates Optimally Weighted in Proportional Election using Approval voting)** is a method of [proportional representation](https://electowiki.org/wiki/Proportional_representation "Proportional representation") that uses [approval voting](https://electowiki.org/wiki/Approval_voting "Approval voting") and gives elected candidates differing weights in parliament or the body into which they are elected. It was first proposed in 2016 by [Toby Pereira](https://electowiki.org/wiki/Toby_Pereira "Toby Pereira")<sup id="cite_ref-1"><a href="https://electowiki.org/wiki/COWPEA#cite_note-1">[1]</a></sup> and was written up as a paper in 2023.<sup id="cite_ref-2"><a href="https://electowiki.org/wiki/COWPEA#cite_note-2">[2]</a></sup> It also works on the same principle as the random-ballot tie-break procedure for [score voting](https://electowiki.org/wiki/Score_voting "Score voting").<sup id="cite_ref-3"><a href="https://electowiki.org/wiki/COWPEA#cite_note-3">[3]</a></sup>

The weight each candidate gets in parliament is the same as the probability that they would be elected in the following lottery:

> Start with a list of all candidates. Pick a ballot at random and remove from the list all candidates not approved on this ballot. Pick another ballot at random, and continue with this process until one candidate is left. Elect this candidate. If the number of candidates ever goes from >1 to 0 in one go, ignore that ballot and continue. If any tie cannot be broken, then elect the tied candidates with equal probability.

COWPEA can also be used to calculate the proportion of seats to be allocated to each party in an approval-based [party-list](https://electowiki.org/wiki/Party-list_proportional_representation "Party-list proportional representation") proportional election, or the candidate "assets" in [Asset voting](https://electowiki.org/wiki/Asset_voting "Asset voting"). It can be used with the [Kotze-Pereira transformation](https://electowiki.org/wiki/Kotze-Pereira_transformation "Kotze-Pereira transformation") for a [score voting](https://electowiki.org/wiki/Score_Voting "Score Voting") variant.

COWPEA is strongly [monotonic](https://electowiki.org/wiki/Monotonicity "Monotonicity") and passes [Independence of Irrelevant Ballots](https://electowiki.org/wiki/Independence_of_Irrelevant_Ballots "Independence of Irrelevant Ballots") (IIB). The [universally liked candidate criterion](https://electowiki.org/wiki/Universally_liked_candidate_criterion "Universally liked candidate criterion") (ULC) is inapplicable since such a candidate would take all the power within the parliament.

The idea behind COWPEA is that if a voter has approved more than one candidate, then the candidates approved on that ballot would be weighted not equally but in a proportional manner according to the rest of the electorate, with all ballots considered. COWPEA is also not simply an election method but an attempt at an answer to the question: How do we determine the mathematically optimal candidate weights in a proportional election?

### COWPEA Lottery

The COWPEA Lottery method, which elects candidates according to the above lottery individually and with equal weight, passes strong monotonicity, IIB and ULC. Achieving all three of these together is very rare and seen as a prerequisite for a "Holy Grail" method for a proportional approval or score method. However, these are achieved at the cost of determinism.

The following lottery is done k times to elect k candidates:

> Start with a list of all currently-unelected candidates. Pick a ballot at random and remove from the list all candidates not approved on this ballot. Pick another ballot at random, and continue with this process until one candidate is left. Elect this candidate. If the number of candidates ever goes from >1 to 0 in one go, ignore that ballot and continue. If any tie cannot be broken, then elect the tied candidates with equal probability.

COWPEA Lottery can be used with the [Kotze-Pereira transformation](https://electowiki.org/wiki/Kotze-Pereira_transformation "Kotze-Pereira transformation") for a [score voting](https://electowiki.org/wiki/Score_Voting "Score Voting") variant. Alternatively, scores or grades can be used as layers of approval. For the first ballot picked in each iteration of the lottery, only the highest rated so-far unelected candidate(s) would remain in the lottery. For each subsequent ballot picked, the highest rated eligible candidate(s) on this ballot would remain.

1.  [↑](https://electowiki.org/wiki/COWPEA#cite_ref-1 "Jump up") ["Proportional approval system based on random ballots"](https://groups.google.com/g/electionscience/c/5skD8rTZ82k/m/twtzkcPBBQAJ). _groups.google.com_. Retrieved 2021-10-20.
2.  [↑](https://electowiki.org/wiki/COWPEA#cite_ref-2 "Jump up") Pereira, Toby (2023-05-17). ["COWPEA (Candidates Optimally Weighted in Proportional Election using Approval voting)"](https://arxiv.org/abs/2305.08857). _arXiv_.
3.  [↑](https://electowiki.org/wiki/COWPEA#cite_ref-3 "Jump up") ["RangeVoting.org - Tie breaking methods"](https://rangevoting.org/TieBreakIdeas.html). _rangevoting.org_. Retrieved 2021-10-20.
