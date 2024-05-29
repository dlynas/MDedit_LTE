---
source: en.m.wikipedia.org
url: https://en.m.wikipedia.org/wiki/Ranked_pairs
---

**Ranked pairs** (or **RP**), sometimes called the **Tideman method**, is a [tournament-style](https://en.m.wikipedia.org/wiki/Round-robin_voting "Round-robin voting") system of [ranked-choice voting](https://en.m.wikipedia.org/wiki/Ranked_voting "Ranked voting") first proposed by [Nicolaus Tideman](https://en.m.wikipedia.org/wiki/Nicolaus_Tideman "Nicolaus Tideman") in 1987.<sup id="cite_ref-Tideman2_1-0"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-Tideman2-1">[1]</a></sup><sup id="cite_ref-2"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-2">[2]</a></sup>

Ranked pairs begins with a [round-robin tournament](https://en.m.wikipedia.org/wiki/Round-robin_tournament "Round-robin tournament"), where the one-on-one margins of victory for each candidate are compared to find a [majority winner](https://en.m.wikipedia.org/wiki/Condorcet_winner_criterion "Condorcet winner criterion"). If there is a [Condorcet cycle](https://en.m.wikipedia.org/wiki/Condorcet_paradox "Condorcet paradox") (a rock-paper-scissors sequence **A** > B > C > **A**), the cycle is broken by dropping nearly-tied elections, i.e. the closest elections in the cycle.<sup id="cite_ref-3"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-3">[3]</a></sup>

## Procedure [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=1 "Edit section: Procedure")

The ranked pairs procedure is as follows:

1.  Consider each pair of candidates round-robin style and [calculate the pairwise margin](https://en.m.wikipedia.org/wiki/Pairwise_counting "Pairwise counting") for each in a one-on-one matchup.
2.  Sort the pairs by the ([absolute](https://en.m.wikipedia.org/wiki/Absolute_value "Absolute value")) margin of victory, going from largest to smallest.
3.  Going down the list, check whether adding each matchup would create a [cycle](https://en.m.wikipedia.org/wiki/Condorcet_cycle "Condorcet cycle"). If it would, [cross out](https://en.m.wikipedia.org/wiki/Cross_out "Cross out") the election; this will be the election(s) in the cycle with the smallest margin of victory (near-ties).<sup id="cite_ref-4"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-4">[note 1]</a></sup>

At the end of this procedure, all cycles will be eliminated, leaving a unique winner who wins every one-on-one matchup (that has not been crossed out). The lack of cycles means that candidates can be ranked linearly based on the matchups that have been left behind.

## Example [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=2 "Edit section: Example")

### The situation [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=3 "Edit section: The situation")

-   [v](https://en.m.wikipedia.org/wiki/Template:Tenn_voting_example "Template:Tenn voting example")
-   [t](https://en.m.wikipedia.org/wiki/Template_talk:Tenn_voting_example "Template talk:Tenn voting example")
-   [e](https://en.m.wikipedia.org/wiki/Special:EditPage/Template:Tenn_voting_example "Special:EditPage/Template:Tenn voting example")

[![Tennessee and its four major cities: Memphis in the far west; Nashville in the center; Chattanooga in the east; and Knoxville in the far northeast](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Tennessee_map_for_voting_example.svg/500px-Tennessee_map_for_voting_example.svg.png)](https://en.m.wikipedia.org/wiki/File:Tennessee_map_for_voting_example.svg)

Suppose that [Tennessee](https://en.m.wikipedia.org/wiki/Tennessee "Tennessee") is holding an election on the location of its [capital](https://en.m.wikipedia.org/wiki/Capital_(political) "Capital (political)"). The population is concentrated around four major cities. [All voters want the capital to be as close to them as possible.](https://en.m.wikipedia.org/wiki/Spatial_model_of_voting "Spatial model of voting") The options are:

-   [Memphis](https://en.m.wikipedia.org/wiki/Memphis,_Tennessee "Memphis, Tennessee"), the largest city, but far from the others (42% of voters)
-   [Nashville](https://en.m.wikipedia.org/wiki/Nashville,_Tennessee "Nashville, Tennessee"), near the center of the state (26% of voters)
-   [Chattanooga](https://en.m.wikipedia.org/wiki/Chattanooga,_Tennessee "Chattanooga, Tennessee"), somewhat east (15% of voters)
-   [Knoxville](https://en.m.wikipedia.org/wiki/Knoxville,_Tennessee "Knoxville, Tennessee"), far to the northeast (17% of voters)

The preferences of each region's voters are:

| 42% of voters  
<small>Far-West</small> | 26% of voters  
<small>Center</small> | 15% of voters  
<small>Center-East</small> | 17% of voters  
<small>Far-East</small> |
| --- | --- | --- | --- |
| 
1.  **Memphis**
2.  Nashville
3.  Chattanooga
4.  Knoxville

 | 

1.  **Nashville**
2.  Chattanooga
3.  Knoxville
4.  Memphis

 | 

1.  **Chattanooga**
2.  Knoxville
3.  Nashville
4.  Memphis

 | 

1.  **Knoxville**
2.  Chattanooga
3.  Nashville
4.  Memphis

 |

  
The results are tabulated as follows:

<table><caption>Pairwise election results</caption><tbody><tr><td><p>A</p><p>B</p></td><td><b>Memphis</b></td><td><b>Nashville</b></td><td><b>Chattanooga</b></td><td><b>Knoxville</b></td></tr><tr><td><b>Memphis</b></td><td></td><td>[A] 58%<p>[B] 42%</p></td><td>[A] 58%<p>[B] 42%</p></td><td>[A] 58%<p>[B] 42%</p></td></tr><tr><td><b>Nashville</b></td><td>[A] 42%<p>[B] 58%</p></td><td></td><td>[A] 32%<p>[B] 68%</p></td><td>[A] 32%<p>[B] 68%</p></td></tr><tr><td><b>Chattanooga</b></td><td>[A] 42%<p>[B] 58%</p></td><td>[A] 68%<p>[B] 32%</p></td><td></td><td>[A] 17%<p>[B] 83%</p></td></tr><tr><td><b>Knoxville</b></td><td>[A] 42%<p>[B] 58%</p></td><td>[A] 68%<p>[B] 32%</p></td><td>[A] 83%<p>[B] 17%</p></td><td></td></tr></tbody></table>

-   \[A\] indicates voters who preferred the candidate listed in the column caption to the candidate listed in the row caption
-   \[B\] indicates voters who preferred the candidate listed in the row caption to the candidate listed in the column caption

### Tally [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=4 "Edit section: Tally")

First, list every pair, and determine the winner:

| Pair | Winner |
| --- | --- |
| Memphis (42%) vs. Nashville (58%) | Nashville 58% |
| Memphis (42%) vs. Chattanooga (58%) | Chattanooga 58% |
| Memphis (42%) vs. Knoxville (58%) | Knoxville 58% |
| Nashville (68%) vs. Chattanooga (32%) | Nashville 68% |
| Nashville (68%) vs. Knoxville (32%) | Nashville 68% |
| Chattanooga (83%) vs. Knoxville (17%) | Chattanooga: 83% |

The votes are then sorted. The largest majority is "Chattanooga over Knoxville"; 83% of the voters prefer Chattanooga. Thus, the pairs from above would be sorted this way:

| Pair | Winner |
| --- | --- |
| Chattanooga (83%) vs. Knoxville (17%) | Chattanooga 83% |
| Nashville (68%) vs. Knoxville (32%) | Nashville 68% |
| Nashville (68%) vs. Chattanooga (32%) | Nashville 68% |
| Memphis (42%) vs. Nashville (58%) | Nashville 58% |
| Memphis (42%) vs. Chattanooga (58%) | Chattanooga 58% |
| Memphis (42%) vs. Knoxville (58%) | Knoxville 58% |

### Lock [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=5 "Edit section: Lock")

The pairs are then locked in order, skipping any pairs that would create a cycle:

-   Lock Chattanooga over Knoxville.
-   Lock Nashville over Knoxville.
-   Lock Nashville over Chattanooga.
-   Lock Nashville over Memphis.
-   Lock Chattanooga over Memphis.
-   Lock Knoxville over Memphis.

In this case, no cycles are created by any of the pairs, so every single one is locked in.

Every "lock in" would add another arrow to the graph showing the relationship between the candidates. Here is the final graph (where arrows point away from the winner).

In this example, Nashville is the winner using the ranked-pairs procedure. Nashville is followed by Chattanooga, Knoxville, and Memphis in second, third, and fourth places respectively.

### Summary [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=6 "Edit section: Summary")

In the example election, the winner is Nashville. This would be true for any [Condorcet method](https://en.m.wikipedia.org/wiki/Condorcet_method "Condorcet method").

Under [first-past-the-post](https://en.m.wikipedia.org/wiki/First-past-the-post_voting "First-past-the-post voting") and some other systems, Memphis would have won the election by having the most people, even though Nashville won every simulated pairwise election outright. Using [instant-runoff voting](https://en.m.wikipedia.org/wiki/Instant-runoff_voting "Instant-runoff voting") in this example would result in Knoxville winning even though more people preferred Nashville over Knoxville.

## Criteria [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=7 "Edit section: Criteria")

Of the formal [voting criteria](https://en.m.wikipedia.org/wiki/Voting_criteria "Voting criteria"), the ranked pairs method passes the [majority criterion](https://en.m.wikipedia.org/wiki/Majority_criterion "Majority criterion"), the [monotonicity criterion](https://en.m.wikipedia.org/wiki/Monotonicity_criterion "Monotonicity criterion"), the [Smith criterion](https://en.m.wikipedia.org/wiki/Smith_criterion "Smith criterion") (which implies the [Condorcet criterion](https://en.m.wikipedia.org/wiki/Condorcet_criterion "Condorcet criterion")), the [Condorcet loser criterion](https://en.m.wikipedia.org/wiki/Condorcet_loser_criterion "Condorcet loser criterion"), and the [independence of clones criterion](https://en.m.wikipedia.org/wiki/Independence_of_clones_criterion "Independence of clones criterion"). Ranked pairs fails the [consistency criterion](https://en.m.wikipedia.org/wiki/Consistency_criterion "Consistency criterion") and the [participation criterion](https://en.m.wikipedia.org/wiki/Participation_criterion "Participation criterion"). While ranked pairs is not fully [independent of irrelevant alternatives](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives "Independence of irrelevant alternatives"), it still satisfies [local independence of irrelevant alternatives](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives#Local_independence "Independence of irrelevant alternatives")<sup>[<i><a href="https://en.m.wikipedia.org/wiki/MOS:BROKENSECTIONLINKS" title="MOS:BROKENSECTIONLINKS"><span title="The anchor (Local independence) has been deleted. (2024-03-24)">broken anchor</span></a></i>]</sup> and [independence of Smith-dominated alternatives](https://en.m.wikipedia.org/wiki/Independence_of_Smith-dominated_alternatives "Independence of Smith-dominated alternatives"), meaning it is likely to roughly satisfy IIA "in practice."

### Independence of irrelevant alternatives [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=8 "Edit section: Independence of irrelevant alternatives")

Ranked pairs fails [independence of irrelevant alternatives](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives "Independence of irrelevant alternatives"), like all other [ranked voting systems](https://en.m.wikipedia.org/wiki/Ranked_voting "Ranked voting"). However, the method adheres to a less strict property, sometimes called [independence of Smith-dominated alternatives](https://en.m.wikipedia.org/wiki/Independence_of_Smith-dominated_alternatives "Independence of Smith-dominated alternatives") (ISDA). It says that if one candidate (X) wins an election, and a new alternative (Y) is added, X will win the election if Y is not in the [Smith set](https://en.m.wikipedia.org/wiki/Smith_set "Smith set"). ISDA implies the Condorcet criterion.

### Comparison table [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=9 "Edit section: Comparison table")

The following table compares ranked pairs with other [preferential](https://en.m.wikipedia.org/wiki/Ranked_voting "Ranked voting") single-winner election methods:

Comparison of voting systems
| Criterion: | [Majority](https://en.m.wikipedia.org/wiki/Majority "Majority") | [Majority loser criterion](https://en.m.wikipedia.org/wiki/Majority_loser_criterion "Majority loser criterion") | [Mutual majority criterion](https://en.m.wikipedia.org/wiki/Mutual_majority_criterion "Mutual majority criterion") | [Condorcet winner](https://en.m.wikipedia.org/wiki/Condorcet_winner "Condorcet winner")<sup id="cite_ref-condorcet-iia-incompatibility_5-0"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [Condorcet loser](https://en.m.wikipedia.org/wiki/Condorcet_loser "Condorcet loser") | [Smith](https://en.m.wikipedia.org/wiki/Smith_criterion "Smith criterion")<sup id="cite_ref-condorcet-iia-incompatibility_5-1"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [ISDA](https://en.m.wikipedia.org/wiki/Independence_of_Smith-dominated_alternatives "Independence of Smith-dominated alternatives")<sup id="cite_ref-condorcet-iia-incompatibility_5-2"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [LIIA](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives#Local_independence "Independence of irrelevant alternatives") | [IIA](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives "Independence of irrelevant alternatives")<sup id="cite_ref-condorcet-iia-incompatibility_5-3"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [Cloneproof](https://en.m.wikipedia.org/wiki/Independence_of_clones "Independence of clones") | [Monotone](https://en.m.wikipedia.org/wiki/Monotonicity_criterion "Monotonicity criterion") | [Participation](https://en.m.wikipedia.org/wiki/Participation_criterion "Participation criterion") | [Reversal](https://en.m.wikipedia.org/wiki/Reversal_symmetry "Reversal symmetry") | [Later-no-harm](https://en.m.wikipedia.org/wiki/Later-no-harm "Later-no-harm")<sup id="cite_ref-condorcet-iia-incompatibility_5-4"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [Later-no-help](https://en.m.wikipedia.org/wiki/Later-no-help "Later-no-help")<sup id="cite_ref-condorcet-iia-incompatibility_5-5"><a href="https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_note-condorcet-iia-incompatibility-5">[Tn 1]</a></sup> | [Polynomial time](https://en.m.wikipedia.org/wiki/Polynomial_time "Polynomial time") | [Resolvability](https://en.m.wikipedia.org/wiki/Resolvability_criterion "Resolvability criterion") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Schulze](https://en.m.wikipedia.org/wiki/Schulze_method "Schulze method") | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | Yes | Yes | No | Yes | No | No | Yes | Yes |
| Ranked pairs | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | Yes | Yes | No | Yes | No | No | Yes | Yes |
| [Tideman alternative](https://en.m.wikipedia.org/wiki/Tideman_alternative_method "Tideman alternative method") | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | Yes | No | No | No | No | No | Yes | Yes |
| [Kemeny–Young](https://en.m.wikipedia.org/wiki/Kemeny-Young_method "Kemeny-Young method") | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | Yes | No | Yes | No | No | No | Yes |
| [Copeland](https://en.m.wikipedia.org/wiki/Copeland%27s_method "Copeland's method") | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | Yes | No | Yes | No | No | Yes | No |
| [Nanson](https://en.m.wikipedia.org/wiki/Nanson%27s_method "Nanson's method") | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | Yes | No | No | Yes | Yes |
| [Black](https://en.m.wikipedia.org/wiki/Black%27s_method "Black's method") | Yes | Yes | No | Yes | Yes | No | No | No | No | No | Yes | No | Yes | No | No | Yes | Yes |
| [Instant-runoff voting](https://en.m.wikipedia.org/wiki/Instant-runoff_voting "Instant-runoff voting") | Yes | Yes | Yes | No | Yes | No | No | No | No | Yes | No | No | No | Yes | Yes | Yes | Yes |
| [Borda count](https://en.m.wikipedia.org/wiki/Borda_count "Borda count") | No | Yes | No | No | Yes | No | No | No | No | No | Yes | Yes | Yes | No | Yes | Yes | Yes |
| [Baldwin](https://en.m.wikipedia.org/wiki/Baldwin%27s_method "Baldwin's method") | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No | Yes | Yes |
| [Bucklin](https://en.m.wikipedia.org/wiki/Bucklin_voting "Bucklin voting") | Yes | Yes | Yes | No | No | No | No | No | No | No | Yes | No | No | No | Yes | Yes | Yes |
| [Plurality](https://en.m.wikipedia.org/wiki/Plurality_voting "Plurality voting") | Yes | No | No | No | No | No | No | No | No | No | Yes | Yes | No | Yes | Yes | Yes | Yes |
| [Coombs](https://en.m.wikipedia.org/wiki/Coombs%27_method "Coombs' method") | Yes | Yes | Yes | No | Yes | No | No | No | No | No | No | No | No | No | No | Yes | Yes |
| [Minimax](https://en.m.wikipedia.org/wiki/Minimax_Condorcet "Minimax Condorcet") | Yes | No | No | Yes | No | No | No | No | No | No | Yes | No | No | No | No | Yes | Yes |
| [Anti-plurality](https://en.m.wikipedia.org/wiki/Anti-plurality_voting "Anti-plurality voting") | No | Yes | No | No | No | No | No | No | No | No | Yes | Yes | No | No | No | Yes | Yes |
| [Dodgson](https://en.m.wikipedia.org/wiki/Dodgson%27s_method "Dodgson's method") | Yes | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No | Yes |

#### Table notes [edit](https://en.m.wikipedia.org/w/index.php?title=Template:Comparison_of_voting_systems&action=edit&section=T-1 "Edit section: Table notes")

1.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-0) [<sup><i><b>b</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-1) [<sup><i><b>c</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-2) [<sup><i><b>d</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-3) [<sup><i><b>e</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-4) [<sup><i><b>f</b></i></sup>](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-condorcet-iia-incompatibility_5-5) [Condorcet](https://en.m.wikipedia.org/wiki/Condorcet_criterion "Condorcet criterion"), [Smith](https://en.m.wikipedia.org/wiki/Smith_criterion "Smith criterion") and [Independence of Smith-dominated alternatives](https://en.m.wikipedia.org/wiki/Independence_of_Smith-dominated_alternatives "Independence of Smith-dominated alternatives") criteria are incompatible with [Independence of irrelevant alternatives](https://en.m.wikipedia.org/wiki/Independence_of_irrelevant_alternatives "Independence of irrelevant alternatives"), [Consistency](https://en.m.wikipedia.org/wiki/Consistency_criterion "Consistency criterion"), [Participation](https://en.m.wikipedia.org/wiki/Participation_criterion "Participation criterion"), [Later-no-harm](https://en.m.wikipedia.org/wiki/Later-no-harm "Later-no-harm"), [Later-no-help](https://en.m.wikipedia.org/wiki/Later-no-help_criterion "Later-no-help criterion"), and [Favorite betrayal](https://en.m.wikipedia.org/wiki/Sincere_favorite_criterion "Sincere favorite criterion")<sup>[<i><a href="https://en.m.wikipedia.org/wiki/Wikipedia:Please_clarify" title="Wikipedia:Please clarify"><span title="The text near this tag may need clarification or removal of jargon. (October 2016)">clarification needed</span></a></i>]</sup> criteria.

## Notes [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=10 "Edit section: Notes")

1.  **[^](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-4 "Jump up")** Rather than crossing out near-ties, step 3 is sometimes described as going down the list and confirming ("locking in") the largest victories that do not create a cycle, then ignoring any victories that are not locked-in.

## References [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=11 "Edit section: References")

1.  **[^](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-Tideman2_1-0 "Jump up")** Tideman, T. N. (1987-09-01). ["Independence of clones as a criterion for voting rules"](https://doi.org/10.1007/BF00433944). _Social Choice and Welfare_. **4** (3): 185–206. [doi](https://en.m.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/BF00433944](https://doi.org/10.1007%2FBF00433944). [ISSN](https://en.m.wikipedia.org/wiki/ISSN_(identifier) "ISSN (identifier)") [1432-217X](https://www.worldcat.org/issn/1432-217X). [S2CID](https://en.m.wikipedia.org/wiki/S2CID_(identifier) "S2CID (identifier)") [122758840](https://api.semanticscholar.org/CorpusID:122758840).
2.  **[^](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-2 "Jump up")** Schulze, Markus (October 2003). ["A New Monotonic and Clone-Independent Single-Winner Election Method"](https://web.archive.org/web/20200711055629/www.votingmatters.org.uk/ISSUE17/INDEX.HTM). _Voting matters (www.votingmatters.org.uk)_. **17**. McDougall Trust. Archived from [the original](http://www.votingmatters.org.uk/ISSUE17/INDEX.HTM) on 2020-07-11. Retrieved 2021-02-02.
3.  **[^](https://en.m.wikipedia.org/wiki/Ranked_pairs#cite_ref-3 "Jump up")** Munger, Charles T. (2022). ["The best Condorcet-compatible election method: Ranked Pairs"](https://doi.org/10.1007%2Fs10602-022-09382-w). _[Constitutional Political Economy](https://en.m.wikipedia.org/wiki/Constitutional_Political_Economy "Constitutional Political Economy")_. **34** (3): 434–444. [doi](https://en.m.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/s10602-022-09382-w](https://doi.org/10.1007%2Fs10602-022-09382-w).

## External links [edit](https://en.m.wikipedia.org/w/index.php?title=Ranked_pairs&action=edit&section=12 "Edit section: External links")

-   [Descriptions of ranked-ballot voting methods](https://accuratedemocracy.com/download/software/rbvote/desc.html) by Rob LeGrand
-   [Example JS implementation](https://gist.github.com/asafh/a8e9af7a3e5282cbba27) by Asaf Haddad
-   [Pair Ranking Ruby Gem](https://bitbucket.org/bparanj/rasam) by Bala Paranj
-   [A margin-based PHP Implementation of Tideman's Ranked Pairs](https://github.com/pivot-libre/tideman/)
-   [Rust implementation of Ranked Pairs](https://github.com/corydickson/pairwise-voting) by Cory Dickson
