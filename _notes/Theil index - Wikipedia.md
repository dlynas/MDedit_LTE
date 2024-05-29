---
source: en.wikipedia.org
url: https://en.wikipedia.org/wiki/Theil_index
---

From Wikipedia, the free encyclopedia

The **Theil index** is a statistic primarily used to measure [economic inequality](https://en.wikipedia.org/wiki/Economic_inequality "Economic inequality")<sup id="cite_ref-1"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-1">[1]</a></sup> and other economic phenomena, though it has also been used to measure racial segregation.<sup id="cite_ref-2"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-2">[2]</a></sup><sup id="cite_ref-policymap_3-0"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-policymap-3">[3]</a></sup>

The Theil index _T_<sub>T</sub> is the same as [redundancy](https://en.wikipedia.org/wiki/Redundancy_(information_theory) "Redundancy (information theory)") in [information theory](https://en.wikipedia.org/wiki/Information_theory "Information theory") which is the maximum possible [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory) "Entropy (information theory)") of the data minus the observed entropy. It is a special case of the [generalized entropy index](https://en.wikipedia.org/wiki/Generalized_entropy_index "Generalized entropy index"). It can be viewed as a measure of redundancy, lack of diversity, isolation, segregation, inequality, non-randomness, and compressibility. It was proposed by a Dutch [econometrician](https://en.wikipedia.org/wiki/Econometrics "Econometrics") [Henri Theil](https://en.wikipedia.org/wiki/Henri_Theil "Henri Theil") (1924–2000) at the [Erasmus University Rotterdam](https://en.wikipedia.org/wiki/Erasmus_University_Rotterdam "Erasmus University Rotterdam").<sup id="cite_ref-policymap_3-1"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-policymap-3">[3]</a></sup>

Henri Theil himself said (1967): "The (Theil) index can be interpreted as the expected information content of the indirect message which transforms the population shares as prior probabilities into the income shares as posterior probabilities."<sup id="cite_ref-:0_4-0"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-:0-4">[4]</a></sup>

[Amartya Sen](https://en.wikipedia.org/wiki/Amartya_Sen "Amartya Sen") noted, "But the fact remains that the Theil index is an arbitrary formula, and the average of the logarithms of the reciprocals of income shares weighted by income is not a measure that is exactly overflowing with intuitive sense."<sup id="cite_ref-:0_4-1"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-:0-4">[4]</a></sup>

## Formula\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=1 "Edit section: Formula")\]

For a population of _N_ "agents" each with characteristic _x_, the situation may be represented by the list _x_<sub><i>i</i></sub> (_i_ = 1,...,_N_) where _x_<sub><i>i</i></sub> is the characteristic of agent _i_. For example, if the characteristic is income, then _x<sub>i</sub>_ is the income of agent _i_.

The Theil _T_ index is defined as<sup id="cite_ref-Formulas_5-0"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-Formulas-5">[5]</a></sup>

![{\displaystyle T_{T}=T_{\alpha =1}={\frac {1}{N}}\sum _{i=1}^{N}{\frac {x_{i}}{\mu }}\ln \left({\frac {x_{i}}{\mu }}\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/83d79be6674579085cbb2bf9a6048e5d8bc68a8e)

and the Theil _L_ index is defined as<sup id="cite_ref-Formulas_5-1"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-Formulas-5">[5]</a></sup>

![{\displaystyle T_{L}=T_{\alpha =0}={\frac {1}{N}}\sum _{i=1}^{N}\ln \left({\frac {\mu }{x_{i}}}\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d0c448553e879aaced28310229bb12725053ca5e)

where ![{\displaystyle \mu }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9fd47b2a39f7a7856952afec1f1db72c67af6161) is the mean income:

![{\displaystyle \mu ={\frac {1}{N}}\sum _{i=1}^{N}x_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2917e28c1e3d194c1456de021709eb9b034eb5ce)

Theil-L is an income-distribution's dis-entropy per person, measured with respect to maximum entropy (...which is achieved with complete equality).

(In an alternative interpretation of it, Theil-L is the natural-logarithm of the geometric-mean of the ratio: (mean income)/(income i), over all the incomes. The related Atkinson(1) is just 1 minus the geometric-mean of (income i)/(mean income),over the income distribution.)

Because a transfer between a larger income & a smaller one will change the smaller income's ratio more than it changes the larger income's ratio, the transfer-principle is satisfied by this index.

Equivalently, if the situation is characterized by a discrete distribution function _f_<sub><i>k</i></sub> (_k_ = 0,...,_W_) where _f_<sub><i>k</i></sub> is the fraction of the population with income _k_ and _W_ = _Nμ_ is the total income, then ![{\displaystyle \sum _{k=0}^{W}f_{k}=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f16ebde2d1eb3267e7c2cd0ead1271cd2a92691a) and the Theil index is:

![{\displaystyle T_{T}=\sum _{k=0}^{W}\,f_{k}\,{\frac {k}{\mu }}\ln \left({\frac {k}{\mu }}\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68b4a660e2b5e9d291f14fd2733911ec6b85bc6b)

where ![{\displaystyle \mu }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9fd47b2a39f7a7856952afec1f1db72c67af6161) is again the mean income:

![{\displaystyle \mu =\sum _{k=0}^{W}kf_{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/28cbcb828c0ca2b4790591effdde3f5cde5c75bd)

Note that in this case income _k_ is an integer and _k=1_ represents the smallest increment of income possible (e.g., cents).

if the situation is characterized by a continuous distribution function _f_(_k_) (supported from 0 to infinity) where _f_(_k_) _dk_ is the fraction of the population with income _k_ to _k_ + _dk_, then the Theil index is:

![{\displaystyle T_{T}=\int _{0}^{\infty }f(k){\frac {k}{\mu }}\ln \left({\frac {k}{\mu }}\right)dk}](https://wikimedia.org/api/rest_v1/media/math/render/svg/efecd55ca5be6098f4e3e6ce1184b463033b4bb6)

where the mean is:

![{\displaystyle \mu =\int _{0}^{\infty }kf(k)\,dk}](https://wikimedia.org/api/rest_v1/media/math/render/svg/374b8d5bbc883206a3e15122de683587c3b87678)

Theil indices for some common continuous probability distributions are given in the table below:

| Income distribution function | PDF(_x_) (_x_ ≥ 0) | Theil coefficient (nats) |
| --- | --- | --- |
| [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function "Dirac delta function") | ![{\displaystyle \delta (x-x_{0}),\,x_{0}>0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/db5b0aa87688e6070ee35465aee14f4de31b8a10) | 0 |
| [Uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous) "Uniform distribution (continuous)") | ![{\displaystyle {\begin{cases}{\frac {1}{b-a}}&a\leq x\leq b\\0&{\text{otherwise}}\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/46b1d475e512469b9c3a6df38b655b6d432e5810) | ![{\displaystyle \ln \left({\frac {2a}{(a+b){\sqrt {e}}}}\right)+{\frac {b^{2}}{b^{2}-a^{2}}}\ln(b/a)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/57c5095603bc838db5bc36558e490dc9e2575a2b) |
| [Exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution "Exponential distribution") | ![{\displaystyle \lambda e^{-x\lambda },\,\,x>0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7d446981e5008b4f43bed33306548a985d0f0f61) | ![{\displaystyle 1-}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3034f863e78e58606d50a78090620dd035271c5d) [![{\displaystyle \gamma }](https://wikimedia.org/api/rest_v1/media/math/render/svg/a223c880b0ce3da8f64ee33c4f0010beee400b1a)](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant "Euler–Mascheroni constant") |
| [Log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution "Log-normal distribution") | ![{\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{(-(\ln(x)-\mu )^{2})/\sigma ^{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0eabe943cd4c6b5c8ae559ec7144f641dda0b500) | ![{\displaystyle {\frac {\sigma ^{2}}{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c68a5957e09585db4cbd1e92efca1e97d7dde94) |
| [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution "Pareto distribution") | ![{\displaystyle {\begin{cases}{\frac {\alpha k^{\alpha }}{x^{\alpha +1}}}&x\geq k\\0&x<k\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/03e401ef333be0869460084ec9d062270cd19dd4) | ![{\displaystyle \ln(1\!-\!1/\alpha )+{\frac {1}{\alpha -1}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a6566821d490f82628c1128c09bb86f6ece963c0)    (α>1) |
| [Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution "Chi-squared distribution") | ![{\displaystyle {\frac {2^{-k/2}e^{-x/2}x^{k/2-1}}{\Gamma (k/2)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/719d8e1d90a6a3e6a020d8a047217991772da586) | ![{\displaystyle \ln(2/k)+}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d9f98087674a87a382b28b649571e28d3c5bbbc3) [![{\displaystyle \psi ^{(0)}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80c4a6496a6abadc15d4bccfc091316f26c4f0c8)](https://en.wikipedia.org/wiki/Polygamma_function "Polygamma function")![{\displaystyle (1\!+\!k/2)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cd59248c6c963e856426dd0368c630d463dc762a) |
| [Gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution "Gamma distribution")<sup id="cite_ref-McDonald1974_6-0"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-McDonald1974-6">[6]</a></sup> | ![{\displaystyle {\frac {e^{-x/\theta }x^{k-1}\theta ^{-k}}{\Gamma (k)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/46052c4c41cbbeb2b008a53ddb7c73d7df30564d) | [![{\displaystyle \psi ^{(0)}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80c4a6496a6abadc15d4bccfc091316f26c4f0c8)](https://en.wikipedia.org/wiki/Polygamma_function "Polygamma function")![{\displaystyle (1+k)-\ln(k)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7b1eb1fced77bc21bef30ab650cd0202103f1e03) |
| [Weibull distribution](https://en.wikipedia.org/wiki/Weibull_distribution "Weibull distribution") | ![{\displaystyle {\frac {k}{\lambda }}\left({\frac {x}{\lambda }}\right)^{k-1}e^{-(x/\lambda )^{k}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/77e290ae1ff63fb2994cbeaf26c25dad48cb6b3f) | ![{\displaystyle {\frac {1}{k}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e8560804e21ad155b4f9d8e8a8acd6fae698bb6) [![{\displaystyle \psi ^{(0)}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80c4a6496a6abadc15d4bccfc091316f26c4f0c8)](https://en.wikipedia.org/wiki/Polygamma_function "Polygamma function")![{\displaystyle (1+1/k)-\ln \left(\Gamma (1+1/k)\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/19d7f23dac6f4e9768f132c4ac8e245fde817224) |

If everyone has the same income, then _T_<sub>T</sub> equals 0. If one person has all the income, then _T_<sub>T</sub> gives the result ![{\displaystyle \ln N}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9a2c6c380596b8d0e34cafc070f8efdfa7b21559), which is maximum inequality. Dividing _T_<sub>T</sub> by ![{\displaystyle \ln N}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9a2c6c380596b8d0e34cafc070f8efdfa7b21559) can normalize the equation to range from 0 to 1, but then the [independence axiom](https://en.wikipedia.org/wiki/Economic_inequality_metrics "Economic inequality metrics") is violated: ![{\displaystyle T[x\cup x]\neq T[x]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8de3131f72f208326b14b501980cc6d8a0268e3) and does not qualify as a measure of inequality.

The Theil index measures an entropic "distance" the population is away from the egalitarian state of everyone having the same income. The numerical result is in terms of negative entropy so that a higher number indicates more order that is further away from the complete equality. Formulating the index to represent negative entropy instead of entropy allows it to be a measure of inequality rather than equality.

### Relation to Atkinson Index\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=2 "Edit section: Relation to Atkinson Index")\]

The Theil index can be transformed into an [Atkinson index](https://en.wikipedia.org/wiki/Atkinson_index "Atkinson index"), which has a range between 0 and 1 (0% and 100%), where 0 indicates perfect equality and 1 (100%) indicates maximum inequality. (See [Generalized entropy index](https://en.wikipedia.org/wiki/Generalized_entropy_index "Generalized entropy index") for the transformation.)

## Derivation from entropy\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=3 "Edit section: Derivation from entropy")\]

The Theil index is derived from [Shannon](https://en.wikipedia.org/wiki/Claude_Shannon "Claude Shannon")'s measure of [information entropy](https://en.wikipedia.org/wiki/Information_entropy "Information entropy") ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2), where entropy is a measure of randomness in a given set of information. In information theory, physics, and the Theil index, the general form of entropy is

![{\displaystyle S=k\sum _{i=1}^{N}\left(p_{i}\log _{a}\left({\frac {1}{p_{i}}}\right)\right)=-k\sum _{i=1}^{N}\left(p_{i}\log _{a}\left({p_{i}}\right)\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2d2b5b7f133c711c7587da872b1330c93128045b)

where

When looking at the distribution of income in a population, ![{\displaystyle p_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5bab39399bf5424f25d957cdc57c84a0622626d2) is equal to the ratio of a particular individual's income to the total income of the entire population. This gives the observed entropy ![{\displaystyle S_{\text{Theil}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/07258c0ee4f901b7e2dc4cae400e0cadeab19e40) of a population to be:

![{\displaystyle S_{\text{Theil}}=\sum _{i=1}^{N}\left({\frac {x_{i}}{N{\bar {x}}}}\ln \left({\frac {N{\bar {x}}}{x_{i}}}\right)\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/045520b63599b75f58680d47ca681966a906d768)

where

The Theil index ![{\displaystyle T_{T}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2f0f690d607e62041991925f1c2defcd216c0950) measures how far the observed entropy (![{\displaystyle S_{\text{Theil}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/07258c0ee4f901b7e2dc4cae400e0cadeab19e40), which represents how randomly income is distributed) is from the highest possible entropy (![{\displaystyle S_{\text{max}}=\ln \left({N}\right)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/75b11a1ba9a3302216c594d69bc54ef09f8f800b),<sup id="cite_ref-9"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-9">[note 3]</a></sup> which represents income being maximally distributed amongst individuals in the population– a distribution analogous to the \[most likely\] outcome of an infinite number of random coin tosses: an equal distribution of heads and tails). Therefore, the Theil index is the difference between the theoretical maximum entropy (which would be reached if the incomes of every individual were equal) minus the observed entropy:

![{\displaystyle T_{T}=S_{\text{max}}-S_{\text{Theil}}=\ln \left({N}\right)-S_{\text{Theil}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f69d1832649e8f66d46a275671be81e5ed774292)

  
When ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) is in units of population/species, ![{\displaystyle S_{\text{Theil}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/07258c0ee4f901b7e2dc4cae400e0cadeab19e40) is a measure of biodiversity and is called the [Shannon index](https://en.wikipedia.org/wiki/Shannon_index "Shannon index"). If the Theil index is used with x=population/species, it is a measure of inequality of population among a set of species, or "bio-isolation" as opposed to "wealth isolation".

The Theil index measures what is called [redundancy](https://en.wikipedia.org/wiki/Redundancy_(information_theory) "Redundancy (information theory)") in information theory.<sup id="cite_ref-Formulas_5-2"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-Formulas-5">[5]</a></sup> It is the left over "information space" that was not utilized to convey information, which reduces the effectiveness of the [price signal](https://en.wikipedia.org/wiki/Price_signal "Price signal").<sup>[<i><a href="https://en.wikipedia.org/wiki/Wikipedia:No_original_research" title="Wikipedia:No original research"><span title="The material near this tag possibly contains original research. (June 2020)">original research?</span></a></i>]</sup> The Theil index is a measure of the redundancy of income (or other measure of wealth) in some individuals. Redundancy in some individuals implies scarcity in others. A high Theil index indicates the total income is not distributed evenly among individuals in the same way an uncompressed text file does not have a similar number of byte locations assigned to the available unique byte characters.

| Notation | Information theory | Theil index T<sub>T</sub> |
| --- | --- | --- |
| ![{\displaystyle N}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5e3890c981ae85503089652feb48b191b57aae3) | number of unique characters | number of individuals |
| ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) | a particular character | a particular individual |
| ![{\displaystyle x_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e87000dd6142b81d041896a30fe58f0c3acb2158) | count of _i_th character | income of _i_th individual |
| ![{\displaystyle N{\bar {x}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0f89609fde593d80aa6288b331b1a851fe376c1) | total characters in document | total income in population |
| ![{\displaystyle T_{T}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2f0f690d607e62041991925f1c2defcd216c0950) | unused information space | unused potential in price mechanism<sup>[<i><a href="https://en.wikipedia.org/wiki/Wikipedia:No_original_research" title="Wikipedia:No original research"><span title="The material near this tag possibly contains original research. (June 2020)">original research?</span></a></i>]</sup> |
|  | data compression | progressive tax<sup>[<i><a href="https://en.wikipedia.org/wiki/Wikipedia:No_original_research" title="Wikipedia:No original research"><span title="The material near this tag possibly contains original research. (June 2020)">original research?</span></a></i>]</sup> |

## Decomposability\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=4 "Edit section: Decomposability")\]

According to the [World Bank](https://en.wikipedia.org/wiki/World_Bank "World Bank"),

> "The best-known entropy measures are Theil’s T (![{\displaystyle T_{T}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2f0f690d607e62041991925f1c2defcd216c0950)) and Theil’s L (![{\displaystyle T_{L}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ee8de51b033092db57d6f739ecc540e753eca3b)), both of which allow one to decompose inequality into the part that is due to inequality within areas (e.g. urban, rural) and the part that is due to differences between areas (e.g. the rural-urban income gap). Typically at least three-quarters of inequality in a country is due to within-group inequality, and the remaining quarter to between-group differences."<sup id="cite_ref-10"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-10">[7]</a></sup>

If the population is divided into ![{\displaystyle m}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a07d98bb302f3856cbabc47b2b9016692e3f7bc) subgroups and

then Theil's T index is

![{\displaystyle T_{T}=\sum _{i=1}^{m}s_{i}T_{i}+\sum _{i=1}^{m}s_{i}\ln {\frac {{\overline {x}}_{i}}{\mu }}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/022441b20a44d2249aa5b942211f0927a34e54e8) for ![{\displaystyle s_{i}={\frac {N_{i}}{N}}{\frac {{\overline {x}}_{i}}{\mu }}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5d6ef5092a8bf0fd8dd316f6709c81b7fed93f66)

For example, inequality within the United States is the average inequality within each state, weighted by state income, plus the inequality between states.

[![Map of economic inequality in the United States using the Theil Index. A high positive theil index indicates more income than population while a negative value shows more population than income. A value of zero shows equality between population and income.](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Theil_USCounties.png/500px-Theil_USCounties.png)](https://en.wikipedia.org/wiki/File:Theil_USCounties.png "Map of economic inequality in the United States using the Theil Index. A high positive theil index indicates more income than population while a negative value shows more population than income. A value of zero shows equality between population and income.")

**Note**: This image is not the Theil Index in each area of the United States, but of contributions to the Theil Index for the U.S. by each area. The Theil Index is always positive, although individual contributions to the Theil Index may be negative or positive.

The decomposition of the Theil index which identifies the share attributable to the between-region component becomes a helpful tool for the positive analysis of regional inequality as it suggests the relative importance of spatial dimension of inequality.<sup id="cite_ref-Spatial_decomposition_11-0"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-Spatial_decomposition-11">[8]</a></sup>

### Theil's _T_ versus Theil's _L_\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=5 "Edit section: Theil's T versus Theil's L")\]

Both Theil's _T_ and Theil's _L_ are decomposable. The difference between them is based on the part of the outcomes distribution that each is used for. Indexes of inequality in the generalized entropy (GE) family are more sensitive to differences in income shares among the poor or among the rich depending on a parameter that defines the GE index. The smaller the parameter value for GE, the more sensitive it is to differences at the bottom of the distribution.<sup id="cite_ref-12"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-12">[9]</a></sup>

GE(0) = Theil's _L_ and is more sensitive to differences at the lower end of the distribution. It is also referred to as the [mean log deviation](https://en.wikipedia.org/wiki/Mean_log_deviation "Mean log deviation") measure.

GE(1) = Theil's _T_ and is more sensitive to differences at the top of the distribution.

The decomposability is a property of the Theil index which the more popular [Gini coefficient](https://en.wikipedia.org/wiki/Gini_coefficient "Gini coefficient") does not offer. The Gini coefficient is more intuitive to many people since it is based on the [Lorenz curve](https://en.wikipedia.org/wiki/Lorenz_curve "Lorenz curve"). However, it is not easily decomposable like the Theil.

## Applications\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=6 "Edit section: Applications")\]

In addition to multitude of economic applications, the Theil index has been applied to assess performance of [irrigation](https://en.wikipedia.org/wiki/Irrigation "Irrigation") systems<sup id="cite_ref-13"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-13">[10]</a></sup> and distribution of [software metrics](https://en.wikipedia.org/wiki/Software_metrics "Software metrics").<sup id="cite_ref-14"><a href="https://en.wikipedia.org/wiki/Theil_index#cite_note-14">[11]</a></sup>

## See also\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=7 "Edit section: See also")\]

-   [Generalized entropy index](https://en.wikipedia.org/wiki/Generalized_entropy_index "Generalized entropy index")
-   [Atkinson index](https://en.wikipedia.org/wiki/Atkinson_index "Atkinson index")
-   [Gini coefficient](https://en.wikipedia.org/wiki/Gini_coefficient "Gini coefficient")
-   [Hoover index](https://en.wikipedia.org/wiki/Hoover_index "Hoover index")
-   [Income inequality metrics](https://en.wikipedia.org/wiki/Income_inequality_metrics "Income inequality metrics")
-   [Suits index](https://en.wikipedia.org/wiki/Suits_index "Suits index")
-   [Wealth condensation](https://en.wikipedia.org/wiki/Wealth_condensation "Wealth condensation")
-   [Diversity index](https://en.wikipedia.org/wiki/Diversity_index "Diversity index")

## Notes\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=8 "Edit section: Notes")\]

## References\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=9 "Edit section: References")\]

1.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-1 "Jump up")** [Introduction to the Theil index from the University of Texas](http://utip.gov.utexas.edu/papers/utip_14.pdf)
2.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-2 "Jump up")** ["Segregation Measures"](https://www.urban.org/research/data-methods/data-analysis/quantitative-data-analysis/segregation-measures). _www.urban.org_. Urban Institute. Retrieved 5 February 2018.
3.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-policymap_3-0) [<sup><i><b>b</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-policymap_3-1) Parker, Lauren (20 July 2015). ["Racial and Ethnic Segregation: In the News and On PolicyMap"](https://www.policymap.com/2015/07/racial-and-ethnic-segregation-in-the-news-and-on-policymap/). _PolicyMap_. Retrieved 5 February 2018.
4.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-:0_4-0) [<sup><i><b>b</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-:0_4-1) Conceicao, Pedro NMI2; Ferreira, Pedro M. (2000). ["The Young Person's Guide to the Theil Index: Suggesting Intuitive Interpretations and Exploring Analytical Applications"](http://www.ssrn.com/abstract=228703). _SSRN Electronic Journal_. [doi](https://en.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.2139/ssrn.228703](https://doi.org/10.2139%2Fssrn.228703). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier) "ISSN (identifier)") [1556-5068](https://www.worldcat.org/issn/1556-5068). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier) "S2CID (identifier)") [19009769](https://api.semanticscholar.org/CorpusID:19009769).
5.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-Formulas_5-0) [<sup><i><b>b</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-Formulas_5-1) [<sup><i><b>c</b></i></sup>](https://en.wikipedia.org/wiki/Theil_index#cite_ref-Formulas_5-2) [http://www.poorcity.richcity.org](http://www.poorcity.richcity.org/) (Redundancy, Entropy and Inequality Measures)
6.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-McDonald1974_6-0 "Jump up")** McDonald, James B; Jensen, Bartell C. (December 1979). "An Analysis of Some Properties of Alternative Measures of Income Inequality Based on the Gamma Distribution Function". _Journal of the American Statistical Association_. **74** (368): 856–860. [doi](https://en.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.1080/01621459.1979.10481042](https://doi.org/10.1080%2F01621459.1979.10481042).
7.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-10 "Jump up")** "6. Inequality Measures". [_Poverty Manual_](http://siteresources.worldbank.org/PGLP/Resources/PMch6.pdf) (PDF). [World Bank](https://en.wikipedia.org/wiki/World_Bank "World Bank"). 8 August 2005. p. 95. Retrieved 4 February 2018.
8.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-Spatial_decomposition_11-0 "Jump up")** Novotny, J. (2007). ["On the measurement of regional inequality: Does spatial dimension of income inequality matter?"](http://web.natur.cuni.cz/~pepino/NOVOTNY2007AnnalsofRegionalScience.pdf) (PDF). _Annals of Regional Science_. **41** (3): 563–580. [doi](https://en.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/s00168-007-0113-y](https://doi.org/10.1007%2Fs00168-007-0113-y). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier) "S2CID (identifier)") [51753883](https://api.semanticscholar.org/CorpusID:51753883).
9.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-12 "Jump up")** ["Inequality Measures"](https://www.urban.org/research/data-methods/data-analysis/quantitative-data-analysis/inequality-measures). _www.urban.org_. Urban Institute. Retrieved 5 February 2018.
10.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-13 "Jump up")** Rajan K. Sampath. Equity Measures for Irrigation Performance Evaluation. Water International, 13(1), 1988.
11.  **[^](https://en.wikipedia.org/wiki/Theil_index#cite_ref-14 "Jump up")** A. Serebrenik, M. van den Brand. Theil index for aggregation of software metrics values. 26th IEEE International Conference on Software Maintenance. IEEE Computer Society.

## External links\[[edit](https://en.wikipedia.org/w/index.php?title=Theil_index&action=edit&section=10 "Edit section: External links")\]

-   Software:
    -   [Free Online Calculator](https://archive.today/20121204174230/http://www.wessa.net/co.wasp) computes the Gini Coefficient, plots the Lorenz curve, and computes many other measures of concentration for any dataset
    -   Free Calculator: [Online](http://www.poorcity.richcity.org/calculator.htm) and [downloadable scripts](https://web.archive.org/web/20041012085224/http://luaforge.net/project/showfiles.php?group_id=49) ([Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python (programming language)") and [Lua](https://en.wikipedia.org/wiki/Lua_programming_language "Lua programming language")) for Atkinson, Gini, and Hoover inequalities
    -   Users of the [R](http://www.r-project.org/) data analysis software can install the "ineq" package which allows for computation of a variety of inequality indices including Gini, Atkinson, Theil.
    -   A [MATLAB Inequality Package](http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=19968) [Archived](https://web.archive.org/web/20081004090028/http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=19968) 2008-10-04 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"), including code for computing Gini, Atkinson, Theil indexes and for plotting the Lorenz Curve. Many examples are available.
