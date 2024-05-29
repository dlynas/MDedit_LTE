---
source: politicalsim.com
url: https://politicalsim.com/
---

Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim lets players test many types of voting.  From Australia to old Zuidland there are many ways to elect reps.  Each country's voting rule creates hot spots for players on the electoral field.  But those strong positions might move if we change the voting rule.  Some rules elect only centrists, some elect moderates, and some are just erratic.

Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim allows voting by all the widely used rules such as Australia's STV, Japan's SNTV, Finland's list PR, USA's open primary, England's plurality and France's runoff; plus limited, cumulative, and the often illegal bloc voting rules.

Simulated voters rank the candidates, giving 1st choice to the closest, 2nd choice to the 2nd closest, and so on.  Their positions on the screen may represent geography or political opinions.

**Games:** Players take the roles of party leaders positioning rival candidates to maximize support.  Moving a candidate requires paying for ads and answering interview questions can win donations.

Elections for research or fun may have 2 to 16 candidates, competing for 1 to 7 seats.

## _Voting Rules!_

   

![[768e51ecd838541296e81cb784c67284_MD5.gif]]

### _Compare Three Councils_

In this simulated election of a five-seat council, little stick figures ![[6f65356106f6f09f321f0a7491e40c24_MD5.gif]] show the positions of voters.  The huge heads are the candidates.

1) Simulations show that [**Ensemble Rules**](http://accuratedemocracy.com/e_intro.htm) are the best way to represent the center and all sides.  Here [**LER**](http://accuratedemocracy.com/e_ler.htm) elects **Al** then **Bev, Di, Fred**, and **Joe**.  (Each winner's name is in **bold**.)

2) A [_Condorcet Series_](http://accuratedemocracy.com/c_intro.htm) elects the 5 candidates nearest the central voter: _Al, Bev, Fred, GG_, and _Joe_.  There is no rep from the lower-right, so the council cannot balance around the central voter.  _Bloc vote_ and _Borda's rule_ elect the same off-center council.  (Each name is in italic.)

3) The [<u>Single Transferable Vote</u>](http://accuratedemocracy.com/d_stv.htm) winners? <u>Bev, Di, Fred, GG</u>, and <u>Joe</u>.  (Each name is <u>underlined</u>.)  STV did not elect Al!

Only **LER** has Condorcet centering with Single Transferable Vote balancing!

![[bbeaffe9b8bf71f3e9746741f3312f77_MD5.gif]]

Thanks for your interest in PoliticalSim. I'm sorry to have to tell you, years ago Microsoft stopped supporting Excel's original macro language. But I got the following, in December 2018, from a programmer who succeeded in running it. I hope you also succeed.

"Hi Robert,

I'm having some fun using [DOSbox](https://en.wikipedia.org/wiki/DOSBox). It's a tool that runs Windows 3.1, and I got Excel 4.0 running in it too. It took me a while to set up.

I didn't realize this was a game until now. I thought it was a simulator that generated statistics. It seems like it's really developed. This is cool.

It runs!

![[e1ecc53de2987ba934f738f06ad6b7a4_MD5]]

I was able to get into an election and find out who won. I think I did some things out of order, so I had a few errors. I think if I try again and actually read the help pages then it might do better. The really cool thing is that the debugger opened when the errors happened, so I can dive into the code and see how things work.

### Level Zero

-   Uncompress the download file.<sup>(1)</sup>
-   Open the file called Poli\_Sim.xlm or PoliticalSim.xls.
-   Pull down the Elect menu to Cast Ballots.
-   On the Elect menu, choose Tally Votes and click OK.
-   View the results of your first Political Sim!

(1) Most versions can decompress themselves when you open the download file. Versions with a name that ends in “.zip” need a program such as WinZip or SuffIt.

![[afa9eb1f89dacb2e8ea71aafa3663e42_MD5.gif]]

### Commands to Note

### Level 1) Organize Menu

**Get Cities command**  
Try the Checkerboard city for its evenly spaced voters. This will make it easy to see the results of each voting rule. Click a “✓” in the “Get Voters” box.  
Cast Ballots and Tally Votes again to see the results.

![[d6fa7326a2ba46f7bd1c7248c9217129_MD5.gif]]

Get Cities window

---

### Level 2) Create Parties

**1) Register Voters menu**

Do not put a “✓” in Redistribute. This will let you keep the voters in the checkerboard pattern while you change the percentages in each party faction.

For clairity, do not check Mix Factions Together.

On the right of this “dialog box” are 5 rows with 3 boxes in each row. The first column is for a party's name; the second is for its “Z level”, explained below; and the third is for its percentage of voters.

Try putting most voters, 60% to 80%, in the Blue party and make their Z=0. Then put the other voters in the Green party and make their Z=9. These Z levels make all Blue voters rank all Blue candidates above all Green candidates.\*

\* This works because the map is 6 units wide and 6 tall. It is less than 9 units from corner to corner. So the distance between Z=0 and Z=9 puts the Green candidates further from the Blue voters than each of the Blue candidates.

![[853a71321a30ca49f2fc087380849c4b_MD5.gif]]

The X and Y dimensions are the width and height of the Map page on your computer screen. The Z dimension goes in and out from your screen and is shown only by the color of the voter or candidate. If you set parties at different Z levels and forget it, you will wonder why a candidate loses despite being close to many voters on the X-Y screen.

---

**2) Nominate Candidates**: A party's candidates ought to have the same Z level as its voters.

You can move each candidate by hand: Hold down the Control key and slowly click twice on a candidate, then move it along the X or Y dimension. You can also move candidates by directly changing their (X, Y, Z) numbers on the Register page. To update the map, hold the control key as you tap the = (equal sign) key.

![[16a80cea3c038f016f8d714803b7cef5_MD5.gif]]

Distribute Candidatees window

---

### Level 3) Test a New Constitution

**Set Voting Rules**: Now your're becoming a master of political designs. Select a voting rule from the list of proportional, semi-proportional and winner-take-all rules. Then set your rule's quota if needed.

![[a82097648ed60f3f816ff4aefea008cd_MD5.gif]]

---

### Elect Menu

1) **Cast Ballots**

2) **Watch Returns**

The option to [Show STV Transfers](https://politicalsim.com/d_stv2d.htm) is worth watching when running a tally of Single Transferable Vote or the Loring Ensemble Rule.

**Notice:** Are winners all from 1 party? What is the pattern elected by the current voting rule: central, proportional fair shares, one-sided or erratic?

**Single Transferable Vote, Simple Quota, 5 Seats**  
Here's a simple example with all voters and candidates at the same Z level in the Checkerboard City.

![[d1e3a694639f1a73cc5b753d9a30c6e6_MD5.gif]]

![[afa9eb1f89dacb2e8ea71aafa3663e42_MD5.gif]]

PoliticalSim can tally voting rules which require single-member districts but they do not work well in games. They require maps that show which district each voter and candidate is in by the shape of his or her symbol.

PoliticalSim can create new elections automatically, mesmerizing like a screen saver, we call it the **“Lava Lamp” mode**. To start it, select Run Research on the Organize menu and step through the dialog boxes. When you get to “News Coverage”, set the Number of Elections at 99 (or less if you want) and set “Record Results to Column” 0 (zero or blank). Although this mode was built for statistical research, you don't want to create dozens of statistical files while running it for amusement.

![[afa9eb1f89dacb2e8ea71aafa3663e42_MD5.gif]]

   

## _Take The Wraps Off Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim_

Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim was created to make the power of voting rules easy to understand through visual displays.  You don't need to do the tallies.  You don't need to calculate statistics.  The merits of [Condorcet rules](http://accuratedemocracy.com/c_intro.htm) or [Proportional Representation](http://accuratedemocracy.com/d_intro.htm) or both [together](http://accuratedemocracy.com/e_intro.htm) are easy to see and explain in everyday terms: consistently central, or evenly spread out, or centrally balanced.

You can develop an intuitive feel for statistical patterns by playing with them.  You can put voters in random, normal, uniform, or checkerboard patterns.  You can spread the candidates out wide or cluster them near the center, developing a feel for "standard deviation" as you play.

**Students, Activists, Professors and Pollsters:** In addition to games that teach some political science and statistics, Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim creates [slide shows](http://accuratedemocracy.com/d_stv2d.htm) for lectures.  Users can record and recall the voters, candidates and winning positions from typical and unusual simulations.

The sim can record [charts](http://accuratedemocracy.com/d_stv2d.htm) of voters' top choices for each step in a LER or STV tally.  It also calculates a council's "utility" score and the percentages of voters with their first, second or third choices elected.  These statistics and more can be recorded from the results of several rules over many elections and later analyzed.

![[afa9eb1f89dacb2e8ea71aafa3663e42_MD5.gif]]

Most of these compressed files are self-extracting.  (Versions with a name that ends with "zip" need a program such as WinZip or SuffIt.)  After you download one to a disk, double click its icon, to uncompress it.  It will put a PoliticalSim folder on your disk.  You can tell it where to put the folder or move it later, but do not change the name.  Look in that folder to open Poli\_Sim.xlm or PoliticalSim.xls.  (Excel 4 limits names to 8.3 letters so the folder is called Politicl.Sim.)

-   Open the file called Poli\_Sim.xlm
-   Pull down the Elect menu to Cast Ballots.
-   Pull down the Elect menu to Tally Votes.
-   You've just run your first Political Sim!

**See the online [Guide for New Users](https://politicalsim.com/s_guide.htm)**.

### [Other Free Downloads](http://accuratedemocracy.com/download/)

[**Fair-share allocation software**](http://accuratedemocracy.com/p_tools.htm):   For fair-share spending to select and budget one-time events and projects, use a [Moveable Money Votes](http://accuratedemocracy.com/a_workshop.htm#money) tally:  
This simulation game needs Excel 5 or higher: [FairShareSim.xls](http://accuratedemocracy.com/download/FairShareSim.xls).  
An [interactive ballot](http://accuratedemocracy.com/download/FS_Blt_S_16.xls) shows an advanced algorithm.

**Printouts** on the voting rules are easier to study than the screen pages.  You may choose either a terse 9 page article in black and white [elect.pdf](http://accuratedemocracy.com/download/primer/elect.pdf) — or a concise 28 page primer with [color pictures](http://accuratedemocracy.com/z_prints.htm).

**Voting rules explained:** The [Accurate Democracy](http://accuratedemocracy.com/) web site describes the political tendencies and tally methods for most voting rules included in Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim.

[![[3d1a5cf6813734d4d5ab97d28deb4900_MD5.gif]]](http://accuratedemocracy.com/navlast.map)

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]

<table><tbody><tr><td colspan="6"><span face="Verdana, Geneva, Arial, Helvetica, sans serif"><b>&nbsp; A Partial Map to Accurate Democracy<br>&nbsp; &nbsp; &nbsp; &nbsp; </b>The concepts build from one voting situation to the next.&nbsp;<b><br>&nbsp; &nbsp; &nbsp; &nbsp; </b>This web site looks at all of them, from nominations to funding.</span></td></tr><tr><th><div><p><a href="http://accuratedemocracy.com/c_intro.htm"><b>Chair</b><br><img src="https://politicalsim.com/RuleGBG.gif" alt="Condorcet voting rules for electing a chairman or chairwoman."></a></p></div></th><th><div><p><a href="http://accuratedemocracy.com/d_intro.htm"><b>Reps</b><br><img src="https://politicalsim.com/RuleRGR.gif" alt="Full representation election systems for representatives"></a></p></div></th><th><div><p><a href="http://accuratedemocracy.com/e_intro.htm"><b>Council</b><br><img src="https://politicalsim.com/RuleRBR.gif" alt="Mixed-member election systems for councils"></a></p></div></th><th><div><p><a href="http://accuratedemocracy.com/l_intro.htm"><b>Policy</b><br><img src="https://politicalsim.com/RuleGBG.gif" alt="Condorcet and parliamentary rules of order to set policies"></a></p></div></th><th><div><p><a href="http://accuratedemocracy.com/p_intro.htm"><b>Projects</b><br><img src="https://politicalsim.com/RuleRBR.gif" alt="Fair-share voting systems to select and fund projects"></a></p></div></th><th><div><p><a href="http://accuratedemocracy.com/q_intro.htm"><b>Budgets</b><br><img src="https://politicalsim.com/RuleRBR.gif" alt="Point-voting systems to set budgets quickly"></a></p></div></th></tr><tr><td>Ballot<br>Pictorial<br>Tally<br>Runoff<br>Tactics<br>Districts</td><td>Merits<br>Women<br>STV<br>Visual STV<br>Pictorial 2<br>2D charts</td><td>Merits<br>Merits 2<br>CW+STV<br>Notes<br>Seats<br>Shares</td><td>Motions<br>Ballots<br>Tactics<br>Cycles<br>Other<br>Amend</td><td>Uses<br>Need<br>Notes<br>Ballot<br>Tally<br>LAR</td><td>Ballot<br>Coalitions<br>Other<br>Medians<br>HZ Points<br>Cards</td></tr></tbody></table>

 **Humor 8 for politicians:** According to Clare Boothe Luce,  
“\_\_\_\_\_\_\_ has done more to cause the social unrest of the  
20th century than any other single factor.”  
1) [Revolution](https://politicalsim.com/#a1), 2) [Democracy](https://politicalsim.com/#a2), 3) [Socialism](https://politicalsim.com/#a3), 4) [Advertising](https://politicalsim.com/#a4) [?](https://politicalsim.com/#answer)

Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim![[c104b545eb3aa0ceea8bca025458c415_MD5.gif]] has hundreds of interview questions.   
A sample appears in the on-line game [Quotes and Authors](http://accuratedemocracy.com/a_humor.htm).

![[2df4ccc3caf4add53f04913644842a9c_MD5.gif]]  ![[65e4b9f2b76880110af539e1b32deeca_MD5.gif]]

**Notes:**   Why Excel?  Voting tallies are number crunching, so we want a language designed for that.  We want a language that is simple and that many people know how to read and write, with programming tools and help widely available.  PoliticalSim does a great deal with simple spreadsheets and the Excel macros which use spreadsheet formulas.

The download file includes a user's manual with voting-rule definitions.  It is about 1500K zipped, 3100K uncompressed.

Programmers can add features (and fix bugs) because this is "open source" software.  Startup support is available by [email](http://accuratedemocracy.com/z_mail.htm). If your version of Excel gives an error message, simply click "continue", and please tell us.  The graphics in PoliticalSim's Map\_Reps page can push Excel to the breaking point.  The last maintenance update was on 2001-06-16.

Thanks to all those whose feedback has improved Political![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]Sim.

[![[e77f675a4effc01bc4d89241591161ab_MD5.gif]]](http://accuratedemocracy.com/navone.map)

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]

.

Yes ![[a467fe3585fdb1f155c475a1b47419e5_MD5.gif]]Yes![[d79dd631d2b0e9e5a06a479a81a7766c_MD5.gif]] Yes

[Question](https://politicalsim.com/#question)

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]

. . .

No![[2df4ccc3caf4add53f04913644842a9c_MD5.gif]]No![[65e4b9f2b76880110af539e1b32deeca_MD5.gif]]No

[Question](https://politicalsim.com/#question)

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]

Try **PoliticalSim** tm (political sim) a free open-source political-simulation game for Windows, and SimElection tm, electoral simulation software for Macintosh, for interactive simulations of approval voting, Borda rule, Condorcet rules (minmax & Copeland), instant runoff voting (IRV, alternative vote, Hare), majority rule, plurality rule, proportional representation (list PR with largest remainders or divisors), single transferable vote (STV with Droop, Hare or simple quota), choice voting, cumulative vote, limited vote, bloc vote and other voting rules. It demonstrates comparative politics and game theory including multi-winner decision making.

**Answer:** 8) American author and congresswoman Clare Boothe Luce  
heard in detail about the effectiveness of advertising while married to  
purveyor Henry Luce, publisher of _Time_ and _Fortune_ magazines.

[Question](https://politicalsim.com/#question)        [Download](https://politicalsim.com/#download)        [Next pages](https://politicalsim.com/#next)

![[a99e748e778681c567f91aabfc4bc3e5_MD5.gif]]
