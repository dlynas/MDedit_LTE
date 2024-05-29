---
title: code_for_donald_hoffmans_computational
url: https://www.reddit.com/r/MachineLearning/comments/12bj1z3/code_for_donald_hoffmans_computational/
source: reddit
subreddit: MachineLearning
media: no
---
**r/MachineLearning** | Posted by u/MatMou ⬆️ 10 _(2023-04-04 09:23:03)_

## Code for Donald Hoffman's Computational Evolutionary Perception [R]

Original post: [https://www.reddit.com/r/MachineLearning/comments/12bj1z3/code_for_donald_hoffmans_computational/](https://www.reddit.com/r/MachineLearning/comments/12bj1z3/code_for_donald_hoffmans_computational/)

> Hi,
> 
> I was trying to figure out which kinds of alogrithms and code Donald Hoffman and others use in this paper  [Does evolution favor true perceptions? (spiedigitallibrary.org)](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/8651/1/Does-evolution-favor-true-perceptions/10.1117/12.2011609.full?SSO=1) and  [The Interface Theory of Perception | SpringerLink](https://link.springer.com/article/10.3758/s13423-015-0890-8) 
> 
> &#x200B;
> 
> He talks about Computational Evolutionary Perception, but I was wondering if anybody has (re)made the code or used an already implemented code for this?
> 
> &#x200B;
> 
> The reason why I'm asking is because I'm pretty new to using evolutionary algorithms and therefore inexperienced in searching for this type of code.

💬 ~ 3 replies

---

* 🟩 **[deleted]** ⬆️ 3 _(2023-04-05 03:08:37)_

	[https://jpinjpblog.wordpress.com/2020/11/17/learning-genetic-algorithm/](https://jpinjpblog.wordpress.com/2020/11/17/learning-genetic-algorithm/)

	* 🟨 **[MatMou](https://www.reddit.com/user/MatMou) (OP)** ⬆️ 1 _(2023-04-05 13:11:12)_

		Is this the one mentioned in the texts or is it just a reference to some of the ways to implement something like this?

* 🟩 **[justmeeseeking](https://www.reddit.com/user/justmeeseeking)** ⬆️ 2 _(2024-02-14 08:01:22)_

	I think in the paper 'The interface theory of perception' they summarize finding from different simulations, such as the one in 'Does evolution favor trueperceptions?' To my knowledge it is the only simulation with GAs (the others are dealing with evolutionary games and replicator dynamics).

	I couldn't find any code for the GA from Hoffman and his group. However in the paper he mentions first a different GA proposed by Melanie Mitchell in the Book 'Complexity - A guided Tour'. For this GA the code can actually be found on their website. [Here](https://melaniemitchell.me/ExplorationsContent/RobbyTheRobot/) is a version in C as well as a version for NetLogo. NetLogo is a programming language designed for multi agent modelling. There is also a web version of NetLogo and this already contains the GA from Mitchell (find it [here](https://ccl.northwestern.ed[u/netlogo](https://www.reddit.com/user/netlogo)/models/RobbytheRobot)). 

	From these you can get an idea of how to implement the details of a GA and also transfer from Mitchells GA to Hoffmans GA. However since I am also currently working on reproducing Hoffman's GAs, I realize that they don't fully specify every detail in the paper, so work is still in progress. 

	When I have reproduced Hoffman's finding, I plan to publish the code on GitHub and can also share it here. 

	Besides that, if you have any questions feel free to contact me and discuss about the algorithm from the paper.


