---
title: Primers in Complex Systems VI_ Viruses as - Ricard Sole
author: Ricard Solé
tags:
  - book
cover: _resources/books/Primers in Complex Systems VI_ Viruses as - Ricard Sole/cover_image.jpg
---


    
        
        
        Cover
        
            @page {padding: 0pt; margin:0pt}
            body { text-align: center; padding:0pt; margin: 0pt; }
        
    
    
        
            
                
            
        
    

      

![[index-1_1.png]]

VIRUSES AS COMPLEX

ADAPTIVE SYSTEMS

PRIMERS IN COMPLEX SYSTEMS

**EDITORIAL ADVISORY BOARD**

John H. Miller, Editor-in-Chief,

Carnegie Mellon University and Santa Fe Institute

Murray Gell-Mann, Santa Fe Institute

David Krakauer, Santa Fe Institute

Simon Levin, Princeton University

Mark Newman, University of Michigan

Dan Rockmore, Dartmouth College

Geoffrey West, Santa Fe Institute

Jon Wilkins, Santa Fe Institute

**VOLUMES PUBLISHED IN THE SERIES**

_Viruses as Complex Adaptive Systems_,

by Ricard Solé and Santiago F. Elena (2019)

_Natural Complexity: A Modeling Handbook_,

by Paul Charbonneau (2017)

_Spin Glasses and Complexity_,

by Daniel L. Stein and Charles M. Newman (2013)

_Diversity and Complexity_,

by Scott E. Page (2011)

_Phase Transitions_,

by Ricard V. Solé (2011)

_Ant Encounters: Interaction Networks and Colony Behavior_,

by Deborah M. Gordon (2010)VIRUSES AS

COMPLEX ADAPTIVE

SYSTEMS

_Ricard Solé and Santiago F. Elena_

P R I N C E T O N U N I V E R S I T Y P R E S S

_Princeton & Oxford_Copyright © 2019 by Princeton University Press

Published by Princeton University Press,

41 William Street, Princeton, New Jersey 08540

6 Oxford Street, Woodstock, Oxfordshire OX20 1TR

press.princeton.edu]]

All Rights Reserved

ISBN 978-0-691-15884-6

LCCN 2018954901

British Library Cataloging-in-Publication Data is available

Editorial: Alison Kalett and Lauren Bucca

Production Editorial: Brigitte Pelner

Jacket/Cover Credit: Cover art courtesy of Shutterstock

Production: Jacqueline Poirier

Publicity: Alyssa Sanford

This book has been composed in Adobe Garamond and

Helvetica Neue

Printed on acid-free paper ∞

Typeset by Nova Techset Pvt Ltd, Bangalore, India

Printed in the United States of America

1 3 5 7 9 10 8 6 4 2C O N T E N T S

_Preface_

ix

1. The Virosphere

[^1]: 

_1.1 Deep Microspace Field_

[^1]: 

_1.2 The Expanding Viral Universe_

[^7]: 

_1.3 Structural and Genetic Diversity_

[^9]: 

_1.4 Viral Planet_

[^15]: 

2. Alive or Dead?

[^19]: 

_2.1 Computation and Life_

[^19]: 

_2.2 Viruses as Replicating Machines_

[^22]: 

_2.3 Viruses as Phases of Matter_

[^25]: 

_2.4 Evolving Genome Reduction_

[^33]: 

_2.5 The Space of Replicators_

[^36]: 

_2.6 Adaptation at High Mutation Rates_

[^43]: 

_2.7 Viral Quasispecies_

[^45]: 

_2.8 Critical Genome Size_

[^53]: 

3. Landscapes

[^55]: 

_3.1 Climbing High_

[^55]: 

_3.2 Symmetric Competition_

[^62]: 

_3.3 Epistasis in RNA Viruses_

[^68]: 

_3.4 Experimental Virus Landscapes_

[^73]: 

_3.5 The Survival of the Flattest Effect_

[^77]: 

**vi**

Contents

_3.6 Virus Robustness_

[^82]: 

_3.6.1 Intrinsic Mechanisms of Mutational Robustness_

[^85]: 

_3.6.2 Extrinsic Mechanisms of Mutational Robustness_

[^86]: 

_3.7 Selection: Fitness versus Robustness_

[^87]: 

4. Virus Dynamics and Arms Races

[^91]: 

_4.1 Virus-Host Interactions_

[^91]: 

_4.2 HIV Multiscale Dynamics_

[^95]: 

_4.3 Population Dynamics of HIV Infection_

[^98]: 

_4.4 Spatial Dynamics of HIV-1_

[^105]: 

_4.5 Antigenic Diversity Thresholds and AIDS_

[^108]: 

_4.6 Viral Symbiosis_

[^116]: 

5. Epidemics

[^120]: 

_5.1 Outbreak_

[^120]: 

_5.2 SIS Model_

[^125]: 

_5.3 SIS Model in Space and Graphs_

[^130]: 

_5.4 AIDS: Modeling HIV-1 Transmission_

[^137]: 

_5.5 Halting Viruses in Scale-Free Networks_

[^141]: 

6. Emergent Viruses

[^149]: 

_6.1 Ecological Disturbance: Hanta- and Arenaviruses as_

_Case Studies_

[^152]: 

_6.2 The Genetics of Adaptation to Novel Host_

[^154]: 

_6.2.1 Becoming Specialists_

[^156]: 

_6.2.2 Becoming Generalists_

[^158]: 

_6.2.3 The Causes of Specialization_

[^161]: 

_6.3 Epidemics of Emergence_

[^162]: 

7. Origins

[^168]: 

_7.1 Are Viruses Inevitable?_

[^168]: 

_7.2 Evidence from Digital Evolution_

[^170]: 

_7.3 Where Do Viruses Come From?_

[^176]: 

_7.3.1 Regressive Hypothesis_

[^176]: 

_7.3.2 Cellular Origin Hypothesis_

[^177]: 

_7.3.3 Protobiont Hypothesis_

[^178]: 

_7.4 Viruses and the Origin of Cells_

[^185]: 

_7.5 Viruses as Sources of Evolutionary Novelties_

[^187]: 

_7.6 But . . . What Is a Virus Then?_

[^188]: 

Contents

**vii**

8. Computer Viruses and Beyond

[^190]: 

_8.1 Viruses as Programs_

[^190]: 

_8.2 Emergence of Computer Viruses_

[^191]: 

_8.3 Cancer, Languages, and Minds_

[^197]: 

_References_

[^203]: 

_Index_

[^219]: P R E F A C E

Few examples of the way complexity unfolds in nature (and

beyond it) are as fascinating as viruses. Viruses are hypothesized

by some to predate the origins of life and its micro- and

macroevolutionary play. They strongly influence energy flows

in complex ecosystems. They maintain all kinds of relationships

with their hosts, from mutualism to pure parasitism. They are

responsible for some of the most deadly pandemics and yet have

been coevolving with us throughout all our common history.

They have played a major role in our understanding and manip-

ulation of life and have also attracted the interest of biologists,

physicists, and computer scientists alike.

Many key questions emerge when thinking of their nature and

relevance: What exactly are they? Are they living entities? How

did they originate? How similar are computer viruses to their

living counterparts? How complex can they become? What is

their role in shaping the evolution of complex organisms? What

role have they played in the development of society? Can they be

compared with software programs, to be run inside their hosts,

who provide the appropriate hardware? Why are there so many

new emergent viruses and how do they emerge? These questions

will be addressed in this book.

**x**

Preface

Viruses are complex systems, spanning orders of magnitude

in size, and an enormous variety of life cycles and habitats.

But the study of their behavior and structure, particularly from

interdisciplinary frameworks, has also revealed a number of

universal patterns of organization. RNA-based viruses display

high mutation rates, as predicted by theoretical developments

from the 1970s. They live at the edge of disorder, where high

instability but also adaptability occur. This edge is related to

a phase transition phenomenon, and its presence is tied to the

genetic nature of populations, often described as quasispecies.

Other viruses, such as the mimiviruses, are so big that they are

actually larger than some of the smallest cells we know. Their life

cycle reveals surprising properties, placing them in a new position

as a parasitic life form. We will discuss the potential boundaries of

the viral morphospace and their importance, as well as theoretical

models of viral population dynamics and self-assembly. Models

and theoretical approximations have played a key role in this

area, in particular the concept of fitness landscapes given their

importance in defining the dynamics of their genetically complex

populations.

Viruses have shaped the evolution of cells, organisms, ecosys-

tems and even the biosphere. Such influence spans all scales of

biological organization, from genomes to the planet (figure 1]]).

Their dynamics involve nonlinear phenomena, tipping points

and self-organization processes that have many commonalities

with other biological and nonbiological systems. Such similarities

might hide universal properties that pervade complexity and in

this respect viruses offer a unique window into the origins of

complex systems. In this context, we will also pay attention to

other systems, such as computer viruses, that share unexpected

similarities.

Although many excellent books exist concerning the popula-

tion biology and ecology of viruses or the role they have played

within the context of epidemics, there is no major contribution in

![[index-12_1.png]]

Preface

**xi**

Marine viruses drive the

large-scale turnover

Ecological disturbance a

of bacterial cells and

allows viruses to spill over

indirectly (but deeply)

from reservoirs to new hosts

influence climate and

geochemical cycles

Epidemics caused by viral

Bacteria-phage and other

agents have a major impact

virus-host interaction

networks drive biodiversity

changes at the community

Viruses are required to

level

complete the life cycles of

several species of insects,

such as parasitoids

Endogenous retroviruses

are required for the

RNA viruses infecting

maturation and

vertebrates have triggered

development of vertebrate

the evolution of a complex

placenta

and hypervariable immune

cell response.

The evolution of cells has been

deeply influenced by their

interaction with intracellular

Molecular innovations,

parasites

including the origin of

DNA from ancestral RNA

molecules

Origin of first molecular

replicator parasites

Figure 1. All scales of life are affected by and affect the diversity and

evolution of viruses in the biosphere. In this diagram, some key processes

and phenomena influenced or caused by viruses are indicated (central

picture after Odum and Barrett (2005)).

the existing literature that provides the unifying picture presented

here. The book has been written to be of interest to researchers

and graduate students in virology, evolution, mathematical bio-

logy, and physics of complex systems. But we also hope it will

be appealing to advanced undergraduate students interested in

**xii**

Preface

broad questions about viruses: where they come from, where

they may go, and whether they are alive or not. Because of

its multidisciplinary nature, some parts of the book require

familiarity with intermediate-level algebra and calculus. Similarly,

the book requires a basic understanding of molecular biology and

the processes of information flow within the cells from DNA to

proteins. We have made an effort to write every chapter in the

most intelligible way, and more biology-oriented readers may skip

over the mathematical details but still catch a good sense of what

models represent and prove.

We would like to thank our many colleagues within virology

and complex systems who have been helpful in shaping the

ideas presented here, from both the experimental and theoretical

sides, including some researchers, visitors, and good friends from

the Santa Fe Institute. In particular, we would like to thank

Lin Chao, Paqui de la Iglesia, Esteban Domingo, Stephanie

Forrest, Fernando García-Arenal, Murray Gell-Mann, John J.

Holland, Stuart Kauffman, Eugene Koonin, Chris Langton,

Susanna Manrubia, Melanie Moses, Andrés Moya, Tom Ray,

Rafael Sanjuán, Josep Sardanyés, Joan Saldanya, Peter Schuster,

Paul Turner, Sergi Valverde, Eörs Szathmáry, Mark Zwart, plus

a quite long list of PhD students, postdocs, technicians, and

collaborators both in Barcelona and in València

The late physicist John Wheeler said about science: ‘We live on

an island surrounded by a sea of ignorance. As our island grows, so

does the shore of our ignorance.” This applies too to the particular

island that defines today’s understanding of viruses. Very often,

new discoveries deeply change our perspective, expanding our

understanding of the viral universe while the shoreline enlarges

and new questions emerge. We hope this book will help the reader

to walk safely across the tangled boundaries between the mainland

and the uncharted waters.

VIRUSES AS COMPLEX

ADAPTIVE SYSTEMS1.2. The Expanding Viral Universe

**7**

EBOV, on the other hand, represents a good example of

another emergent pathogen notable for the bloody and deadly

way in which it interacts with the human host. But in this

case, the rapid damage caused to the patients prevents the virus

from spreading on a global scale. However, poverty, reduced

investment in healthcare, and some cultural factors have to be

blamed for most EBOV outbreaks.

1.2 The Expanding Viral Universe

The impact of this hidden _virosphere_ on ecosystem functioning

can be summarized by means of some basic numbers (Suttle 2005;

Weitz 2017). The number of viruses that might be present in

the entire marine biota is 1030 (a 1 followed by 30 zeros) and

the number of infection events taking place every second would

amount to no less than 1023. As a consequence of infections,

viruses kill around 20% of the total microbial biomass in a

single day, thus forcing a constant and large-scale population

turnover. Since the microbial component of the marine biota

is responsible for a major fraction of energy flows, the obvious

consequence is that large-scale ecological processes are strongly

constrained by the viral component of the biosphere. Marine

viruses illustrate one of the most obvious results of ecological

research: the realization that our planet is dominated by microbes

and, very especially, by viruses.

In figure 1.4]] we summarize this dominance using two main

quantitative measures: total biomass and population abundance

in marine communities. The biomass is clearly dominated by

bacteria, with prokaryotes and viruses following closely in small

fractions. However, the total number of individuals clearly differs

from what is represented in the biomass picture (figure 1.4]] left).

Here viruses greatly outnumber other taxa, consistently with our

previous picture. As pointed out by Koonin and Dolja (2013), it

![[index-23_1.png]]

**8**

Chapter 1. The Virosphere

Total biomass

Abundance

PROKARYOTES

VIRUSES

PROTISTS

PROTISTS

VIRUSES

PROKARYOTES

Figure 1.4. Viruses are by far the most abundant biological entities in

the oceans, comprising approximately 94% of the nucleic acid-containing

particles, but they only amount for 5% of the total biomass. By contrast,

even though prokaryotes represent less than 10% of the nucleic acid-

containing particles, they represent more than 90% of the biomass

(diagram adapted from Suttle (2007)).

can be claimed that the water in the ocean is literally a virus soup

with up to 109 viral particles per milliliter.

A very different but not less rich facet of the viral universe

plays a crucial role in our own bodies. It is well known that a

human needs to be seen not as an isolated entity carrying around

20,000 genes, but instead as a complex consortium of species. In

particular, we are the carriers of a vast ecological web of interac-

tions that take place among the many species of microorganisms

that colonize our mouth, lungs, gut, or skin. This is known as

the _microbiome_. The microbial part of ourselves carries around

three million additional genes and has been coevolving with us

for millions of years (Boulang and Nagler 2016; Wesemann and

Nagler 2016; Taur and Pamer 2016). After the recognition of the

major impact of the microbial part of our nature, the so-called

_virome_, a no less interesting problem has to do with the inevitable

role played by the microbe’s parasites (Minot et al. 2016).



1.3. Structural and Genetic Diversity

**9**

The example used above provides just a first glimpse of the

enormous relevance of viruses. In this chapter, we will provide an

overview of the complexity of the virosphere, addressing several

key questions: What is this virosphere made of? How have viruses

so successfully expanded over every single scale from bacteria to

humans and even to other viruses? Is this virosphere very diverse?

These questions will help to define the vast scenario that we plan

to explore in this book. It is not only an extraordinary example

of our biosphere’s complexity; viruses themselves are a rich, and

sometimes unexpected, instance of complex systems that perfectly

illustrates the tempo and mode of complexity evolution and how

it pervades nature.

1.3 Structural and Genetic Diversity

Viruses inhabit a domain of size ranges that spans the broad

interval between molecular structures and cells. Some viruses

are so small that it took a long time to detect them (figure 1.5).]]

They were first reported in 1892 by Dmitri Ivanovsky, a Russian

scientist who was studying the process of transmission of a

tobacco disease. Some unknown pathogen was damaging the

plant tissues and in an experiment he filtered a suspension of

infected tissues through a ceramic filter, which was known to

retain bacterial cells. Once filtered, the suspension was free of

bacteria and yet capable of infecting, indicating that a smaller class

of biological agent was responsible for the disease. In this way,

the first virus was discovered: _Tobacco mosaic virus_ (TMV). Other

scientists independently confirmed the existence of this new class

of entities, and the invention of the electron microscope was,

along with the development of molecular genetics, an especially

important breakthrough, since those invisible agents became

visible and their internal structures and genetic components

became available to study.

![[index-25_1.png]]

![[index-25_2.png]]

**10**

Chapter 1. The Virosphere

Red

blood

Flu virus

Animal cell

Pollen

cell

Mitochondria

C60

Protein

Human

Atom

egg

Plant cell

Frog

Lipids

egg

Bacteria

**Relative sizes on a logarithmic scale**

0.1 nm

1 nm

10 nm

100 nm

1 μm

10 μm

100 μm

1 mm

Light microscope

Electron microscope

Figure 1.5. Viruses occupy an intermediate position between the macro-

molecules and living cells and organelles. Most of them are 102 times

smaller than the smallest cells, though the discovery of many giant viruses

along the last decade has changed this view.

Because of their simplicity, viruses cannot replicate outside

of the cellular context. They need the cell machinery to make

copies of themselves (see chapter 2),]] and that of course makes

a big difference. What is perhaps most impressive of viruses is

that they are paramount examples of diversity in all kinds of

contexts. They embody a vast range of replication strategies and

structural forms of organization, spanning orders of magnitude

in genome size and complexity. At the lowest extreme of the

complexity continuum are the viroids, which are small folded

RNA chains no more than a couple of hundred nucleotides long

that do not encode any protein (Flores et al. 2014). At the

other end of the complexity are viruses so large that they were

initially mistaken for bacteria. This group includes mimiviruses,

iridoviruses, pithoviruses, pandoraviruses, and other members of

the brotherhood of giant viruses. In figure 1.6]] we show a few

![[index-26_1.png]]

1.3. Structural and Genetic Diversity

**11**

Satellite Tobacco

Ribgrass

Cowpea Chlorotic

Densovirus

Feline

Bacteriophage M52

Mosaic Virus

Mosaic Virus

Mottle Virus

1dnv

Panleukopenia Virus

2ms2

1a34

1rmv

1fpv

Human Papillomavirus Bacteriophage G4 Foot and Mouth

Hepatitis B Virus

Bacteriophage

Norwalk Virus

L1 Capsid

1gff

Disease Virus

1qgt

Phi-X174 procapsid

1ihm

1dzl

1bbt

1al0

Human Rhinovirus 16 Nudaurelia Capensis

Dengue Virus

Bluetongue Virus

Human Papillomavirus

& cellular receptor

Omega Virus

1k4r

inner layer

1l0t

1d3e

1ohf

2btv

Bacteriophage PRD1

Reovirus Core

1gw7

1ej6

Bacteriophage HK97

1fh6

Rice Dwarf Virus

1uf2

Paramecium Bursaria Chlorella Virus

1m4x

50 nm

Figure 1.6. Some examples of regular structures found in viruses, from

very small, such as _φ X_ 174, whose genome was the first to be sequenced,

to the largest known mimiviruses, which involve hundreds of genes and

have a size even larger than that of the smallest bacteria.

**12**

Chapter 1. The Virosphere

examples of some well-known viruses so we can appreciate the

broad range of sizes. The smaller viruses include the famous

_φX_ 174, the first entity whose genome (a circular, single-stranded

DNA molecule) was fully sequenced (Sanger et al. 1977). The

genome of this bacteriophage involves just 5,386 nucleotides,

required to encode 11 proteins. But we can also find smaller

viruses with some interesting traits besides their tiny size. This

is the case of the satellite RNA of TMV, with a 1,063 single-

stranded RNA genome which codes just for the capsid and one

other protein. This satellite infects tobacco plants already infected

with TMV, worsening their symptoms. In this case the satellite

virus (that is why this name) needs the cell machinery both of the

plant _and_ the one from its host virus, TMV.

At the other extreme of the size spectrum, we have a member

of the _Mimiviridae_ family, including the largest known viruses.

The first microscope observations (in 1992) found them infecting

amoebas, and given their large size and staining properties they

were assumed to be gram-positive bacteria. A correct identifica-

tion of these microorganisms as true viruses took place eleven

years later (La Scola et al. 2003). Since then, many other types

have been found (Abergel et al. 2015). Their genome size is

comparable with that of cellular genomes, and can be longer

than one million base pairs. The finding of this group (as will

be discussed in chapter 7)]] created novel views of the boundaries

between living and nonliving entities.

An especially remarkable feature of viruses is their enormous

genetic diversity. This diversity is not just a matter of size and

composition: it is about the logic of the replication and its

evolutionary consequences for the rest of life on earth. There is a

striking contrast between the homogeneous nature of information

processing that takes place in the nonviral world and what

occurs in the virosphere. Cellular genomes replicate thanks to a

highly complex molecular machinery based on the transcription

of a double-stranded DNA molecule into an RNA chain that

1.3. Structural and Genetic Diversity

**13**

is single-stranded, which itself is then translated by another

equally giant molecular complex (the ribosomes) into the proteins

necessary to build the whole replication complex (Crick 1970).

All cellular organisms respond to this pattern, with very rare

deviations. In the virosphere, by contrast, _all_ kinds of RNA

and DNA combinations and interconversions among them are

observable. Such a broad spectrum of genetic strategies allows

for a potential evolution that makes viruses a true “genomic

laboratory” (Koonin and Dolja 2013). Indeed, one of the first

attempts to classify viruses into groups with similar properties was

by David Baltimore (1971), based on the type of genetic material

(either DNA or RNA, single- or double-stranded) and replication

strategy. According to Baltimore’s scheme seven groups of viruses

can be defined (figure 1.7):]]

1. Group I is formed by those viruses having a

double-stranded (ds) DNA genome. They usually

replicate in the nuclei of infected cells and use cellular

proteins for their replication. Examples are the herpes

viruses and the smallpox virus.

2. Group II includes all viruses having a single-stranded

(ss) DNA genome. They also use the cellular machinery

for their replication. Examples are the Canine

parvovirus and the plant geminiviruses.

3. Group III have dsRNA genomes and replicate in the

cytoplasm of the infected cells. They encode for their

own replication enzymes. Examples are some fungal

viruses.

4. Groups IV and V are the most abundant classes and

have genomes of ssRNA of either positive sense

(group IV) or negative sense (group V). Positive sense

means that the molecule encapsidated can directly be

translated by the cellular translation machinery,

whereas negative sense means that the molecule

**14**

Chapter 1. The Virosphere

**DNA viruses**

**RNA viruses**

**Retro-transcribing viruses**

ds DNA

ss DNA

ds RNA

ss RNA (+)

ss RNA (–)

ss RNA (RT)

ds DNA (RT)

Genetic material present in the viron

Group I

Group II

Group III

Group IV

Group V

Group VI

Group VII

DNA (+/–)

DNA (+)

RNA (+/–)

RNA (+)

RNA (–)

RNA (+)

DNA (+/–)

Reverse

transcription

DNA (+/–)

RNA (–)

Reverse

transcription

mRNA

Proteins

Figure 1.7. A simplified schematic representation of Baltimore’s classi-

fication of viruses according to the nature of their genomes and their

replication intermediates. Adapted from Flint et al. (2015).

encapsidated has to be first transcribed into its

complement and then can be translated into proteins

by the cellular ribosomes. Most known viruses belong

to one of these two families: TMV, _Hepatitis C virus_

(HCV), _Foot-and-mouth disease virus_, EBOV, _Yellow_

_fever virus_, and the several influenza viruses.

5. Group VI corresponds to viruses having a positive sense

ssRNA genome that is replicated via an intermediate

DNA molecule. This group corresponds to the

well-known retroviruses whose most characteristic

1.4. Viral Planet

**15**

representative is the HIV-1. All retroviruses encode for

an enzyme, the reserve transcriptase, that synthetizes

DNA using RNA as template.

6. Group VII corresponds to dsDNA viruses that replicate

through an ssRNA intermediate. This small group of

viruses, whose representative is _Hepatitis B virus_ (HBV),

also encodes for a retrotranscriptase (Baltimore 1971;

Flint et al. 2015).

No less important here is the fact that viruses have coevolved

with their hosts since life began on our planet. This is parti-

cularly obvious from the study and sequencing of genomes of

plants and vertebrates, which display large amounts of virus-

related sequences (Aiewsakun and Katzourakis 2015; Ryan 2016;

Mushegian and Elena 2015).

1.4 Viral Planet

Since their discovery, the importance of viruses and the under-

standing of their ecological and evolutionary impact have only

been growing over the last century. It was revealed early that

they are responsible for many human diseases, and their genetic

plasticity and easy manipulation were crucial in the early days

of molecular biology, when bacteriophages (viruses infecting bac-

teria) were used to test many fundamental ideas concerning the

nature of heritable information and the genetic code (Morange

2000; Creager 2002; Cairns et al. 2007). As mentioned above,

it was later found that they have a great impact in the ecology

of marine ecosystems, with major consequences not only for

populations, but for the planet as a whole (see below).

Our biosphere is a complex adaptive system (Levin 1998)

where multiple scales of organization are shaped by a number of

physical, developmental, ecological, and historical factors. In all

these scales viruses play a relevant role. Matter and energy flows

**16**

Chapter 1. The Virosphere

take place through tangled networks of interacting species. A vast

range of biomasses are involved, from the largest animals to the

smallest cells. But every single organism has at least one, if not

many, virus associated to it. Both unicellular and multicellular

life forms are rich niches where a virus can find opportunities to

evolve. The interactions among hosts and viruses are not always

parasitic (see chapter 4)]] and often lead to disease outbreaks that

can have great consequences (discussed in chapter 5).]] Getting

back to the oceans, since viruses have a great impact in the

population dynamics of their hosts, and indirect impact on other

organisms that prey on their hosts, they also affect deeply the

large-scale dynamics of nutrient cycles (Weitz 2016).

Figure 1.8]] summarizes the magnitude of the impact of viruses

on carbon cycling in the oceans. For comparison, figure 1.8a]]

displays the effects of anthropogenic activities associated to the

intensive use of fossil fuels along with the role played by land

forests. The basic network of carbon flows2 is described in

figure 1.8b.]] Viruses kill plankton cells at a rapid pace, leading

to both particulate organic carbon (POC) and dissolved organic

carbon (DOC). Instead of sinking to the depths, where huge

amounts of carbon are being stored, both become suspended

or dissolved and thus do not sink. Without the presence of

viruses, a large fraction of planktonic carbon is retained in

surface waters where it can respire and be photo-oxidized and in

chemical equilibrium with the atmosphere. The lytic infection

triggered by viruses results in further viral particles and in a

complex mixture of molecular pieces forming the cellular debris.

This includes small molecules (both monomers and polymers),

colloids, and cellular fragments. Most of these components will

be incorporated into bacteria and other organisms living in the

upper ocean layer (Fuhrman 1999).

2Carbon flows are given in Gigatonnes (Gt) per year. A gigatonne indicates

one billion tonnes or 1015 grams.

![[index-32_1.png]]

![[index-32_2.png]]

![[index-32_3.png]]

of

just

eath

of

d

POC

**50 Gt**

the

UV

on

(instead

effects

surface

no

ells

their

water

2

**93 Gt/y**

ted c

of

CO

DOC

**700 Gt**

viruses

the

y

ec

**3 Gt/y**

b

**150 Gt/y**

sis of plankt

to

ess

Ly

Uninf

and detritus sink

ecause

oc

B

n

close

ical and

o

ted

ec

virusy

scale.

inf

b

atmosphere.

Biolog

Plankt

chemical pr

remains

the

**90 Gt/y** 2

in

CO

planetary

lysis

2

a

no

**ean**

at

cell

CO

**e**

of

**5 Gt**

ermocline

**Oc**

h

**38,500 Gt**

Plankt

T

from

cycling

**805 Gt + 4 Gt/y**

balances

**Atmospher**

(POC)

he

carbon

the

carbon

affects

on

**5 Gt/y**

organic

strongly

Fossil fuel use

impact

hisT

deep

**Fossil fuels 7,000 Gt**

a

particulate

ave

ocean).

h

deep

resulting

estation

the

**2 Gt/y**

Viruses

or

the

Def

1.8.

into

Figure

plankton,

sinking

**18**

Chapter 1. The Virosphere

Viruses define in some ways the coastline of life; little can

be understood about evolution of the biosphere without taking

viruses into account as major (perhaps dominant) players. It is

often said that life is almost everywhere in the planet except inside

volcanoes and similar hyper-extreme environments. We can also

say that viruses thrive everywhere where life has flourished. This

might well be the case for _any_ life we find in other worlds,

with molecular parasites inevitably associated to self-replicating

autonomous entities. In this book we aim to explore the origins

of their special status, their universal features and origins from a

complex systems perspective. Moreover, viruses are not confined

to life. Their properties and propagation dynamics have been an

inspiration for understanding the rise of some key evolutionary

novelties, such as language and other aspects of cultural and

technological evolution.

**2**

A L I V E O R D E A D ?

2.1 Computation and Life

Molecular biology and information technology (IT) emerged

almost simultaneously around the middle of the twentieth

century and have evolved in parallel since then. Despite the

great differences existing between living structures and computer

hardware and software, a continuous exchange of ideas and

terms took place in the early development of both disciplines

(Maynard Smith 2001). An interesting convergence also took

place. Engineers building the new technological engines capable

of manipulating information used previous theoretical models of

computation (as defined by Alan Turing), but they also actively

contributed to another important (and much older) domain: the

coding and decoding of messages.

Around the 1950s, coding and decoding secret information

became a major target of the Cold War efforts. Computer

designers and programmers had also to find ways of performing

computations at the lowest cost. The early machines were still

expensive and had a limited power, and everything needed

to be properly designed under strong constraints. That meant

writing short, optimized programs, using appropriate coding

schemes, and compressing information. A struggle that was being

**20**

Chapter 2. Alive or Dead?

performed by small living beings already for billions of years of

evolution, although such a race was unnoticed to any scientist

by the time the IT revolution started. The reason we mention

these similarities between the two fields is that they require the

presence of machines ( _in silico_ or _in vivo_) capable of executing

programs. These two components of computation are usually

known as hardware and software, and for understanding the

nature of viruses we need to approach the question of how close

they are to containing these two components.

The classical view of viruses, seen as intracellular parasites

requiring the available molecular machinery to replicate them-

selves, suggests that we can consider them as some sort of

program. In this context, viruses would mainly be considered as

encapsulated pieces of software, to be executed by the cellular host

hardware. In all these cases, the function that is being executed is

a _computation_, and using this concept will be extremely useful

in our exploration of viruses as computational objects. The idea

of a general machine capable of performing computations was

formalized in theoretical terms by the British mathematician Alan

Turing.1 In figure 2.1]] we display a mechanical implementation of

Turing’s view of a machine performing computations (Hopcroft

1984; Bennett and Landauer 1985). Here a computer is repre-

sented by a printing head moving along a long tape where symbols

are written and can be read and typed by the machine. Despite

the simplicity of this _Turing machine_, it can be shown that (given

enough time) it can perform any computation executable by any

digital computer.

An interesting and often unnoticed implication of Turing’s

result has to do with the molecular counterparts of the Turing

1Turing’s goal was not to define computing machines but instead to address

a major problem posed by David Hilbert concerning a way to define a systematic

method to establish the truth or falsity of any mathematical statement. The

turing machine’s formulation of the method is a proof that no such method

exists.

![[index-36_1.png]]

2.1. Computation and Life

**21**

**a**

**b**

• • • 0

**0** 0

1

0

0

1 • • •

RNA

A read/write head

RNApol (head)

tape

• • • 0

1

**0** 1

0

0

1 • • •

B

DNA (tape)

• • • 0

1

0

**1** 0 0

1 • • •

B

Figure 2.1. The Turing machine (a) is the abstract representation of a

computational device that can be built in such a way it can perform any

operation done by a computer. It is defined in terms of an infinite tape

where 0’s and 1’s are written and that can be read and written on by a

“head.” This head moves along the tape, changing its internal state in a

deterministic way. Several molecular processes within cells (b) remind us

of this scheme. Here the RNA polymerase is shown “reading” the DNA

chain and “writing” an RNA molecule as a result (adapted from Goodsell

(2012)).

machine. Usually, the Turing approach to computation is only

connected with computer viruses (see chapter 8),]] with no special

attention to real viruses. When Turing formulated his theory,

molecular biology did not exist and no one knew that molecular

information was in fact stored in long (sometimes very long)

polymer chains. Moreover, the process of transcription and

translation strongly resembles the Turing metaphor (figure 2.1b).]]

Such a match between a purely mathematical approach (Tur-

ing’s machine does not pretend to entail a real computer) with

the molecular logic of information processing and molecular

replication is remarkable. It points toward a universal form of

performing computations that might be inevitable when physical

polymers are at work.

If cells include (among other things) these molecular machines

capable of identifying and reading biological polymers, it seems

clear that viral genomes can be seen as pieces of tape with start2.3. Viruses as Phases of Matter

**25**

suggests that, if applicable, viruses are less than self-replicating

machines, since they are actually dependent upon the operations

executed by the machines they infect. Is this a formal argument

against viruses as living systems?

2.3 Viruses as Phases of Matter

In chapter 1]] we presented an overview of the diversity of known

viruses. We paid attention to the differences in organization, size,

ecological adaptation, and lifestyle. Moreover, in the previous

sections we considered the nature of viral replication and virus life

cycles from a complex systems, logical perspective. As it happens

with their life forms, target hosts, and strategies of infection, the

ways viruses reproduce span a wide array of possibilities. At the

level of both structure and function, molecular parasites seem

to display a great variety of designs. Indeed, the viral universe

is vastly diverse and changing, but there are also some key,

generic mechanisms associated to virus development that reveal

deep and common physical processes pervading viral complexity.

Similarly, there are strong constraints to structural organization in

a large class of spherical viruses that remind us of the fundamental

role played by physics. All these features are connected with the

hardware of the system, and by inspecting its nature we can also

better locate viruses within the abstract computational schemes

outlined above.

Typically, the size of a given viral particle is proportional to

the size of its genome. But it was early well known that the

genome was much smaller, in terms of mass, than the total

mass of the whole viral particle. This observation prompted

Watson and Crick in particular to suggest that the viral capsid

should be composed by the association of multiple copies of

basic capsid protein(s). As noted by these authors (Crick and

Watson 1956, 1957), the capsids of many viruses are formed

from a minimum number of gene products, given the small

size of viral genomes. As a consequence, spherical viruses should

![[index-41_1.png]]

**26**

Chapter 2. Alive or Dead?

Figure 2.3. Packing a closed volume by using simple geometrical motifs.

The left image shows five so-called _Platonic_ shapes, obtained by using

an identical motif (triangles, squares, pentagons, etc.) and packing them

so that they minimize the resulting surface. Spherical viruses almost

universally pack their genetic material by using icosaedra (right) through

a process of self-assembly of multiple capsomers.

have the symmetry of regular polyhedra, also known as _Platonic_

_solids_ (figure 2.3).]] In these objects, all faces are identical perfect polygons that correspond to protein units. An icosahedron would

be formed by 60 of such units, in which all protein units sit

in identical environments; the largest shell of this kind is an

icosahedron consisting of 60 equivalent subunits. Subsequent

capsid structure determinations confirmed the special role of

icosahedral symmetry, but also indicated that larger numbers of

protein subunits were involved.

Spherical viruses and rod-like structures are two major classes

of generic forms associated to mature virions infecting all types

of hosts, from bacteria to higher plants and mammals. All these

viruses are made by a tightly packed, regular distribution of

a limited number of subunits forming capsids. The process of

capsid assembly involves geometry, since regular packing needs

some geometric constraints at the level of units. The fact that no

virus carries out metabolic activity by itself indicated that, unlike

cells, their assembly could be understood in terms of standard

2.3. Viruses as Phases of Matter

**27**

equilibrium thermodynamics. An elegant confirmation of this

idea was the discovery that under _in vitro_ conditions the rod-

like TMV self-assembles spontaneously and unassisted into fully

infectious viral particles (Frankel 1955). The basic sequence is

summarized in figure 2.3a,]] where the self-assembly process is dis-

played. One single monomer unit gets polymerized into a helical

structure, and this is a thermodynamically favorable process. Here

the helical structure is an intrinsic property of the protein, which

gets organized into disks (Klug 1999). The RNA gets attached

to the growing rod as time proceeds. Regularities in the pattern

of TMV genomic RNA folding into secondary structures serve

as packaging signals, repeated according to capsid symmetry, aid

formation of the required capsid protein conformers at defined

positions, resulting in significantly enhanced assembly efficiency.

The precise mechanistic roles of packaging signal interactions

may vary between viruses (Stockley et al. 2013).

The widespread relevance of self-assembly mechanisms in

orchestrating the causal process behind virus morphogenesis has

an interesting consequence. It depends on energy-driven, physical

forces, which have no direct connection with genetics or biology.

They can be directly associated to physical laws, and thus we

can treat viral assembly as a physics problem that might be more

complex than a simple physics problem involving point particles

and orbits, but it is in the end no different from the point of view

of molecular forces and energy minimization processes (Rossman

and Rao 2012).

How can such model be formulated and what are its conse-

quences? Several studies have used well-defined physical models

of capsomer structure and capsomer interactions, usually based

on different extensions of well-known reaction kinetic models

including self-assembly and polymerization (Kushner 1969), and

in particular physical models of viral assembly based on the

minimization of energy functions (Bruinsma et al. 2003; Zandi

et al. 2004; Hagan 2014). Among the most interesting results

![[index-43_1.png]]

![[index-43_2.png]]

**28**

Chapter 2. Alive or Dead?

**a**

**b**

0.9

Finite

stacks

Single-helix

phase

phase

0.7

3’

5’

Disk

phase

ength 0.5

Ionic str 0.3

A-protein

phase

0.1

3’

3’

5’

5.0

6.0

7.0

8.0

9.0

10.0

pH

Figure 2.4. Self-assembly and growth of the TMV particle. The basic

monomers required to build the entire virus particle self-assemble, form-

ing a characteristic ordered, helical structure. The RNA chain attaches to

this growing structure. The picture displays a phase diagram showing the

ranges over which particular structural patterns of protein assemblies are

stable (redrawn from Klug (1999)). Here two parameters are used, namely

the pH and the ionic strength.

offered by these theories when applied to spherical viruses is

the finding that the limited repertoire of possible icosahedral

“solutions” corresponds to the minima of an energy landscape

(Bruinsma et al. 2003), showing that physics pervades the con-

straints associated to the universe of viral forms. One important

side effect of this result is the explanation for the discrete nature

of possible icosahedral viruses and their “mathematical” nature

(Stewart 1999).

The simplest picture of self-assembly processes is provided by

a kinetic model leading to a dynamical pattern of aggregation

characterized by the presence of a phase transition behavior (Dill

and Bromberg 2011). This can be illustrated by a minimal model

where a set of _n_ monomers4 aggregates into an aggregate. If we

4We use this model to discuss the self-assembly of viruses, but it has

been used in many other contexts, particularly in the formation of micelles

(Mouritsen 2005).

2.3. Viruses as Phases of Matter

**29**

indicate by _A_ 1 a single building block and by _An_ the assembled

system, the reaction for the whole process would be described by

_K_

_n A_ 1 −→ _An,_

(2.1)

where _K_ = [ _An_] _/_[ _A_ 1] _n_ is the associated equilibrium constant. If we indicate by _C_ 0 the initial concentration of _A_ 1, the reaction

kinetics for _A_ 1 would be described by a nonlinear equation

_d A_ 1 _/dt_ = − _K An_ 1 whose solution is given by

1

_C_

_n_−1

_A_

0

1( _t_ ) =

_,_

(2.2)

1 + _K C_ 0( _n_ − 1) _t_

which can be shown to display two markedly different behaviors

as a function of the equilibrium parameter. This can be done

by looking at the fraction _ν_( _x_ ) of components associated to

assembled aggregates as a function of _K_ , where _x_ = [ _A_ 1]. Since

[ _A_ 1] + _n_[ _An_] is the total number of monomers and [ _A_ 1] + [ _An_]

is the total number of “objects” (either aggregates or single

monomers), it can be shown that

_ν_( _x_) = 1 + _nK xn_−1 _,_

(2.3)

1 + _K x n_−1

which exhibits a sharp transition close to a critical value

_xc_ = _K_ −1 _/_( _n_−1)

(2.4)

jumping from 1 to _n_ (i.e., from all _A_ 1s single to all in aggregate).

This cooperative behavior indicates that, once a given con-

centration of monomers is reached, the system experiences a

rapid (and irreversible) transition into large structures with a

characteristic size. This occurs in a thermodynamically favored

direction, and thus the resulting assemblies are highly stable

structures. In a chemical system formed by inert molecules, self-

assembly takes place by an energy-minimization process (that is

captured in the irreversible reaction described above), eventually

ending up in stable assemblies. An infective virus particle will

**30**

Chapter 2. Alive or Dead?

create the conditions for this transition as more and more copies

accumulate until the right conditions for assembly are met. It can

be said that the final part of the developmental path followed by

a spherical virus life cycle requires a cooperative transition.

The specific application of this approach to the self-assembly

of viral capsids can be used to obtain an expression for the fraction

of capsids _f_ ( _ρ_) present in a given system (such as the inner space

of the cell) as a function of the monomer concentration ( _ρ_),

assuming that (as before) we neglect all molecular intermediates

except free subunits (Hagan 2014). If we the total concentration

of capsid units _ρT_ is given by

_ρT_ = _ρ_ 1 + _NρN_

(2.5)

where _N_ is the number of capsomers in one capsid, and _ρ_ 1

and _ρN_ are the densities of single subunits and whole capsids,

respectively, define the fraction of subunits in capsids as

_fc_ = _NρN_

_ρ_ ;

(2.6)

_T_

a critical concentration _ρ_∗ exists such that a phase transition

occurs, separating a sub-critical phase with essentially no self-

assembly of viral particles, i.e.,

_ρ_

_N_

_f_

_T_

_c_ ( _ρT_ ) ≈

_ρ_∗

(2.7)

for _ρT_ _ρ_∗, and another phase where virus capsids form, and

_f_ reads

_ρ_∗

_fc_ ( _ρT_) = 1 − _ρ_

(2.8)

_T_

when _ρT_ _ρ_∗. The phase transition curves predicted from the

model are displayed in figure 2.5a,]] using three different values of

_N_. An experimental test of this model is shown in figure 2.5b,]]

where different concentrations of capsid subunits have been

used under variable salt concentrations (which enhance the self-

assembly process).

![[index-46_1.png]]

2.3. Viruses as Phases of Matter

**31**

**a** 1.0

0.8

0.6

_f_

0.4

0.2

0.0 0

2

4

6

_ρ_/ _ρ_*

**b** 1.0

0.7 M NaCl

0.8

0.5 M NaCl

0.3 M NaCl

0.6

_f_

0.4

0.2

0.0 0

2

4

6

8

10

12

14

Dimer concentration

Figure 2.5. Phase transition in the capsid assembly process. In (a) we

show the predicted theoretical result _fc_ ( _ρT_) = 1 − ( _ρ_∗ _/ρT_) for (from left to right) _N_ = 12,60, and 1,000, respectively. _f_ ( _ρ_) represents the fraction of capsids present in a given system as a function of the monomer

concentration ( _ρ_). An experimental test of this theoretical result is

provided in figure (b) using empty capsids of HBV (inset) under different

dimer subunit and salt concentrations. Adapted from Hagan (2014).

The need for self-assembly, in both cells and viruses, implies

that part of von Neumann’s scheme described above needs to be

mapped into an embodied set of rules that cannot be separated

from the self-organized nature of living matter. This is indicated

**32**

Chapter 2. Alive or Dead?

Virus

Cellular hardware + software

New viruses

software + capsid

_Pν_

_Cν_

_Φ_(A + B + C)

_Φν_

_Φν_

_Φ_’’ _ν_

(A + B + C)

_Φ_’ _ν_

_Φ_’ _ν_

_Φν_

_Φν_

_Φν_

_Φν_

Self-assembly

Figure 2.6. The extended von Neumann scheme for viral replication

when both capsid and genome are considered. Here a virus is defined

by a blueprint _φv_ packed within a closed boundary _Cv_ made of a given

number of identical proteins _Pv_ (left). Once it infects the cell, the viral

information makes use of both _A_ and _B_ to build capsid proteins and new _φv_. Instead of a controlled process of development, viral packing involves

self-assembly (dashed box) leading to a packed capsid containing a copy of

the original genome, although mutated versions ( _φ_ _, φ_) are also possible.

in the extended von Neumann diagram shown in figure 2.6.]] The

two main differences (in relation to the scheme of figure 2.2)]] are

the existence of a physical-driven mechanism of organization that

is not encapsulated by the “program” given by _φ_ and the fact that

the outcome of the process can include a different blueprint as

a result of mutations. What other factors can modify the initial

scheme? Since viruses can be more complex and interact with

the three components of the cellular machinery ( _A_, _B_, _C_ ), and

even themselves carry pieces of molecular machinery, the resulting

interaction scheme can be far from a simple cell versus virus

mixture.



2.4. Evolving Genome Reduction

**33**

These results provide useful insight into the ways some viruses

exploit the self-organization properties of matter to create order

out of chemical homogeneity.5 These results suggest that we can,

to some extent, look at viruses as molecular entities with some

special capabilities associated to reproduction. But there is much

more. In the next two sections we will consider first a classical

experiment where such prevalence of chemical self-replication is

the final outcome of artificial evolution. Secondly, we will look

at the space of replicators to see if this simple image of viruses is

correct.

2.4 Evolving Genome Reduction

An essential part of genome evolution has to do with the ex-

pansion and shrinking of genomes. In simple life forms, genome

complexity correlates with genome length, since the information

content stored in the genome needs to be made compact in

order to compress all required instructions while replicating in

an efficient way. For viruses, if more complex sets of decisions are

required to infect their hosts, replicate, assemble, move out, or

integrate, larger genomes are expected to be required. What hap-

pens when we relax this constraint and allow genomes to change?

What lessons can we learn from this? In 1970, a classical set

of experiments performed by Sol Spiegelman provided a unique

instance of evolution toward simpler genomes and illustrated

some key ideas on viruses, replicators, and the power of selection

(Spiegelman 1970).

Using the Q _β_ phage, Spiegelman created the conditions for

replication of RNA viruses in a cell-free context (figure 2.7).]]

Specifically, RNA chains of this phage, with a genome of

5In reality, the situation is much more complex, since viruses also make use

of cellular proteins, named chaperones that dynamically help in folding other

proteins.

![[index-49_1.png]]

**34**

Chapter 2. Alive or Dead?

transfer 1

transfer 2

last transfer

t=0

incubation

incubation

incubation

Figure 2.7. Evolution of shorter RNA genomes was observed in transfer

experiments using cell-free conditions where shorter Q _β_ molecules gen-

erated by mutation won a fitness advantage by the virtue of being shorter

and replicating faster.

_ν_ ∼ 4,500 nucleotides length, were placed in a test tube along

with free nucleotides and the Q _β_ replicase required to replicate

the RNA chains. In these conditions RNA molecules can make

copies of themselves, along with mutations caused by the error-

prone replication machinery. Among other types of mistakes,

shorter sequences can be generated. After one of these incubation

processes has been completed and no more RNA chains are

formed, a sample of the final soup is transferred to a new test

tube under the same original conditions.

These transfers are repeated a number of times. As this artificial

selection experiment proceeded, it was found that shorter and

shorter sequences were obtained after each round of selection.

Since no cells are present, any part of the Q _β_ genome not

required to bind to the replicase becomes superfluous and at

the end of the experiment the resulting chains had just _ν_ ∼ 200

nucleotides and were completely unable to infect cells.

The experiment is relevant for several reasons. On the one

hand it fully illustrates the power of selection, leading to the sur-

vival of the fastest: the shorter, the better. No other trait than fast

speed (and thus short length) is at work. This actually corresponds

2.4. Evolving Genome Reduction

**35**

to the simplest standard replicator competition model, which can

be described as a set of _n_ equations,

_d xi_ = _f_

_d t_

_i xi_ − _xi_ ( _t_ ) _,_

(2.9)

where _x_ = ( _x_ 1 _, ..., xn_) indicates the populations of replicators (such as different RNA sequences in Spiegelman’s experiment),

each one growing at a given rate _fi_ . Here no mutations are con-

sidered and only competition is introduced in the last term, ( _x_ ),

of the right-hand side. If we impose the condition

_x_

_i_

_i_ = 1,

which provides a population limit, it is easy to see that the sum

over all the populations gives

_n_

_dx_

_n_

_n_

_i_ = _d_

_x_

=

_f_

_x_

_d t_

_d t_

_i_

_i xi_ −

_i_ ( _t_ ) _,_

(2.10)

_i_=1

_i_

_i_=1

_i_=1

and, since

_x_

_i_

_i_ is constant, this gives

_n_

( _t_) =

_fi xi ,_

(2.11)

_i_=1

which is nothing but the average replication rate _f_ , and thus

the previous set of equations can be written as

_d xi_ = ( _f_

_d t_

_i_ − _f_ ) _xi ,_

(2.12)

which has one single winner: the one with the highest replication

rate. Since shorter strings are expected to be faster replicators, the

expected outcome of this simple model is that smaller genomes

must be the winners.

What kinds of viruses are selected, beyond those with small

size? Further experiments (Mills et al. 1967) revealed that as RNA

particles became shorter, they also were less infective, and at some

point most sequences were simply unable to infect their original

host cells. In other words, once freed from the host cell context,

all elements required for the virus life cycle associated to infection

are simply removed as useless. No cell context, no infection.

**36**

Chapter 2. Alive or Dead?

If we return to von Neumann’s scheme of a formal replicating

machine, Spiegelman’s experiment has an interesting implication.

Once the virus becomes independent of all host-dependent com-

ponents, the context-free machinery gets closer to the “virus as

software”: a tape being read by a molecular machine that makes

new copies. What is the lower bound? One key requirement for

replication is the molecular recognition between RNA and its

replicase. A too-short chain would fail to be recognized and thus

no replication would take place (Adami 2006).

So far, the biology of cells and viruses seems to be about

replicators and their parasites. Cells replicate by means of a

regulated machinery that follows von Neumann’s scheme. Viruses

instead would be the outcome of the rich molecular toolkit

provided by the cellular context. The picture, however, is more

interesting, and the separation between viral and cellular life less

sharp than it seems.

2.5 The Space of Replicators

The result of von Neumann’s inquiry was a logical scheme

that captures what is really crucial for an autonomous entity to

complete a replication cycle. It is probably not an accident that

here theory and molecular biology match quite well: perhaps the

logic of self-replicating life has only one logical form. We use

this theoretical picture because we would like to understand this

fundamental property of living matter as a key for answering the

question “what is life?” And since any answer will need to provide

the boundaries of the problem, we can say that viruses define

the coastline of living complexity. It could be argued that to

answer our previous question we just need to answer first another

question, namely: “are viruses alive?” But it turns out that things

are not easy here either.

Viruses, as we have already discussed, can replicate themselves

provided that a given cellular context is present. However, the

broad spectrum of interactions among viruses and their hosts

2.5. The Space of Replicators

**37**

and an accurate list of properties defining life reveal a much

more tangled picture (Koonin and Starokadomsky 2016). As

an example, viruses are often considered nonliving because they

lack the metabolic activity that is required to maintain cellular

structures. On the other hand, living cells also include potential

dormant states that are practically considered alive but are no less

inert than viral particles outside their hosts. In these dormant

systems, no growth or detectable metabolism will take place over

very long periods of time. Are these dormant phases alive?

To further explore this question, Koonin and Starokadomskyy

have used the _replicon paradigm_ to properly define the space

of possible forms of living organization where the degree of

autonomy and selfishness in particular can be used as quali-

tative axes (Koonin and Starokadomskyy 2016). The starting

point requires defining (and distinguishing between) replicons

and replicators. The latter can be identified with autonomous

replicating units (Dawkins 1982; Szathmáry 2006) displaying

some autonomy with respect to genome replication. To a large

extent, this corresponds to von Neumann’s formulation, since

both definitions assume that the “genome” is associated—in a

stable manner—with a replicator. As defined, a replicator can

contain a genome but also a number of additional “replicons”,

i.e., units of replication lacking the autonomy of a full replicator.

As an example, an eukaryotic cell is a replicator carrying several

replicons, whereas the genome of an intracellular organelle is a

true replicon. Clearly a major feature that needs to be considered

here is the degree of autonomy displayed by the replicator. One

could easily conclude that viruses are nonautonomous replicators

whereas cells are equipped with full autonomy. But a close

analysis questions this view.

The previous definition suggests an almost binary split

between the two types of units; a careful consideration of the

properties of different replicators gives a richer and less clear-cut

picture. Following again Koonin and Starokadomskyy (2016) we

define a three-dimensional space of replicators (figure 2.8a)]] where

![[index-53_1.png]]

**38**

Chapter 2. Alive or Dead?

**a**

**c**

Vi

V ro

ir ids

oids

Ly

L tic DNA V

ytic DNA

Int

n e

t ins

eins

Te

T mperate

emperat V

e V

Ly

L tic RNA V

ytic RNA

elfishnessS

Non-lytic V

Non-lytic V

Retro

Retr -V

-

Non-

Non-co

c ding R

oding RT

Tr

T a

r nsposons

ansposons

Chro

Chr mosomes

omosomes

**d**

y

Small P

Larg

Lar e P

Small P

ge P

Org

Or anelle DNA

ganelle DNA

tion

Rolling-

Rolling-C P

P

oduc

ooperativitC

ce pr

Autonomy

Resour

**b**

**e**

Lytic DNA V

Lytic RNA V

Viroids

Retro-V

Inteins

Temperate V

Non-coding RT

elfishness

Non-lytic V

S

Transposons

**f**

y

Large P

Small P

Rolling-C P

ooperativitC

Organelle DNA

Chromosomes

Autonomy

Figure 2.8. The space of replicators. (a) Here we arrange the location of

different classes of replicating systems, from the smallest to the largest,

using three basic coordinates involving the degree of selfishness (vertical

axis) as well as autonomy and resource production. The projections reveal

discrete classes. The diagram is inspired in Koonin and Starokadomskyy

(2016). In (c–f) we display four examples of replicons (see text for details).

_P_ corresponds to DNA plasmids while _V_ corresponds to viruses.

three axes are used to characterize (in an approximate way) the

locations of different replicators. The vertical axis introduces the

degree of selfishness: lower values are associated to cooperative

2.5. The Space of Replicators

**39**

replicators; more parasitic replicators occupy the upper part. A

second axis calibrates the degree of autonomy displayed by the

different replicators. Finally, a third axis introduces the number

of resources required (or modified) to complete the replicators,

reproduction. Despite the three axes being continuous, the actual

locations of known replicators seem clustered in distinct subsets,

as shown in figure 2.8b,]] where only the projected planes are

shown. These four classes plus chromosomes are highlighted by

means of light closed lines.

Looking at the autonomy-selfishness plane, we see that four

classes are delineated by the criteria of presence or absence of

signals for replication and/or transposition and the respective

protein machinery. In this projection, five occupied quadrants

are defined. The upper and lower domains would separate selfish

from cooperative systems, whereas the three sets within the hori-

zontal axis reveal three levels of autonomy, involving (from left to

right) the types of signals enabling the replicative autonomy. Two

basic classes can be defined either as parasitic or cooperative. Here

the first class includes some obvious members such as lytic viruses

that grow and eventually destroy their hosts and others (such as

retrotransposons) that simply spread within their host genomes

(sometimes constituting the majority of them). Plasmids,6 on the

one hand, are strongly dependent on the host replication cycle

and can provide advantages to their hosts, thus acting as coopera-

tors. Chromosomes, on the other hand, are the cellular replicators

encoding a whole repertoire beyond the pure replication function

and are clearly separated in the autonomy axis.

6A plasmid is a small DNA molecule that lives inside a cell and is physically

separated from chromosomal DNAs and can replicate independently. It is

most commonly found in bacteria as a small circular, double-stranded DNA

molecule. Plasmids also exist in archaea and eukaryotic organisms. In nature,

plasmids often carry genes, for example, antibiotic resistances or virulence

factors, that may benefit the survival of the host organism (Thomas and

Summers 2008).

**40**

Chapter 2. Alive or Dead?

The third axis is a useful, orthogonal dimension that also

defines a potential continuum. Here we introduce the number of

resources that are produced and/or modified by the correspond-

ing replicator. Here two major categories are present (Koonin and

Starokadomskyy 2016). One group includes complex replicators

that make (or import) either all or part of the resources, as

one would expect from cell-like entities. The second broad class

encapsulates those simple replicators lacking any of these features,

which would correspond to virus-like, parasitic entities. In this

context, our third axis weights the resource autonomy of different

replicators.

But here there are blurred boundaries that change everything.

Many life forms clearly fitting the cell-like class require a cel-

lular or multicellular host from which energy and resources are

extracted. One example of such blurred limits is represented by

endosymbiotic bacteria that live inside the cytoplasm of their host

cells and are absolutely dependent on the host cell for replication

and survival (Archibald 2015). An alternative example at the

other extreme is represented by the cyanophages, a particular

class of large bacteriophages that infect marine cyanobacteria of

the genera _Synechococcus_ and _Prochlorococcus_ and that contain in

their genomes key genes involved in the light harvesting apparatus

used by these bacteria and plant chloroplasts (Clokie and Mann

2006). But the most important outsider in this scheme is the

“nonproducers” that carry very large genomes coding (among

other things) for enzymes and other key molecules that affect

cellular metabolism and biosynthetic pathways. These large-sized

nonproducers, particularly members of the weird _Mimiviridae_

family, challange the binary scheme by placing themselves in an

intermediate position.

In 1992 microbiologists from the Universities of Leeds and

Marseille described what they thought was a tiny gram posi-

tive bacteria infecting the amoeba _Acanthamoeba polyphaga_, and

named it _Bradfordcoccus_. A decade later, Claverie and co-workers

2.5. The Space of Replicators

**41**

Phagocytosis

Mimivirus in a vacuole

0h

12h

Mature virion

factory

0h–1h

6h–12h

Startgate

3h–6h

capsid opening

1h–3h

Early virion factory

Figure 2.9. Life cycle of a giant virus. Here the sequence for the

mimivirus _Acanthamoeba castellanii_ is shown. This 12-hour cycle involves

several marked phases that are illustrated by some snapshots obtained

from electron microscopy. Redrawn from Claverie and Abergel (2010).

published an astonishing paper in _Science_ (Raoult et al. 2004)

concluding that the tiny bacteria in reality was a giant virus, as

never seen before, which indeed belongs to Baltimore’s group I

(i.e., with a dsDNA genome). This virus was name _Mimivirus_

and was the first of its class. This was the first in a run of

discoveries in which larger and larger viruses, all sharing genomic

properties and conserved genes, were found and characterized.

The largest one added to the family was the huge _Pandoravirus_,

with a genome size similar to that of some eukaryotic parasites

(Philippe et al. 2013). As was the case for the _Mimivirus_, the

_Pandoravirus_ was also known before its characterization as a virus.

In 2008 a German clinical microbiologist, Patrick Scheid, study-

ing amoebae living in the contact lenses of a woman suffering

from ocular keratitis described what he called endocytobionts,

**42**

Chapter 2. Alive or Dead?

particles of about 1 _μ_ m size, living inside the amoebae. All these

giant viruses infect unicellular amoeba. These giant viruses are so

different from any other viruses that they share a characteristic

property of cellular organisms: they have their own parasites.

Two classes of molecular parasites hosted by mimiviruses

have been so far described. First, the Sputnik virophages, named

analogously to the bacteriophages that infect bacteria (La Scola

et al. 2008). Sputnik satellites have a dsDNA genome, larger than

some bona fide viruses, of about 18 kb and encoding for about

20 proteins. Sputnik, however, parasitizes the functions encoded

by its helper mimivirus and has been shown to be involved in

the transfer of genes between mimivirus species. Second, as cells,

the mimivirus genomes also carry transposable elements, in this

case named transpovirons (Desnues et al. 2012). Transpovirons

are linear DNA elements of about 7 kb that encode about

seven protein-coding genes needed for their own mobilization.

Some of these genes are homologous to Sputnik’s own genes.

All mimiviruses share some structural, genomic, and functional

similarities with some long-time known members of Baltimore’s

group I viruses (see chapter 1),]] for example, poxviruses infecting

vertebrates (including humans) and arthropods. Well-known

examples are the smallpox (variola), vaccinia and cowpox viruses.

All together, these viruses are known as the nucleocytoplasmic

large DNA viruses or NCLDVs. NCLDVs share a core set of

47 genes that include enzymes involved in DNA replication and

repair, transcription factors, and proteins that interfere with host

cell proliferation (Colson et al. 2013). Such a level of complexity,

closer to the cellular machinery than to the standard view of viral

software, is puzzling. We will return to this in chapter 7.]] Let us

just mention for now that the virophage concept challenges the

simple picture of viral software using cellular hardware to replicate

itself. In fact, the ways virophages act on the _Mimivirus_ molecular

replication machinery strongly reminds us of the diagram of virus

infecting cells.

2.6. Adaptation at High Mutation Rates

**43**

2.6 Adaptation at High Mutation Rates

Although most viruses share striking similarities with computer

programs, they depart from this analogy in several ways. On

the one hand, the parasitic software carried by these tiny agents

makes no sense unless we place it in the context of a preexisting

cell machinery that is hijacked to guarantee virus replication. As

with the rest of biology, viral life cycles make sense only under

the light of evolution. And evolution requires both variation and

selection, even when dealing with man-made computer viruses

(see chapter 8).]] Mutation is not a component of software. On the

other hand, almost by definition, programs need to preserve even

their minor components from mistakes. Viruses instead might

need to face the challenge of a host organism that fights back, and

as a consequence an arms race between viruses and their hosts

ensues (see chapter 4).]] One particularly remarkable outcome of

such an arms race is that instability is pushed to the limit.

In previous sections of this chapter, we mentioned the promi-

nent role played by information and computation as defining

traits of living entities. Because of their intrinsic simplicity, and

due to their strong dependence upon a host molecular machinery

in order to replicate, viruses are unique dynamical systems. One

particularly important trait of RNA viruses is their high mutation

rates, much higher than any other rates exhibited by cellular

systems and a consequence of the lack of repair mechanisms asso-

ciated to their RNA-dependent RNA polymerases. This enzyme

catalyzes the replication of RNA from an RNA template, and

mutation rates per nucleotide and replication cycle are in the

range 10−4–10−5 (Sanjuán et al. 2010). In DNA-based systems,

such as cells, the process of DNA polymerization is usually

associated to a proofreading and repair mechanism that effectively

reduces mutation rates to a range 10−8–10−11, ensuring a con-

trolled replication cycle (Drake et al. 1998). In stark contrast,

RNA polymerases lead to high mutation rates that are orders of

**44**

Chapter 2. Alive or Dead?

magnitude larger. Since high mutation carries a burden of phe-

notypic errors, that implies that many resulting viral genomes can

contain deleterious changes leading to nonviable viral particles.

Mutation is a crucial component of evolution, as genetic

variability is the fuel on which natural selection operates to adapt

populations to their environment. In this sense, an error-prone

polymerase can be seen as useful in order to keep pace with the

always changing environmental conditions in which RNA viruses

live (Domingo 2000). However, keeping in mind that mutation

is a random process independent of the value that the mutations

generated may have in the future generations, mutation itself

is a double-edged sword: too many mutations per genome may

simply drive fitness levels so low that they are not compatible

anymore with a succesful replication. Therefore, mutation rates,

like any other trait, themselves have evolved and have been

optimized for the lifestyle of RNA viruses: just high enough

but not more (Elena and Sanjuán 2005). For RNA viruses, a

heterogeneous population results in a so-called _viral quasispecies_.

A viral quasispecies can be seen as a swarm of genomes dominated

by a _master sequence_ that may coincide with the average sequence

of the population, the consensus sequence.

The quasispecies structure has many implications on the

biology of RNA viruses. The most important is that the swarm

stores a reservoir of phenotypes crucial for coping with environ-

mental uncertainties: within the context of the virus infection and

pathogenesis, that includes the host responses tied to immunity

but also others such as tissue specificity or resistance to drugs

(Andino and Domingo 2015; Domingo et al. 2012; Lauring and

Andino 2010; Holmes 2010).

One particularly unexpected consequence of the quasispecies

nature of viral populations is deeply tied to information. This

is known as the _error catastrophe_ problem (Eigen 1971; Eigen

et al. 1987; Schuster 1994; Domingo and Holland 1994) and

is deeply connected with phase transitions in physics. It was

2.7. Viral Quasispecies

**45**

originally defined within the context of an abstract population of

mutating and replicating molecules (or entities), generically called

_replicators_, competing for limiting resources. More precisely,

Eigen and Schuster considered a (large) population of strings

(genomes or polymers) where each sequence can replicate at

some rate. Replication rate will be sequence-dependent and the

relation between sequence and growth rate should be expected

to be complex (see chapter 3).]] Additionally, we assume that

every time a chain replicates, mutations can occur at a given

rate _μ_. Eigen (1971) predicted that mutation imposes a limit

on the amount of information (in terms of genome length, _ν_)

that is consistent with stable information. Specifically, it was

shown that there is a critical mutation rate _μc_ ∼ 1 _/ν_ beyond

which no Darwinian evolution can occur. His theoretical work

(see below) thus made a key prediction: no viable sequences

would be observable for mutations higher than the critical one,

i.e., for _μ > μc_ . In that case, random drift would be observed.

Instead, below the threshold, selection operates and information

can be maintained in stable ways. Available information confirms

this inverse relationship, as shown in figure 2.10a.]] Mutation

rates decrease as an inverse power law of genome length. RNA

viruses exhibit the highest rates, orders of magnitude larger than

DNA viruses, as dramatically illustrated by viroids. These are

extremely small viruses, equipped with a minimal, non-protein

coding genome (figure 2.10b)]] that infects plants and uses their

RNA polymerases to replicate. As larger genomes are analyzed,

mutation rates rapidly decay. Two questions emerge: What is

the origin of such a relationship? What are the limits (if any) on

mutation rates in viruses?

2.7 Viral Quasispecies

Because of their high mutation rates, RNA virus populations

are highly heterogeneous, thus defining a cloud of mutationally

**46**

Chapter 2. Alive or Dead?

**a**

10–2

Viroids

10–3

RNA viruses

10–4

10–5

_μ_ ~ _ν_–1

10–6

ssDNA

_μ_

viruses

10–7

Higher

dsDNA

Bacteria

eukaryotes

10–8

10–9

10–10

Lower eukaryotes

10–11

109

108

107

106

105

104

103

102

1010

_ν_

**b**

**A**

**A**

U U

**G** U

C

**A**

·

**A**

80

··

**U**

**–**

G

**U**

A

·

U

·

**A**

·

·

A

·

160

·

·

· · · · · ·

**U**

· · · · · · · · **U**

·

C

·

·

C

·

·

C

· · ·

·

·

120

· ·

**+**

·

**A**

G

**+C**

··

A

G

A

· · · ·

· · ·

**C** U

· ·

· · · · ·

· · · · ·

· · · ·

· · · ·

· · · · ·

· · ·

U

·

C

G

U

G

C U

A

A

·

1

**U**

·

G

**U**

· · · · · **G**

· ·

200

·

·

A·

·

C

**U**

**A C A**

· U

C

·

A

**U**

40

·

·

· C

**A**

·

· · · ·

U ·

U

·

·

G

·

·

G

U

**A**

A

C

·

G· U

A

·

·

**C**

**C**

**A**

A

A

G ·

G U

U

·

C

**G**

**U**

**G**

·

240

·

**U**

**C**

**G** 360

**A**

·

G

··

U

A

A

U

· · · · ·

· · · · ·

· · · · ·

· · · G · ·

U

G

A G

**A** U · · 280

G

**–** C

**A**

· ·

**A**

**–**

**U**

C G

C U

**G**

· · · · ·

C

**U**

320

· · ·

**U** C G· ·

Figure 2.10. A scaling law in per-site mutation rate versus genome size.

(a) Includes chosen examples of RNA viruses, including the _Chrysanthe-_

_mum chlorotic mottle viroid_ (CChMoVd), with a 399-nucleotide genome,

with a secondary structure displayed in (b). Larger genomes are repre-

sented by both ss and ds RNA and DNA viruses, microbes, and a few

eukaryotes (adapted from Gago et al. (2009)). The continuous line is used

to highlight the inverse law linking mutation rate _μ_ and genome length

_ν_ predicted by the error threshold theory.

2.7. Viral Quasispecies

**47**

related sequences (Eigen et al. 1989; Domingo et al. 1989, 2012).

There is thus a mutant spectrum, rather than a genome or a

small collection of genomes, and it is more than simple sets of

independent mutant sequences. Instead, viral quasispecies involve

a repertoire of variants that can help overcome selection pressures.

A mathematical approach to the behavior of these mutant clouds

was provided by the Eigen-Schuster model. This model considers

a set of populations { _xi_ } representing the abundance of different

genomes, changing in time by the following set of equations:

_d x_

_i_ =

_f_

_d t_

_j μ_( _j_ → _i_ ) _x j_ − (**x** _, t_ ) _xi ,_ (2.13)

_j_

where _xi_ indicates the fraction of the population associated to

the _i_ th mutant genome equipped with an _M_-letter alphabet (here

_i_ = 1 _, ..., n_, where _n_ = _Mν_ is very large) so that a normalization

condition applies, namely,

_x_

_j_

_j_ = 1. Here _f j_ is the growth

rate of the _j_ th mutant, _μ_( _j_ → _i_) is the probability of having a mutation from sequence _j_ to sequence _i_, and (**x**) is the average fitness associated to the population vector **x** = ( _x_ 1 _, ..., xn_), i.e.,

⎛

⎞

(**x** _, t_) =

_f_

⎝

⎠

_j x j_

_μ_( _j_ → _i_) =

_f j x j_ = _f_ _._

_j_

_j_

_j_

(2.14)

This model can sometimes be treated analytically under a well-

defined set of conditions, showing that the population structure

corresponds to a cloud of sequences (Eigen 1971; Eigen et al.

1987; Schuster 1994). Let us consider a specific case that will

illustrate how mutation can sharply limit the length of genomes

and thus the amount of information stored in a quasispecies.

Consider the general model described above and now use only

two values for the replication (fitness) of genomes, namely _fm_ for

the master and _f_ for any other sequence (i.e., _f_ 1 = _f_ 2 = _..._ =

_fn_ = _f_ ), where _n_ is very large ( _n_ 1). Hereafter we assume

**48**

Chapter 2. Alive or Dead?

**a**

_x_ 1

_f_

_x_ 2

_m_ (1 – _μ_)

_x_

•

_m_

•

•

_xi_





2.8. Critical Genome Size

**53**

2.8 Critical Genome Size

As discussed above, a scaling law seems to connect the mutation

rate of a given genome and its mutation rate (figure 2.10a).]] We

are now in a position to mathematically derive this remarkable

dependence. In our previous calculations, _μ_ defines the mutation

rate (for each replication round) per genome. But the accurate

definition of mutation requires considering the units forming

each string of length _ν_. If _μb_ is the mutation rate per site, it is

not difficult to see that it is related to _μ_ by

_μ_ = 1 − (1 − _μb_) _ν._

(2.32)

Here _p_ = (1 − _μb_) _ν_ is the probability that none of the units

are mutated; the difference 1 − _p_ is the probability that some unit

(and thus the genome) does mutate. Since _μb_ is typically small,

we can use the approximation7

_μ_ ≈ 1 − _e_− _μbν_ ≈ 1 − _μbν._

(2.33)

If we return to the previous critical condition for mutation

rates and write it down as a function of _μb_, we have

_α_

_μc_ = _,_

_b_

_ν_

(2.34)

where _α >_ 0 is a constant. The last expression actually cor-

responds to the observed inverse decay of mutation rates as

an inverse of their genome size (figure 2.10a).]] In particular,

RNA viruses have been shown to follow this inverse law, thus

being consistent with Eigen’s theory. Many different extensions

of these models have been proposed (Manrubia et al. 2010)

considering, for example, more complex landscapes (Saakian et al.

2006; Saakian and Hu 2006; Schuster 2016), spatial dynamics

(Altmeyer and McCaskill 2001; Pastor-Satorras and Solé 2001;

7Here we made use of the first two terms of the Taylor expansion of the

exponential function, i.e., _e x_ ≈ 1 + _x_ + _x_ 2 _/_ 2! + _..._ .

**54**

Chapter 2. Alive or Dead?

Aguirre and Manrubia 2008), or the role played by secondary

structure on phenotypic thresholds (Ancel and Fontana 2000;

Stitch et al. 2007), to cite just two.

We can appreciate that the model is very simple and yet very

rich in dynamical complexity and—what is more important—

makes a well-defined prediction: There is an upper bound to the

rate of disorder that an adaptive system can tolerate. Nowadays we

know that RNA viruses live on the edge of catastrophe (Schuster

1994; Domingo and Holland 1994; Solé et al. 1996), taking

advantage of the mixture of order and disorder characteristic

of critical points. An interesting consequence of this result is

that, since the error threshold is a phase transition point, it

defines a sharp boundary separating two phases, one of which

involves the loss of the master sequence. Once this occurs, a

uniform diffusion of populations will take place within the non-

master set, losing the quasispecies structure, and no Darwinian

adaptation can occur. The theory thus predicts that even a small

increase of mutation rates beyond _μc_ leads to the extinction

phase. Experimental tests using mutagenic drugs fare consistently

with this prediction, indicating that a potential path (particularly

combined with other therapies) to fight viral populations could

increase mutagenesis (Loeb et al. 2000; Perales et al. 2012). This

provides an elegant example of how phase transitions could be

exploited to fight disease in nonstandard ways.8

8More generally, the dynamical behavior of RNA quasispecies is relevant to

several aspects of therapeutics (Perales et al. 2012), including the outcome of

multidrug treatments and the role played by population fluctuations.**62**

Chapter 3. Landscapes

population condition

_x_ ( _s , t_) = 1 the function reads (see

_s_

previous chapter):

( _t_) =

_f_ ( _S_) _x_ ( _S_ _, t_) = _f_ _._

(3.8)

_S_

Despite the popularity of the fitness landscape picture inter-

preted as a more or less irregular surface, this view is, in most

cases, misleading. Instead of this picture in which populations

crawl across hills and valleys in search of higher locations, the

right picture deals with high-dimensional sequence spaces formed

by vast neutral networks linking equal-fit genotypes (Aguirre et al.

2011 and references therein). Among other things, the view of

populations getting trapped on some local fitness peak vanishes.

As we will show in this chapter, the structure of the fitness

landscape is more interesting and can often lead to unexpected

properties.

3.2 Symmetric Competition

Before we move into some intricacies associated to rugged land-

scapes, let us consider a simple experiment with RNA viruses.

The example illustrates how the landscape picture can be helpful

in explaining some counterintuitive observations (Clarke et al.

1994). In the experiment, two strains of the _Vesicular stomatitis_

_virus_ (VSV, figure 3.3a)]] were mixed and allowed to evolve and compete with each other. Specifically, two clonal populations of

VSV having the same fitness were shown to exhibit steady gains in

fitness using standard virus plaque assays (Novella et al. 1995).4

As they evolved through time, each strain evolved by increasing

4Genetically marked monoclonal antibody resistant (MARM) clones of

equal fitness to the wild-type VSV were used and their relative frequencies

were monitored along passages by exposing the mixture to the corresponding

antibody and counting the number of viruses capable of growing in its presence

and absence, respectively.

![[index-78_1.png]]

3.2. Symmetric Competition

**63**

**a**

**b**

102

wto

101

100

10–1

10–2

tion of oritional ratio t

rac 10–3

F

0

10

20

30

40

50

Passage

Figure 3.3. Experimental evolution of two competing clones of (a) VSV.

In (b) we display three examples of the competition passages using

BHK-21 cells as hosts. Here the points indicate the measured fractions

of the two clones. Redrawn after Clarke et al. (1994).

its replication rate by an equivalent amount, indicating that

both populations were able to keep competing while constantly

changing. In figure 3.3b]] three outcomes (among many) of the

experiment are shown. The general pattern found here is that

both populations remain close until, after a given number of

passages, their trajectories diverge.

The fact that both populations remain close despite both

populations experiencing fitness increases is a counterintuitive

result. Since these populations compete for resources, one would

expect rapid divergences right from the beginning: the faster

replicator should overcome the slower one. Such a change, where

both populations display an increase in order to just keep in

place, indicates that this is a good illustration of the famous

Red Queen5 effect (Van Valen 1973; Stenseth and Maynard-

Smith 1984). Both competing populations grew showing the

5Just like the Red Queen in Lewis Carroll’s _Through the Looking Glass_, where

Alice and the Red Queen run faster and faster just to remain in the same place,

each species in the experiment is forced to keep changing just to remain in the

competition.

**64**

Chapter 3. Landscapes

same steady increases in fitness6 but, at some point, one of

the populations suddenly dominated, excluding the other one.

The winner of this competition process was not always the same.

Sometimes one of the populations dominated, sometimes the

other one (figure 3.3a).]] But they never coexisted. Why?

This question can be answered by using a general scenario

where two quasispecies compete. This can be easily formulated

in mathematical terms as follows. Here two different populations

_x_ 1 and _x_ 2 are considered, each one formed by a set of mutants.

Specifically, we have { _x k_}

_i_

(with _i_ = 1 _, . . . , n_; _k_ = 1 _,_ 2), which

compete for a given set or resources, with _x k_ =

_x k_

_i_

_i_ . Assuming

that mutations occur with the same rates for all strains, we

can write down the following system of equations (see previous

chapter):

_d x k_

_i_ = _f k_

+

_f kμ_( _j_ → _i_) _x k_ − _x k_( _t_)

(3.9)

_d t_

_i_ (1 − _μ_) _x k_

_i_

_j_

_j_

_i_

_j_ = _i_

_μ_

= _f k_

+

_i_ (1 − _μ_) _x k_

_i_

( _x_

( _t_)

(3.10)

_n_

_k_ − _x k_

_i_ ) − _x k_

_i_

≈ _xk_

_._

_i_

_f k_

_i_ (1 − _μ_) − ( _t_ )

(3.11)

The last equation is the replicator equation already introduced in

the previous chapter.

In the context of the experiments with VSV, we are consid-

ering two clonal populations competing for the cells in the cell

6In order to estimate these fitness changes, the population was sampled at the

end of each passage and cultivated along with the wild-type. After their growing

together, the fitness is estimated from the relative difference in populations of

each type.

3.2. Symmetric Competition

**65**

culture (specifically BHK-21 cells). In this case, summing all the

equations for _x k_

_/_

_i_ we have _d xk /d t_ =

( _d x k d t_), i.e.,

_i_

_i_

_d x_

_n_

_k_ =

_x k_

_d t_

_i_

_i_=1

_n_

_n_

× _f k_

−

_i_ (1 − _μ_) −

_f_ 1 _j_(1 − _μ_) _x_ 1 _j_

_f_ 2 _j_(1 − _μ_) _x_ 2 _j_

_i_=1

_i_=1

(3.12)

_n_

_n_

_n_

≈

_x k_

−

−

_,_

_i_

_e ki_

_e_ 1 _jx_ 1 _j_

_e_ 2 _jx_ 2 _j_

(3.13)

_i_=1

_i_=1

_i_=1

where we use _e k_ =

_i_

_f k_

_i_ (1 − _μ_). By defining the average value

_n ek_

_e_

_j_ =1

_j x kj_

_k_ ( _t_ ) =

_n_

(3.14)

_x k_

_j_ =1

_j_

after some algebra we obtain a set of equations:

_d x_ 1 = _e_

_d t_

1 _x_ 1 (1 − _x_ 1 − _β_ 21 _x_ 2)

(3.15)

_d x_ 2 = _e_

_d t_

2 _x_ 2 (1 − _x_ 2 − _β_ 12 _x_ 1) _,_

(3.16)

where we define

_β_

_e_ 2

_e_ 1

21 =

_β_

·

(3.17)

_e_

12 =

1

_e_ 2

This set of equations is a special case of the well-known Lotka-

Volterra model of species competition (Case 2000). This model

is known to exhibit two main types of solutions: species either

coexist or exclude each other. In particular, for the symmetric case

111

111

111

111

011

011

011

011

**2 _x_**

101

001

101

001

101

001

101

001

010

010

010

010

110

110

110

110

100

000

100

000

100

000

100

000

–

–

–

–

–

–

–

–

111

111

111

111

011

011

011

011

**1**

101

001

101

001

101

001

101

001

_**x**_

010

010

010

010

110

110

110

110

**d**

100

000

100

000

100

000

100

000

200

50

**c**

80

_x_ 2

60

_x_ 1

150

1 _k_

40

5

_x_

Time

Time

20

Red Queen

0

100

02

Time

80

0.6

0.4

0.2

Fitness

**b**

60

50

2 _k_

40

_x_

Time

20

**a**

0

0

0

0

8,000

6,000

4,000

2,000

5,000

4,000

3,000

2,000

1,000

10,000

Population

Population

3.2. Symmetric Competition

**67**

_β_ = _βij_ it is easy to show that for _β <_ 1 coexistence occurs, while for _β >_ 1 only one of the species can win, with the other decaying

into extinction. In our model, we can see that _β_ 12 = 1 _/β_ 21,

and the analysis of this system reveals that coexistence is never

possible, independently of the specific values of the competition

coefficients (Solé et al. 1999). The previous experiments were

also simulated (Solé et al. 1999) using a bit-string model that

considered a population of _N_ binary sequences. This model

allows us to keep the mutation terms required to move through

the fitness landscape. At each time generation (passage), the

algorithm repeated _N_ times the following rules: a random string,

say _Si_ , of the population was chosen for replication. Replication is

proportional to _f_ ( _Si_ ) and takes place by replacing another string,

say _S j_ , by a copy of _Si_ . Errors occur at a rate _μ_ (per bit and replication cycle).

The model consistently reproduced the experimental results

(figure 3.4a-c).]] The populations were initialized with identical

genomes and numbers of strings, in such a way that their initial

fitness was low. During the simulations, strings were competing

for the _N_ available sites. For a while, both populations gained

fitness (inset of figure 3.4a)]] but remained close in terms of

population size (figure 3.4a)]] since replication rates were not

strong enough. However, after a given number of passages, waves

of growth and decay emerged (figure 4b-c) as fitter variants

appeared by mutation. At some point (also predictable, as in the

Figure 3.4. Modeling the Red Queen dynamics of the VSV competition

experiment with equal fitness strains. In (a–c) we display several examples

of the time evolution of the bit-string model using digital genomes of

length _ν_ = 16 and _μ_ = 10−3. After some time, the two populations

diverge (a) while diffusing over sequence space. In (b-c) we show the

different population waves of more fit strings. At the beginning both

strains show similar waves of replacement, but eventually one of them gets

extinct. A simplified picture of the two coupled landscapes is depicted on

the right side.



**68**

Chapter 3. Landscapes

experiments) one of the two populations started outcompeting

the other one, which eventually disappeared (for details, see Quer

et al. 1996; Solé et al. 1999). The simplified diagram shown

in figure 3.4]] depicts the evolution process using two coupled

landscapes (one for each competitor), each with 3-bit genomes.

Initially, both competitors expand in their landscapes, climbing

toward the global optimum, but competition eventually selects

only one winner (left column).

3.3 Epistasis in RNA Viruses

The two landscapes studied so far from the point of view

of evolutionary dynamics define two rather special scenarios.

One assumes a rather unrealistic sharp peak with high fitness

surrounded by a flat landscape composed by all the rest of

sequences displaying equal (lower) fitness. The one presented in

the previous section considers a linear decay of fitness as we move

away from the peak. But it has been found that, in fact, the shape

of the landscape around a fitness peak can sensibly depart from

the linear picture.

A key concept to determine the ruggedness of a landscape

is _epistasis_, namely the nonlinear interaction between genes in

determining a phenotype, in this particular case, the phenotype

being fitness. Epistasis is a pervasive concept in evolutionary

biology that is central for theories seeking to explain genetic

systems such as sex and recombination, dominance, robustness,

and the rate of adaptive evolution (de Visser and Krug 2014).

Let us first consider a simple case with just two loci, where

the wild-type will be _A B_ and the double mutant will be _a b_.

If the combined effect of two mutations in fitness can be fully

predicted from the effect of each individual mutation, then no

epistasis exists and the expected fitness will be equal to the

sum of the fitness effects of the individual mutations (the linear

landscape described above would be an example). In terms of

3.3. Epistasis in RNA Viruses

**69**

**a**

**b**

**e**

ab

Ab

aB

aB

AB

AB

ab

ab

Ab

Ab

**No epistasis**

**Magnitude epistasis**

itness

**c**

**d**

F

aB

AB

aB

aB

AB

AB

ab

ab

Ab

Ab

**Sign epistasis**

**Reciprocal sign epistasis**

Figure 3.5. Different types of epistases between two loci defining the

fitness of a genotype. Capital letters indicate the wild-type and small

letters the mutant alleles. (a) In case of no epistasis, the fitness of the

double mutant _ab_ results from multiplying the fitness effects of both

mutations on the wild type genetic background (i.e., the fitnesses of

genotypes _Ab_ and _aB_). (b) If magnitude epistasis exists, the fitness of the double mutant _ab_ is different from the multiplicative expectation.

In the example, the observed fitness of _ab_ is larger than expected as

a consequence of positive epistasis. In the cases both of no epistasis

or of magnitude epistasis, the effects of mutations _aB_ and _Ab_ are

unconditionally beneficial. (c) If the effect of one of the mutations is

conditionally beneficial (i.e., beneficial in one genetic background but

deleterious in another), then we are in the situation of sign epistasis.

(d) Finally, if both mutations _aB_ and _Ab_ are deleterious by themselves, but beneficial when combined, we are in the situation of reciprocal sign

epistasis.

fitness landscapes, this situation depicts a smooth surface with no

curvature (figure 3.5a).]] If the observed fitness of a double mutant

exceeds the additive effects expectation by a factor of _ξ_ then the

two mutations (or genetic loci) had positive epistasis (sometimes

called synergistic). Conversely, if the observed fitness of a double

**70**

Chapter 3. Landscapes

mutant is less than the additive effects expectation by a factor of _ξ_ ,

then the two mutations had negative epistasis (sometimes called

antagonistic). This is the so-called magnitude epistases and its

effect on the fitness landscape is to introduce a degree of curvature

_ξ_ (figure 3.5b;]] in this particular case, positive).

The situation can be more complicated. Figure 3.5c]] illustrates

the case of sign epistasis, meaning that the sign of a fitness

effect depends on the genetic background where it happens. For

example, a mutation may have a beneficial given effect one

background while being deleterious given another one. Sign

epistasis creates ruggedness in the fitness landscapes by introduc-

ing ridges and valleys. Ridges represent accessible evolutionary

paths, whereas valleys represent low-fitness regions that are not

accessible by natural selection. Still, a population can move from

the starting to the final point through the ridge. A final situation,

depicted in figure 3.5d,]] is the case of reciprocal sign epistasis, in which the signs of both mutations vary depending on the genetic

background where they appear. In the example, both mutations

are deleterious by themselves but overcompensate for their effects

when pooled together. Reciprocal sign epistasis creates valleys

that cannot be traversed by the populations simply by natural

selection. Populations get trapped in a peak even if it might not

represent the optimal evolutionary solution.

If we return to the peaked landscape view again, one way of

depicting the deviations from the linear case is by writing down a

generalized fitness function associated to the Hamming distance,

defined as the number of single site differences from the wild type.

If we assume a given “master” sequence _Sm_ (see chapter 2)]] and the distance to it, we can write the fitness of a sequence separated

mutations from the master as:

_f_ ( _Dh_) = 1 − 1

_,_

_ν Dξh_

(3.18)

where the Hamming distance was defined above, and _ξ_ measures

the sign and strength of epistasis (Elena et al. 2010). For _ξ_ = 1

3.3. Epistasis in RNA Viruses

**71**

**a** 1.0

**b** 1.2

Antagonistic

Antagonistic

_ξ_ < 1

1.0

_W ij_

_f_ ( _S_) 0.5

0.8

ed fitness v

_f_ ( _S_) = 1 – _Dh_/ _v_

0.6

Obser

Synergistic

_ξ_

Synergistic

> 1

0.0

0.4

0

8

16

24

32

0.4

0.6

0.8

1.0

1.2

_Dh_

Expected fitness _Wi Wj_

Figure 3.6. (a) Simple fitness landscapes where deleterious mutations lead

to a decrease in fitness can be described in terms of the distance to the wild

type sequence, following a general functional form _f_ ( _S_) = 1 − _Dξ /ν_

_h_

.

Here _Dh_ is the Hamming distance, _ν_ is the genome length, and the effect of mutations is introduced by a parameter _ξ_ . Two domains are indicated

here, associated to positive or synergistic (gray area, _ξ >_ 1) and negative

or antagonistic (white area, _ξ <_ 1) effects. (b) Evaluation of the pattern

of epistasis among pairs of random mutations in VSV. The diagonal

represents the case of no epistasis (additive effects).

we have just a linear decay (straight line, figure 3.6a),]] indicating

additive effects. However, when _ξ <_ 1, antagonistic epistasis is

present, with fitness decaying in a slower way, indicating that

the additional mutations have a smaller impact on fitness as

mutations are added. This is the so-called antagonistic (positive)

epistasis, to be opposed to the so-called synergistic one (for _ξ >_

1), where fitness decays faster as mutations accumulate.

Is it possible to quantify the strength and type of epistasis from

experimental data? The answer is positive (Sanjuán et al. 2004;

Sanjuán and Elena 2006). Consider the possibility of having both

the fitnesses associated to a given set of _n_ loci, namely _W_ 1 _,...,i,...,n_.

Additionally, consider the fitness of each single mutant, _Wi_ . This

number if obtained from experimental data and is defined relative

to a wild-type genome. If _ρ_ is the average per cell progeny

**72**

Chapter 3. Landscapes

for the wild-type, and we indicate as _ri_ and _r_ 0 the respective

mutant and wild-type growth rates, _Wi_ is given by (Sanjuán and

Elena 2006):

_ρri/r_ 0 − 1

_Wi_ =

_._

_ρ_ −

(3.19)

1

If no epistatic effects exist, it should be expected that the overall

fitness associated to all loci would be just the product of all _Wi_

terms, consistently with statistical independence. Deviations from

such a rule would indicate epistasis. In Sanjuán et al. (2004) and

Sanjuán and Elena (2006) the following index is given:

_n_

_ξ_ 1 _,...,i,...,n_ = _W_ 1 _,...,i,...,n_ −

_Wj ._

(3.20)

_j_ =1

In this way, it was possible to provide a quantitative measure of

epistasis. Moreover, this coefficient can be positive or negative,

indicating the presence of antagonistic and synergistic epista-

sis, respectively. When this measure was applied to a number

of model organisms, including viruses, bacteria, yeast, molds,

and fruitflies, the epistasis coefficient was shown to decay with

genome complexity (Sanjuán and Elena 2006). Here simpler

organisms (viruses and bacteria) displayed positive values of

_ξ_ 1 _,...,i,...,n_ while higher organisms presented a negative association.

In a systematic analysis of RNA viruses using many genotypes

of VSV, each carrying pairs of specific nucleotide mutations,

it was possible to use this method to determine the presence

of epistatic interactions. The results are shown in figure 3.6b,]]

where observed fitness _Wi j_ is displayed against the expected

multiplicative value _Wi Wj_ . Mutations included both deleterious

(filled circles) and beneficial (open circles) effects. The straight

line marks the null hypothesis _Wi j_ = _Wi Wj_ while deviations

indicate the presence of epistatic interactions, i.e., _ξi j_ = _Wi j_ −

_Wi Wj_ = 0. The reported results revealed a very significant role

of epistatic interactions, both synergistic and antagonistic. On

average, epistasis was pervasive and positive, meaning that the

3.4. Experimental Virus Landscapes

**73**

effect of two mutations together was weaker than expected from

their independent effects. These results also indicate that, despite

the high adaptability of RNA viruses, the presence of antagonistic

epistasis between different parts of their genomes can actually

impose some barriers on viral adaptation (Holmes 2003).

3.4 Experimental Virus Landscapes

Can we experimentally evaluate the structure and ruggedness of

virus fitness landscapes larger than pairs of random mutations?

This is a very complex and time-consuming task, but the answer

again is positive. Indeed, given the genomic simplicity of viruses,

this shall be a much easier task than for other more complex

organisms. In recent years, much effort has been devoted to

experimentally explore the topography of adaptive fitness land-

scapes for single molecules and for evolving bacteria adapting to

a simple environment (reviewed in de Visser and Krug 2014).

In all cases the experimental procedures are similar. Imagine

that during an evolution experiment, evolving populations have

fixed _k_ mutations. We can precisely identify these mutations by

sequencing the genomes of the ancestral and evolved organisms.

Depending on how developed the genetic analyses tools for

each particular biological system are, it may be possible to

generate all possible 2 _k_ mutant genotypes, that is, all genotypes

containing every single mutation individually, all genotypes con-

taining all pairwise combinations of mutations, all genotypes

containing all triplets of mutations, and so on until the genotype

containing all _k_ mutations. These genotypes describe the full

genotypic landscape that corresponds to the adaptive process

observed in the laboratory (figure 3.7).]] In the case of small

viruses for which an infectious plasmid containing a copy of the

viral genome exists, all these genotypes can be constructed by

site-directed mutagenesis, a standard technique implemented in

most modern virology laboratories. Finally, the fitness of each

**74**

Chapter 3. Landscapes

00000

10000

01000

00100

00010

00001

11000

10100

10010

10001

01100

01010

01001

00110

00101

00011

11100

11010

11001

10110

10101

10011

01110

01101

01011

00111

11110

11101

11011

10111

01111

11111

Figure 3.7. Empirical fitness landscape of size _k_ = 5. The presence/

absence of a given mutation is indicated by 1/0, respectively. Genotypes

are ordered top-down starting from the ancestral wild type virus (00000)

and finishing with the genotype carrying five mutations (11111). Each

row represents genotypes with equal number of mutations. Lines repre-

sent potential mutational steps.

genotype in the empirical landscape can be measured to provide

a quantitative description of the “height” of the peaks. In the

case of RNA viruses, proxies to fitness can be infectivity, virus

accumulation, or growth rates that can be expressed relative to

the wild-type genotype.

Unfortunately, few empirical studies have addressed the

topography of the fitness landscape for viruses. Characterization

of the type of epistasis among random pairs of mutations has been

done for several RNA viruses (reviewed in Elena et al. 2010).

Following the definitions and methods outlined in the previous

section, Lalić and Elena (2012) followed a similar approach to

evaluate the fitness of a collection of random single and double

mutant-generated by site-directed mutagenesis on the genome

of _Tobacco etch virus_ (TEV), a plant RNA virus. The fitness

of all these mutants was evaluated in the natural host tobacco

3.4. Experimental Virus Landscapes

**75**

( _Nicotiana tabacum_). In this case, epistasis was also very common,

and of positive sign.

More interestingly, sign and reciprocal sign epistases were

pervasive, suggesting that the fitness landscape of this virus was

rugged. These two studies, however, explore epistasis among

random pairs of mutations, which itself provides very useful

information. However, from an adaptive dynamics perspective, it

would be much more informative to characterize the ruggedness

of the landscape defined by sets of beneficial mutations. To tackle

this problem, in a recent set of studies, the landscape defined by

the five mutations fixed by TEV during experimental evolution

and adaptation to its novel host _A. thaliana_ has been thoroughly

characterized. All 25 = 32 possible genotypes were constructed

and their fitness measured in the novel host (Lalić and Elena

2015). The resulting landscape is shown in figure 3.8a.]] The

topography of this landscape was rugged, defined by prevailing

epistatic effects between mutations.

Cases of reciprocal sign epistasis were common among pairs

of mutations, defining fitness valleys. The landscape contained

two fitness peaks, neither of which corresponded to the geno-

type containing all five mutations. Interestingly, the landscape

contained a whole region of deleterious and lethal genotypes (in

red), suggesting that these mutations rose in the population in

genotypes that already contained compensatory mutations. Very

interestingly, higher-order epistasis was found to be as important

as pairwise epistasis in its contribution to fitness. Higher-order

epistasis corresponds to interactions between more than pairs of

mutations. From a geometric perspective, third-order epistasis

represents the effect that a third mutation exerts on the surface

defined by a pair of mutations. Likewise, fourth-order epistases

quantify the effect that a surface (defined by a pair of mutations)

exerts on the surface defined by another pair of mutations.

In a follow-up study (Cervera et al. 2016) the effect of

the host species on the ruggedness of the landscape was also

analyzed. To do so, the authors evaluated the fitness of the

**76**

Chapter 3. Landscapes

**a**

00000

10000

01000

00100

00010

00001

11000

10100

10010

10001

01100

01010

01001

00110

00101

00011

11100

11010

11001

10110

10101

10011

01110

01101

01011

00111

11110

11101

11011

10111

01111

11111

**b**

00000

10000

01000

00100

00010

00001

11000

10100

10010

10001

01100

01010

01001

00110

00101

00011

11100

11010

11001

10110

10101

10011

01110

01101

01011

00111

11110

11101

11011

10111

01111

11111

Figure 3.8. Empirical fitness landscapes evaluated for the set of five

mutations fixed by TEV during its experimental adaptation to _Arabidopsis_

_thaliana_. The fitness of the 32 genotypes was evaluated in the novel host

(a) and in the original one, _N. tabacum_ (b). Each string of bits represents

a genotype. 1’s represent a mutation in the corresponding locus, while

0’s correspond to the wild-type allele on this locus. Genotypes in a

green box correspond to local fitness peaks. Green lines correspond to

beneficial mutations, genotypes in red are deleterious, and black dashed

lines correspond to neutral changes (in the direction from wild-type to

the quintuple mutant genotype).

3.5. The Survival of the Flattest Effect

**77**

same collection of TEV mutants, but with the original host,

_N. tabacum_ (figure 3.8b).]] Two important conclusions can be

drawn from this study. First, the topography of the landscape

was smoother in the novel host than in the ancestral one. This

has important evolutionary implications, for example, exploration

of the landscape is more efficient in the novel host. Second,

both landscapes were uncorrelated, meaning that genotypes that

were beneficial in the novel host were deleterious in the ancestral

one. This is the typical situation of antagonistic pleiotropy that

will be discussed in chapter 6]] in the context of emerging viral

infections. Differences between the two landscapes, however,

were local rather than global, with particular genotypes changing

their relative height in the landscape and resulting in different

patterns of epistatic interactions with their neighbors.

This dependence of the topography of the fitness landscape on

the host supports the notion of dynamic landscapes rather than

of static ones. Nonetheless, both landscapes shared common fea-

tures, such as the existence of fitness holes due to unconditionally

lethal genotypes or the presence of pervasive epistatic interactions.

The topography of both empirical landscapes matches pretty well

with the expectations from a random uncorrelated landscape;

lying somewhere between the extreme case of the House-of-Cards

model (Kingman 1987), in which the fitness of each genotype is

absolutely independent of the fitness of the other genotypes, and

the less radical case of the rough Mount Fujimori model (Aita

et al. 2000), which combines properties of both the House-of-

Cards and a purely multiplicative landscape.

3.5 The Survival of the Flattest Effect

The existence of a quasispecies strongly affects the way selection

acts, because the evolutionary success of individual genomes

depends not only on their own replication rate but also on

the average growth rate of the quasispecies they belong to.

**78**

Chapter 3. Landscapes

Mutation acts as a selective agent that shapes the genome in

a manner that causes the entire quasispecies to become robust

against mutations, and fast replicating genomes that produce low-

fitness offspring can be outcompeted by slow replicating genomes

provided the latter quasispecies inhabits a region of sequence

space characterized by high neutrality and connectivity (Schuster

1988; van Nimwegen 1999; Wilke 2001b). This phenomenon

has been dubbed the “quasispecies effect” (van Nimwegen 1999;

Wilke 2001a) or more recently as “the survival of the flattest”

(Wilke et al. 2001), in clear reference to Darwin’s “survival of

the fittest” concept. Indeed, authors who cast doubts about the

relevance of the model to real viruses based their criticism on the

fact that the quasispecies effect was not observed in vivo (Holmes

2002).

However, a recent experiment gave support to the validity of

the “quasispecies effect” in real viral populations. In one of them,

Codoñer et al. (2006) selected two different viroids that infected a

common host. These two viroids largely differ in their replication

rates and in the extent of genetic variability they generate within

their host. CChMoVd generated lots of variants after being

inoculated but accumulated to very low titers. _Chrysanthemum_

_stunt viroid_ (CSVd) accumulated to very high titers but showed

little genetic variation. The authors hypothesized that CChMoVd

may represent the case of a flat organism replicating in a neutral

network (NN) whereas CSVd may not. To test this hypothesis

both viroids were co-inoculated into the same plants and allowed

to compete. As expected, CSVd quickly outcompeted CChMoVd

owing to its faster replication rate. However, when the mutation

rate was artificially increased by UVC radiation, the situation was

reversed and CChMoVd persisted in the mixed population.

In another experiment, Sanjuán et al. (2008) provided addi-

tional evidence of the survival of the flattest effect. Two VSV

populations that differed in evolutionary history were chosen.

Population _A_ was formed by individuals that on average had

3.5. The Survival of the Flattest Effect

**79**

lower fitness than those from population _B_ but that were more

diverse in fitness. The authors hypothesized that population _A_

was the flattest while population _B_ was the fittest. As in the

viroids case, these two populations were allowed to compete in

standard conditions and at increasing mutation rates (in this case

by adding either one of two chemical mutagens, 5-FU or 5-AzC).

The results showed that while population _B_ outcompeted pop-

ulation _A_ under standard conditions, _B_ was able to reverse its

fortune as the concentration of mutagens increased.

A minimal mathematical model can be used to describe the

survival of the flattest effect (figure 3.9e-f).]] We use a mean

field model to analyze the dynamics between two quasispecies

located in two different (but coupled through competition)

fitness landscapes. The state of the system is thus described by

a state = ( _x_ 0 _, x_ 1 _, y_ 0 _, y_ 1) such that

( _x_

_i_

_i_ + _yi_ ) = 1 (constant

population constraint). The model is given by the next four-

dimensional dynamical system, with two equations for the “fit”

populations reading

_d x_ 0 = _r_

_d t_

0 _Qx_ 0 − _x_ 0 ( )

(3.21)

_d x_ 1 = _r_

_d t_

0(1 − _Q_) _x_ 0 + _r_ 1 _x_ 1 − _x_ 1 ( ) _,_ (3.22)

which include a Swetina-Schuster approach (see chapter 2)]] with

_r_ 0 _> r_ 1 and associated with a “sharp” peak. These two equations

are coupled with the other two by means of the competition

terms including the ( ). The “flat” component now involves

two additional equations,

_d y_ 0 = _r_

_d t_

0 _Qy_ 0 + _r_ 1(1 − _Q_) _y_ 1 − _y_ 0 ( ) (3.23)

_d y_ 1 = _r_

_d t_

1 _Qy_ 1 + _r_ 0(1 − _Q_) _y_ 0 − _y_ 1 ( ) _,_ (3.24)

![[index-95_1.png]]

**80**

Chapter 3. Landscapes

**a**

**b**

**c**

**d**

Low mutation

High mutation

**e**

**f**

_R Q_

_r Q_

0

0

_x_

_y_

0

0

Φ

_R_ (1 – _Q_)

_r_ (1 – _Q_)

_r_ (1 – _Q_)

0

0

1

_x_

_y_

1

1

_R_

_r Q_

1

1

Figure 3.9. The fittest versus the flattest. Here two idealized landscapes

are indicated with their populations (gray spheres) associated to the peaks.

For the sharp peak (a-b) at low mutations, genomes are close to the peak

whereas increasing mutation pushes them far toward low fitness values.

For a flat landscape (c-d) the situation is different, since the spread has

little impact on average fitness. A minimal model of this phenomenon

can be described in terms of a simple quasispecies model (e-f).

3.5. The Survival of the Flattest Effect

**81**

that allow back mutations and thus a diffusion-like coupling.

To make things simpler, we will asume that _r_ 0 = _r_ 1 = _r_ , and

additionally we will have _r_ 0 _> r > r_ 1, meaning that the flat strain has an intermediate fitness value between the maximum and the

minimum of the fit one.

Given the homogeneous replication rate _r_ , the two “flat”

components will be undistinguishable, and it is easy to see that

the two last equations can be collapsed into a single one using

_y_ = _y_ 0 + _y_ 1, namely

_d y_ = _ry_ − _y_( ) _._

(3.25)

_d t_

The analysis of the resulting three-species system (now we have

= ( _x_ 0 _, x_ 1 _, y_)) gives a condition for the survival of the flattest: _Q < r_ ;

(3.26)

_r_ 0

or, using the mutation rate _μ_ = 1 − _Q_, if the critical condition

_μ > μc_ = _Q <_ 1 − _r_

(3.27)

_f_ 0

is met. We thus have a well-defined condition connecting the

relative distance between the fitness of the highest peak and the

one associated to the flat strain. The dynamics under the two

different regimes can be better appreciated by using a spatial

model (Sardanyés et al. 2008). In figure 3.10]] we illustrate the

outcome of competition under low (a) and high (b) mutation

rates in a cellular automaton model where four states are used.

The lighter areas in both pictures correspond to the fittest sites,

which propagate at the expense of the flat states until the lattice is

filled. Conversely, the darker sites associated with the flat states

are the winners in the second case. Note that the expansion

process takes longer in the second scenario, in accordance with

the lower replication rate of the less-fit species.

![[index-97_1.png]]

![[index-97_2.png]]

![[index-97_3.png]]

![[index-97_4.png]]

**82**

Chapter 3. Landscapes

τ = 100

τ = 150

τ = 200

τ = 250

τ = 400

τ = 550

0.6

0.5

_S_ 0

0.4

_S_ 2 _S_ 3

0.4

0.3

entration

_S_ 1

0.2

0.2

oncC

_S_ 3

0.1

_S_

_S_ 1

2

0.0

0.0

0

300

600

0

500

1,000

τ

τ

τ = 250

τ = 300

τ = 662

τ = 700

τ = 850

τ = 1042

Figure 3.10. The survival of the flattest in a two-dimensional cellular

automaton model (Sardanyés et al. 2008). The left and right diagrams

and snapshots are obtained for low and high mutation rates.

3.6 Virus Robustness

In the previous section, we discussed a particularly interesting

point, namely, selection may favor not the fittest (i.e., faster

replicators) but the flattest (i.e., more robust replicators), which

better tolerate the accumulation of deleterious mutations. The-

oretically, viruses with high mutation rates may be favored in

stressful environmental situations where the input of beneficial

mutations allows for escape and survival (e.g., changing cell

types, tissues, and hosts, or the presence of antiviral responses

or drugs). However, in all situations, deleterious and lethal

mutations represent the larger fraction of all possible mutations,

3.6. Virus Robustness

**83**

thus jeopardizing viral fitness. How do RNA viruses maintain

their functionality in this scenario? Are they robust against the

accumulation of deleterious mutations? Is the survival of the

flattest the only mechanism they may enjoy to buffer the effect

of mutations?

In a hallmark article, de Visser et al. (2005) reviewed the

notion of robustness and explored its causes and consequences.

Robustness is the preservation of the phenotype in the face of

perturbations. The robustness of phenotypes appears at various

levels of organization: from gene expression, protein folding,

metabolic flux, physiological homeostasis, and development, to

fitness. Three reasons may explain the evolution of mutational

robustness. Firstly, as long as it is heritable, shows variability

among individuals, and affects fitness, mutational robustness

can be a selectable trait. The more frequent mutations are,

the stronger will selection be at promoting the evolution of

mutational robustness. Secondly, mutational robustness is a side

effect of stabilizing selection acting on different traits. Thirdly,

given that environmental fluctuations often have a strong impact

on fitness, selection would favor mechanisms of environmental

robustness, and then mutational robustness simply evolves as a

side effect (dubbed plastogenetic congruence). This last explana-

tion is particularly appealing for RNA viruses as they must cope

not only with deleterious mutations but also with dramatic and

fast fluctuations in their environments.

Elena et al. (2004) elaborated on the possible mechanisms

by which RNA viruses may attain mutational robustness,

distinguishing two classes of mechanisms. Mechanisms of

intrinsic robustness are the consequence of RNA-genome

architecture, replication peculiarities, and population dynamics.

Intrinsic robustness mechanisms operate efficiently at the pop-

ulation level. By contrast, extrinsic robustness results from the

exploitation of cellular buffering mechanisms by viruses.

![[index-99_1.png]]

**84**

Chapter 3. Landscapes

Giant component

Figure 3.11. Neutral networks in sequence space. Two idealized exam-

ples of the neutral networks connecting sequences that lead to the same

type of fold (adapted from Schuster (2010)). As a result of neutrality, the

landscape of RNA folds associated with different RNA sequences displays

islands of connected neutral phenotypes that can percolate through

sequence space.

3.6. Virus Robustness

**85**

3.6.1 Intrinsic Mechanisms of Mutational Robustness

In the previous sense, the survival of the flattest discussed above

can be considered as an _intrinsic_ mechanism of robustness. It

depends on selection, pushing viral populations toward regions

of genotypic space in which mutations may have a more neutral

effect. These regions of high neutrality, or NNs (figure 3.10),]]

allow the virus to accumulate mutations without suffering fitness

losses. A positive consequence of the existence of such NNs is

that viral populations may efficiently explore distant regions of

sequence space.

The existence of such NNs has a strong implication on

the antigenic evolution of _Influenza A virus_ (IAV) H3N2. The

observed patterns of epochal antigenic evolution of H3N2,

alternating periods of phenotypic stasis punctuated by sudden

changes in the antigenic phenotype, can easily be explained in

terms of NNs. At the onset of an epochal evolution cycle, an

H3N2 population is distributed over the NN of an antigenic

cluster. Neutral mutations accumulate, allowing the virus to

explore and reach distant regions of this particular NN. At some

point, a mutation at the edge of the network will create an

individual that belongs to a new NN that corresponds to a

different antigenic cluster. This antigenic innovation corresponds

to an epidemiological peak in the number of infections. The

new antigenic variant now starts exploring the new NN, and the

process repeats itself (Koelle et al. 2006; Van Nimwegen 2006).

A second mechanism of mutational robustness is high ploidy.

Viruses are _n_-ploid organisms; _n_ is variable during infection.

At initial stages, multiplicity of infection (MOI) is low and

viruses are effectively haploid. However, as infections progress,

high MOIs ensure frequent co-infections and increasing ploidy.

An immediate consequence of polyploidy is genetic comple-

mentation. Strong complementation slightly reduces the average

population fitness by weakening the efficiency of purifying

selection but significantly enhances population diversity and

**86**

Chapter 3. Landscapes

mutational robustness, especially if epistasis among deleterious

mutations is antagonistic.

Different modes of genome replication may also affect

mutational robustness. The stamping-machine replication strat-

egy uses always the same molecule as template for producing

all the progeny, thus minimizing the number of mutations at

the cost of being slower than a geometric replication strategy.

Geometric replication is faster, but has the drawback of using

progeny genomes as templates, and thus generating offspring with

a number of mutations that increases geometrically. Furthermore,

it has been shown that, in combination with selection, the

stamping machine accumulates less mild-effect mutations than

geometric replication. Indeed, the difference between both repli-

cation schemes in terms of minimizing deleterious mutational

load is enhanced if mutations show negative epistasis.

A final mechanism of intrinsic mutational robustness is viral

sex, resulting from recombination of homologous molecules or in

segregation of segments in a multipartite genome. Sex recreates

mutation-free genotypes and helps to keep the average population

fitness high. Both forms of sex are common among RNA viruses.

3.6.2 Extrinsic Mechanisms of Mutational Robustness

Prokaryotes, archaea, and eukaryotic cells all have a set of

proteins that respond to stress, the best known ones being those

responding to thermal stress. These heat-shock proteins (HSP)

operate as molecular chaperones assisting other proteins to fold

properly into their active structures as they are synthesized under

thermal stress (Borges and Ramos 2005). In addition to their

activity under exogenous stress conditions, it has also been shown

that HSP chaperones assist in the folding of mutated proteins,

buffering the effect of mutations on the structure, even in the

absence of thermal stresses (Queitsch et al. 2002). Indeed, HSPs

are considered as capacitators of evolution because they maintain

3.7. Selection: Fitness versus Robustness

**87**

genetic variability hidden from the action of purifying selection;

this variation may become visible under stress (e.g., an envi-

ronmental change) when the chaperones are diverted into their

original function (Queitsch et al. 2002). Therefore, chaperones

can be seen as robustness machines.

A well-established observation is that viral infections induce

the cellular stress response, including the over-expression of many

members of the HSP family (Jacob et al. 2017; Neckers and

Tatu 2008). Very interestingly for the discussion in hand, it has

been shown that most viruses not only induce HSPs’ expression

as a result of cellular stress, but also need cellular chaperones

during their life cycle to solve their own protein-folding problems

(Aparicio et al. 2005; Geller et al. 2012; Low and Fassati 2014),

to assist during RNA replication, and to interfere with cellular

processes such as signal transduction. Therefore, it is tempting to

suggest that viruses are hijacking the cellular HSPs for their own

benefit as a way of buffering mutations that otherwise may have

a negative impact on their fitness due to destabilizing effects on

protein structures.

3.7 Selection: Fitness versus Robustness

A mathematical model provides a consistent picture of this selec-

tion for robustness associated to the presence of neutrality (Wilke

2001a). Although this model is somewhat related to the mean

field model discussed above, it explicitly incorporates neutrality

as a system’s parameter and allows us to make predictions that

can be explicitly defined and related to relevant variables such as

genome size.

Consider first one neutral network ⊂ H _ν_ and the probabil-

ity _Q_ that a mutant string _S_ is generated from _S_ ∈ (Ofria and Adami 2001). To do this calculation, a parameter _η_ is

introduced, giving the probability that a single site mutation has

**88**

Chapter 3. Landscapes

**a**

_S_

_S_

**c** 0.12

_i_ 1

_ik_

_Siv_

. . .

. . .

0.10

_q_ 0.08

Robustness

_S_’ _ik_ = _Sik_

0.06

**b**

_η_

_S_’ _ik_

Mutation 1– 0.04

_μ_

_S_

_b_

_ik_

0.02

1– _η_

Replication speed

1– _μ_

0.00

_b_

_S_’ _ik_ = _Sik_

0.0

0.2

0.4

0.6

0.8

1.0

Neutrality _v_ 1

Figure 3.12. Modeling the interplay between replication and neutrality.

Given a digital genome (a) the probability _Q_ of a neutral mutation

is estimated from the two favorable events indicated in (b). In (c) the

two phases consistent with either selection for spread or selection from

robustness are shown.

no phenotypic effect. If _μb_ is the mutation rate per site, we have

(see figure 3.12a):]]

_Q_ = [1 − _μb_(1 − _η_)] _ν_ ≈ _e_ − _μb_(1− _η_) _ν._

(3.28)

This calculation can now be used to develop a first population

dynamics model where _x_ 1 and _xd_ will stand for the concentrations

of genomes respectively within the neutral network and outside

of it. The model thus uses _x_ 1 + _xd_ = 1 and the dynamics is

given by:

_d x_ 1 = _r_

_d t_

1 _Qx_ 1 − _x_ 1 ( _x_ 0 _, xd_ )

(3.29)

_d xd_ = _r_

_d t_

1(1 − _Q_) _x_ 1 − _xd_ (( _x_ 0 _, xd_ ) _._

(3.30)

3.7. Selection: Fitness versus Robustness

**89**

As defined, the model assumes that the sequences outside

are unable to replicate and using this assumption the equilibrium

concentration is

_x_ 1 = _Q_ = _e_ − _μb_(1− _η_) _ν._

(3.31)

The importance of this result is that knowing how _x_ 1 changes

as _μb_ grows it is possible to estimate the network’s neutrality,

which follows this prediction accurately even when sophisticated,

molecular-level frameworks are used (Wilke 2001a).

Finally, the conditions for selection for replication speed

versus those for robustness will be obtained by analysing a three-

population model where two populations are associated to two

different neutral networks and again the one for genomes outside

both networks is included:

_d x_ 1 = _r_

_d t_

1 _Qx_ 1 − _x_ 1 ( _x_ 1 _, x_ 2 _, xd_ )

(3.32)

_d x_ 2 = _r_

_d t_

2 _Qx_ 2 − _x_ 2 ( _x_ 1 _, x_ 2 _, xd_ )

(3.33)

_d xd_ = _r_

_d t_

1(1 − _Q_) _x_ 1 + _r_ 2(1 − _Q_) _x_ 2 − _xd_ ( _x_ 1 _, x_ 2 _, xd_ ) _,_ (3.34)

where the condition _x_ 1 + _x_ 2 + _xd_ = 1 leads to = _r_ 1 _x_ 1 +

_r_ 2 _x_ 2. The analysis of this system leads to a condition for the

critical mutation rate separating the two selection phases:

_μc_ = 1 − ln( _r_ 2 _/r_ 1) _._

_ν_

(3.35)

( _η_ 1 − _η_ 2)

Two possible steady states exist (obtained from _d xk/dt_ = 0,

_k_ = 1 _,_ 2 _, d_). These are ( _Q_ 1 _,_ 0 _,_ 1 − _Q_ 1) and (0 _, Q_ 2 _,_ 1 − _Q_ 1).

We can see them drawn in figure 3.12b.]] As the figure illustrates,

in one, the successful strategy for the population _x_ 1 is to be a

**90**

Chapter 3. Landscapes

fast replicator, whereas for mutation rates larger than the critical

value, the successful strategy requires neutrality.

The landscape picture helps to conceptualize the idea of evolu-

tion of a population of genomes and to include relevant properties

(such as neutrality of ruggedness) in an explicit manner. The

previous definitions and approximations provide a general

background to illustrate the key concepts associated to the

genotype-phenotype mapping. Formal generalizations have been

proposed (Stadler 1999; Stadler et al. 2001; Reydis and Stadler

2002), as well as extensions that incorporate a multiscape picture

(Catalán et al. 2017). But perhaps the most crucial missing

element here is that viruses have evolved in a host context where

both partners are forced to change. To understand the nature of

viruses, we need to put both hosts and pathogens at play.

**4**

V I R U S D Y N A M I C S A N D A R M S R A C E S

4.1 Virus-Host Interactions

The life histories of viruses cannot be understood outside the

context of their host partners. Because they cannot exist without

the environment defined by their target organisms, understanding

the behavior of viruses inevitably leads to consideration of how

they and their hosts coevolve. In the previous chapters we have

already discussed the structural, computational and ecological

features associated to viruses. But the whole picture would be

incomplete unless we take into account the coevolution of viruses

and their hosts. As stated by Theodosius Dobzhansky, “nothing

makes sense unless under the light of evolution,” and this is

particularly true for viruses, which are rapidly evolving entities

with an enormous impact on the evolutionary history of their

hosts; and, as we will see, the converse holds too. Moreover,

the lessons learned from their study have also shed light on

several important approaches to both applied biomedical and

basic research.

Mathematics is also key to understanding evolution. Charles

Darwin himself wrote once that he “deeply regretted that I did

not proceed far enough at least to understand something of the

great leading principles of mathematics.” Darwin perceived that

**92**

Chapter 4. Virus Dynamics and Arms Races

a formal picture of natural processes gave their users “an extra

sense” (May 2004). At the time Darwin wrote this, physics was

already a well-established and powerful discipline, and its power

would only increase in the next two centuries thanks to the

development of mathematical models capable of astonishingly

accurate predictions. Biology is seen by many as a much more

messy and qualitative field, but the development of population

genetics and theoretical biology and the rise of systems biology at

the end of the twentieth century rapidly changed these views. In

this chapter we will study several models describing key aspects

of virus-host dynamics on different scales. As an illustrative

example, we will focus our discussion on the interaction between

HIV-1 and the immune system, using both ecological and

evolutionary models. Such modeling is, in principle, a highly

challenging goal. The immune system is far from simple, and a

serious consideration of the relevant biology rapidly ends up in

a clumsy, multi-parametric model that is of little use in terms of

insight. This is one of the problems faced by complex systems

practitioners: what to ignore as nonessential and what to include

in the model description.

Because multiple players are involved, from specific molecular

complexes to a high diversity of cell types, modeling these

interactions is a difficult task (Perelson and Weisbuch 1997;

Molina-Paris and Blythe 2011). One key step in defining a set

of equations or rules is deciding which details should be included

and which should be left aside. This choice implies some degree

of arbitrariness, and the guiding principle must be. “What is

my question?” This is not a minor point. Oftentimes, models

can look too abstract to specialists (usually trained in a highly

specialized area) since they ignore biologically relevant features of

the “real” biology. However, it is not less true that real insight

into many difficult problems requires some degree of abstraction

and some simplicity (Gell-Mann 1994; Solé and Goodwin 2001;

Mitchell 2012).

4.1. Virus-Host Interactions

**93**

The problem is illustrated by the diagram depicted in

figure 4.1a,]] where we show a small part of the interactions

between immune system defense mechanisms related to HIV-1

infection dynamics (Walker and Yu 2013). Both the innate and

adaptive immune responses are included, involving several classes

of specialized cells as well as complex molecular signals. This

defines a network of interactions involving several scales in terms

of the nature of biological players, but also different temporal and

spatial scales related to fast responses as well as long-term memory

dynamics. In this chapter we will not describe the organization

of immune responses, which include different classes of response

mechanisms (see, for example, Janeway 2001) and would require

a lengthy presentation. Only some specific features and players

will be taken into account and introduced as needed. Let us

mention only that any foreign agent (such as a virus) can be

detected, ingested by some cells, and broken into pieces. Each

one of these foreign fragments acts as a specific antigen that can

be recognized by another class of cells in specific ways. When

this happens, the cell population grows and expands rapidly, and

results in the removal of all cells marked with that specific marker.

If the virus does not mutate fast, this immune response can get rid

of the virus. If the virus is able to generate “escape” mutants, the

process starts again.

Similarly, the life cycle of HIV-1, which involves several

key steps associated to attachment to cell surface, reverse

transcription, integration in the host’s genome, and maturation of

newly produced viral particles (figure 4.1b),]] will not be explicitly considered. However, the knowledge of these molecular processes

allows us to introduce specific modeling rules that explain the

dynamics of viral propagation and how it is affected by drugs

targeting some of these steps. Here mathematical models can

help us gain an understanding of the tempo and mode of viral

evolution and its impact on disease progression. The HIV-1 case

is a wake-up call on the views of viruses as simple parasites

**94**

Chapter 4. Virus Dynamics and Arms Races

**a**

T cell help

Cell-intrinsic

antiviral

MHC

MHC

MHC

immunity?

class I

class I

class I

T cell help

DC

CD4+

CD8+ CTL

T cell

MHC

LILR

class II

Cytolysis

TCR

Peptide

**HIV-1-infected**

Cytolysis

**CD4+ T cell**

T 17 cell

H

B cell

?

HIV-1

BCR

Cell-intrinsic

ER

antiviral

immunity

?

Integration of viral

Neutralization?

DNA into the

host genone

_γδ_ T cell

ADCC?

?

ADCVI?

KIR

Macrophage

ADCP?

Cell-intrinsic

NK cell

antiviral immunity

**Maturation**

**b**

**13**

**1 Attachment**

Tetherin

Protease

Fusion

inhibitors

inhibitors

Env

**12 Release**

**Budding**

Accessory viral proteins

CCR5

Gag

**11**

Vpu

Vif

inhibitors

CD4

Gag Pol

Rev

ALIX,

Tot

**Assembly 10**

ESCRT-I,

CCR5

ESCRT-III

**9**

AAA

**2 Fusion**

APOBEC3G

**Nuclear**

AAA

Gag Pol Gag

SAMHD1

**import**

**5**

**Nuclear 8**

**9 Translation**

TRIM5

NRTIs,

**export**

CRM1

PIC

AAA

NNRTIs

INSTIs

AAA

**6**

AAA

**3**

AAA

AAA

**4**

**Integration**

AAA

**Uncoating**

**Reverse**

LEDGF

AAA

**transcription** Nucleus

Nucleus

**7 Transcription**

RNA Pol II

5’LTR 3’LTR

P-TEFb

Figure 4.1. Continued caption on next page.**98**

Chapter 4. Virus Dynamics and Arms Races

under control by the immune system and that the emergence of

AIDS might have to do with other factors not directly related to

HIV-1. Some authors even claimed that AIDS had nothing to

do with HIV-1 and could even be a by-product of antiretroviral

drugs.1 To solve the puzzle, a combination of both experimental

and mathematical approaches is required.

4.3 Population Dynamics of HIV Infection

Take the following example. When a model of predator-prey

interactions is to be built, population biologists usually consider

the number of individuals in each of two species (say _X_ and _Y_ for

preys and predators, respectively) as the key variables. Interaction,

growth, and mortality parameters are then introduced and the

main problem is how to properly express the functional relations

associated to all these processes (Case 2000). These types of

models often map interactions into some class of “reactions”

among components (figure 4.3 a-b):]] a predator finding a prey

can be reduced to a particle of a given class _Y_ “colliding” with

a particle of class _X_ . As a result, with some probability, the

_X_ particle gets removed while a new copy of the _Y_ particle

emerges in its place. Moreover, both types of particles “die”

with given probabilities, leaving some empty space available for

other particles. The list of reactions required to represent this so-

called Lotka-Volterra model (May 1973; Gotelli 1988) is given

in figure 4.3b.]] One could say that this is too simple to represent

the true complexity of a natural predator-prey system, but the

truth is that this toy model accounts for one particularly relevant

property of these systems, namely the presence of cycles, which

are a consequence of the internal dynamics of the system. Instead

1Such an unfortunate kind of claim, along with irresponsible political

decisions grounded in wrong assumptions, extreme religious positions, and

ignorance have to be blamed for much of the spread of the pandemics.

![[index-114_1.png]]

4.3. Population Dynamics of HIV Infection

**99**

**a**

**b**

_μ_

_X_ + _Y_

2 _Y_







4.4. Spatial Dynamics of HIV-1

**105**

that the virus was cleared very rapidly from chronically infected

patients, whereas the maintenance of its stable levels required an

enormous rate of production. On the other hand, despite the

rapid response to therapy, the high mutation rate (see chapter 2)]]

along with the production levels implied that, during HIV-1

replication, every single possible mutation would be present

(Coffin 1996; Perelson et al. 1997). As it became soon clear, the

HIV-1 quasispecies would become easily resistant to any single

drug. The rapid production and clearance of HIV-1 revealed also

that, whatever was taking place during the latency phase, it was

likely to involve a highly dynamical phenomenon.

In the next two sections we will take a step further in order

to provide two alternative (not necessarily exclusive) explanations

of the latency phase. The first considers the impact of spatial

dynamics in creating a delay in the expansion of the virus due

to the constraints created by limited growth within lymph nodes.

The second instead explicitly introduces genetic variability and

thus evolutionary dynamics.

4.4 Spatial Dynamics of HIV-1

A key component of the organization of immune responses within

our bodies is given by a network of connected elements known as

lymph nodes, where CD4+ T cells are produced (Janeway et al.

2001). Lymph nodes have a complex structure and are also known

to be a reservoir of the majority of HIV-1 particles (Kelly and

Taiwo 2015; Lorenzo-Redondo et al. 2016). The model assumes

that interactions between CD4+ T cells and HIV-1 take place

on a space that can be assimilated to a square lattice (Zorzano

dos Santos and Coutinho 2001). This is partially justified by the

spatial structure of lymph nodes, which are somewhat similar to

a mesh (Willard-Mack 2006).

Cellular automata models have been used to model immune

responses associated to viral infections (Stauffer and Pandey

**106**

Chapter 4. Virus Dynamics and Arms Races

1992; Papa and Stallis 1996). The model considered here assumes

a square lattice with _N_ = _L_ × _L_ sites, where each site _Si_ ∈

can be in one among four possible states from a set

= { _H, I_ 1 _, I_ 2 _, D_} _,_

(4.18)

where _H_=healthy site, _I_ 1=infected cell capable of spreading

viruses, _I_ 2 = aging infected cell, susceptible to the immune

attack, and _D_ stands for dead (empty) sites. Initially, the lattice

is filled with _N_(1 − _p_ HIV) _H_ cells and only a very small fraction of _Np_ HIV occupied by ( _Sk_ = _I_ 1) infected cells. Afterward, the

following set of rules applies:

1. Infection: _H_ → _I_ 1 for a site _Si_ occurs if at least one

neighbor _S j_ of this site cell is infected (i.e. _S j_ = _I_ 1). If this condition is not met, infection can also occur if at

least _R_ neighbors are of _I_ 2 class.

2. Decay of infected cells: A transition _I_ 1 → _I_ 2 occurs

after _τ_ time steps. Here _τ_ would represent the time

scale for developing a response aimed at killing infected

cells.

3. Death and cell removal: a transition _I_ 2 → _D_ occurs

with probability 1.

4. Colonization: expansion into empty sites _D_ → _H_

occurs with probability _pr_ (1 − ). Otherwise, we have

_D_ → _I_ 1 with probability _pr_ . Here is the probability of spontaneous infection.

In figure 4.5]] we display the outcome of this model for a

given set of parameters;5 specifically a square _L_ × _L_ lattice with

_L_ = 700 was used. Here the time series includes healthy cells

(open squares), infected cells (full circles), and dead cells (open

triangles), respectively. We can see the close similarities between

5Most parameters have been calibrated using available information to

provide proper orders of magnitude.

![[index-122_1.png]]

4.4. Spatial Dynamics of HIV-1

**107**

**a**

Infection

Latency phase

AIDS

1.0

**b**

**c**

0.8

0.6

0.4

ell densitiesC

0.2

0.0

**d**

**e**

5

10

0

2

4

6

8

10

12

Weeks

Years

Figure 4.5. Time evolution of the cellular automaton model for HIV-1

immune system interactions on a lattice. In (a) the populations of infected

(filled circles), healthy (open squares), and dead (triangles) cells are

displayed, respectively. In (b-e) four snapshots of one of the runs are

shown. Different gray levels correspond to different states. Here we can

see how propagation occurs in waves that create an effective delay in

achieving a global infection level.

this model results and those reported from blood samples of HIV-

1-infected patients. In particular, the number of infected cells _I_ 1

clearly reflects a lagged response that is consistent with the latency

phase. The results of these simulations have been averaged over

500 runs (this is why error bars are shown) using different initial

random conditions.

After a rapid initial phase of infection with high numbers of

infected cells (whose numbers provide a surrogate of the viremia)

a rapid decline occurs followed by a latency phase and, later on,

the expansion of infection consistent with the AIDS dynamical

pattern. The characteristic time introduced by _τ_ leads to the

formation of waves with length _τ_ + 1. After an initial infection

starting from a random subset of sites, these seeds originate

a rapid spread and most sites will get infected (figure 4.5b,]]

brighter area) after about five weeks in the simulation. After

2 _τ_ + 1 steps, the number of infected cells strongly decays and is

**108**

Chapter 4. Virus Dynamics and Arms Races

followed by rare, new infections on a lattice dominated by _H_ cells

(figure 4.5c).]] These new seeds initiate a structured spatial process involving propagating fronts (figure 4.5 d-c).]] Because of these

slow-expanding waves, infection requires now a much longer time

to spread and cover the lattice, thus causing a marked latency.

Other spatial models have been developed providing consistent

results (Perelson and Weisbuch 1997; Bernaschi and Castiglione

2002; Shi et al. 2008; Perelson and Shuai 2010).

4.5 Antigenic Diversity Thresholds and AIDS

The cellular automata model includes the spatial structure of

lymph nodes (in an oversimplified fashion) and provides a

potential explanation of the latency phase. In this case, latency is

largely due to the spatial constraints that limit the propagation of

infections through the system. However, despite the qualitative

matching, some important variables and rules have been ignored.

One in particular is the high potential for mutation displayed

by RNA viruses (including HIV-1), which is largely responsible

for adapting and evading immune responses. On the other hand,

the mirror image of this fast change is provided by the immune

system responses and its intrinsic diversity. These are features

that can be observed and measured, and it was soon realized

that HIV-1 was capable of developing great variability both

among patients as well as over time within the same patient

(Cichutek et al. 1992; Sanjuán et al. 2004).

Many models of HIV-1-immune system interactions have

been developed (Arnaout et al. 2000; Bittner et al. 1997; Callaway

et al. 1999; Nowak et al. 1991, 1996; Wikramaratna et al.

2015; Nowak and Bangham 1996; Wodarz and Nowak 1999,

2002) from different perspectives and involving several levels of

complexity. A common feature of all of them is the presence of a

diverse set of viral strains and a specific cellular response mediated

4.5. Antigenic Diversity Thresholds and AIDS

**109**

by strain-specific CD4+ T cells. During the asymptomatic phase

of infection (figure 4.2),]] error-prone replication of HIV-1 gen-

erates increasing numbers of antigenic variants (i.e., viruses that

differ in their coat proteins and thus present different epitopes

to the CD4+ T cells). During the early period of infection,

the immune system is capable of coping with this increasing

variability and regulates the growth of the HIV-1 population.

However, there is a threshold value in antigenic variability, and

this is the key component of the model, above which the immune

system cannot exert effective control and the viral population

induces the collapse of the CD4+ T lymphocyte population.

Therefore, the model asumes that HIV-1 antigenic diversity is

the cause of AIDS and not its consequence (Nowak et al. 1991).

In the following paragraphs we will present the fundamental

properties of this model.

Instead of lumping together all viral strains into a single

phenotypic class, we introduce viral diversity by modeling the

underlying fitness landscape of HIV-1: different viral strains

correspond to different genomes, each one leading to a different

phenotype. Empirical evidence suggests that the underlying

HIV-1 fitness landscape is quite complex, characterized by

regions of high ruggedness (that depend on the type of epistatic

interactions among mutations; see chapter 3)]] interrupted by flat

regions where mutations are effectively neutral (Bonhoeffer et al.

2004; Hinkly et al. 2011; Kouyos et al. 2012). Interestingly, these

properties of the fitness landscape do not strongly depend on

whether viral fitness is measured in very permissive conditions or

in harsh ones owing to the presence of antiviral drugs (Kouyos

et al. 2012). Here we will limit ourselves to a very simple

interaction scheme where specific HIV-1 strains interact only

with some specific strains of CD4+ T cells capable of clearing

the virus but also being damaged by its infection. The specific

nature of the response is introduced in a minimal model with 2 _n_

**110**

Chapter 4. Virus Dynamics and Arms Races

equations (Nowak 1992) defined as:

_d vi_ = _v_

_d t_

_i_ ( _r_ − _p xi_ )

(4.19)

_d xi_ = _kv_

_d t_

_i_ − _uvxi ._

(4.20)

Here _xi_ and _vi_ indicate populations asssociated to the _i_ th virus strain and its corresponding CD4+ T-cell partner. For simplicity

(this is an obvious oversimplification) we assume that all viruses

replicate at the same rate _r_ and the immune response given by

the term _p xi vi_ is also homogeneous. Similarly, the growth and

death terms in the second equation use identical parameters for

all strains.

Summing over all the previous equations, we obtain for the

total viral population the expression

_d v_

_n_

_v_

= _v r_ − _p_

_x i_

(4.21)

_d t_

_i v_

_i_=1

and for the corresponding immune cell response,

_d x_ = _kv_ − _uvx,_

(4.22)

_d t_

where we have used _x_ =

_x_

_i_

_i_ . The virus population will be

under the control of the immune response provided that

_r_

_n_

_v_

_<_

_x i ._

(4.23)

_p_

_i v_

_i_=1

From the equation for _xi_ , we can see that the immune response

leads to a stationary state

_xi_ = _kvi ._

(4.24)

_uv_

Using this result and applying it to the total viral population,

we obtain an equation for the overall virus population that

4.5. Antigenic Diversity Thresholds and AIDS

**111**

depends on the actual diversity:

_d v_ = _v_

_k_

_r_ − _p D ,_

(4.25)

_d t_

_u_

where _D_ stands for Simpson’s diversity index (Magurran 1988),

namely

_n_

_v_ 2

_D_ =

_i_

_,_

_v_

(4.26)

_i_=1

and is used in theoretical ecology as an inverse measure of

diversity. For a homogeneous population, with all individuals be-

longing to the same species (strain), we have _D_ = 1 (maximum),

whereas in a completely heterogeneous system where all species

are equally represented, we have _D_ = 1 _/n_.

This is a very interesting result, which connects the determin-

istic model to a statistical index related to ecological diversity.

In our problem, this actually measures antigenic diversity as

defined by the phenotypic differential traits displayed by the viral

population. From the previous equation for the viral load, it is

clear that it will decline or increase depending on the diversity _D_

compared with the critical value

_Dc_ = _r u ._

(4.27)

_pk_

If _D < Dc_ we will have _dv/dt >_ 0, and _the virus escapes to the_ _immune system’s control_. If we make the additional approximation

that _D_ = 1 _/n_ (uniform viral population), the previous critical

condition can be expressed in terms of the total number of

different strains present, i.e., the condition for viral escape is:

_n > nc_ = _pk ._

(4.28)

_r u_

This model thus provides an elegant explanation of what is

taking place throughout the latency phase. It also allows us to

understand it in terms of a virus-immune system arms race and

**112**

Chapter 4. Virus Dynamics and Arms Races

makes a well-defined prediction. The model suggests (as seems

to be the case) that the long and apparently calm interval of low

viremia and slow decay of CD4+ T cells hides a rapid turnover

of constantly emerging viral escape mutants while progressive

damage to immune responses takes place. This would explain the

apparent dormancy of the virus: in reality there is a constant battle

between host defenses and the new variants being created through

mutation. This battle keeps the viral load at low levels, but also

involves a high cost due to the constant turnover of CD4+ T cells.

The prediction is that, as antigenic diversity grows over time

(more and more mutants are likely to persist), the potential for

response decreases until collapse takes place, with a rapid increase

in viral diversity, measured in both numbers of present strains

and Simpson’s index. The outcome of the model is exemplified

in figure 4.6.]] The model starts with a single strain and new strains are added within a time interval _d t_ with a probability _P v_( _t_) _dt_, thus proportionally to the viral load (here _P_ = 0 _._ 1). Figure 4.6a]]

displays the total population of viruses _v_ =

_v_

_i_

_i_ ( _t_ ), which has

a very slow progression and a long transition with low levels

followed by exponential growth at the equivalent of the in silico

AIDS phase. Figure 4.6b]] instead shows the detailed population

growth and decay of different variants of the virus, which are

more and more frequent as time proceeds. Finally, figure 4.6c]]

shows the antigenic diversity, measured as both the total number

of observed strains (continuous line) and the Simpson’s diversity

index. By using a more detailed implementation of the HIV-1

quasispecies, it is possible to introduce a mutation matrix

connecting different viral strains, as shown in figure 4.7]] for a

given matrix and a given set of initial conditions. As displayed

on the time series of HIV-1 strains, the three phases are easily

identified.

The model so far discussed can be extended to accommodate

additional, relevant components of the immune response. In

particular, one missing element in our previous assumptions is

![[index-128_1.png]]

4.5. Antigenic Diversity Thresholds and AIDS

**113**

0.5

**a**

AIDS

0.4

0.3

tal virus v

0.2

To

0.1

0.0

**b**

0.03

0.02

0.01

irus mutant strainsV

40

**c**

30

y

_n_

ersit

_c_

20

irus divV 10

0

0

1

2

3

4

5

6

7

8

Time (years)

Figure 4.6. A numerical simulation of the simplest model that includes

antigenic variation in the HIV-1 population, the stimulation of specific

immune responses, and the impairment of the immune function. The

parameters used are _r_ = 1 _, p_ = 20 _, u_ = 1, and _k_ = 1. These parameters predict a critical value _nc_ = 20 (the gray areas indicate _n > nc_ ). Here we have: (a) Total virus population size (virus density in arbitrary units);

(b) abundance (density) of the individual HIV-1 variants, and (c) the total

number of strains (continuous line) and the inverse of the Simpson index

(broken line) as a measure for population diversity.

![[index-129_1.png]]

**114**

Chapter 4. Virus Dynamics and Arms Races

0.07

**Latency phase**

**AIDS**

0.06

0.05

0.04

0.03

0.02

irus mutant populationsV

0.01

0.00

0

2

4

6

8

10

Time (years)

Figure 4.7. A numerical simulation of a quasispecies model (adapted

from Nowak (1992)). The model incorporates the mutation matrix

connecting different HIV-1 strains.

the consideration of nonspecific responses (see Nowak and May

2000 and references therein). The model considered a one-to-one

( _xi_ ↔ _vi_ ) matching between viral and cell strains, and thus lacks

cross-reactive responses. However, such an assumption ignores

a well-known observation: some parts of the virus genome (and

thus of its associated proteins) are highly conserved and less prone

to mutation. In terms of the immune system, that means that

these are efficient targets that can allow control of the infection.

This could explain the more rich spectrum of possible progression

pathways reported from some HIV-1-infected individuals. In

this context, along with the previous three-phase development

of AIDS, it has also been observed that some patients rapidly

develop the disease with no previous delay whereas some do not

display the symptoms even many years after the infection. Can

we explain these three outcomes with a single model?

Cross-reaction can be introduced by relaxing the assumption

that immune responses are only specific. To illustrate how this

4.5. Antigenic Diversity Thresholds and AIDS

**115**

can be done, let us expand the previous model as follows

(Nowak and May 2000):

_d vi_ = _v_

_d t_

_i_ ( _r_ − _p xi_ − _q z_)

(4.29)

_d xi_ = _kv_

_d t_

_i_ − _uvxi_

(4.30)

_d z_ = _kv_ − _bz,_

(4.31)

_d t_

where _z_ incorporates the cross-reactive immune response (as we

can see, if _q_ = 0 we have the previous model). As defined by the

third equation, this nonspecific response is also stimulated by the

presence of viruses and each viral strain can be removed at a rate

_q zvi_ . Despite the apparently small change introduced, the new

model displays now three different classes of behavior, reported

from the study of HIV-1 and other lentiviruses. Very shortly,

these phases are:

1. Lack of latency phase. It occurs for _r u > kq_ + _c p_, and

the virus here rapidly expands with no delayed growth.

2. Chronic infection with no disease. This phase occurs

when _kq > r u_. In this case, viruses get established and

are eventually controlled and kept at low abundance.

3. Chronic infection leading to disease. This is observed

within the interval of parameters _kq_ + _c p > r u > kq_

and corresponds to the AIDS scenario discussed above

with a latency phase.

The results from this model illustrate how the combination

of specific and nonspecific responses provide a diverse (but

finite) set of possibilities concerning the outcome of infections

in lentiviruses. More generally, they give us a powerful picture

of the evolutionary dynamics responsible for the asymptomatic

phase and its meaning in terms of a virus-immune system arms

**116**

Chapter 4. Virus Dynamics and Arms Races

race. In the next section we will explore this idea in a different

context, illustrating the importance of evolutionary dynamics in

shaping the architecture of the interaction webs among viruses

and their hosts.

The models described in the previous sections need to be seen

as useful ways of reducing the overwhelming complexity of virus-

host exchanges in order to achieve some understanding of the

events taking place at a given scale. Other modeling approaches

are required to analyze the treatment of AIDS patients, which

needs proper statistical and immunological models (Sloot et al.

2005; 2006) to generate patient-specific medical simulations

(Sadiq et al. 2008a). Similarly, the design of antiretroviral

inhibitors call for molecular simulation tools as close as possible

to the physicochemical events (Sadiq et al. 2008b). But they

must not be seen as better alternatives to the simple mathematical

models discussed above. Instead, as with other complex systems,

multiple scales are at work and different goals are associated to

the modeling paths taken in each case.

To close this section, we think it is worth mentioning the

existence of an alternative recent model that gives a more relevant

role to antibody responses in the control of viremia, and suggests

that escape from or progressive loss of quality of CD8+ T-cell

responses are associated with an acceleration of disease progres-

sion, the underlying cause of the breakdown of virus control

is the loss of antibody induction due to depletion of CD4+ T

cells (Wikramaratna et al. 2015). This more complex model does

better match with genomic data that indicate repeated selective

sweeps that result in purging antigenic diversity (Walker and

Korber 2001; Frost et al. 2005; Wibmer et al. 2013).

4.6 Viral Symbiosis

So far the general view of viruses emerging from previous chapters

offers a picture of these entities dominated by their parasitic

![[index-132_1.png]]

4.6. Viral Symbiosis

**117**

LTR retrotransposons

DNA transposons

SINEs

Simple sequence repeats

8.3%

2.9%

13.1%

Segmental

3%

duplications

5%

LINEs

Miscellaneous

8%

20.4%

heterochromatin

1.5%

11.6%

Miscellaneous

25.9%

unique sequences

Protein-

coding

genes

Introns

Figure 4.8. Frequency of different components of the human genome.

There is only a small percentage of the total genome that seems to play

a standard functional role, namely genes transcribed into proteins (just

1 _._ 5%), but a very high frequency of diverse genetic elements including

transposons and endogenous retroviruses.

nature. We have however already mentioned that this is an

incomplete perspective and that the more we know about viruses

the more we can appreciate a broader picture. We have discussed

in chapter 2]] the special nature of giant viruses, escaping from

the simplified view of viruses as pieces of software infecting the

cellular hardware. But there is more than that. In fact, viruses

can have beneficial effects on their hosts, creating a symbiotic

relationship (Roossinck 2011; Ryan 2009). And this might be far

from anecdotic. Many examples of viruses that provide functional

benefits to their hosts are known to create a mutualistic tie

(Roossinck 2011).

Strong evidence of a special relation between viruses and

their host organisms (and primates in particular) is provided

by the widespread presence of so-called endogenous retroviruses

(ERVs), which account for 8% of the total DNA content of the

human genome (Sverdov 2000; Belshaw et al. 2004). What is

the evolutionary significance of ERVs? One sound possibility,

**118**

Chapter 4. Virus Dynamics and Arms Races

supported by well-documented studies (Tarlinton et al. 2006)

of Australian koalas, indicates that endogenization of ERVs

has taken place, protecting their carriers against other lethal

pathogens (Denner and Young 2013).

More generally, we face a completely different scenario where

viruses infect the germ line, which allows long-term persistence

of viruses (Villareal 1997; Katzourakis et al. 2005). As pointed

out by Ryan (2009), a new evolutionary dynamics enters the

scene, allowing for novelties, and for selection to operate at the

level of host-virus interaction. This includes the possibility of an

evolving symbiotic relationship. Perhaps the best illustration of

this potential role in major evolutionary leaps is given by the

evolution of placental mammals (Harris 1991; Haig 2012).

The development of the placenta6 requires the presence of

ERVs. Specifically, the proper development of this multifunc-

tional organ proceeds through a process of cell fusion that takes

place between cells belonging to different tissues. Syncytin, a key

protein required for the fusion process, is provided by an endoge-

nous retrovirus (Villareal 1997; Haris 1998; Mi et al. 2000; Rote

et al. 2004). As pointed out by David Haig, the origin of the

placenta created a new niche that provided new opportunities for

ERVs to pass from mother to offspring. The resulting arms race

between host defenses and evasion mechanisms led to a final, tight

mutualistic relationship (Haig 2012).

Other remarkable examples include a long-term coevolution

between a large class of viruses (the polydnaviruses) and their

host wasps (Villareal 1997; Roossinck 2011). These wasps are

parasitoids: they are different from standard predators, since they

lay their eggs inside the larvae of their prey species, which develop

inside the body of the living larvae by eating them from inside.

The normal outcome of this should be an immune response

6The virus-driven evolution of the placenta took place independently at least

six times (Haig 2012 and references therein).

4.6. Viral Symbiosis

**119**

capable of encapsulating the injected eggs and inhibiting egg

development. However, the endogenous virus carried by the wasp

egg suppresses this response. The coevolutionary ties are very

strong and some authors have questioned how appropriate it is

to consider the polydnavirus as a real virus.7

From a more general perspective, viruses have played major

roles in promoting speciation and host innovation (Villareal

1997), even driving the host to increase in genome complexity.

These arms races have shaped ecological webs and have also

affected our own history. In the next two chapters, we explore

how viruses propagate through populations and how social and

transportation networks might affect epidemic outbreaks.

7As an example of the complex relationship between both partners, let us

mention that the genes required for viral replication and packaging have moved

to the wasp genome.5.2. SIS Model

**125**

The rise of industrial civilization and the increasing dom-

inance of cities clearly influenced the impact of epidemic

spreading. Once horse carts were replaced by fast, long-distance

transportation, the potential for pathogens to spread and even-

tually affect all human beings became inevitable. The invention

of commercial flights changed everything. Just a few decades after

the first short-lived experiment performed by the Wright brothers

in 1903, hundreds of humans were using aerial transportation.

How can these factors be incorporated in a modeling framework?

In this chapter we present some key results that allow us to explain

the nonlinearities and breakpoints that characterize epidemics,

including their rise and fall.

5.2 SIS Model

Epidemic modeling has been a very active area of research for

several decades (Anderson and May 1992; Keeling and Rohani

2007), with an enormous practical impact on our understanding

of the dynamics of infectious diseases. One of the simplest

models considers just two subpopulations, namely _infective_ ( _I_ )

and _susceptible_ ( _S_) individuals. The first are infected and carry the

pathogen with them while the second are pathogen-free and can

become infected. The states of these individuals can change due

to two basic processes: recovery ( _I_ → _S_) and infection ( _S_ → _I_ ), which occur with some fixed rates (that can be determined from

epidemiological data). While the recovery process is independent

of the state of other individuals, the infection process is not:

the more individuals are infected, the larger the probability of

infection.

The basic logic of the model, which contains the rules as-

sociated with transitions among alternative states, is shown in

figure 5.4a.]] The simplicity of this model can be appreciated by

comparing it with other more accurate ones, including the SIR

(for susceptible-infected-recovered) model (figure 5.4b).]] Here an

**126**

Chapter 5. Epidemics

**a**

**c**

_S_

_I_

_Is_

_R_

_S_

_E_

_Ip_

_H_

_F_

**b**

_S_

_I_

_R_

Figure 5.4. Transition graphs for different scenarios of epidemic propa-

gation. Here we include (a) the SIS model, (b) the SIR model, (c) the

SEIR model, and an example of a more complex transition diagram (d)

associated with the Ebola virus. Susceptible ( _S_), Exposed ( _E_ ), Infectious ( _I_ ), Hospitalized ( _H_), and Funeral ( _F_ ) indicate transmission from handling a diseased patient’s body, in contrast to Recovered/Removed ( _R_).

additional compartment has been included ( _R_), incorporating an

additional population of recovered individuals that are temporar-

ily immune to infection. In other cases, such as the epidemic

spreading of EBOV, a more complex set of transitions needs to

be added (figure 5.4c),]] including two additional classes of infected individuals as well as hospitalized and unburied corpses.

In this section a detailed analysis of the SIS model is intro-

duced. This is a toy model, and some basic assumptions are

required. One is that _I_ + _S_ = _N_, which means that, at some

scale, the total population remains constant. Secondly, there is

no heterogeneity and thus all interactions between individuals are

weighted with exactly the same parameter values. In a well-mixed

system, the rules outlined above can be described as two reactions

associated to infection and recovery, given by

_μ_

_I_ + _S_ −→ 2 _I_

(5.1)

_α_

_I_ −→ _S,_

(5.2)

5.2. SIS Model

**127**

and it is easy to show that the equations describing our system are

_d I_ = _μ_

_d S_

_I S_ − _α I_

= − _μI S_ + _αI,_

(5.3)

_d t_

_d t_

which, as we can see, gives _d I /dt_ = − _d S/dt_; and since the total

population _I_ + _S_ is conserved, using a normalized density of

infected individuals, _ρ_ = _I /N_, we have

_dρ_ = _μρ_(1 − _ρ_) − _αρ,_

(5.4)

_d t_

consistently with our previous result. We have a one-dimensional

model that can be solved by integrating the previous equation.

This equation can actually be rewritten as a logistic-like form:2

_dρ_ = _μρ_( _ρ_∗ − _ρ_) _,_

(5.5)

_d t_

where _ρ_∗ = 1 − _α/μ_. If _ρ_ 0 is the initial population of infected individuals, we obtain:

_ρ_∗

_ρ_( _t_) =

_._

(5.6)

1 + _ρ_∗

_ρ_ − 1 _e_ −( _μ_− _α_) _t_

0

The previous equation provides two interesting results. One is

the steady state reached for long times, i.e., for the limit _ρ_∞ =

lim _t_→∞ _ρ_( _t_), we have two possible solutions, namely _ρ_∞ = _ρ_∗

when _μ > α_ and _ρ_∞ = 0 when _μ < α_. The first point involves a stable epidemic event that would infect a fraction (1 − _α/μ_)

of individuals of the population, whereas the second represents

the extinction of the virus. The critical point _μc_ = _α_ separates

the subcritical phase, where the epidemic dies out, from the

supercritical phase, where the epidemic is self-maintained.

These two possible states are associated with two qualitatively

different phases, as it occurred with the numerical experiment

2In population dynamics, one of the simplest equations describing growth

of a population _N_ under limited resources is the _logistic equation_, defined as _d N/dt_ = _r N_(1 − _N/K_ ), where _K_ is the carrying capacity.

**128**

Chapter 5. Epidemics

described above using an SIS model on a lattice. We can compare

the predicted infected population with the previous result involv-

ing a spatial patterning. We have also run the previous model,

but in this case once we choose an empty site and then choose

a random site (not a nearest neighbor) that is infected, the first

can be infected too with a probability _μ_. The exact location of

the transition point has moved and the shape of the curve on the

right-hand side is slightly different, but the phenomenon itself

remains preserved.3

A second implication of the previous solution _ρ_( _t_) is that,

at the supercritical phase, the initial growth of the epidemics is

exponential. This can be shown by assuming that the current

relative frequency of infected individuals is very small, i.e.,

_ρ_ 1. In this case, it is possible to make the approximation

1 − _ρ_ ≈ 1, and thus the equation for epidemic spreading now

becomes

_dρ_

= ( _μ_ − _α_) _ρ,_

(5.7)

_d t_

_ρ_1

which is easily solved and leads to an exponential solution:

_ρ_( _t_) = _ρ_(0) _e_( _μ_− _α_) _t._

(5.8)

This approximated solution holds in early phases of an outbreak;

and we will observe a rapid propagation provided that _μ > α_

(otherwise the epidemic dies out). As defined above, it is easy to

see that the previous equation can be also written as

_ρ_( _t_) = _ρ_(0) _eα_( _R_ 0−1) _t,_

(5.9)

where _R_ 0 is the so-called _basic reproductive number R_ 0, defined

here as

_μ_

_R_ 0 =

_._

_α_

(5.10)

3The use of space makes propagation more difficult, since infection is limited

to a small number of neighbors instead of potentially affecting _any_ individual.

5.2. SIS Model

**129**

Table 5.1. Examples of viral pathogens involving different forms of trans-

mission between individuals and their characteristic basic reproductive

numbers _R_ 0.

Disease

Transmission Route

_R_ 0

EBOV (2014 outbreak)

Body fluids

1.5–2.5

HCV

Blood-to-blood contact

1.2–1.7

HIV-1

Sexual contact

2–5

IAV H1N1 (1918 pandemic)

Airbone droplet

2–3

Measles

Airbone

12–18

Mumps

Airbone droplet

4–7

Polio

Fecal-oral route

5–7

Rubella

Airbone droplet

5–7

SARS coronavirus

Airbone droplet

2–5

Smallpox

Saliva

6–7

This result captures a fundamental message: propagation occurs

provided that _R_ 0 is larger than 1.4 This parameter is usually de-

fined as the expected number of secondary infections produced by

a single (typical) infection in a completely susceptible population.

Table 5.1]] shows the _R_ 0 values estimated for some well-known viral diseases. Values widely range from 1.2 (for genotype 6 of

HCV) to 18 (for the measles virus) and are clearly influenced

by the route of transmission. Epidemic spreading will occur if

_R_ 0 _>_ 1 and die out instead for _R_ 0 _<_ 1. It is interesting to note that _R_ 0 involves several components, including the infectivity of

the pathogen _μ_ but also the population size _N_.

An important message needs to be taken from the early growth

equation: if the pathogen has an _R_ 0 _>_ 1, the outbreak will

result in exponential growth, meaning that unless the process is

controlled at early stages, it can easily escape out of control. Such

a situation (as discussed below) is exacerbated by the modern

4If we normalize our population to _I_ + _S_ = _N_ we obtain _R_ 0 = _μN/α_, thus including the population size _N_ as a key component. This is actually consistent with the transition found in figure 5.3a,]] where a critical _Nc_ ≈ 3 × 104 seems to be at work.



**130**

Chapter 5. Epidemics

scenario of widespread and fast human mobility patterns, which

strongly favor the spread of the pathogen. However, knowing the

exact value of _R_ 0 is also the key for limiting or even stopping

the epidemic outbreak. It is easy to show that, when a fraction

_r_ of individuals in the population has been vaccinated or simply

isolated from others, the basic reproductive number gets corrected

to _R_ 0 = 1 _/_(1 − _r_ ). That means that proper action on a fraction of the total population can trigger an epidemic to die out.

It can be shown, for example, that for the EBOV case with

_R_ 0 = 1 _._ 5, just a third ( _r_ ≈ 1 _/_ 3) of the individuals need to be treated. This is in fact the basis of vaccination, which does not

necessarily require a whole-population treatment. In some cases,

however, high _R_ 0 numbers require vaccination of all involved

agents.

5.3 SIS Model in Space and Graphs

The previous equations defining the SIS model dynamics can be

extended in many ways to incorporate more elements of realism.

On the one hand, individuals do not interact in a fully mixed

fashion: to some extent, infection is a process that requires locality

as we are more likely to interact with some subsets of individuals

than with others that live beyond some distance. On the other

hand, the use of transportation systems also has a major impact

on the patterns of infection. Moreover, models described by

differential equations miss an important ingredient: the stochastic

nature of epidemic spreading. In order to address these missing

parts, it is convenient to take a new look at the SIS model from a

microscopic perspective.

Consider a given system composed by _N_ individuals interact-

ing through these SIS rules. For simplicity, assume that each in-

dividual in this system occupies a node in a network. Interactions

here are described by edges. The resulting graph can, for example,

be random (figure 5.5a),]] with nodes having a probability _p_ of

5.3. SIS Model in Space and Graphs

**131**

being connected to each other. This is the so-called Erdös-Rényi

random graph. In general, if the population can be represented as

a network where vertices _vi_ (with _i_ = 1 _, ..., N_) are individuals and edges (links) between them indicate potential interactions,

a given individual can have _ki_ (with 1 ≤ _ki_ ≤ _N_) edges. This

quantity is known as the _degree_ of the _vi_ agent (Newman 2010)

and the _average degree_ of the graph is given by

_N_

_k_ = 1

_k_

_N_

_i ,_

(5.11)

_i_=1

and provides a statistical measure of the network connectivity.

Moreover, this graph has an associated distribution of connec-

tions, or _degree distribution_, _P_ ( _k_), that follows a binomial shape,

_N_ − 1

_P_ ( _ki_ = _k_) =

_pk_(1 − _p_) _N_− _k_−1 _._

(5.12)

_k_

Here _P_ ( _k_) is a homogeneous distribution, with a well-defined

average degree5 _k_ = _p_( _N_ − 1). An example of a random graph

of this type (if we ignore the location of nodes) is shown in

figure 5.5a.

A lattice (figure 5.5b)]] is another limit case of a graph where

each node has exactly the same number of neighbors, i.e.,

_P_ ( _k_) = _δqk_, for all vertices.6 An intermediate situation is given by figure 5.5c,]] where interactions are random but spatially

limited to nearest sites. The rules of the SIS model described

above can be easily mapped into our networks. In figure 5.6]]

we show how this works. Consider a given noninfected site

(open circle) with just three neighbors. Suppose that this node

can be infected with probability _μ_ if one of these neighbors is

5More generally, the average degree can be obtained from _P_ ( _k_) by means of

the integral _k_ = _K P_ ( _k_) _dk_, with _k_

_k_

0 and _K_ indicating the limit values of _k_.

0

6The distribution _δqk_ is the so-called Dirac’s delta function, defined as

_δqk_ = 1 when _k_ = _q_ and zero otherwise.

![[index-147_1.png]]

![[index-147_2.png]]

**132**

Chapter 5. Epidemics

**a**

**b**

Figure 5.5. Networks of interactions. Two different examples of net-

works are shown here, where nodes (empty circles) represent individuals

in a population and their links indicate the presence of (potential)

interactions. The examples include (a) a random graph where every two

elements (randomly scattered) are connected to each other with some

probability and (b) a square lattice, with each individual having exactly

_q_ = 4 neighbors (zoomed area).

![[index-148_1.png]]

5.3. SIS Model in Space and Graphs

**133**

**a**

**c**

_μ_

3 _μ_

**b**

**d**

2 _μ_

_α_

**e**

_qρμ_

**f** 0.7

0.6

0.5

0.4

_ρ_

0.3

0.2

0.1

0.0

0.00

0.05

0.10

0.15

0.20

0.25

0.30

_μ_

Figure 5.6. Phase transition in the SIS model. The rules are indicated in

(a-d) for a system where each element is connected to just three neighbors,

here • ≡ _I_ and ◦ ≡ _S_, respectively. For a given _μ_, infection (a-c) will be more likely as the fraction _ρ_ increases. Additionally, recovery (d) occurs

with a probability _α_. In an arbitrary case, such as a lattice (e) with _q_

nearest sites, the probability of infection will grow proportionally to _qρ_.

In (f) we display _ρ_ against _μ_ using a square lattice with _L_ = 100

and _α_ = 0 _._ 1. A marked transition occurs at _μc_ ( ) ≈ 0 _._ 15. Three spatial snapshots are also indicated (inset).

**134**

Chapter 5. Epidemics

infected (figure 5.6a).]] If more than one is infected, for small _μ_

this probability grows linearly7 (figures 5.6b-c).]] The recovery rule instead is independent of the states of the neighbors (figure 5.6d).]]

The SIS model reactions defined above can be easily expanded

to arbitrary networks, including regular lattices (Newman 2010).

The previous algorithm can be easily extrapolated to other net-

works and lattices. In figure 5.6e]] we indicate this for a square

lattice having a fraction _ρ_ of infected nodes and a given number _q_

of nearest sites. For this particular case, where epidemic spreading

is confined to nearest sites, a stochastic cellular automaton is

defined on an _L_ × _L_ lattice = { _r_ = ( _i, j_ )|1 ≤ _i, j,_ ≤ _L_}.

The state of each site _σ t_ ∈ {

_t_

0 _,_ 1} at a given step _t_ indicates

the presence of infected (1) or susceptible (0) individuals. The

simulation starts from a random initial condition with a fraction

of infected sites _σ t_ =

_x_

1 and the rest set to zero (susceptible). The

rules of the simplest version of the model (see Solé and Bascompte

2006 for details) are:

1. Choose a site _r_ ∈ at random.

2. If _σr_ = 1, a transition to _σr_ = 0 occurs with

probability _α_.

3. If _σr_ = 0, choose a random neighbor _σu_. If _σu_ = 1, an

infection event will occur with probability _μ_.

4. Repeat (1)

In figure 5.6f]] we show the results of a numerical simulation of

an epidemic spreading on a two-dimensional 100 lattice, where

we start from an initial condition with half (randomly chosen)

of the individuals being infected (here indicated as black dots).

Three examples of the dynamical patterns are shown in the inset

7The exact form of this probability is obtained as follows. If a given site

is empty, and _ρ_ is the fraction of the infected site, the probability none

of them will infect is (1 − _μρ_) _q_ , and thus the probability that some will is 1 − (1 − _μρ_) _q_ ≈ 1 − _e_ − _μρq_ . For small _μρ_ we have _e_ − _μρq_ ≈ 1 − _μρq_ , and a linear relation is obtained.

5.3. SIS Model in Space and Graphs

**135**

plots. Using different infection probabilities _μ_, we measure the

probability of propagation by determining if infected individuals

can be found after _T_ = 500 steps. By averaging over _M_ = 100

runs, and using a probability of recovery _α_ = 0 _._ 10, we obtain

a phase transition diagram displaying a sharp change at a given

_μc_ ( ) = 0 _._ 15. The simulation thus shows a phase transition

between epidemic die out and propagation, but the predicted

(mean field) value is different from the _μc_ = _α_ mean field

expectation. The reason for this difference is to be found in the

strong limitations imposed by local interactions.8

The previous result is generic: if local interactions are taken

into account, the resulting dynamical patterns and predicted

thresholds depart from the mean field approximation (Hinrichsen

2000; Marro and Dickman 1997). If we depart from the lattice

model and move into a random graph organization, we recover

the basic results predicted by the mean field model. This can be

tested by simulating the previous rules on an Erdös-Rényi graph,

where the “neighbors” are now replaced by connected nodes in

the network. A comparative plot is displayed in figure 5–7.]] Here

a lattice as well as a random graph with _N_ = 100 nodes have been

used. For the random web we have used a _p_ value that gives an

average degree _k_ ≈ 4 that compares with the _q_ = 4 neighbors

of the lattice model. The two curves clearly illustrate the main

difference in terms of the speed of propagation of the epidemics.

While the lattice model displays a slow, almost linear growth, the

random graph allows for a rapid expansion.

An important message (to be reanalyzed at the end of this

chapter) is that geography—or its absence—deeply constrains

8A formal approach to the spatial spread of epidemics on a given domain

is to consider a continuous field _ρ_ = _ρ_( _x , t_) that follows a partial differential equation

_∂ρ/∂t_ = _μρ_(1 − _ρ_) − _αρ_ + _D_(1 − _ρ_)∇2 _ρ,_

where the diffusion coefficient reads _D_ =

_μ_( _r_ ) _r_ 2 _dr_ (Kephart and White

1991).

![[index-151_1.png]]

**136**

Chapter 5. Epidemics

800

600

400

Fraction of infected sites 200

0

0

100

200

300

400

500

Time

Figure 5.7. The impact of network topology on epidemic spreading.

Here two different types of graphs with _N_ = 100 nodes have been used.

These include an Erdös-Rényi graph where two nodes are connected with

a probability _p_ (thin line) to be compared with a square lattice (thick

line). Here _q_ = 4 and _p_ = 0 _._ 04, so that the average number of neighbors is _k_ = 4. Three snapshots of the lattice model, with different initial

seeds of infected sites, are shown in the inset for three different early

stages.

virus propagation. In general, local dynamics leads to propagating

fronts (Murray 2004; Shigesada and Kawasaki 1997), and the

linear growth displayed by the lattice model was first reported in

the growth of viruses on cell monolayers in Petri dishes (Koch

1964). Before transportation was efficient, the role played by

geography was also dominant in spreading diseases. Smallpox

propagated in waves across the Old World (possibly originating in

Egypt)9 long before it arrived to the New World carried by Cortés

and his warriors. In both cases, viruses and other pathogens were

carried by humans through old transportation networks. Since

then, our society and technology have experienced enormous

changes, including the rapid spread of individuals. Geography,

9Skin lesions found in mummies are consistent with smallpox symptoms.

5.4. AIDS: Modeling HIV-1 Transmission

**137**

in a way, is gone. But we cannot completely ignore it. As climate

change modifies our biosphere, the geographic ranges of disease

vectors (such as mosquitoes) slowly expands, along with the

viruses they carry.

5.4 AIDS: Modeling HIV-1 Transmission

The SIS model is an oversimplified picture of epidemic spreading

but it gives us a powerful insight into the presence of eradication

thresholds. Moreover, despite its simplicity it is used as a baseline

for several well-known epidemics. In chapter 7]] we will consider

a natural extension of the model incorporating a “recovered”

compartment, where individuals who have been infected do not

return to the susceptible state. More generally, we might ask how

to proceed when the problem under consideration requires more

population compartments and thus a larger number of parameters

and equations.

In this section we consider a model proposed by Anderson

and May (1998) that is aimed at studying the spread of AIDS in

a structured population where four compartments are included

(figure 5.7).]] The model assumes a population of _N_( _t_) susceptible males that receives an input flow (at a rate _β_) of new individuals

representing a constant immigration. If _X_ ( _t_) stands for the num-

ber of susceptibles at time _t_, the model assumes that infectious

males are generated at a given rate _λc_ , where _λ_ is the probability

of becoming infected from a partner, i.e.,

_η_

_λ_ = _Y ,_

(5.13)

_N_

_η_ being the rate of transmission. This population can now

experience two possible transitions: toward either patients develo-

ping AIDS or individuals who have antibodies against the virus

(seropositive) but show no symptoms of infection and are not

infectious. All compartments incorporate a natural death rate _μ_,

**138**

Chapter 5. Epidemics

but an additional rate needs to be used for the AIDS patients.

The diagram depicted in figure 5.7]] summarizes all the potential

transitions and relevant parameters.

The final model can be described by a set of four differential

equations, namely:

_d X_ = _β_ − _μX_ − _λc X_

(5.14)

_d t_

_d Y_ = _λc X_ − ( _ν_ + _μ_) _Y_

(5.15)

_d t_

_d A_ = _pνY_ − ( _d_ + _μ_) _A_

(5.16)

_d t_

_d Z_ = (1 − _p_) _νY_ − _μZ_;

(5.17)

_d t_

a total population is given by

_N_( _t_) = _X_ ( _t_) + _Y_ ( _t_) + _Z_( _t_) + _A_( _t_) _,_ (5.18)

which in this case is not constant (since flows include mortality

and thus no strict conservation). In these system, _p_ provides the

rate of seropositives that are infectious, whereas _ν_ will define the

transition rate from infected to AIDS cases. It is important to

realize that _λ_ is given by

_η_

_λ_ =

_Y_

_,_

(5.19)

_X_ + _Y_ + _Z_

and the model also assumes that _A_ _N_.

One specific question related to this model is: can we provide

a reliable estimate of _R_ 0? To answer this question, let us first

determine the sum of all the previous equations, which gives a

simple expression:

_d N_ = _B_ − _μN_ − _d A._

(5.20)

_d t_

Now if we take the previous equation for the evolution of the

number of infectious individuals _Y_ , it is possible to see that, at

5.4. AIDS: Modeling HIV-1 Transmission

**139**

time _t_ = 0, we can write:

_d Y_

≈ ( _βc_ − _ν_ − _μ_) _Y._

(5.21)

_d t_

_t_=0

This will lead to a propagation of the epidemic if

_d Y_

_>_ 0

(5.22)

_d t_

_t_=0

and thus if

( _βc_ − _ν_ − _μ_) = _ν_( _R_ 0 − 1) _>_ 0 _,_

(5.23)

where we have defined

_βc_

_R_ 0 = _ν_

(5.24)

as the basic reproductive number. Although other results can also

be derived from the model using the appropriate assumptions,10

we have already obtained an interesting result that, despite the

rough assumptions, works very well.

Can we also derive time-dependent estimates of the numbers

of individuals developing AIDS? Following the previous approxi-

mation, the solution to the approximated equation for _d Y/dt_ at

early times gives an exponential function,

_Y_ ( _t_) = _Y_ (0) _e ν_( _R_ 0−1) _t,_

(5.25)

predicting exponential growth of the number of infected indi-

viduals. If we take this result as a good approximation for the

beginning of the outbreak, we can now use the equation for the

number of AIDS patients and include the previous result:

_d A_ = _pνY_( _t_) − ( _d_ + _μ_) _A_;

(5.26)

_d t_

10For example, it is possible to provide estimates of the duration of epidemic

outbreaks and other dynamical and stability properties.

**140**

Chapter 5. Epidemics

**a**

Susceptible X

**b** 1.0

_β_

_μ_

_λc_

0.8

Seropositive

Infectious Y

0.6

_pv_

_μ_

(1 – _p_) _v_

0.4

AIDS A

Seropositive

Proportion

non-infectious Z

AIDS

0.2

_d_

_μ_

_μ_

0 0

4

8

12

16

20

24

28

Years

Figure 5.8. Flow diagram of the Anderson and May (1998) model for the

development of the AIDS pandemic. Four compartments are included

in the model description, as discussed in the text. In (b): Numerical

solution of the Anderson-May model for AIDS propagation. Here both

seropositive and AIDS populations are displayed (redrawn after Anderson

et al. (1986)). The system starts with an initial condition _S_(0) + _Y_ (0) =

_N_(0) = 100 _._ 000, and a reproductive rate _R_ 0 ≈ _βc /v_ ∼ 5 _._ 15 is used.

Adapted from Murray (1999).

and if _A_(0) = 0 it is possible to show that the predicted number

for _A_( _t_) follows

_e ν_( _R_ 0−1) _t_ − _e_ ( _d_+ _μ_) _t_

_A_( _t_) = _pνY_ (0)

_._

(5.27)

_r_ + _d_ + _μ_

The estimated parameters obtained from existing populations

within these groups allowed us to estimate how long it would take

to double the number of seropositives, which gave an ∼ _nine_ -

month window. Similarly, the basic reproductive number was

calculated to be _R_ 0 ≈ 3 − 4. An illustrative example of the model

predictions is shown in figure 5.8,]] where the time evolution

of both seropositive patients and those developing AIDS is

displayed.

The modeling of the AIDS pandemic has been a very active

field, and models have been improved to incorporate more

detailed information, from additional classes of individuals to age

structure (Chavez 1989, 2013; Huang et al. 1992). However,

5.5. Halting Viruses in Scale-Free Networks

**141**

some crucial aspects of the epidemic dynamics require consider-

ing an element that has been neglected in the previous models:

viruses spread on networks made by individuals who can be

connected in complex ways.

5.5 Halting Viruses in Scale-Free Networks

In previous sections we have considered models of epidemic

spreading that occur either in a well-mixed (mean field) context,

random graphs, or in a spatial domain where interactions are

limited to contacts among nearest neighbors on a lattice. The

first type deals with a geography-free world whereas the second

explicitly takes into account the local nature of the infection

process. As discussed in previous sections, the two approaches

offer interesting insights, but neither is completely realistic:

humans are neither well mixed nor so limited by two-dimensional

spatial constraints. In order to fully understand the patterns of

epidemic spreading, it is essential to take into account the social

networks that underlie human behavior.

What is thus missing from our previous examples? In section]]

5.4]] we have discussed a simple model for the AIDS pandemic,

where the population was split into several classes, finding an

estimate of _R_ 0. What would be the relevance of adding the

structure of human interactions? A crucial finding was to show

that sexually transmitted diseases (STDs) seem to propagate

across highly heterogeneous networks (figure 5.9a)]] involving a

vast number of individuals having a small number of contacts

while a handful have a large number of contacts, thus acting as

hubs in the network (Liljeros et al. 2001; Lloyd and May 2002;

Schneeberger et al. 2004; Latora et al. 2006).

The resulting degree distribution for these sexual contact

networks (figure 5.9b)]] is a _scale-free_ one, and the impact of their heavily asymmetric probability distribution, with a long tail

of low-contact cases, deeply changes our perception of disease

![[index-157_1.png]]

**142**

Chapter 5. Epidemics

**a**

**b** 100

10–1

_α_

_k_) 10–2

( _P_ >

10–3

Females

Males

10–4

102

101

100

_k_

Figure 5.9. Sexual contact networks. In (a) we display an idealized picture

of these webs, where most individuals have one or two contacts whereas a

handful have many (graph generated using the Barabási and Albert (1999)

preferential attachment model; see text). In (b) an example of the observed

degree distribution _P>_ ( _k_) of sexual partners in a given community is shown. Adapted from Liljeros et al. (2001).

propagation and the role played by social interactions. Specifi-

cally, scale-free networks (SFNs) display a degree distribution that

decays as a power law, namely:

_P_ ( _k_) = 1 _k_− _γ ,_

(5.28)

_Z_

with 2 _< γ <_ 3 and _Z_ being a normalization constant. Before

proceeding with the analysis of the dynamical process that takes

place on a highly heterogeneous scale-free network (SFN), let us

consider one possible way of modeling such a network.

The simplest mechanism that allows to build an SFN is the

so-called _preferential attachment_ rule (Barabási and Albert 1999).

In order to build this type of net, we start from a given small

network with _m_ 0 nodes, and then apply two simple rules: (i) at

each time step, add one new node to the system and (ii) link

the new node to _m_ randomly chosen nodes. When choosing the

5.5. Halting Viruses in Scale-Free Networks

**143**

nodes, we assume that the probability _π_( _ki_ ) that a new node will

be connected to node _i_ will be proportional to its degree, i.e.,

_π_( _ki_) = _ki_

_._

(5.29)

_k_

_j_

_j_

After _t_ time steps a network with _N_ = _t_ + _m_ 0 nodes (and _mt_ edges) is generated, exhibiting an SF topology with _γ_ = 3

(figure 5.8a).]] Other possibilities include considering aging and

cost (Amaral et al. 2000), and can be easily introduced in order

to include cut-offs at given connectivities.

The problem of epidemic spreading in SFNs will be explored

by means of an SIS model. As before, each node in the graph

of interactions will be an individual and each link a potential

pathway of disease spreading. The average density of infected

individuals, _ρ_( _t_) (prevalence), at the mean-field level is

_dρ_( _t_) = _μ_ _k_ _ρ_( _t_)[1 − _ρ_( _t_)] − _αρ_( _t_); (5.30)

_d t_

by defining an effective spreading rate _λ_ = _μ/α_, we can simply

write:

_dρ_( _t_) = _λ_ _k_ _ρ_( _t_)[1 − _ρ_( _t_)] − _ρ_( _t_) _._

(5.31)

_d t_

The benefit of this mean-field equation stems from the fact

that density correlations are ignored. On random graphs and

related graphs, one can assume that _k_ _k_ . Following our

previous analysis of the contact processes, it is easy to see that

a nonzero epidemic threshold exists at _λc_ = _k_ −1 such that

_ρ_ = 0

if _λ < λc ,_

(5.32)

_ρ_ ∼ 1 − 1

_k_

if _λ_ ≥ _λc ._

(5.33)

So far, everything seems pretty much the same. But a crucial prop-

erty of SFN changes everything (Pastor-Satorras and Vespignani

2001a, 2001b; Lloyd and May 2001; Dezsö and Barabási 2001;

Barabási 2016).

**144**

Chapter 5. Epidemics

As discussed in section 5.3,]] simple random graphs have a

characteristic average number of links per site that is properly

represented by the average degree _k_ . Statistically, that means

that the networks are homogeneous and thus they have a well-

defined standard deviation _σ_ =

_k_ 2 − _k_ 2 around the mean

value. In stark contrast, the fluctuations _k_ 2 in SFNs diverge

for any value 2 _< γ <_ 3, and thus highly connected nodes

are statistically significant: the mean field approximation breaks

down. In order to take into account these fluctuations, the relative

density _ρk_( _t_) of infected nodes with given connectivity _k_ must

be taken into account. The mean-field equations can thus be

written as

_dρk_( _t_) = _λk_ [1 − _ρ_

_d t_

_k_ ( _t_ )] ( _ρ_( _t_ )) − _ρk_ ( _t_ )

(5.34)

for _k_ = 1 _, ..., N_. A new term ( _ρ_( _t_)) indicates the probability that any given link points to an infected node. The probability

that a link points to a node with _k_ links is proportional to _k P_ ( _k_).

A randomly chosen link is thus more likely to be connected to an

infected node with high connectivity, yielding

_k P_ ( _k_) _ρ_

( _ρ_( _t_)) =

_k_

_k_ ( _t_ )

_,_

(5.35)

_k P_ ( _k_)

_k_

where

_k P_ ( _k_) = _k_ by definition. At the steady state

_k_

_dρk_( _t_) _/dt_ = 0, and we get

_λ_

_ρ_

_k_

_k_ =

_,_

(5.36)

1 + _λk_

and the following relation follows:

_λ_

= 1

_k ,_

_k P_ ( _k_)

(5.37)

_k_

1 + _λk_

_k_

where is now a function of _λ_ alone.

The solution = 0 is always satisfying the previous equation.

A nonzero stationary prevalence ( _ρk_ = 0) is obtained when the

right-hand side and the left-hand side of equation 5.40, expressed

5.5. Halting Viruses in Scale-Free Networks

**145**

as function of , cross in the interval 0 _<_ ≤ 1, allowing a

nontrivial solution. It is easy to realize that this corresponds to

the inequality

_d_

1

_λk_

_k P_ ( _k_)

≥ 1

(5.38)

_d_

_k_

1 + _λk_

_k_

=0

being satisfied, defining the critical epidemic threshold by:

_k P_ ( _k_) _λ_

_k_ 2

_k_

_c k_ =

_λ_

_k_

_k_ _c_ = 1;

(5.39)

in other words, we obtain:

_λ_

_k_

_c_ =

_,_

(5.40)

_k_ 2

which is nothing but the inverse of the coefficient of variation

(CV; see Anderson and May 1991). This result means that _in_

_SFNs with γ_ ∈ (2 _,_ 3) _we have λc_ = 0 _, and thus for any λ the_ _infection can pervade the system with a finite prevalence_ (Pastor-Satorras and Vespignani 2001). For small _λ_ it is possible to solve

explicitly the previous equation and calculate the prevalence in

the endemic state as follows:

_ρ_ =

_P_ ( _k_) _ρk._

(5.41)

_k_

In the particular case of the Barabási-Albert network with _γ_ = 3,

we find _ρ_ ∼ exp(− _C/λ_) where _C_ is a constant.

The absence of any epidemic threshold in this network can

be understood by noticing that in heterogeneous systems the

basic reproductive number _R_ 0 contains a correction term linearly

dependent on the standard deviation of the connectivity distri-

bution. In SFNs the divergence of the connectivity fluctuations

leads to an _R_ 0 that always exceeds unity at any rate _λ_. This

ensures that epidemics always have a finite probability of surviving

indefinitely.

**146**

Chapter 5. Epidemics

0.3

0.2

_ρ_

0.1

0.0

0.0

0.1

0.2

0.3

0.4

0.5

_λ_

Figure 5.10. Lack of eradication thresholds in epidemic models on scale-

free networks. Here the mean field model prediction displaying a phase

transition (in an SIS model) is compared with the one shown for a scale-

free network (dashed line).

Is there a way out of this bad news? The good news is that

a proper assessment of how to prevent hubs from spreading

the disease can bring the dynamics back to the threshold-like

behavior. This method has been dubbed “curing the hubs”

(Dezsö and Barabási 2002), where a cost-effective approach

is taken with a policy biased toward hubs. Its authors have

proposed a strategy where they assume some degree of accuracy

in identifying hubs, measured by means of a parameter , with

curing of a given node _vi_ being proportional to _ki_. This factor

now will replace the recovery rate _α_ used in our previous models.

When = 0, the curing is random and we recover the previous

scenarios, while _>_ 0 indicates a degree of success scaling with .

It is possible to show that even small values of allow us to recover

the epidemic threshold condition. This can be achieved even if no

complete information is available concerning the exact identity of

hubs, it is possible to drive the virus into extinction.

![[index-162_1.png]]

e

can

b

(picture

might

them

spreading

nodes

etweenb

other

epidemic

and

Since

ubshy

connections

b

played

440,000

heterogeneous.

role

about

veryis otential

with

p

the

network

world,

the

the

in

identifying

network,

ebs,

airports

w

contact

these

4,000

to

sexual

around

the

thanks

of

ap

with

event

m

s

a

A

is

andemic

Here

p

rokman).

a

B

importance.

5.11.

irk

into

D

crucial

Figure

after

expand

of

**148**

Chapter 5. Epidemics

The architectures of social and transportation networks, both

displaying heterogeneous structures (figure 5.10),]] represent a

threatening risk for the large-scale spread of pandemics, and in

this context forecasting and control is a great challenge (Hufnagel

et al. 2004; Vespignani 2011). The impact of one of these events

can be harmful, even devastating for our society and economy.

More importantly, we are pushing the boundaries of our planet to

its limits due to a combination of demographic explosion and the

overexploitation of and damage to the biosphere. These impacts

pervade a crucial aspect of epidemics: how they originate and how

they can become pandemic.

**6**

E M E R G E N T V I R U S E S

As we have discussed in previous chapters, viruses have been

major players through evolution, including the origin of some

key transitions of life, the history of humankind, and even that of

the entire planet, influencing ecological dynamics, geochemical

cycles, and biomass turnover. They are not only everywhere,

they are also a crucial component of ecological webs. Ecosystems

have been deeply modified by humans and, under the right

circumstances, these modifications can become a serious threat.

Anthropogenic effects and an explosive demography are the

triggers of multiple sources of perturbations: habitat loss and

fragmentation, species invasions, hunting to extenuation, and

extensive agronomical practices that have dramatically changed

the landscape are the main examples of such changes. They

are occurring at a very fast pace, much faster in fact than any

previous biotic change that has taken place on the planet, with

the exception of some of the most devastating mass extinction

events (LeGuenno 1995; Holmes 2009).

A rather undesirable outcome of such human-driven changes

as bringing in close contact farm animals and crops with wild

animals and plants that may be reservoirs of a number of viruses

is the “emergence” of new pathogenic viruses (Woolhouse et al.

![[index-165_1.png]]

**150**

Chapter 6. Emergent Viruses

a

b

c

d

e

f

Figure 6.1. Three examples of emergent viruses (left column) and some

of their carriers. Hantavirus (a) is one of the recent, most deadly emerging

viruses resulting from the jump from its natural carriers (mice; b) to

humans. The EBOV (c) may be transmitted to humans through the

ingestion of meat from chimpanzees (d). Similarly, the _Tomato torrado_

_virus_ (e) is an aphid-transmitted virus that infects tomato plants (f) and

was first detected in Spain in 2006.

2001, 2005). Indeed, a virus can be defined as “emerging” if it

meets one or more of the following conditions:

1. An already known viral disease that spreads out in a

new geographic area or population. Examples of this

type of emerging viruses are Zika, Dengue,

Chikungunya, West Nile, yellow fever, or the tomato

leaf curly geminivirus.

2. A new infection resulting from the evolution of an

existing virus that has acquired new biological

Emergent Viruses

**151**

properties (e.g., host range, pathogenicity, vector

transmission ...). Examples of this second type of

emerging virus are many: EBOV (jumping from bats to

humans), HIV-1 (from monkeys to humans), the

four-corners hantavirus (from rodents to humans), and

the canine parovirus (from cats to dogs), and the

_Canine distemper virus_ infecting sea lions in the North

Sea or lions in West Africa; but it also incorporates the

periodic rise of new genomic rearrangements of the

IAV (H5N1 in Hong-Kong in 1997, H1N1 in Mexico

in 2013).

3. A disease or virus that has been infecting us for a long

time but remained undetected until diagnosed for the

first time due to increased surveillance or to new

diagnostic tools. In this sense, all viruses have been

“emergent” at some point. Examples of this third class

are the human papillomaviruses, the Epstein-Barr

(infectious mononucleosis), and the HBV.

The rise of such emergent viruses requires three phases

(Woolhouse et al. 2001, 2005). The first phase represents ecolog-

ical opportunities (section 6.1]] below), that is, the chances of the

virus spilling over from its reservoir host to a new one. Spillovers

can occur with or without changes in the genetic structure or

biological properties of the virus, simply as a consequence of

increased opportunities of transmission due to perturbations in

the ecosystem. However, in many other instances, these early

steps in the process of emergence strongly depend on the popula-

tion genetics of the virus in its reservoir (e.g., how much genetic

variability is generated and maintained within the population of

the reservoir host), as the likelihood of succeeding in the novel

host would depend on the fitness of the different genetic variants

maintained in the reservoir host. The second phase is considered

to start once the virus infects a novel host and corresponds to all**152**

Chapter 6. Emergent Viruses

Human

West Nile

monkeypox

virus

Enterovirus 71

Whitewater

Hepatitis C

H5N1

arroyo virus

Ebola

SARS

Lassa

HIV

Dengue

Hantavirus

Marburg

Zika

Nipah

Zika

Human

Hendra

monkeypox

Figure 6.2. Geographic distribution of original outbreaks of emergent

(and re-emerging) viruses. Different locations and the associated virus are

indicated.

the genetic and evolutionary processes that drive its adaptation to

the novel host (section 6.2]] below), including changes both in the

virus’ genome and in its fitness, infectivity, and virulence. This

phase usually involves profound changes in the way the virus and

the host cells interact. The third and final phase of the emergence

process describes the epidemiological spread of the new virus,

already more or less adapted, into the global population of the

novel host (section 6.3]] below). This epidemiological phase is

dominated by the demography and behavior (population size and

density) and migration patterns, among other factors. Obviously,

these three phases are not entirely sequential but can overlap in

time and affect each other.

6.1 Ecological Disturbance: Hanta- and

Arenaviruses as Case Studies

Many examples of emergent viruses have been reported

(figure 6.2).]] A good example of emergent diseases linked to the

6.1. Ecological Disturbance

**153**

breakdown of the equilibrium between a species and its habitat

are those caused by the Hanta- or Arenaviruses. Hanta- and

Arenaviruses are zoonotic RNA viruses that are transmitted from

rodents (e.g., mice and rats) to humans. These rodents are merely

a step in the transmission chain between the virus and humans.

The relationship between the rodent and the virus is a typical case

of commensalism,1 with the rodents acting as the reservoir host

and being unaffected by the virus.

Although direct transmission of the virus (i.e., through bites)

is uncommon, infection can occur as a result of eating conta-

minated food, or touching the mouth or nose after handling

a contaminated surface, or even by airborne transmission of

the aerosol particles released by the rodents with their saliva.

Infection with Hanta- or Arenaviruses can cause quite serious

diseases: Hantavirus infection can cause Haemorrhagic Fever

with Renal Syndrome (HFRS) or Pulmonary Syndrome (HPS),

the latter being a very serious and actually fatal condition in

about half the reported cases. Scientists have demonstrated that

habitat destruction and climate change can increase the possibility

of Hanta- or Arenavirus infection in human populations. The

question is: how and through what mechanisms?

It is well known that rodents can thrive in a wide range of

habitats, from forest to grassland, canyon, and desert. They can

survive in any dry land habitat and invade and exploit disturbed

areas. The deer mouse, in particular, is one of the most common

transmitters of Hantaviruses to humans; it is extremely common

in areas affected by flooding, fire, avalanches, and mining or

construction work. Rodents are omnivores and store food for

winter consumption, making human-occupied areas especially

attractive given the supply of acorns, nuts, insects, other small

invertebrates, and various plant parts that rodents need to survive.

1A type of relation involving two different kinds of organisms, which benefits

one and does not harm the other.

**154**

Chapter 6. Emergent Viruses

Therefore, habitat destruction in the vicinity of suburban areas

furnishes an attractive environment to these animals, triggering

sizable population outbreaks. These outbreaks are regulated in

part by climate change, since variations in temperature and/or

rainfall patterns influence rodent populations given the indirect

impact on both the total nutritional biomass available (plants,

fruits, and invertebrates) and animal reproductive processes (e.g.,

reproductive seasons or gravidity rates). Hanta- and Arenaviruses

are clearly linked directly to ecosystem degradation: changes in

habitat or climate have a direct impact on rodent populations

and, therefore, eventually cause the emergence of viruses. Nature,

however, is not always so evident in terms of cause and effect.

As mentioned above, we can expect an extinction cascade to

result in the collapse of an ecosystem. As a collateral effect we

are also likely to see new species playing an important role in

the altered ecosystem, as well as the interaction of new species

(and/or habits), thereby opening the door to significant expansion

of infectious agents.

6.2 The Genetics of Adaptation to Novel Host

Viruses live in an always fluctuating world (figure 6.3).]] They

move from host to host, sometimes being air- or water-borne

but sometimes using vectors (e.g., insects) in which they may

or may not reproduce. Within an individual host, viruses face

multiple tissues and cell types that differ in physiological and

biochemical properties and are constantly being challenged by

a diversity of antiviral responses. Some viruses have evolved to

be specialized in infecting one or very few host species while

others are generalists that successfully infect different host species,

sometimes not even related taxonomically. Examples of specialists

are Coxsackieviruses, the Epstein-Barr virus, HCV, and the

measles and mumps viruses, whose only known mammalian host

are humans. Examples of generalist viruses are _Cucumber mosaic_

6.2. The Genetics of Adaptation to Novel Host

**155**

**a**

**b**

Figure 6.3. Viruses face a world always changing. The figure illustrates

the changing environments in which many viruses live. Viruses may move

between different hosts, in some instances using vectors into which they

may even replicate (as is the case for arboviruses, which use insects as

vectors, and the Hanta and Arena-viruses, which use rodents as vectors).

Within an infected host, in some instances viruses may show strong

tropisms and only replicate in a limited number of tissues and cell types,

whereas in other cases, viruses can replicate in different tissues and cell

types. Although the image only shows animals, a similar scheme can be

drawn for plant viruses.

_virus_, which infects more than 1,000 species including monocots

and dicots, herbaceous plants, shrubs, and trees, and IAV, which

infects birds and several different species of mammals. Likewise,

some viruses show a strict tissue tropism, infecting only a few cell

types, for example, HCV or _Herpes simplex virus_, while others are

very generalist and infect multiple tissues, e.g., IAV or EBOV.

By specializing in a single host (species or cells), viruses may

reduce competition at the cost of accessing a more limited set of

available resources (Futuyma and Moreno 1988). In contrast, a

generalist virus would be capable of exploiting multiple hosts,

thus enhancing its fitness. Since generalist viruses are not the

norm, it is generally assumed that generalism comes with a cost,

**156**

Chapter 6. Emergent Viruses

in keeping with the adage that _a Jack of all trades is a master of_

_none_ (Whitlock 1996). Classically, evolutionary biologists justify

the evolution of specialization in the existence of fitness trade-

offs that limit the fitness of generalists in any alternative hosts

(Whitlock 1996; Fry 1996) (figure 6.4a),]] that is, a generalist

will always be a worse competitor on each possible host than the

corresponding specialist. What are the causes of such trade-offs?

The most obvious mechanism is call antagonistic pleiotropy.

Antagonistic pleiotropy means that mutations that are bene-

ficial in one host may be deleterious in an alternative one (Fry

1996): a mutation in a viral protein that allows interacting with

a given host protein may enhance fitness in the actual host, but if

the amino acid sequence and structure of the host protein differ

somehow among hosts, then the interaction may not work well

in alternative ones, and vice versa. A second mechanism that

promotes trade-offs is mutation accumulation, in which neutral

mutations accumulate by drift in genes that are useless in the

actual host but may be essential in a future new one (Kawecki

1994). Both mechanisms involve differences in fitness across

hosts; however, they are not equivalent phenomena: natural

selection is the only reason for antagonistic pleiotropy, as genetic

drift is for mutation accumulation.

6.2.1 Becoming Specialists

A number of evolution experiments with bacteriophages and

arboviruses have shown that whenever a virus is adapted to a

single novel host type (figure 6.4b),]] it becomes a specialist that

pays a fitness host in alternative hosts. VSV (Holland et al. 1991;

Novella et al. 1999; Remold et al. 2008; Turner and Elena 2000;

Presloid et al. 200)), _Eastern equine encephalitis virus_ (EEEV)

(Weaver et al. 1999; Cooper et al. 2001), _Sindbis virus_ (SINV)

(Greene et al. 2005), and _Venezuelan equine encephalitis virus_

(VEEV) (Coffey et al. 2008) have been evolved in and adapted

to different lineages of animal cells in _in vitro_ cultures.

6.2. The Genetics of Adaptation to Novel Host

**157**

**a**

S

S

G

itness

G

F

Host A

Host B

A

A

A

A

**b**

B

B

B

B

A

B

A

B

**c**

AA

BB

ABAB

ABAB

itnessF

AA

BB

A

B

Figure 6.4. Fitness trade-offs across hosts. (a) Expected fitness for spe-

cialist and generalist viruses if a trade-off exists. Although both specialist

genotypes perform well in their respective hosts, each one is poorly

adapted in the other host. In (b) the three classes of experiments are

indicated and in (c) is the outcome of three evolution experiments.

Viruses evolved in a single host ( _A A A_ or _B B B_) become specialists on their respective hosts; by contrast, a virus evolved in a fluctuating host

landscape ( _A B A B_) becomes a generalist and improves fitness in both

hosts at the same time.

**158**

Chapter 6. Emergent Viruses

A common result of all these studies is that viral populations

evolved on a single cell host type increased fitness in the new host

and paid the cost in any alternative host cell type, including the

ancestral one (figures 6.4b-c).]] Likewise, there are several studies

with plant viruses in which the same phenomenon has been

described. For example, Agudelo-Romero et al. (2008) evolved

independent lineages of TEV by serial passages in two different

hosts. While TEV lineages maintained in the original tobacco

host showed no increase in either viral load or virulence, lineages

evolved in the new host pepper showed increases in both traits.

However, these increases were specific to the pepper host, and

the pepper-adapted lineages did not show any replicative fitness

increment in the ancestral tobacco host.

6.2.2 Becoming Generalists

In a second set of studies, the effect of temporal host hetero-

geneity has been addressed experimentally (figure 6.4b).]] Despite

methodological differences and the use of different host types,

most of these studies came to a common observation: when the

viral population alternated in time between two host types,

natural selection improved fitness in each type to a similar extent

as when adaptation happened to each one individually. For

example, VSV populations became generalists without paying

fitness costs in any of the alternative hosts (Turner and Elena

2000). However, a significant cost was paid by these general-

ist viruses in the ancestral host cell type not included in the

fluctuation treatment. The same observation was made for EEEV

populations evolved in two alternating cell types (hamster and

mosquito): EEEV reached replicative fitness values on each cell

type similar to those reached by viral lineages evolved only on

single cell types (Weaver et al. 1999).

Therefore, all these results suggest that no fitness trade-off

exists when the host landscape fluctuates fast, since the replicative

fitness in both environmental extremes is maximized (figure 6.4),]]

6.2. The Genetics of Adaptation to Novel Host

**159**

potentially generating generalist viruses. However, the observa-

tion of a lack of fitness trade-off seems not to be ubiquitous.

For example, for some but not all SINV lineages alternatively

passaged in mosquito and hamster cells, the replicative fitnesses

on each alternative host were lower than those reached by SINV

lineages evolved on each host held constant (Greene et al. 2005).

This result is still compatible with the existence of a fitness

trade-off across hosts. The fact that not all SINV generalist

lineages showed the trade-off might be explained by some lineages

overcoming the trade-off by finding the right combination of

mutations whereas the lineages still showing the trade-off did not

find such combinations.

The above discussion concerns evolution in temporally fluc-

tuating hosts. Another highly relevant, and related, issue is

evolution in spatially fluctuating hosts. This is, for example,

an essential component of mammalian viruses that may use

the bloodstream as a highway to spread across different tissues.

Yet the question is then, how does spatial heterogeneity affect

viral evolutionary dynamics? Cuevas et al. (2006) addressed this

question experimentally using VSV. They found that the extent

to which VSV adapts to diverse host cell types strongly depends

on the migration rate among cell types: increasing migration

rate selects for generalist viruses (figure 6.4).]] By contrast, in the absence of migration, VSV lineages specialized in their local host

cell type (figure 6.5).]]

This result supports the view that migration among hosts

must be sufficiently low relative to the strength of selection to

generate specialists. Indeed, the conditions for the coexistence

of specialist viruses in a heterogeneous host environment are

very restrictive. If the selective differences among hosts are not

so large, then the balance of production from each host must

be roughly equal in order to maintain diversity. This implies

that there must be lots of opportunities for generalists to evolve

in heterogeneous environments, even if selection favors in the

**160**

Chapter 6. Emergent Viruses

S

G

y

G

S

equenc

G

S

e fr

G

S

Relativ

G

S

Migration rate

Figure 6.5. Effect of migration rate among different hosts in the fraction

of generalist viruses that can be maintained in the population. Migration

rate increases from left to right. Increasing migration rate among different

cell types favors generalist genotypes ( _G_), whereas a reduced migration

rate would favor viral genotypes specialized on each host ( _S_). In the

absence of migration, specialist viruses (dark bars) dominate the

population. Frequency of generalist viruses (white bars) increases with

migration rate.

short term specialization to the host wherein virus productivity

is maximized.

Despite their conceptual interest, these studies suffer from

the limitation of being undertaken in a highly artificial cell

culture system. This limitation has been overcome in recent

years by running evolution experiments in whole hosts, which

represents a more biologically realistic situation. For example,

Coffey et al. (2008) evolved independent lineages of VEEV either

in _Aedes aegypti_ mosquitoes or rodents, or alternating between

both animals. As expected by the trade-off hypothesis, serial

_in vivo_ mosquito passages resulted in enhancement of mos-

quito infectivity but at the cost of reduced replication ability

in rodents. Consistently, VEEV populations serially passaged in

rodents showed an increased replication rate in the vertebrate host

but reduced infectivity in mosquitoes. Interestingly, alternating

6.2. The Genetics of Adaptation to Novel Host

**161**

_in vivo_ passages between mosquitos and rodents did not increase

VEEV fitness in either host.

More recently, evolution experiments done with TEV, in

which pepper and tobacco hosts were alternated through time,

showed a similar pattern of evolution: viruses evolved in both

alternating hosts were as fit on each host as the corresponding

specialists (Bedhomme et al. 2012). When only one host was



**162**

Chapter 6. Emergent Viruses

A second very remarkable example of antagonistic pleiotropy

driving virus specialization to a novel host comes from the

plant virus _Pelargonium flower break virus_ (PFBV) populations

adapted to the experimental host _Chenopodium quinoa_ (Rico

et al. 2006). PFBV isolates maintained for a long time on

_C. quinoa_ all fixed five specific amino acid substitutions in the

coat protein, which were never found in natural isolates from the

natural host geranium. When a wild-type isolate from geranium

was mechanically inoculated onto _C. quinoa_ leaves, the viral

population generated right after the first passage had already

fixed two of the _C. quinoa_-specific changes, and after only four

additional serial passages the entire _C. quinoa_-specific pattern was

fixed in all lineages (Rico et al. 2006). The fact that this pattern

has never been found in the natural host, not even incompletely,

suggests that it may impose a strong burden for viral replicative

fitness on the natural host geranium.

6.3 Epidemics of Emergence

In previous sections we have explored the tempo and mode of

emergence of new viruses and the role played by several factors.

Different examples have been provided and the adaptation strate-

gies analyzed. Most of these examples and adaptation scenarios

describe host-virus interactions that can be understood in terms

of the trade-offs and opportunities provided by novel hosts. But

there is a global picture that we have not yet addressed concerning

the global scale of the phenomenon, namely the population

dynamics of emergence. Modeling the rise of new pathogens is a

difficult task, since both ecological and evolutionary components

are at work, linking the life histories of different species as well

as novel forms of interactions. However, a number of general

theoretical results can be derived by analysing the conditions

under which a virus can successfully expand within a population

of susceptible individuals. Such results can help us derive some

6.3. Epidemics of Emergence

**163**

key relationships between the efficiency of the viral strain (as given

by _R_ 0) and the size of the outbreak, thus providing a clue to the

requirements for a pandemic to emerge.

In order to predict the size of an epidemic outbreak and

how it can depend upon the initial size of the infection, an SIR

model will be used. The SIR model (Kermack and McKendrick

1927) involves three distinct subsets, namely _S_ = susceptible,

_I_ = infected, and _R_ = recovered. It is somewhat related to the

SIS model described in the previous chapter, but the additional

compartment makes a difference: instead of returning to the

susceptible state, infected individuals overcome the infection but

cannot return to the initial, infected compartment. In this case,

the reactions defining the SIR model are

_r_

_I_ + _S_ −→ 2 _S_

(6.1)

for the infection event and

_α_

_I_ −→ _R_

(6.2)

for the transition for the recovery process. A constant population

_S_ + _I_ + _R_ = _N_ will also be assumed.

The associated differential equations are now:

_d S_ = − _r IS_

(6.3)

_d t_

_d I_ = _r IS_ − _αI_

(6.4)

_d t_

_d R_ = _αI._

(6.5)

_d t_

This model allows us to make some important predictions

concerning the final size of an outbreak of an infectious disease

and connect two important parameters: the initial size of the event,

_I_ 0 (the number of primary cases), and the basic reproductive

number, _R_ 0.

**164**

Chapter 6. Emergent Viruses

In order to obtain these results, a number of (reasonable)

assumptions will be needed. The first is that the initial state (when

_t_ = 0) is given by _S_ 0 = _N_ − _I_ 0 (and a reasonable approximation is thus _S_ 0 ≈ _N_, while _I_ 0 _>_ 0 and _R_(0) = 0). A first result can be obtained by considering the conditions that allow the epidemic

event to start propagating. This requires

_d I_

= _I_

_d t_

0( _r S_ 0 − _α_) _>_ 0 _,_

(6.6)

_t_=0

and this leads to the condition _r S_ 0 _/α >_ 1 or, since _S_ 0 ≈ _N_, to a basic reproductive number

_R_ 0 = _r N >_

_α_

1 _,_

(6.7)

which sets our definition for this parameter.

Our goal here is to know how many people get infected

through the outbreak, which means counting the final (steady)

number of recovered individuals, to be indicated as _R_∞. Using

the relation

_d S_

_d S_

= _dt_

(6.8)

_d R_

_d R_

_d t_

it is easy to see that this leads to

_d S_ = − _R_ 0 _S._

(6.9)

_d R_

_N_

This can be integrated to give an exponential decay

_S_( _t_) = _S_ 0 exp − _R_ 0 _R ._

(6.10)

_N_

If we include this in the equation for _d R/dt_ we have now:

_d R_ = _α_ ( _N_ − _S_ − _R_)

(6.11)

_d t_

= _α N_ − ( _N_ − _I_ 0) exp − _R_ 0 _R_ − _R ._

(6.12)

_N_

6.3. Epidemics of Emergence

**165**

10,000

_I_ = 103

0

1,000

_I_ final

_I_ = 102

0

100

_I_ = 10

0

10

Final epidemic size,

Epidemic outbreak

_I_ = 1

0

1

0.0

0.5

1.0

1.5

2.0

_R_ 0

Figure 6.6. Impact of the basic reproductive number _R_ 0 on the popu-

lation dynamics of pathogen emergence. (a) Relationship between final

epidemic size (log scale) and _R_ 0 for a total population _N_ = 10 _,_ 000, for different initial infection size _I_ 0.

The outbreak will end once the condition _d R/dt_ = 0 is

achieved, which gives our final result for the final value for _R_∞:

_R_∞ = _N_ − ( _N_ − _I_ 0) exp − _R_ 0 _R_∞ _._

(6.13)

_N_

The previous equation gives us an implicit relation that

measures the impact of the pathogen efficiency (as measured

by _R_ 0) on the population dynamics of viral emergence (Wool-

house et al. 2001) and its dependence on _I_ 0. The curves displayed

in figure 6.6]] illustrate the role played by the initial infection

combined with the potential for transmission. For values of _R_ 0

below the critical _R_ 0 = 1 we can see that small initial infections

barely propagate through the total population, and infections are

directly acquired from the primary cases.

Instead, for _R_ 0 _>_ 1 this limited spread will be replaced by

a major epidemic (gray area), and most infection events are a

consequence of propagation from new infected hosts. Examples

**166**

Chapter 6. Emergent Viruses

A A

g g

A ricultural

gricultur

riculturalal

Ind

n . wildlif

d.

d wildli e

f

. wildlif

management

management

management

Human dw

Human d ellings

we

Human dw llings

ellings

Wildlif

Wi

W ldli e management

fe

ildlif management

e management Ind

n . ag

d.

nd a ricultural

gr

. ag icultural

ricultural

Ve

V t

e e

t rinarian r

er

e inarian esear

re

rinarian r sea cher

rc

esear her

cher

Ve

V c

e torborne

to

t rborne

orborne

Ind

n . human dw

d.

d human d ellings

we

. human dw llings

ellings

Ind

n .

d ec

. e ot

co

ec ourism

to

ot urism

ourism

Ind

n .

d c

. . o

c

c ntaminat

on

o tamina ed f

te

ntaminat d ood

fo

ed f od

ood

Ec

E ot

co

Ec ourism

to

ot urism

ourism

Pe

P t

e

Pe

Zoo sanc

Zo

Z o sanc

oo sanctuar

tuar

tuary

Hunt

Hun ed

te

Hunt d

ed

Tr

T ade

ra

r de

ade

Lab pathogen

Consumed

Co

C nsumed

onsumed

Ind. waterborne

Laboratory

Ind. trade

Ind. laboratory

Ind. markets

Market

Figure 6.7. A bipartite graph linking emergent viruses transmitted from

wildlife to humans and different classes of high-risk interfaces. The latter

are displayed as circles with varying size and labeled. Viruses capable

of exploiting diverse interfaces appear more connected. After Kreuder

Johnson et al. (2015).

of the first category are avian influenza or monkeypox, whereas

the second include HIV-1, IAV, and the SARS coronavirus

(Woolhouse et al. 2005). As we already discussed in the previous

chapter, this is a critical change that has an important implication:

any given pathogen slightly below _R_ 0 = 1 can become an emer-

gent one by acquiring a small advantage that allows it to cross the

critical boundary.

The challenge of predicting, preventing, and fighting emergent

diseases, particularly those of viral origin, is enormous. Under-

standing emergent viruses requires an integration of ecological,

epidemiological, social, cultural, and engineering components.

Multiple interfaces between humans and pathogens exist that

can facilitate the emergence of viral novelties. In figure 6.7]] a

network has been constructed linking known zoonotic viruses

6.3. Epidemics of Emergence

**167**

(circles with no labels) and potential high-risk interfaces of disease

transmission (Kreuder Johnson et al. 2015). This graph displays

high-risk interfaces whose size is proportional to the number of

viruses reported for each transmission interface, including direct

and indirect contact as well as transmission by vector (large

node on the left). Virus node size (here 86 viruses were studied)

reflects the number of connections to different transmission inter-

faces. Larger numbers of connections indicate a higher ecological

plasticity of viruses through use of multiple opportunities for

transmission.

As discussed in Kreuder Johnson et al. (2015), more dedicated

research of the epidemiology of zoonoses at high-risk human-

animal interfaces is needed to assess risk of viral disease emergence

and direct global, as well as local, disease prevention and control.

Ongoing studies indicate that the risk for new virus emergence

is higher at those interfaces that facilitated disease threats in the

past. Unfortunately, wild animal hosts and high-risk interfaces

facilitating spillover of zoonotic viruses, particularly beyond their

first emergence, remain vastly underreported. In this area, mathe-

matical and computational models could play a key role.

      

# Document Outline

- Cover]]
- Title]]
- Copyright]]
- CONTENTS]]
- Preface]]
- 1. The Virosphere]]
    - 1.1 Deep Microspace Field]]
    - 1.2 The Expanding Viral Universe]]
    - 1.3 Structural and Genetic Diversity]]
    - 1.4 Viral Planet]]
- 2. Alive or Dead?]]
    - 2.1 Computation and Life]]
    - 2.2 Viruses as Replicating Machines]]
    - 2.3 Viruses as Phases of Matter]]
    - 2.4 Evolving Genome Reduction]]
    - 2.5 The Space of Replicators]]
    - 2.6 Adaptation at High Mutation Rates]]
    - 2.7 Viral Quasispecies]]
    - 2.8 Critical Genome Size]]
- 3. Landscapes]]
    - 3.1 Climbing High]]
    - 3.2 Symmetric Competition]]
    - 3.3 Epistasis in RNA Viruses]]
    - 3.4 Experimental Virus Landscapes]]
    - 3.5 The Survival of the Flattest Effect]]
    - 3.6 Virus Robustness]]
        - 3.6.1 Intrinsic Mechanisms of Mutational Robustness]]
        - 3.6.2 Extrinsic Mechanisms of Mutational Robustness]]
    - 3.7 Selection: Fitness versus Robustness]]
- 4. Virus Dynamics and Arms Races]]
    - 4.1 Virus-Host Interactions]]
    - 4.2 HIV Multiscale Dynamics]]
    - 4.3 Population Dynamics of HIV Infection]]
    - 4.4 Spatial Dynamics of HIV-1]]
    - 4.5 Antigenic Diversity Thresholds and AIDS]]
    - 4.6 Viral Symbiosis]]
- 5. Epidemics]]
    - 5.1 Outbreak]]
    - 5.2 SIS Model]]
    - 5.3 SIS Model in Space and Graphs]]
    - 5.4 AIDS: Modeling HIV-1 Transmission]]
    - 5.5 Halting Viruses in Scale-Free Networks]]
- 6. Emergent Viruses]]
    - 6.1 Ecological Disturbance: Hanta- and Arenaviruses as Case Studies]]
    - 6.2 The Genetics of Adaptation to Novel Host]]
        - 6.2.1 Becoming Specialists]]
        - 6.2.2 Becoming Generalists]]
        - 6.2.3 The Causes of Specialization]]
    - 6.3 Epidemics of Emergence]]
- 7. Origins]]
    - 7.1 Are Viruses Inevitable?]]
    - 7.2 Evidence from Digital Evolution]]
    - 7.3 Where Do Viruses Come From?]]
        - 7.3.1 Regressive Hypothesis]]
        - 7.3.2 Cellular Origin Hypothesis]]
        - 7.3.3 Protobiont Hypothesis]]
    - 7.4 Viruses and the Origin of Cells]]
    - 7.5 Viruses as Sources of Evolutionary Novelties]]
    - 7.6 But . . . What Is a Virus Then?]]
- 8. Computer Viruses and Beyond]]
    - 8.1 Viruses as Programs]]
    - 8.2 Emergence of Computer Viruses]]
    - 8.3 Cancer, Languages, and Minds]]
- References]]
- Index]]**170**

Chapter 7. Origins

2016). Lastly, but not less interestingly, parasites have even been

implicated in the origins of sex, as they may have been driving

selection of mechanisms to generate new genetic variation that

may help hosts escape from recognition by their parasites (Lively

2010).

7.2 Evidence from Digital Evolution

In previous chapters we have studied a number of theoretical

and computational approaches to the modeling of virus dynamics

and how viruses coevolve with their potential hosts. In all these

models, both viruses (parasites) and their hosts are already present

from the beginning. However, we should consider these models

under a more general framework in which parasites can emerge.

One of the relevant questions that can be formulated here is

whether virus-like agents can emerge in other contexts different

from biology. One example that we will explore in chapter 8]] is

computer viruses. They can be seen as a negative effect of the

rise and expansion of computers since the personal computer

revolution that started at the end of the 1970s. Although—as

discussed in chapter 2—the]] IT revolution started in the 1950s, a

crucial component of the information infrastructures that had to

be in place for the emergence of computer bugs was the presence

of the right information-storing systems (Augarten 1984; Gleick

2011; Dyson 2012) and, more importantly, a network that

connects computers. As also happens in an epidemic spreading

scenario (see chapter 5),]] infection will not take place unless

individuals interact, making effective spreading of the pathogen

possible.1

1In this context, it has been claimed that the telegraph was the _Victorian_

_Internet_, which shared many surprising commonalities with the modern world

wide web. However, a major difference between the two was the lack of

information storage in the old version, preventing the Victorian web from the

development of viruses but also from becoming a true information network.

7.2. Evidence from Digital Evolution

**171**

Some insight into the origins of viruses can be obtained, once

again, from the analysis of evolving artificial life systems. Some

early attempts at creating digital organisms were undertaken by

Niles Barricelli, a Norwegian-Italian researcher formerly trained

in genetics of viruses and with some background in physics, who

was invited by John von Neumann to work at the Institute for

Advanced Studies. ENIAC, the largest computer at the time,

provided an unexpected arena for making the first steps toward

artificial life (Barricelli 1962, 1963). In a surprisingly visionary

way, Barricelli aimed at exploring evolution by supplying a virtual

world of bits where the first digital creatures emerged from

a simulation. Barricelli’s programs were confined to the low-

memory domains of ENIAC, but even with such limitations

he was able to prove how complex interactions and innovations

could result from a virtual evolution experiment. The simulations

involved a one-dimensional world not too different from the

cellular automata models invented a few years before (in 1940)

by Stanislaw Ulam and von Neumann. The universe was limited

to a line of 512 “genes” that could adopt a range of integer values.

By defining a simple set of rules for mutation and reproduction,

new numbers would be generated, and the process was repeated

again and again. Among Barricelli’s findings was the emergence

of simple codes acting as parasitic entities that sometimes spread

exponentially and eventually filled all the available memory space,

which was followed by a subsequent extinction of the entire

ecosystem.2

The idea of evolving virtual creatures in the computer and its

potential implications lay dormant for decades until the 1990s,

when ecologist Tom Ray found that—among other things—

parasitic programs were an inevitable outcome of digital ecologies

2Actually, it is interesting to notice that, in order to prevent parasites

(especially the smaller ones) from spreading and overloading the system,

Barricelli made up some additional ad hoc rules to limit the spontaneous

emergence and spread of viral-like entities (Dyson, 2012).

**172**

Chapter 7. Origins

(Ray 1992, 1994; Adami 1998). Driven by the question of

how diverse ecosystems emerge and persist, he designed a digital

model of evolving species based on a set of computer programs

competing for the computer memory and displaying mistakes

while copying themselves (Ray 1992) to be stored in available

memory positions. Under the constraints imposed by finite

computer resources, the so-called Tierra model was able to show

how some evolutionary innovations can spontaneously develop.

In particular, some major transitions took place as soon as

programs started to compete.

An early event was a genome reduction innovation, related to

the fact that shorter programs can replicate faster than larger ones.

This occurs when parts of the coded program can be removed

with no consequences. In that respect, redundant pieces of code

could be deleted with no harm. Later on, shorter programs

emerged, unable to replicate themselves. In other words, parasites

came to (digital) life. Hyperparasites, that is, programs able to

replicate using pieces of code carried out by parasites, came later,

and some programs developed the capacity for exchanging parts

of their codes, mainly as a response to escape from parasites

(Hamilton et al. 1990; Hillis 1990), thus defining an innovation

that we can label as a primitive version of sex (Ray 1991, 1994,

1998). Eventually, groups of slow replicating programs were able

to replicate faster through cooperation.

Since these early efforts, many other studies have been devoted

to the study of the evolution of artificial host-parasite systems.

Most of these models assume the presence of a distinction

between the two classes of agents, but not so many have explored

the emergence of parasites. One elegant illustration of a model

aiming at explaining the emergence of viral entities is provided

by the work of Paulien Hogeweg and co-workers (Takeuchi and

Hogeweg 2008; Colizzi and Hogeweg 2016).

One especially simple example is where agents evolve coopera-

tion in a two-dimensional lattice (Colizzi and Hogeweg 2016).

7.2. Evidence from Digital Evolution

**173**

The model introduces the use of public goods produced by

agents, which on one hand share the public good and use it for

reproduction, and on the other compete for existing available

sites. Reproduction takes place with mutation and the result

of this process is the speciation of a cooperative and a selfish

lineage.

Specifically, these authors use an _L_ × _L_ square lattice =

{ _r_ = ( _i, j_)|1 ≤ _i, j_ ≤ _L_}, where each site _f_ ∈ can be occupied by an individual— _S_( _r_ ) = 1—or empty— _S_( _r_ ) = 0. Each individual produces a good with rate _φ_( _r_ ) per time step, which

is shared with all _q_ neighbors in a neighborhood ( _r_ ). The

reproduction probability of each occupied site—provided that

an empty site is present within the neighborhood—defines the

fitness _f_ ( _r_ ) of the individual. The benefit _B_( _r_ ) is given by the availability of the public good, i.e.,

_φ_( _r_ )

_B_( _r_ ) = _b_

+ 1

_φ_( _u_) _,_

(7.1)

_q_ + 1

_q_ + 1 _u_∈ ( _r_)

where _b_ is the benefit per unit of the public good and _q_ = 8

nearest neighbors were used in the original study. There is a cost

_ρ_( _r_ ) for each site producing the public good, which is taken as

proportional to production, i.e., _ρ_( _r_ ) = _c φ_( _r_ ). The fitness _f_ ( _r_ ) associated to a given (occupied) site will be the difference between

cost and benefit, i.e.,

_f_ ( _r_ ) = ( _B_( _r_ ) − _C_ ( _r_ )) _,_

(7.2)

where ( _z_) = _z_ for _z >_ 0 and zero otherwise. The total fitness of a set of _m_ neighboring individuals competing for a given empty

site will be

_F_ = _f_ ( _r_ ) +

_f_ ( _k_) _,_

(7.3)

_k_

**174**

Chapter 7. Origins

and a given site with _S_( _r_ ) = 1 will occupy the adjacent empty site

with a probability (of replication)

_R_( _r_ ) = _f_ ( _r_ ) 1 − _e_ − _F ._

(7.4)

_F_

Here the term in parentheses provides the probability that

at least one site replicates. This is consistent with the intuition

that replication is more likely to occur near sites with higher

availability of public goods.

The model is completed by specific rules introducing muta-

tion: each time a replication occurs from a site _r_ ∈ , the new

site _k_ ∈ ( _r_ ) will have a different _φ_( _k_) value. This happens with a probability _μ_, and the new value will be _φ_( _k_) = _P_ ( _r_ ) + _ξ_ , with _ξ_

a random number within the interval [− _δ/_ 2 _, δ/_ 2]. The model is

completed with movement and death rules: individuals can ran-

domly move to nearest positions and also die with probabilities

_kmov_ and _kd_ , respectively.

The generic result of this model and its variants is that there

is always an evolutionary bifurcation (figure 7.1a)]] between the

two classes of replicators. The upper and lower branches are

associated with cooperators producing large amounts of public

goods and parasites exploiting cooperators (and thus showing

low production levels), respectively. The gray scale provides an

estimate of the population size. The spatial dynamics of this

system is exemplified in the sequence of snapshots (figure 7.1b-g)]]

where complex spatial structures arise as the two populations

coevolve, with cooperators forming coherent waves followed

by parasites (dark borders surrounding the waves) that will

exploit the public good. These parasites appear aggregated on

the edge of cooperating clusters, whose stability is undermined

by the cost of cooperation. Despite the cost of maintaining

cooperation, this model shows that cooperators and parasites both

emerge, with the latter favoring the increase in cooperation of the

former.

![[index-190_1.png]]

7.2. Evidence from Digital Evolution

**175**

**a**

b

cd

e

f

g

10

_Μ_

+

8

6

_ρ_

4

2

–

0

0

20,000

40,000

60,000

80,000

100,000

Time

**b**

**c**

**d**

_ρ_

+

–

**e**

**f**

**g**

Figure 7.1. Evolution of replicators and viruses in a model of public

good production (adapted from Colizzi and Hogeweg (2016)). Here

populations evolve on a two-dimensional lattice where they share a public

good and compete for available empty sites. Individuals produce a public

good at a rate _p_ that spreads evenly over the local neighbors, conferring

a benefit on all sites affected. A price is also paid by individuals for the

production of the public good. Along with mutation and some stochastic

effects, both cooperators and parasites evolve with a characteristic bi-

furcation (a). In (b-g) several snapshots of the system (indicated above)

are displayed, showing how cooperator fronts spread while followed by

a front of parasites. Here _b_ = 10 _, μ_ = 0 _._ 05 _, δ_ = 0 _._ 1 _, kmov_ = 0 _._ 02, and _kd_ = 0 _._ 2.



**176**

Chapter 7. Origins

This is a highly simplified model, but provides a powerful

illustration of the role played by the interplay between mutation

and local dispersal, which is considered a crucial component in

the evolution of early cells and viruses (Koonin et al. 2006).

7.3 Where Do Viruses Come From?

Viruses are found infecting all forms of life and have probably

been around since the first cells arose, or perhaps even before

them. Tracing back the origin of viruses is a titanic, almost

impossible, endeavor because they do not form fossils, and the

only sources of information are molecular phylogenies and com-

parative techniques that have been extensively used to compare

the DNA or RNA genomes of today’s viruses, and reconstruct

backwards their evolutionary history, hopefully, to reach their

origins. It has been often stated that viruses are polyphyletic,

i.e., that different viral lineages originated independently and

thus they have no single origin. In particular, RNA and DNA

viruses were thought to be evolutionarily unrelated. However, the

overall structural similarity between the viral proteins forming the

envelopes and capsids suggests at least a common mechanism for

their appearance (Abrescia et al. 2012; Krupovic and Bamford

2010). Three main hypotheses have been brought forward to

explain the origins of viruses (Forterre 2006a; Forterre and

Prangishvili, 2009).

7.3.1 Regressive Hypothesis

This is also called the degeneracy hypothesis, or the reduction

hypothesis. The regressive hypothesis suggests that viruses may

have once been small cells that parasitized larger cells. As time

went on and the parasite became more dependent on the host

cell to complete its life cycle, genes not strictly necessary for their

acquired parasitism were lost. This hypothesis is grounded on

the observation that bacteria such as _Rickettsia_, _Chlamydia_, and

**178**

Chapter 7. Origins

situation can be seen from the opposite perspective and consider

the retrotransposons as retroviruses inserted long ago that have

lost some of its functions, notably the ability to encapsidate and

transmit among cells.

The cellular origin hypothesis has several drawbacks as well.

(i) It does not specify how a free nucleic acid could have

recruited a capsid and the complex mechanisms required to

deliver its content inside a host cell. In this context, it is

worth noting that viral capsids do not share any structural

or sequence resemblance with cellular components. (ii) The

hypothesis predicts that viruses infecting the three domains of

cellular life would have originated within each domain, that is,

bacteriophages would have originated from bacterial genomes

whereas the origin of eukaryotic viruses would be the genome of

a eukaryotic cell. Therefore, one may expect to find similarities

between viral proteins encoded by viruses from one domain

and their cellular homologues in that domain, but homologies

between viruses from different domains cannot be expected.

Reality has been perverse with this hypothesis: the similarities

between viral genes from different domains are larger than they

are among viral genes and their corresponding host cell genes.

Of course, in a few cases, viral proteins resemble homologous

proteins encoded by their hosts, indicating a recent transfer of

these proteins from cells to viruses. From this observation, it has

been argued by defendants of the escape hypothesis that all viral

proteins must have a cellular origin, and their “ancestrality” is just

an artifact generated by phylogenetic methods due to the fast rates

of evolution shown by viral genomes. However, obviously, this

explanation fails to account for the vast majority of viral proteins

without cellular homologues.

7.3.3 Protobiont Hypothesis

This is also called the virus-first hypothesis and suggests that

viruses may have evolved from complex molecules of protein

7.3. Where Do Viruses Come From?

**179**

+sRNA

metazoans

dsRNA

bacteria

–sRNA

plants

retroid RNA

fungi

retroid DNA

Archea

ssDNA

dsDNA

Unicellular Euk

Figure 7.2. Viruses and their host niches. Here we display a bipartite

graph including the different classes of viral genomes (left) and their

potential host niches (right). The lines indicate known interactions and

their thickness provides a relative measure of strength, with thin and

thick links corresponding to rare and common virus-host interactions

respectively. Based on Koonin et al. (2006).

and ribonucleic acids at the same time as cells first appeared

on earth, and would have been dependent on cellular life from

the very beginning. In the primitive precellular soup, as in any

other replicating system, parasites would had also evolved that

grew at the expenses of other more complex molecular systems.

When cellular membranes first arose and complex replicative

**180**

Chapter 7. Origins

hypercycles isolated themselves from the environment by acquir-

ing membranes, these innovations pushed molecular parasites

into strong selection to acquire the ability to cross the primitive

membranes. In this context, mathematical and computer models

support the idea that complex spatial structures (not necessarily

vesicles) can make a big difference (as discussed above).

This hypothesis was dismissed for a long time since all present-

day viruses are obligatory parasites requiring an intracellular

development stage for their reproduction. This “ancient virus

world” hypothesis implies that the primordial origin of diverse

viral replication-expression strategies coevolved with the increase

in complexity of their corresponding hosts. Positive-sense RNA

viruses are thought to be the most ancient type and evolved within

the primordial soup, along with the primitive RNA-based cells.

The dsRNA and negative-sense ssRNA viruses, which carry their

replication machinery within virions, are then most likely to have

evolved later on, derived from the positive-sense ssRNA viruses.

Indeed, negative-sense ssRNA viruses probably originated during

the radiation of primitive arthropods (Li et al. 2015), with a

later jump to the plants on which these arthropods feed. Under

this vision, positive-sense ssRNA viruses are indeed the direct

descendants of the primordial RNA-protein world, whereas the

reverse-transcribing viruses provide a possible intermediate for the

transition to the DNA world.

Therefore, the central debating point in the discussion about

the origin of viruses is whether they are ancient, first appearing

before the last universal cellular ancestor (LUCA), or have evolved

more recently, such that their ancestry lies with genes that escaped

from the genomes of their cellular host organisms. Studies of

viral origins have been bolstered in the last two decades by two

remarkable observations: the discovery and genome sequencing

of giant viruses and the report of apparent homology between the

capsid architectures of viruses that possess no primary sequence

similarity. As Patrick Forterre (2006b) has pointed out, we cannot

![[index-196_1.png]]

7.3. Where Do Viruses Come From?

**181**

?

Bacterial

Archaeal

viruses

viruses

Bacteria

Archaea

Ancient virosphere

Modern

LUCA

virosphere

Ancestors of

modern viruses

Ancestors of

modern viruses

Modern

virosphere

Eukaryotic

viruses

Eukarya

Figure 7.3. Redefining viruses. Here we represent the three domains of

life (that have evolved from a LUCA) along with viruses with their

capsids. Newly defined viruses have a capsid but no ribosome (modified

from Raoult and Forterre (2008)).

pretend to understand the origin of viruses from the perspective

of the modern biosphere (i.e., modern viruses infect modern

cells; modern cells cannot regress to viral forms; free DNA

cannot recruit proteins for encapsidation; etc). Therefore, the

three hypotheses must be revisited by considering that viruses

originated before LUCA.

The idea of RNA viruses, and even more clearly of viroids,3 be-

ing ancient was easily accepted in the context of the RNA World

theory (Gilbert 1986). It has been convincingly argued by several

authors than RNA viruses and viroids could be relics of a pre-

DNA world in which organisms, even primitive cells, had RNA as

the only carrier of genetic information, and proteins as machines

3Subviral pathogens of plants composed only by a really small noncoding

circular molecule of RNA (Flores et al. 2014).

**182**

Chapter 7. Origins

to ensure the transmission of this information. Retroviruses

would be relics of the RNA-to-DNA world transition. A priori,

the idea that RNA viruses preceded cells in the history of life

may sound weird since they are most commonly found infecting

eukaryotic cells, although both ssRNA and dsRNA viruses are

found infecting bacteria. More interestingly, bacteria-infecting

and eukaryote-infecting dsRNA viruses share strong structural

similarities and life cycles, thus supporting a common origin

before the separation of both cellular domains.

The pre-cellular origin of DNA viruses was also postulated by

Forterre (2006a, 2006b) on the basis of the sequence similarity (or

lack there) between bacteriophage T4 type II DNA topoisomerase

and bacterial girase and eukaryotic type II DNA topoisomerase.

Likewise, human Adenovirus and _Bacillus subtillis_ bacteriophage

_φ_ 29 use a similar atypical protein-priming mechanism to replicate

their DNA (nonexisting in the cellular world) and encode for a

unique type of DNA polymerase that can use such a template to

initiate its own replication. These proteins were clearly of neither

bacterial nor eukaryotic origin but representative of a new domain

that existed before the separation of the three cellular domains.

Viroids are molecules of RNA that are not classified as viruses

because they lack a protein coat. However, they have charac-

teristics that are common to several viruses and are often called

subviral agents. Other subviral agents are the RNA satellites,

hyperparasites that parasitize an RNA virus (Palukaitis 2016).

Although RNA satellites are more common among plant RNA

viruses than among animal RNA viruses, a particularly well-

known case of such satellites is the _Hepatitis delta virus_ of

humans, which has an RNA genome similar to viroids but has

a protein coat derived from its helper virus, HBV, and cannot

produce one of its own (Littlejohn et al. 2016). It is, therefore, a

defective virus and cannot replicate without the help of HBV. A

particularly interesting example of DNA satellites is the virophage

that infects giant mimiviruses (Zhou et al. 2013) that are parasites

7.3. Where Do Viruses Come From?

**183**

of amoebae; its prototype is the Sputnik virophage that parasitizes

the giant _Acanthamoeba polyphaga_ mimivirus (La Scola et al.

2008) (already presented in chapter 2).]] Sputnik has a ca. 18 kb

circular dsDNA genome, like a huge plasmid, and, amazingly, it

encodes for proteins with homology to the three cellular domains

as well as proteins homologous to ATPases from bacteriophages

and eukaryotic viruses. Satellites may represent evolutionary

intermediates between viroids and viruses or, more likely, other

remnants of the RNA world.

The paradigm that viruses have small genomes and are rela-

tively simple in comparison to cellular life has been overturned

with the discovery of giant viruses (already presented in

chapter 2),]] larger than some of the smallest bacteria (e.g., _My-_

_coplasma genitalium_). Over a decade ago, Raoult et al. (2004)

characterized the 1.8 Gb genome of the first mimivirus. This

genome contained more than 900 putative genes, some resem-

bling nonviral genes involved in translation and protein produc-

tion. Two contending hypotheses have been brought forward

to explain the origin of these genes. Firstly, they could have

been acquired from their cellular hosts. Second, mimiviruses may

have descended from a free-living cell that gradually lost most

of its genes as it became a parasite (according to the cellular

origin hypothesis). This mimivirus precursor may represent a new

branch of the tree of life, one predating the emergence of the three

major branches (bacteria, archaea, and eukaryotes).

Since the discovery of the first mimivirus, the brotherhood

of giant viruses has been enlarged with members having larger

and larger genomes, the largest one described so far being the

giantic pandoraviruses (named so because of their amphora

shape and the surprises they contain) (figure 7.4)]] (Philippe

et al. 2013). They have strikingly different genes and physical

appearances from other viruses. After being discovered in the

late nineteenth century, viruses were quickly demoted to inert

particles, too simple to be living beings: no more than a protein

![[index-199_1.png]]

**184**

Chapter 7. Origins

Mimiviridae

Pandoraviridae

osisyt

Phagoc

Unloading

yrotca fnoirVi

Figure 7.4. Electron microphotographs comparing mimivirus and

pandoravirus mechanisms of cell entry, uncoating (and shape), and

formation of cellular factories. Both classes of giant viruses largely differ

in these steps and structures.

package enclosing a tiny genetic material without any metabolic

capability. The giant viruses have destroyed this naive perspective

of the viral world. Giant viruses thus can be viewed as an

intermediate form between a true cell and a virus. Indeed, the

mimivirus genome encodes several proteins that are also present

in the three domains of life, and a phylogenetic tree places

the mimivirus proteome in between Archaea and Eukarya, as

expected for a representative of a fourth domain with no longer

existing free-living representatives. In the following sections we



7.4. Viruses and the Origin of Cells

**185**

will discuss some of the evolutionary implications of these new

giant viruses on the evolution of the eukaryotic cell.

As already mentioned, there are problems with all the hypothe-

ses for the origin of viruses: the regressive hypothesis did not

explain why even the smallest of cellular parasites do not resemble

viruses in any way. The escape hypothesis did not explain the

complex capsids and other structures on virus particles. The virus-

first hypothesis contravened the definition of viruses in that they

require host cells. Nonetheless, viruses are now recognized as

ancient and as having origins that predate the divergence of life

into the three domains. This discovery has led modern virologists

to reconsider and reevaluate these three classical hypotheses.

The evidence of an ancestral world of RNA cells and computer

analysis of viral and host DNA sequences are giving a better

understanding of the evolutionary relationships between different

viruses, and may help identify the ancestors of modern viruses. To

date, such analyses have not proved which of these hypotheses is

correct (Koonin et al. 2006; Koonin and Dolja 2013). However,

it seems unlikely that all currently known viruses have a common

ancestor, and viruses have probably arisen numerous times in the

very remote past by one or more mechanisms.

7.4 Viruses and the Origin of Cells

An obvious question emerging from the RNA world hypothesis

is about where DNA comes from. Forterre (2002) proposed that

DNA was a viral invention to gain resistance against the RNA-

specific defense mechanisms that at that time may have evolved in

the RNA host cells. By incorporating this chemical modification

into their genetic code, the newly emerged DNA viruses had a

clear selective advantage. This is supported by the fact that most

modern DNA viruses encode for ribonucleotide reductases and

thymidylate synthases enzymatic activities required to produce

DNA precursors (Myllykallio et al. 2002). To explain how

**186**

Chapter 7. Origins

DNA replaced RNA chromosomes in the primitive cells, Forterre

argues that DNA viruses in persisting infections (non-lytic) lost

genes encoding their capsid proteins and lytic functions, thus

becoming something similar to a DNA plasmid in an RNA cell.

These plasmids could then increase in size by acquiring host

RNA genes by the action of a reverse transcriptase enzyme. If

the DNA plasmid was replicatively more efficient and stable,

it would be to the benefit of the RNA cell to transfer all its

genes into this new DNA chromosome, thus slowly replacing

RNA chromosomes by DNA ones. The larger stability of DNA

molecules compared to RNA molecules opened the door for

increasing the size of chromosomes to levels impossible to attain

by primitive RNA chromosomes, thus opening the possibility for

increasing complexity.

Furthermore, Forterre (2006) argues that given the differences

among Bacteria, Archaea, and Eukarya in their replication and

translation machinery, it is likely that three independent events

of association between large-DNA viruses and RNA-cells took

place. These three symbiotic events resulted in the three cellular

domains of life that we know now, all three processes taking place

in a relatively short period of time or in isolation, so they out-

competed their surrounding RNA cell ancestors. Consequently,

additional possible domains have not survived nowadays (or have

not been discovered yet . . . ). Another explanation for why there

are only three cellular domains is that the events described in the

previous paragraph are so rare and complex that the probability

of more cases rendering additional cellular domains would be

too low.

The above theories explain the origin of DNA as the contem-

porary genetic material of a cell, but do not explain the origin

of the eukaryotic nucleus. Bell (2001, 2006) proposed the viral

eukaryogenesis theory to explain the origin of the complex

eukaryotic nucleus as the result of a consortium between an

archaeal cell that provided the cytoplasm, a bacterium that

7.5. Viruses as Sources of Evolutionary Novelties

**187**

provided the mitochondrion, and a large DNA virus (possibly

mimivirus-like) that provided the nucleus. In a process similar to

those described in the previous paragraph, the DNA virus genome

acquired genes from both the bacteria and the archaea and took

over the role of information storage for the consortium. The ar-

chaeal host retained its function of gene translation and of general

metabolism upon transferring the relevant genes into the viral

chromosome; the bacterium retained its ability to anaerobically

produce energy (ATP) and transferred most of its functions to

the viral chromosome. Bell also proposes that mitosis, meiosis,

and sexual cycles arose as a consequence of selective pressures

upon the lysogenic virus to maintain itself at a low copy number

(not blowing out the consortium) while still being capable of

transmitting into the population.

7.5 Viruses as Sources of Evolutionary Novelties

It should be clear now that viruses had an essential role in

the early evolution of life and the origin of eukaryotic cells.

However, the impact of viruses on evolution not only as harmful

parasites goes beyond the origins of cellular domains of life

and extends to the acquisition of many evolutionary novelties.

For example, in eukaryotes, sequences derived from transpo-

son mobile elements and endogenous retroviruses can account

for at least 50% of mammalian genomes and up to 90% of

plant genomes (Lynch and Conery 2003). Although integrated

transposons are the subject of strong functional suppression by

eukaryotes, they are potentially the source of new cellular genes

by exaptation4 (Freschotte and Pritham 2007). Examples of viral

genes impacting cellular evolution include bacteriphages that

provided their bacterial hosts with powerful toxins that bacteria

possibly originally used to fight against predator protists (Wagner

4A change in the function of a trait during evolution.

**188**

Chapter 7. Origins

and Waldor 2002). Integration of _Bracoviruses_ in wasp genomes

allowed the larvae to feed on arthropod hosts using viral-encoded

proteins to manipulate their victims (Herniou et al. 2013).

Another nice example is the exaptation of the RNA interference

and methylation-inactivation systems by eukaryotes that have

now become the basis of the RNAi-based innate immunity

defense mechanism of cells (Villarreal 2011).

A very interesting and well-studied innovation in mammal

cells has already been introduced in chapter 4:]] the exaptation of

the retroviral envelope protein into today’s syncytins (Villarreal

2016) involved in the fusion of trophoblast cells during placenta

formation could explain why embryos are protected against their

mother’s immune system, because the original role of these viral

proteins was to interfere with host immunity. Important roles

have also been suggested for a particular type of retroelement call

SINE in the origin and development of the mammalian brain

(Sasaki et al. 2008). One may speculate that the major differences

between chimps and us derived from the differences in viral

integrations that occurred upon separation of our two lineages,

activating or inactivating different genes.

7.6 But . . . What Is a Virus Then?

Most eukaryotic viruses share an interesting property: during

infection, they build complex and specialized intracellular struc-

tures associated with membranes (sometimes in close proximity to

organelles) taken from the reticulum. Inside these vesicules, viral

genomes are transcribed, translated into proteins, and replicated

(Romero-Brey and Bartenschlager 2014; Fernandez de Castro

et al. 2016). These structures are known as “virus factories” and

they provide a protected environment in which genomes can

be naked while still protected from the myriad of cytoplasmic

factors that cells activate as antiviral defenses to degrade them.

Virus factories are comparable with obligate intracellular parasitic

7.6. But . . . What Is a Virus Then?

**189**

bacteria: they are enclosed in membranes derived from the

endoplasmic reticulum, contain ribosomes and cytoskeletal

elements, and recruit the mitochondria and suck ATP from

it. The resemblances to cytoplasmic bacterial parasites become

obvious, especially if these tiny bacteria are compared to the giant

mimiviruses.

And here is the final reflection about what viruses are and

whether they are alive: considering the virion particle as the true

virus is equivalent to considering a grain of pollen as a redwood

or an ovulum as a human. The virion would be equivalent to the

germ line of the virus while the virus factory would equate to the

somatic line. Following Claverie (2006), the virus factory must be

considered as the real virus. With this interpretation in mind, the

living nature of viruses is out of discussion. The virus factory has

its own metabolism and contains ribosomes, and all information-

processing processes take place isolated from the environment.

Virus factories as a whole rather than as individual viral genomes

will represent the living fossils of those ancestral parasites that

were in the origin of the eukaryotic cell (see discussion above). So

yes, we think viruses are alive and, after all, we think it is plausible

that they evolved from parasitic entities that spontaneously arose

coupled to pre-cellular RNA-protein replicators (hypercycles).

Once membrane-bounded cells evolved, these parasites made

their way into them and since then have been coevolving into

what we now call viruses.

**8**

C O M P U T E R V I R U S E S A N D B E Y O N D

8.1 Viruses as Programs

In previous chapters we have considered the multiple facets of

viruses, their structure and evolution, and how they explore

their landscapes, strongly influencing the biosphere and our own

evolution as species. But the concept of virus itself, as a parasitic

entity able to propagate within and between living systems and

self-perpetuating its information through a process of copying

and infection, might be broader than we can imagine. With the

development of a theory of cultural evolution, the possibility of

defining a general form of propagating ideas, concepts, or symbols

that were not supported by genetic material became a very

appealing possibility. Here we want to explore the application of

key concepts associated to virus dynamics to other fields and see

how far the metaphors can be stretched.

As we pointed out in previous chapters, the fluid nature of

genomes makes it easy for viruses to emerge. Genomes include a

whole molecular toolkit that provides the raw material and rules

to create a wide range of virus-like entities. This occurs under an

evolutionary framework where viruses can act as replicators and

spread within their worlds, pushing the boundaries of biological

complexity and helping biological systems to overcome selection

barriers and even acquire new properties. But there is much more

8.2. Emergence of Computer Viruses

**191**

than viruses. If we consider this from a more abstract perspective,

we can now look at other complex systems where the nature and

dynamics of viruses can provide some insights into their origins

and evolution.

As philosopher Daniel Dennett points out, we can understand

evolution as a process leading to a given result not very different

from what computer scientists call an _algorithm_. For Dennett,

Darwin’s discovery is nothing but the discovery of a well-defined

algorithm (Dennett 1995; Blackmore 1999). An algorithm

correctly provides a formal framework to define a set of operations

that, starting from a set of boundary conditions (a data set for

a computer program), leads to a dynamical sequence of events

(such as the operations performed by the program) that end up in

some “solution” (the program output). This is one relevant piece

for our discussion below, along with how successful evolutionary

innovations propagate.

Three different case studies will be considered: (a) the origin

and evolution of computer viruses, (b) the evolution of cancer cell

populations, and (c) the emergence of human language. In each

case, comparing viruses and these apparently unrelated systems

will be more than an interesting set of analogies.

8.2 Emergence of Computer Viruses

In chapters 2]] and [^7] we have discussed the nature and inevitability of viruses within the context of digital genomes. Following von

Neumann’s conjecture on self-replicating machines, we have used

theoretical tools to describe viruses as sort of programs that make

copies of themselves using the molecular machinery of their hosts.

One of the main conclusions was that parasites are the inevitable

outcome of a flexible set of rules allowing the replication, cutting,

and pasting (with errors) of information. A somewhat similar

situation was in place a few decades after the starting of the IT

revolution. Software became the driving force for IT and smaller,

personal computers (figure 8.1a)]] became available to millions of

![[index-207_1.png]]

![[index-207_2.png]]

**192**

Chapter 8. Computer Viruses and Beyond

**a**

36

**b**

36

16

28

28

18

14

31

31

39

33

10

14

12

10

38

38

30

27

13

16

40

40

20

24 26 22 39

39

37

32

34

12

37

**c**

Personal computer

RF

Floppy disk

**d**

Computer virus

RF

**e**

RF

Antivirus software

1970

1980

1990

2000

Time

Figure 8.1. Computer viruses and the rise of information technology.

Two major innovations, namely personal computers (a) and floppy disks

(b) strongly contributed to the emergence and spread of computer viruses.

These two innovations appear to have grown markedly (c) in the early

8.2. Emergence of Computer Viruses

**193**

users, along with new magnetic storage media, particularly floppy

disks (figure 8.1b).]] At this point, all the requirements for the

propagation of computer viruses (CVs) were in place.

There are two reasons for our choice of CVs as a case study. On

one hand, it gives strong support for the inevitability hypothesis:

no matter whether biological or technological, the favorable

preconditions lead to emergence. The second reason is that the

sequence of events that took place in the evolution of CVs exhibits

strong parallelisms with their biological counterparts, despite

their obvious man-made (intentional) nature.1

Although the term _computer virus_ was introduced in 1985, the

beginnings of CVs can be found in 1971 (Levy 1992; Cohen

1994), when the first computer bug was created. It was limited

to a simple code that copied itself on other machines using a local

network of servers. The first bugs were rather harmless, and served

to illustrate the principles of replication in the computer context.

But virtual vandalism came shortly after. In the 1980s, a warning

message like DISK ERROR on the computer screen was a sign

of a coming catastrophe. And the diversity of CVs increased at a

very fast pace.

The handful of CVs existing in 1990 rapidly grew, at an

exponential pace. In 1996, it was estimated that more than

10,000 DOS-based CVs had been already created (Nachenberg

1997). Such growing complexity was a by-product of the

1The intentional design of CVs is a big departure from the nondesigned

nature of biological evolution. However, since CVs have to coevolve with chang-

ing environments, including the design of antivirus programs, the underlying

constraints on the evolution of CVs might be responsible for the universal

properties shared by both.

Figure 8.1. ( _Continued_ ) 1980s as personal computers became widely

adopted by millions of users. Computer viruses (d) and antivirus software

(e) followed. Data for figures c-e have been generated using the Google

Ngram Viewer. Here RF = relative frequency.

**194**

Chapter 8. Computer Viruses and Beyond

response of programmers, who started to develop systems able

to detect and destroy the virtual parasites. The emerging

technological developments were accompanied by the use of

well-known terms from epidemics. As Richard Dawkins puts it

(Dawkins, 1993):

Again predictably, the epidemic of computer viruses has

triggered an arms race. Anti-viral software is doing a roaring

trade. These antidote programs—“Interferon,” “Vaccine,”

“Gatekeeper” and others—employ a diverse armory of

tricks. Some are written with specific, known and named

viruses in mind. Others intercept any attempt to meddle

with sensitive system areas of memory and warn the user.

The list of tricks adopted by programmers in order to make

their worms more effective or even invisible is too large to

summarize here. At the beginning of our story, antivirus software

was mainly based on detecting specific sequences of bytes that

somewhat defined the signature of a given virus. Those early

programs involved finding given strings by searching for them

over the entire program under scrutiny. As the number of

potential viruses increased, this approach became more and more

involved and less efficient. New viruses became more difficult to

detect and remove. Old tricks (such as appearing with a nice

message such as “I love you”) had to be replaced by a great

invention: polymorphism (Nachenberg 1997).

Polymorphic CVs incorporated a powerful weapon mutation.

As it occurs with real viruses, constantly escaping from the

selection forces imposed by immune responses, detection, and

removal strategies is a major driver of genomic variability. As

we have already discussed, RNA viruses escape from the immune

system pressure by means of an error-prone molecular machinery

that is tuned to its error threshold. Polymorphic viruses are able

to keep their basic functions intact and yet appear “different” to

the infected machine. We can easily identify here the two types

8.2. Emergence of Computer Viruses

**195**

**a**

**b**

**c**

DOS

DOS

DOS

File A

DOS

y

Disk

File B

File A

File A

emorM

Virus

File B

Virus

Figure 8.2 Loading the DOS operating system (a) allows a given program

to be read (b) but it also provides the door for the entry of a computer

virus (c). Adapted from Dewdney (1989).

of information being carried by the computer viruses: a conserved

one (required for proper replication and infection) and a variable

one, playing the role of the variable domains of the genome more

prone to change. The new challenge was responded to by novel

antivirus software, but the arms race is still unfolding.

The emergence of computer viruses constitutes a very interest-

ing piece of cultural evolution. It illustrates quite well some key

similarities between biological and artificial (designed) change, for

example, the fact that mutation was the result of the conscious

realization that change was a requirement. It was thus an inven-

tion, and a rather intentional one, as opposed to the intrinsic,

inevitable errors that constantly take place in living systems.

Moreover, we know that most mutations affecting a virus genome

are harmful, impeding or threatening their replication potential.

How many mutations in their man-made counterparts are lethal?

None. There is a sharp separation between the part of the pro-

gram associated with variation and all the rest. No interactions are

allowed to occur affecting functional traits. As a consequence, the

mutations are de facto simulations of mutational events, instead

of a consequence of a faulty replication machinery. No true

quasispecies concept can be defined here. Moreover, although the

program-like nature of many viruses suggests that these entities

**196**

Chapter 8. Computer Viruses and Beyond

are somehow described under the Turing machine umbrella

(see chapter 2),]] it has been argued by various authors that

Turing’s formalism might fall short due to the nature of viral life

cycles, which require interactions with other machines leading to

spread of further programs (Thimbleby et al. 1998).

Beyond the infection and propagation dynamics of CVs there

are many other aspects of their evolution that are of interest to our

comparison with their biological counterparts. One in particular

is the emergence of Trojans that can integrate themselves within

the software of the host machines, resulting in a less harmful

infection (Hruska 1990; Thimbleby et al. 1998). Being invisible

to the user, not causing damage other than using some chunks

of memory and perhaps processing power, they remind us of the

group of lentiviruses (like HIV-1) that also integrate into the host

genome and remain apparently silent over years. Trojans and

other designed bugs can use computers as the sources of attack

on other machines, as generators of junk information, or even

as a parallel web of slave computers working together. As social

networks expanded on top of computer and email webs, new

threats have been emerging.

A further development in the evolutionary arms races between

computer viruses and antivirus programs was the possibility of

creating an artificial immune system (AIS) capable of adapting

to changing infectious programs. Such a view is inspired by

the natural immune responses (Farmer et al. 1986) that fight

pathogens within our own bodies (Kephart et al. 1995; Forrest

et al. 1997; Forrest and Beauchemin 2007). In chapter 4]] we

discussed some of these responses by means of simple models,

particularly in the context of highly variable retroviruses. These

AISs are designed in such a way that they incorporate some

key aspects of immune responses, while operating as computer

programs. One especially interesting component of an AIS is

the potential for learning to distinguish between self and nonself

(Janeway 1992; Forrest et al. 1994): as it occurs with the naturalR E F E R E N C E S

Abergel, C., Legendre, M., and Claverie, J. M. 2015. _The rapidly_

_expanding universe of giant viruses: mimivirus, pandoravirus, pithovirus_

_and mollivirus_. FEMS Microbiol. Rev. 39, 779–796.

Abrescia, N.G.A., Bamford, D. H., Grimes, J. M., and Stuart, D. I.

2012. _Structure unifies the viral universe_. Annu. Rev. Biochem. 81,

795–822.

Adami, C. 1998. _Introduction to Artificial Life_. Springer, New York.

Adami, C. 2006. _Digital genetics: unravelling the genetic basis of evolution_.

Nature Reviews Genetics, 7, 109–118.

Agudelo-Romero, P., de la Iglesia, F., and Elena, S. F. 2008. _The_

_pleiotropic cost of host-specialization in Tobacco etch potyvirus_. Infect.

Genet. Evol. 8, 806–814.

Aiewsakun, P., and Katzourakis, A. 2015. _Endogenous viruses: connecting_

_recent and ancient viral evolution_. Virology 479–480, 26–37.

Aita, T., Uchiyama, H., Inaoka, T., Nakajima, M., Kokubo, T., and

Husimi, Y. 2000. _Analysis of a local fitness landscape with a model of_

_the rough Mt. Fuji-type landscape: application to prolyl endopeptidase_

_and thermolysis_. Biopolymers 54, 64–79.

Aktipis, C. A., Boddy, A. M., Jansen, G., et al. 2015. _Cancer across the_

_tree of life: cooperation and cheating in multicellularity_. Phil. Trans. R.

Soc. B, 370, 20140219.

Anderson, R. M., and May, R. M. 1992. _Infectious Diseases of Humans_.

Oxford University Press.

**204**

References

Angly, F. E., Felts, B., Breitbart, M., et al. 2006. _The marine viromes of_

_four oceanic regions_. PLoS Biol, 4, e368.

Andino, R., and Domingo, E. 2015. _Viral quasispecies_. Virology

479–480, 46–51.

Archibald, J. M. 2015. _Endosymbiosis and eukaryotic cell evolution_. Curr

Biol 25, R911–921.

Arnaout, R. A., Nowak, M. A., and Wodarz, D. 2000. _HIV-1 dynamics_

_revisited: biphasic decay by cytotoxic T lymphocyte killing?_ Proc. R.

Soc. B. 2267, 1347–1354.

Baltimore, D. 1971. _Expression of animal virus genomes_. Bacteriol. Rev.

35, 235–241.

Barricelli, N. A. 1962. _Numerical testing of evolution theories_. Acta

Biotheoretica, 16, 69–98.

Barricelli, N. A. 1963. _Numerical testing of evolution theories_. Acta

Biotheoretica, 16, 99–126.

Bedhomme, S., Lafforgue, G., and Elena, S. F. 2012. _Multihost experi-_

_mental evolution of a plant RNA virus reveals local adaptation and host-_

_specific mutations_. Mol. Biol. Evol. 29, 1481–1492.

Bell, P.J.L. 2001. _Viral eukaryogenesis: was the ancestor of the nucleus a_

_complex DNA virus?_ J. Mol. Evol. 53, 251–256.

Bell, P.J.L. 2006. _Sex and the eukaryotic cell cycle is consistent with a viral_

_ancestry for the eukaryotic nucleus_. J. Theor. Biol. 243, 54–63.

Bennett, C. H., and Landauer, R. (1985). _The fundamental_

_physical limits of computation_. Scientific American, 253(1),

48–56.

Bittner, B., Bonhoeffer, S., and Nowak, M. A. 1997. _Virus load and_

_antigenic diversity_. Bull. Math. Biol. 59, 881–896.

Blackmore, S. 1999. _The meme machine_. Oxford University Press.

Bocharov, G., Ford, N. J., Edwards, J., Breinig, T., Wain-Hobson,

S., and Meyerhans, A. 2005. _A genetic-algorithm approach to sim-_

_ulating human immunodeficiency virus evolution reveals the strong_

_impact of multiply infected cells and recombination_. J. Gen. Virol 86,

3109–3118.

Bonhoeffer, S., Chappey, C., Parkin, N. T., Whitcomb, J. M., and

Petropoulos, C. J. 2004. _Evidence for positive epistasis in HIV-1_.

Science 306, 1547–1550.

References

**205**

Boulange, C. L., Neves, A. L., Chilloux, J., Nicholson, J. K., and

Dumas, M. E. 2016. _Impact of the gut microbiota on inflammation,_

_obesity, and metabolic disease_. Genome Med. 8, 42.

Brown, J. S., and Pavlovic, N. B. 1992. _Evolution in heterogeneous_

_environments: effects of migration on habitat specialization_. Evol. Ecol.

6, 360–382.

Bruinsma, R. F., Gelbart, W. M., Reguera, D., Rudnick, J., and

Zandi, R. 2003. _Viral self-assembly as a thermodynamic process_. Phys.

Rev. Lett. 90, 248101.

Brum, J. R., and Sullivan, M. B. 2015. _Rising to the challenge: accelerated_

_pace of discovery transforms marine virology_. Nat. Rev. Microbiol. 13,

147–159.

Bushman, F. D., Fujiwara, T., and Craigie, R. 1990. _Retroviral DNA_

_integration directed by HIV integration protein in vitro_. Science 249,

1555–1558.

Cahill, D. P., Kinzler, K. W., Vogelstein, B., and Lengauer, C. 1999.

_Genetic instability and Darwinian selection in tumours_. Trends Cell

Biol. 9, M57–M60.

Cairns, J., Stent, G. S., and Watson, J. D. 2007. _Phage and the origins of_

_molecular biology_. Cold Spring Harbor Laboratory Press. Cold Spring

Harbor: USA.

Callaway, D. S., Ribeiro, R. M., and Nowak, M. A. _Virus phenotype_

_switching and disease progression in HIV-1 infection_. Proc. R. Soc. B.

266, 2523–2530.

Case, T. J. 2000. _Illustrated Guide to Theoretical Ecology_. Oxford

University Press.

Catalán, P., Arias, C. F., Cuesta, J. A., and Manrubia, S. 2017. _Adaptive_

_multiscapes: an up-to-date metaphor to visualize molecular adaptation_.

Biol. Direct 12, 7.

Cervera, H., Lalic, J., and Elena, S. F. 2016. _Effect of host species on_

_the topography of fitness landscapes for a plant RNA virus_. J. Virol. 90,

10160–10169.

Cichutek, K., Merget, H., Norley, S., Linde, R., Kreuz, W.,

Gahr, M., and Kurth, R. 1992. _Development of a quasispecies of_

_Human immunodeficiency virus type 1 in vivo_. Proc. Natl. Acad. Sci.

USA 89, 7365–7369.

**206**

References

Clarke, D. K., Duarte, E. A., Elena, S. F., Moya, A., Domingo, E., and

Holland, J. J. 1994. _The Red Queen reigns in the kingdom of RNA_

_viruses_. Proc. Natl. Acad. Sci. USA 91, 4821–4824.

Claverie, J. M. 2006. _Viruses take center stage in cellulare evolution_.

Genome Biol. 7, 110.

Clokie, M.R.J., and Mann, N. H. 2006. _Marine cyanophages and light_.

Env Microbiol 8, 2074–2082.

Codoñer, F. M., Darós, J. A., Solé, R. V., and Elena, S. F. 2006. _The_

_fittest versus the flattest: experimental confirmation of the quasispecies_

_effect with subviral pathogens_. PLoS Pathog. 2, 1187–1193.

Coffey, L. L., Vasilakis, N., Brault, A. C., Powers, A. M., Tripet, F., and

Weaver, S. C. 2008. _Arbovirus evolution in vivo is constrained by host_

_alternation_. Proc. Natl. Acad. Sci. USA 105, 6970–6975.

Colizzi, E. S., and Hogeweg, P. 2016. _High cost enhances cooperation_

_through the interplay between evolution and self-organisation_. BMC

evolutionary biology, 16, 31.

Colson, P., De Lamballerie, X., Yutin, N., Asgari, S., et al. 2013.

_“Megavirales”, a proposed new order for eukaryotic nucleocytoplasmic_

_large DNA viruses_. Arch. Virol. 158, 2517–2521.

Cooper, L. A., and Scott, T. W. 2001. _Differential evolution of east-_

_ern equine encephalitis virus populations in response to host cell type_.

Genetics 157, 1403–1412.

Creager, A.N.H. _The Life of a Virus: Tobacco Mosaic Virus as an_

_Experimental Model, 1930–1965_. University of Chicago Press.

Crick, F. 1970. _Central dogma of molecular biology_. Nature 227,

561–563.

Crick, F. H., and Watson, J. D. 1956. _Structure of small viruses_. Nature

177, 473–475.

Crick, F.H.C., and Watson, J. D. 1957. _Virus structure: general_

_principles_. The Nature of Viruses, 5–18.

Crill, W. D., Wichman, H. A., and Bull, J. J. 2000. _Evolutionary_

_reversals during viral adaptation to alternating hosts_. Genetics 154,

27–37.

Cuevas, J. M., Moya, A., and Elena, S. F. 2003. _Evolution of RNA virus_

_in spatially structured heterogeneous environments_. J. Evol. Biol. 16,

456–466.

References

**207**

Dennett, D. C. 1995. _Darwin’s dangerous idea_. The Sciences, 35,

34–40.

Desnues, C., La Scola, B., Yutin, N., Fournous, G., et al. D. 2012.

_Provirophages and transpovirons as the diverse mobilome of giant viruses_.

Proc. Natl. Acad. Sci. USA 109, 18078–18083.

De Visser, J.A.G.M., and Krug, J. 2014. _Empirical fitness landscapes and_

_the predictability of evolution_. Nat. Rev. Genet. 15, 480–490.

De Visser, J.A.G.M., Hermisson, J., Wagner, G. P., Ancel Meyers, L.,

et al 2005. _Evolution and detection of genetic robustness_. Evolution 57,

1959–1972.

DeLong, E. F. 1997. _Marine microbial diversity: the tip of the iceberg_.

Trends Biotech. 15, 203–207.

Dill, K., and Bromberg, S. 2010. _Molecular driving forces: statistical_

_thermodynamics in biology, chemistry, physics, and nanoscience_. Garland

Science.

Dolja, V. V., Kreuze, J. F., and Valkonen, J. P. 2006. _Comparative and_

_functional genomics of Cloteroviruses_. Virus Res. 117, 38–51.

Domingo, E. 2000. _Viruses at the edge of adaptation_. Virology 270,

251–253.

Domingo, E., and Holland, J. J. 1997. _RNA virus mutations and fitness_

_for survival_. Annu. Rev. Microbiol. 51, 151–178.

Domingo, E., Sheldon, J., and Perales, C. 2012. _Viral quasispecies_

_evolution_. Microbiol. Mol. Biol. Rev. 76, 159–216.

Drake, J. W., Charlesworth, B., Charlesworth, D., and Crow, J. F.

1998. _Rates of spontaneous mutation_. Genetics 148, 1667–1686.

Dyson, G. 2012. _Turing’s Cathedral: The Origins of the Digital Universe_.

Pantheon.

Eigen, M. 1971. _Selforganization of matter and the evolution of biological_

_macromolecules_. Naturwissenschaften 58, 465–523.

Eigen, M., McCaskill, J., and Schuster, P. 1988. _Molecular quasi-species_.

J. Phys. Chem. 92, 6881–6891.

Elena, S. F., Carrasco, P., Daros, J. A., and Sanjuán, R. 2004. _Mecha-_

_nisms of genetic robustness in RNA viruses_. EMBO Rep. 7, 168–173.

Elena, S. F., and Sanjuán, R. 2005. _Adaptive value of high mutation_

_rates of RNA viruses: separating causes from consequences_. J. Virol. 79,

11555–11558.

**208**

References

Elena, S. F., Solé, R., and Sardanyés, J. 2010. _Simple genomes, complex_

_interactions: epistasis in RNA virus_. Chaos 20, 026106.

Ellner, P. D. 1998. _Smallpox: gone but not forgotten_. Infection 26,

263–269.

Faria, N. R., Rambaut, A., Suchard, M. A., Baele, G., et al. 2014.

_HIV epidemiology. The early spread and epidemic ignition of HIV-1 in_

_human populations_. Science 346, 56–61.

Farnet, C. M., and Haseltine, W. A. _Integration of human immuno-_

_deficiency virus type 1 DNA in vitro_. Proc. Natl. Acad. Sci. USA 87,

4164–4168.

Fernández de Castor, I., Tenorio, R., and Risco, C. 2016. _Virus assembly_

_factories in a lipid world_. Curr. Opin. Virol. 18, 20–26.

Flint, S. J., Enquist, L. W., Racaniello, V. R., and Skalka, A. M. 2015.

_Principles of Virology_. ASM Press. Washington DC: USA.

Flores, R., Gago-Zachert, S., Serra, P., Sanjuán, R., and Elena,

S.F. 2014. _Viroids: survivors from the RNA world?_ Annu. Rev.

Microbiol. 68, 395–414.

Forrest, S., Hofmeyr, S. A., and Somayaji, A. 1997. _Computer immuno-_

_logy_. Comm. ACM 40, 88–96.

Forrest, S., and Beauchemin, C. 2007. _Computer immunology_. Immuno-

logical Rev. 216, 176–197.

Forterre, P. 2002. _The origin of DNA genomes and DNA replication_

_proteins_. Curr. Opin. Microbiol. 5, 525–532.

Forterre, P. 2006a. _The origin of viruses and their possible roles in major_

_evolutionary transitions_. Virus Res. 117, 5–16.

Forterre, P. 2006b. _Three RNA cells for ribosomal lineages and three DNA_

_viruses to replicate their genomes: a hypothesis from the origin of cellular_

_domain_. Proc. Natl. Acad. Sci. USA 103, 3669–3674.

Forterre, P., and Prangishvili, D. 2009. _The origin of viruses_. Res.

Microbiol. 160, 466–472.

Fraenkel-Conrat, H., and Williams, R. C. 1955. _Reconstitution of_

_active tobacco mosaic virus from its inactive protein and nucleic acid_

_components_. Proc. Natl. Acad. Sci USA 41, 690–698.

Freschotte, C., and Pritham, E. J. 2007. _DNA transposons and the_

_evolution of eukaryotic genomes_. Annu. Rev. Genet. 41, 331–368.

Fry, J. D. 1996. _The evolution of host specialization: are tradeoffs over-_

_rated?_ Am. Nat. 148, S84–S107.

References

**209**

Fuhrman, J. A. 1999. _Marine viruses and their biogeochemical and_

_ecological effects_. Nature, 399, 541–548.

Fuhrman, J. A. 2009. _Microbial community structure and its functional_

_implications_. Nature, 459, 193–199.

Futuyma, D. J., and Moreno, G. 1988. _The evolution of ecological_

_specialization_. Annu. Rev. Ecol. Syst. 19, 207–233.

Murray, G. M. 1994. _The Quark and the Jaguar: Adventures in the Simple_

_and the Complex_. Little, Brown and Co. London, UK.

Gilbert, C., Peccoud, J., Chateigner, A., Moumen, B., Cordaux, R., and

Herniou, E. A. 2016. _Continuous influx of genetic material from host to_

_virus populations_. PLoS Genet 12, e1005838.

Gilbert, W. 1986. _Origin of life: the RNA world_. Nature 319, 618.

Goldenfeld, N. 1992. _Lectures on phase transitions and the renormaliza-_

_tion group_. Addison-Wesley.

Gotelli, N. J. 1995. _A Primer of Ecology_. Sinauer.

Greene, I. P., Wang, E., Deardorff, E. R., Milleron, R., Domingo, E.,

and Weaver, S. C. 2005. _Effect of alternating passage on adaptation_

_of Sindbis virus to vertebrate and invertebrate cells_. J. Virol. 79,

14253–14260.

Hagan, M. F. 2014. _Modeling viral capsid assembly_. Adv. Chem. Phys.

155, 1–68.

Hamelaar, J. 2012. _The origin and diversity of the HIV-1 pandemic_.

Trends Mol. Med. 18, 182–192.

Hannoun, C. 2013. _The evolving history of influenza viruses and influenza_

_vaccines_. Expert. Rev. Vaccines 12, 1085–1094.

Herniou, E. A., Huguet, E., Thézé, J., Bézier, A., Periquet, G., and

Drezen, J. M. 2013. _When parasitic wasps hijacked viruses: genomic_

_and functional evolution of polydnaviruses_. Philos. Trans. R. Soc.

B 368, 20130051.

Hinkley, T., Martins, J., Chappey, C., Haddad, M., et al., 2011. _A_

_systems analysis of mutational effects in HIV-1 protease and reverse_

_transcriptase_. Nat. Genet. 43, 487–489.

Holland, J. J., de la Torre, J. C., Clarke, D. K., and Duarte, E.A.

1991. _Quantitation of relative fitness and great adaptability of clonal_

_populations of RNA viruses_. J. Virol. 65, 2960–2967.

Holmes, E. C. 2001. _On the origin and evolution of the human immuno-_

_deficiency virus (HIV)_. Biol. Rev. Camb. Phil. Soc. 76, 239–254.

**210**

References

Holmes, E. C. 2010. _The RNA virus quasispecies: fact or fiction_. J. Mol.

Biol. 400, 271–273.

Hopcroft, J. E. 1984. _Turing machines_. Sci. Am. 250, 86–107.

Hull, R., and Will, H. 1989. _Molecular biology of viral and nonviral_

_retroelements_. Trends Genet. 5, 357–359.

Janeway Jr, C. A., Travers, P., Walport, M., and Shlomchik, M. J. 2004.

_Immunobiology 6th edition_. Garland Science. New York.

Kaneko, K., and Ikegami, T. 1992. _Homeochaos: dynamics stability of_

_a symbiotic network with population dynamics and evolving mutation_

_rates_. Physica D 56, 406–429.

Kauffman, S. A. 1993. _The Origins of Order: Self-Organization and_

_Selection in Evolution_. Oxford University Press.

Kauffman, S., and Levin, S. 1987. _Towards a general theory of adaptive_

_walks on rugged landscapes_. J. Theor. Biol. 128, 11–45.

Kawecki, T. J. 1994. _Accumulation of deleterious mutations and the_

_evolutionary cost of being a generalist_. Am. Nat. 144, 833–838.

Kawecki, T. J. 2000. _Adaptation to marginal habitats: contrasting influ-_

_ence of the dispersal rate on the fate of alleles with small and large effects_.

Proc. R. Soc. B 267, 1315–1320.

Keeling, M. J., and Eames, K. T. 2005. _Networks and epidemic models_.

J. R. Soc. Interface 2, 295–307.

Keeling, M. J., and Rohani, P. 2007. _Modeling Infectious Disease in_

_Humans and Animals_. Princeton University Press.

Kelly, S. G., and Taiwo, B. O. 2015. _HIV reservoirs in lymph nodes and_

_spleen_. Encyclopedia of AIDS. DOI 10.1007/978.

Kerr, P. J., Liu, J., Cattadori, I., Ghedin, E., Read, A. F., and

Holmes, E. C. 2015. _Myxoma virus and the Leporiposviruses: an_

_evolutionary paradigm_. Viruses 7, 1020–1061.

Kingman, J. 1987. _A simple model for the balance between selection and_

_mutation_. J. Appl. Probab. 15, 1–12.

Kloverpris, H. N., Leslie, A., and Goulder, P. 2016. _Role of HLA_

_adaptation in HIV evolution_. Front. Immunol. 6, 665.

Klug, A. 1999. _The tobacco mosaic virus particle: structure and assembly_.

Phil. Trans. R. Soc. B 354, 531–535.

Koelle, K., Cobey, S., Grenfell, B. T., and Pascual, M. 2006. _Epocal_

_evolution shapes the phylodynamics of inerpandemic influenza A (H3N2)_

_in humans_. Science 314, 1898–1903.

References

**211**

Koonin, E. V., and Dolja, V. V. 2013. _A virocentric perspective on the_

_evolution of life_. Curr. Opin. Virol. 3, 546–557.

Koonin, E. V., Senkevich, T. G., and Dolja, V. V. 2006. _The ancient_

_virus world and evolution of cells_. Biol. Direct 1, 29.

Koonin, E. V., and Starokadomskyy, P. 2016. _Are viruses alive? The_

_replicator paradigm sheds decisive light on an old but misguided question_.

Studies in History and Philosophy of Biological and Biomedical

Sciences, 59, 125–134.

Kouyos, R. D., Leventhal, G. E., Hinkley, T., Haddad, M., et al. 2012.

_Exploring the complexity of the HVI-1 fitness landscape_. PLoS Genet. 8,

e1002551.

Kristensen, D. M., Mushegian, A. R., Dolja, V. V., and

Koonin, E. V. 2010. _New dimensions of the virus world discovered_

_through metagenomics_. Trends Microbiol. 18, 11–19.

Krupovic, M., and Bamford, D. H. 2010. _Order to the viral universe_. J.

Virol. 84, 12476–12479.

Krupovic, M., and Koonin, E.V. 2016. _Self-synthesizing transposons:_

_unexpected key players in the evolution of viruses and defense systems_.

Curr. Opin. Microbiol. 30, 25–33.

Kushner, D. J. 1969. _Self-assembly of biological structures_. Bacteriological

reviews, 33, 302–345.

Lalic, J., and Elena, S. F. 2012. _Magnitude and sign epistasis among_

_deleterious mutations in a positive-sense plant RNA virus_. Heredity 109,

71–77.

Lalic, J., and Elena, S. F. 2015. _The impact of higher-order epistasis in the_

_within-host fitness of a positive-sense plant RNA virus_. J. Evol. Biol. 28,

2236–2247.

Lane, J. M. 2006. _Mass vaccination and surveillance/containment in the_

_eradication of smallpox_. Curr. Top. Microbiol. Immunol. 304, 17–29.

La Scola, B., Audic, S., Robert, C., et al. 2003. _A giant virus in amoebae_.

Science, 299, 2033–2033.

La Scola, B., Desnues, C., Pagnier, I., Robert, C., et al. 2008. _The_

_virophage as a unique parasite of the giant mimivirus_. Nature 455,

100–104.

Lauring, A. S., and Andino, R. 2010. _Quasispecies theory and the behavior_

_of RNA viruses_. PLoS Pathog. 6, e1001005.

**212**

References

Leuthäusser, I. 1986. _An exact correspondence between Eigen’s evolu-_

_tion model and a two-dimensional Ising system_. J. Chem. Phys. 84,

1884–1885.

Leuthäusser, I. 1987. _Statistical mechanics of Eigen’s evolution model_. J.

Stat. Phys. 48, 343–360.

Levin, S. A. 1998. _Ecosystems and the biosphere as complex adaptive_

_systems_. Ecosystems 1, 431–436.

Li, C. X., Shi, M., Tian, J. H., Lin, X. D., et al. 2015. _Unprecedent_

_genomic diversity of RNA viruses in arthropods reveals the ancestry of_

_negative-sense RNA viruses_. eLIFE 4, e05378.

Littlejohn, M., Locarnini, S., and Yuen, L. 2016. _Origins and evolution_

_of Hepatitis B virus and hepatitis delta virus_. Cold Spring Harb.

Perspect. Med. 6, a021360.

Lively, C. M. 2010. _A review of Red Queen models for the persistence of_

_obligate sexual reproduction_. J. Hered. 101, S13–S20.

Loeb, L. A., and Mullins, J. I. 2000. _Lethal Mutagenesis of HIV_

_by Mutagenic Ribonucleoside Analogs_. AIDS research and human

retroviruses, 16(1), 1–3.

López-Garcia, P., and Moreira, D. 2009. _Yet viruses cannot be included_

_in the three of life_. Nat. Rev. Microbiol. 7, 615.

Lorenzo-Redondo, R., Fryer, H. R., Bedford, T., et al. 2016. _Persistent_

_HIV-1 replication maintains the tissue reservoir during therapy_. Nature

530, 51–56.

Lynch, M., and Conery, J. S. 2003. _The origins of genome complexity_.

Science 302, 1401–1404.

May, R. M. 2001. _Stability and Complexity in Model Ecosystems_. Prince-

ton University Press.

May, R. M. 2004. _Uses and abuses of mathematics in biology_. Science 303,

790–793.

Maynard Smith, J. 2000. _The concept of information in biolog_ y. Philoso-

phy of science, 67, 177–194.

Mills, D. R., Peterson, R. L., and Spiegelman, S. 1967. _An extracellular_

_Darwinian experiment with a self-duplicating nucleic acid molecule_.

Proc. Natl. Acad. Sci. USA 58, 217–224.

Minot, S., Bryson, A., Chehoud, C., Wu, G. D., Lewis, J. D., and

Bushman, F. D. (2013). _Rapid evolution of the human gut virome_.

Proc. Natl. Acad. Sci. USA 110, 12450–12455.

References

**213**

Mitchell, M. 2009. _Complexity: A Guided Tour_. Oxford University

Press.

Molina-París, C., and Lythe, G. (Eds.). 2011. _Mathematical models and_

_immune cell biology_. Springer.

Morange, M. 2000. _A History of Molecular Biology_. Harvard University

Press.

Motulsky, A. G. 1964. _Hereditary red cell traits and malaria_. Am. J.

Trop. Med. Hyg. 13, S147–S158.

Mouritsen, O. G. 2005. _Life—As a Matter of Fat_. Springer-Verlag.

Mushegian, A. R., and Elena, S. F. 2015. _Evolution of plant virus_

_movement proteins from the 30K superfamily and of their homologs_

_integrated in plant genomes_. Virology 476, 304–315.

Myllykallio, H., Lipowski, G., Leduc, D., Fillon, J., Forterre, P.,

and Liebl, U. 2002. _An alternative flavin-dependent mechanism for_

_thymidylate synthesis_. Science 297, 105–107.

Nachenberg, C. 1997. _Computer virus-coevolution_. Comm. ACM 50,

46–51.

Novella, I. S., Duarte, E. A., Elena, S. F., Moya, A., Domingo, E., and

Holland, J. J. 1995. _Exponential fitness increases of RNA virus fitness_

_during large population transmissions_. Proc. Natl. Acad. Sci. USA 92,

5841–5844.

Novella, I. S., Hershey, C. L., Escarmis, C., Domingo, E., and

Holland, J. J. 1999. _Lack of evolutionary stasis during alternating_

_replication of an arbovirus in insect and mammalian cells_. J. Mol. Biol.

287, 459–465.

Nowak, M. A., Anderson, R. M., Boerlijst, M. C., Bonhoeffer, S.,

May, R. M., and McMichael, A. J. 1996. _HIV-1 evolution and disease_

_progression_. Science 274, 1008–1011.

Nowak, M. A., Anderson, R. M., McLean, A. R., Wolfs, T. F.,

Goudsmit, J., and May, R. M. 1991. _Antigenic diversity thresholds and_

_the development of AIDS_. Science 254, 963–969.

Nowak, M. A., and Bangham, C. R. _Population dynamics of immune_

_responses to persistent viruses_. Science 272, 74–79.

Nowak, M., and May, R. M. 2000. _Virus Dynamics: Mathematical_

_Principles of Immunology and Virology_. Oxford University Press, UK.

Palukaitis, P. 2016. _Satellite RNAs and satellite viruses_. Mol. Plant

Microb. Interact. 29, 181–186.

**214**

References

Pantaleo, G., Graziosi, C., and Fauci, A. S. 1993. _The immunopathogen-_

_esis of human immunodeficiency virus infection_. New England Journal

of Medicine 328, 327–335.

Perales, C., Iranzo, J., Manrubia, S. C., and Domingo, E. 2012. _The_

_impact of quasispecies dynamics on the use of therapeutics_. Trends

Microbiol. 20, 595–603.

Perelson, A. S., and Kauffman, S. A. (eds.) 1991. _Molecular Evolution_

_on Rugged Landscapes_. Addison-Wesley.

Perelson, A. S., and Weisbuch, G. 1997. _Immunology for physicists_.

Reviews of modern physics 69, 1219.

Perelson, A. S., and Nelson, P. W. 1999. _Mathematical analysis of HIV-1_

_dynamics in vivo_. SIAM review, 41, 3–44.

Perelson, A. S. 2002. _Modelling viral and immune system dynamics_.

Nature Rev. Immunol. 2, 28–36.

Perrin, P. 2015. _Human and tuberculosis coevolution: an integrative view_.

Tuberculosis 95, S112–S116.

Philippe, N., Legendre, M., Doutre, G., et al. 2013. _Pandoraviruses:_

_amoeba viruses with genomes up to 2.5 Mb reaching that of parasitic_

_eukaryotes_. Science 341, 281–286.

Presloid, J. B., Ebendick-Corpus, B. E., Zárate, S., and Novella, I. S.

2008. _Antagonistic pleiotropy involving promoter sequences in a virus_.

J. Mol. Biol. 382, 342–352.

Quer, J., Huerta, R., Novella, I. S., Tsimring, L. S., Domingo, E., and

Holland, J. J. 1996. _Reproducible nonlinear population dynamics and_

_critical points during replicate competitions of RNA virus quasispecies_.

J. Mol. Biol. 264, 465–471.

Rambaut, A., Roberston, D. L., Pybus, O. G., Peeters, M., and

Holmes, E. C. 2001. _Human immunodeficiency virus. Phylogeny and_

_the origin of HIV-1_. Nature 410, 1047–1048.

Raoult, D., Audic, S., Robert, C., Abergel, C., et al. 2004. _The_

_1.2-megabase genome sequence of Mimivirus_. Science 306, 1344–1350.

Ray T. S. 1991. An approach to the synthesis of life. 371–408. In:

_Artificial life II: Santa Fe Institute studies in the sciences of complexity_.

Langton, C., Taylor, C. and Farmer, D. (eds). Addison-Wesley.

Ray, T. S. 1994. _Evolution, complexity, entropy and artificial reality_.

Physica D 75, 239–263.

References

**215**

Reidys, C. M., and Stadler, P. F. 2002. _Combinatorial landscapes_. SIAM

review, 44, 3–54.

Remold, S. K., Rambaut, A., and Turner, P. E. 2008. _Evolutionary_

_genomics of host adaptation in vesicular stomatitis virus_. Mol. Biol. Evol.

25, 1138–1147.

Rico, P., Ivars, P., Elena, S. F., and Hernandez, C. 2006. _Insights into_

_the selective pressures restricting Pelargonium flower break virus genome_

_variability: evidence for host adaptation_. J. Virol. 80, 8124–8132.

Romero-Brey, I., and Bartenschlager, R. 2014. _Membraneous replication_

_factories induced by plus-strand RNA viruses_. Viruses 6, 2826–2857.

Roossinck, M. J., Martin, D. P., and Roumagnac, P. 2015. _Plant_

_virus metagenomics: advances in virus discovery_. Phytopathology 105,

716–727.

Rossmann, M. G., and Rao, V. B. 2012. _Viruses: sophisticated biological_

_machines_. In: _Viral Molecular Machines_ (pp. 1-3). Springer.

Ryan, F. P. 2016. _Viral symbiosis and the holobiontic nature of the human_

_genome_. APMIS 124, 11–19.

Sanger, F., Air, G. M., Barrell, B. G., et al. 1977. _Nucleotide sequence of_

_bacteriophage φX174 DNA_. Nature, 265, 687–695.

Sanjuán, R., Codoñer, F. M., Moya, A., and Elena, S. F. 2004. _Natural_

_selection and the organ-specific differentiation of HIV-1 V3 hypervariable_

_region_. Evolution 58, 1185–1194.

Sanjuán, R., Cuevas, J. M., et al. 2009. _Selection for robustness in_

_mutagenized RNA viruses_. PLoS Genet. 3, 939–946.

Sanjuán, R., Moya, A., and Elena, S. F. 2004. _The contribution of_

_epistasis to the architecture of fitness in an RNA virus_. Proc. Natl. Acad.

Sci. USA 101, 15376–15379.

Sanjuán, R., Nebot, M. R., Chirico, N., Mansky, L. M., and

Belshaw,

R.

2010.

_Viral_

_mutation_

_rates_.

J.

Virol.

84,

9733–9748.

Sardanyés, J., Elena, S. F., and Solé, R. V. 2008. _Simple quasispecies_

_models for the survival-of-the-flattest effect: the role of space_. J. Theor.

Biol. 250, 560–568.

Sasaki, T., Nishihara, H., Hirakawa, M., Fujimura, K., et al. 2008.

_Possible involvement of SINEs in mammalian-specific brain formation_.

Proc. Natl. Acad. Sci. USA 105, 4220–4225.

**216**

References

Schuster, P., and Swetina, J. 1988. _Stationary mutant distributions and_

_evolutionary optimization_. Bull. Math. Biol. 50, 635–660.

Schuster, P. 2006. _Prediction of RNA secondary structures: from theory to_

_models and real molecules_. Reports on Progress in Physics, 69, 1419.

Schuster, P. 2009. _Genotypes and phenotypes in the evolution of molecules_.

European Review, 17, 281–319.

Serrao, E., and Engelman, A. N. 2016. _Sites of retroviral DNA integra-_

_tion: from basic research to clinical applications_. Crit. Rev. Biochem.

Mol. Biol. 51, 26–42.

Simmons, P. 2015. _Methods for virus classification nd the challenge_

_of incorporating metagenomic sequence data_. J. Gen. Virol. 96,

1193–1206.

Smyth, R. P., Davenport, M. P., and Mak, J. 2012. The origin of genetic

diversity in HIV-1. Virus research 169 415–429.

Solé, R. V., Ferrer, R., Gonzalez-Garcia, I., Quer, J., and Domingo, E.

1999. _Red Queen dynamics, competition and critical points in a model_

_of RNA virus quasispecies_. J. Theor. Biol. 198, 47–59.

Solé, R. V., and Goodwin, B. 2002. _Signs of Life: How Complexity_

_Pervades Biology_. Basic Books.

Solé, R. 2011. _Phase Transitions_. Princeton University Press.

Spiegelman, S. 1971. _An aproach to the experimental analysis of precellular_

_evolution 1_. Quarterly reviews of biophysics, 4, 213–253.

Stadler, P. F. 1999. _Fitness landscapes arising from the sequence-structure_

_maps of biopolymers_. Journal of Molecular Structure 463, 7–19.

Stadler, B. M., Stadler, P. F., Wagner, G. P., and Fontana, W.

2001. _The topology of the possible: Formal spaces underlying patterns_

_of evolutionary change_. J. Theor. Biol. 213, 241–274.

Stafford, M. A., Corey, L., Cao, Y., et al. 2000. _Modeling plasma_

_virus concentration during primary HIV infection_. J. Theor Biol. 203,

285–301.

Stewart, I. 1998. _Life’s Other Secret. The New Mathematics of the Living_

_World_. John Wiley.

Stockley, P. G., Twarock, R., Bakker, S. E., Baker, A. M., et al. 2013.

_Packaging signals in single-stranded RNA viruses: nature’s alternative to_

_a purely electrostatic assembly mechanism_. J. Biol. Phys. 39, 277–287.

Suttle, C. A. 2005. _Viruses in the sea_. Nature, 437, 356–361.

References

**217**

Szathmáry, E. 2006. _The origin of replicators and reproducers_. Phil. Trans.

Roy. Soc. B 361, 1761–1776.

Thomas, C. M., and Summers, D. 2008. _Bacterial plasmids_.

Encyclopedia of Life Sciences, DOI: 10.1002/9780470015902

.a0000468.pub2.

Taur, Y., and Pamer, E. G. 2016. _Microbiome mediation of infections in_

_the cancer setting_. Genome Med. 8, 40.

Tripathi, K., Balagam, R., Vishnoi, N. K., and Dixit, N. M. 2012.

_Stochastic simulations suggest that HIV-1 survives close to its error_

_threshold_. PLoS Comput Biol, 8, e1002684.

Turner, P. E., and Elena, S. F. 2000. _Cost of host radiation in an RNA_

_virus_. Genetics 156, 1465–1470.

Van Nimwegen, E. 2006. _Influenza escapes immunity along neutral_

_networks_. Science 314, 1884–1886.

Van Nimwegen, E., Crutchfield, J. P., and Huynen, M. (1999). _Neutral_

_evolution of mutational robustness_. Proc. Natl. Acad. Sci. USA 96,

9716–9720.

Van Tienderen, P. H. 1991. _The evolution of generalists and special-_

_ists in spatially structured heterogeneous environments_. Evolution 45,

1317–1331.

Villarreal, L. P. 2004. _Are viruses alive?_ Scientific American 97, 102.

Villarreal, L. P. 2011. _Viral ancestors of antiviral systems_. Viruses 3,

1933–1958.

Villarreal, L. P. 2016. _Viruses and the placenta: the essential virus first_

_view_. APMIS 124, 20–30.

De Visser, J.A.G., and Krug, J. 2014. _Empirical fitness landscapes and the_

_predictability of evolution_. Nature Reviews Genetics 15, 480–490.

Von Neumann, J., and Burks, A. W. 1966. _Theory of self-_

_reproducing automata_. IEEE Transactions on Neural Networks, 5,

3–14.

Wagner, P. L., and Waldor, M. K. 2002. _Bacteriophage control of_

_bacterial virulence_. Infect. Immun. 70, 3985–3993.

Weaver, S. C., Brault, A. C., Kang, W., and Holland, J. J. 1999.

_Genetic and fitness changes accompanying adaptation of an arbovirus to_

_vertebrate and invertebrate cells_. J. Virol. 73, 4316–4326.

Weinberg, R. 2013. _The Biology of Cancer_. Garland Science.

**218**

References

Wesemann, D. R., and Nagler, C. R. 2016. _The microbiome, timing,_

_and barrier function in the context of allergic disease_. Immunity 44,

728–738.

Whitlock, M. C. 1996. _The Red Queen beats the jack-of-all-trades: the_

_limitations on the evolution of phenotypic plasticity and niche breadth_.

Am. Nat. 148, S65–S77.

Wilke, C. O. 2001. _Selection for fitness versus selection for robustness in_

_RNA secondary structure folding_. Evolution 55, 2412–2420.

Wilke, C. O., Forster, R., and Novella, I. S. 2006. _Quasispecies in_

_time-dependent environments_. Curr. Top. Microbiol. Immunol. 299,

33–50.

Willard-Mack, C. L. 2006. _Normal structure, function, and histology of_

_lymph nodes_. Toxicol. Pathol. 34, 409–424.

Wodarz, D., and Nowak, M. A. 1999. _Evolutionary dynamics of HIV-_

_induced subversion of the immune response_. Immunol. Rev. 168,

75–89.

Wodarz, D., and Nowak, M.A. 2002. _Mathematical models of HIV_

_pathogenesis and treatment_. Bioessays 24, 1178–1187.

Woolhouse, M.E.J., and Gowtage-Sequeria, S. 2005. _Host range_

_and emerging and reemerging pathogens_. Emerging Infect. Dis. 11,

1842–1847.

Woolhouse, M.E.J., Taylor, L. H., and Haydon, D. T. 2001. _Population_

_biology of multihost pathogens_. Science 292, 1109–1112.

Yoon, S. W., Webby, R. J., and Webster, R. G. 2014. _Evolution and_

_ecology of influenza A viruses_. Curr. Top Microbiol. Immunol. 385,

359–375.

Zandi, R., Reguera, D., Bruinsma, R. F., Gelbart, W. M., and

Rudnick, J. 2004. _Origin of icosahedral symmetry in viruses_. Proc. Natl.

Acad. Sci. USA 101, 15556–15560.

Zhou, J., Zhang, W., Yan, S., Xiao, J., Zhang, Y., Li, B., Pan, Y.,

and Wang, Y. 2013. _Diversity of virophages in metagenomic data sets_.

J. Virol. 87, 4225–4236.



I N D E X

Adami, Christoph, 36,]] 87,]] [^172]

cancer, 191,]] 197–99,]] [^201]

adaptability, x,]] 55,]] [^73]

capsid, 11,]] 12,]] 25–27,]] 30,]] 31,]] 161,]]

adaptation, 25,]] 43,]] 54,]] 73,]] 75,]] 76,]]

176,]] 178,]] 180,]] 181,]] 185,]] [^186]

152,]] 154,]] 155,]] 157–59,]] 161,]]

CChMoVd, 46,]] [^78]

162,]] [^198]

CD4+ T cells, 94,]] 96,]] 97,]] 105,]] 109,]]

adaptive dynamics, [^75]

110,]] 112,]] [^116]

adaptive walk, 60,]] [^61]

cellular automata, 52,]] 81,]] 105,]] 107,]]

AIDS, 95–98,]] 101,]] 107–9,]] 111–16,]]

108,]] 134,]] [^171]

137,]] 139,]] 140,]] [^141]

Claverie, Jean M., 40,]] 41,]] [^189]

antagonistic pleiotropy, 77,]] 156,]]

compensatory mutations, [^75]

161,]] [^162]

competition, 35,]] 56,]] 62–65,]] 67,]] 68,]]

antigenic diversity, 108,]] 109,]]

78,]] 79,]] 81,]] 155,]] [^199]

111–13,]] 115,]] [^116]

complementation, [^85]

arms races, 43,]] 91,]] 92,]] 94,]] 96,]] 98,]]

computer viruses, ix,]] x,]] 21,]] 43,]] 170,]]

100,]] 102,]] 104,]] 106,]] 108,]] 110–12,]]

191–96

114–16,]] 118,]] 119,]] 169,]] 194,]]

consensus sequence, [^44]

195,]] [^196]

critical mutation rate, 45,]] [^89]

CSVd [^78]

Baltimore, David, 13,]] 14,]] 15,]]

cyanophages [^40]

41,]] [^42]

basic reproductive number, 128,]] 129,]]

Darwin, Charles R., [^199]

130,]] 139,]] 140,]] 145,]] 163–65]]

Dawkins, Richard, 37,]] [^194]

beneficial mutations, 75,]] 76,]] [^82]

deleterious mutations, 71,]] 82,]]

bit-string model, [^67]

83,]] [^86]

**220**

Index

DNA, xi,]] xii,]] 12–15,]] 21–23,]] 38,]] 39,]]

generalism, [^155]

41–43,]] 45,]] 46,]] 94,]] 95,]] 117,]] 169,]]

genetic variability, 44,]] 78,]] 87,]]

176,]] 177,]] 179,]] 180–83,]] 185–87]]

105,]] [^151]

Domingo, Esteban, xii,]] 44,]] 47,]]

genome length, 33,]] 37,]] 45–47,]] 49,]]

54,]] [^55]

53,]] 56,]] [^71]

genotype-phenotype mapping, [^90]

EBOV, 4,]] 6,]] 7,]] 14,]] 124,]] 126,]] 129,]]

giant viruses, 10,]] 41,]] 42,]] 117,]] 180,]]

130,]] 150,]] 151,]] [^155]

183–85

EEEV, 156,]] [^158]

Eigen, Manfred, 44,]] 45,]] 47,]] [^53]

hardware, ix,]] 19,]] 20,]] 23–25,]] 32,]]

Elena, Santiago F., 15,]] 44,]] 70,]] 71,]]

42,]] [^117]

72,]] 74,]] 75,]] 83,]] 156,]] [^158]

Hamming distance, 61,]] 70,]] [^71]

emergence, 98,]] 99,]] 149,]] 151,]] 152,]]

HBV, 15,]] 31,]] 151,]] [^182]

154,]] 162,]] 163,]] 165–67,]] 170–72,]]

HCV, 14,]] 129,]] 154,]] [^155]

183,]] 191–93,]] 195,]] [^196]

heat-shock proteins, [^86]

emergent viruses, ix,]] 6,]] 150–52,]] 154,]]

HIV-1, 4,]] 5,]] 15,]] 92–98,]] 101–5,]]

156,]] 158,]] 160,]] 162,]] 164,]] [^166]

107–9,]] 112,]] 113–15,]] 122,]] 123,]]

endosymbiotic bacteria, [^40]

129,]] 137,]] 139,]] 151,]] 166,]]

ENIAC, 23,]] [^171]

169,]] [^196]

epistasis, 57,]] 68–70,]] 71–75,]] [^86]

Holland, John J., xii,]] 44,]] 54,]] 55,]] [^156]

error catastrophe, 44,]] 51,]] [^199]

Holmes, Edward C., 44,]] 73,]] 78,]]

error threshold, 46,]] 54,]] 194,]] [^198]

122,]] [^149]

ERVs, 117,]] [^118]

hypercycle, 180,]] [^189]

escape mutants, 93,]] 112,]] [^169]

hypercube, 56,]] 58,]] [^59]

evolution, ix–xi,]] 3,]] 4,]] 9,]] 13,]] 18,]] 20,]]

33,]] 34,]] 43–45,]] 56,]] 60,]] 61,]] 63,]] 67,]]

IAV, 85,]] 129,]] 151,]] 155,]] [^166]

68,]] 73,]] 138,]] 140,]] 149,]] 150,]] 156,]]

immune system, 4,]] 92,]] 93,]] 95,]] 96,]]

157,]] 159–62,]] 169,]] 170–73,]]

98,]] 100,]] 107,]] 108,]] 109,]] 111,]] 114,]]

175–78,]] 185,]] 187,]] 190,]] 191,]] 193,]]

115,]] 169,]] 188,]] 194,]] 196,]] [^197]

195–201

infectivity, 58,]] 74,]] 129,]] 152,]] [^160]

experimental evolution, 63,]] [^75]

information, xii,]] 4,]] 12,]] 15,]] 19,]]

21–24,]] 32,]] 33,]] 43,]] 44,]] 45,]] 47,]] 57,]]

fitness, x,]] 34,]] 44,]] 47,]] 57–64,]]

75,]] 106,]] 140,]] 146,]] 170,]] 176,]]

66–81,]] 83,]] 85–87,]] 89,]] 109,]] 151,]]

181,]] 182,]] 187,]] 189,]] 190–92,]]

152,]] 155–59,]] 161,]] 162,]] 169,]]

195–97,]] [^201]

173,]] [^200]

Ising model, [^52]

fitness landscape, x,]] 57–60,]] 62,]] 67,]]

69–71,]] 73–77,]] 79,]] [^109]

Kauffman, Stuart A., xii,]] 58,]] [^60]

Forterre, Patrick, 168,]] 176,]] 180–82,]]

Koonin, Eugene V., xii,]] 4,]] 7,]] 13,]] 37,]]

185,]] [^186]

38,]] 40,]] 168,]] 169,]] 176,]] 179,]] [^185]

Index

**221**

lentivirus, 115,]] [^196]

pandoravirus, 10,]] 41,]] 183,]] [^184]

Lotka-Volterra model, 65,]] 98–100]]

parasite, xi,]] 8,]] 18,]] 20,]] 24,]] 25,]] 36,]] 41,]]

LUCA, 180,]] [^181]

42,]] 93,]] 168–72,]] 174–77,]] 179,]]

180,]] 182,]] 183,]] 185,]] 187,]] 189,]]

Manrubia, Susanna C., xii,]] 53,]] [^54]

191,]] 194,]] [^201]

MARM, [^62]

Pastor-Satorras, Romualdo, 53,]]

master sequence, 44,]] 48–51,]] 54,]]

143,]] [^145]

58,]] [^70]

Perelson, Alan S., 58,]] 92,]] 100,]]

May, Robert L., 92,]] 98,]] 114,]] 115,]]

103–5,]] 108,]] [^197]

125,]] 137,]] 140,]] 141,]] 143,]] [^145]

phase transition, x,]] 28,]] 30,]] 31,]] 44,]]

Maynard Smith, J., 19,]] [^63]

51,]] 52,]] 54,]] 133,]] 135,]] [^146]

mean field, 52,]] 79,]] 87,]] 135,]] 141,]]

phenotype, 44,]] 57,]] 58,]] 60,]] 68,]]

143,]] 144,]] [^146]

83–85,]] 90,]] [^109]

metabolism, 37,]] 40,]] 187,]] [^189]

plasmid, 38,]] 39,]] 73,]] 177,]] 183,]] [^186]

metagenomics, [^3]

Platonic solids, [^26]

microbiome, [^8]

power law, 45,]] [^142]

mimiviruses, x,]] 10,]] 11,]] 41,]] 42,]]

proofreading, 22,]] [^43]

182–84,]] 187,]] [^189]

protein, xii,]] 6,]] 10,]] 12–14,]] 23,]] 25–28,]]

MOI, [^85]

32,]] 33,]] 39,]] 42,]] 45,]] 83,]] 86,]] 87,]] 94,]] 96,]]

mutagenesis, 54,]] 73,]] [^74]

109,]] 114,]] 117,]] 118,]] 156,]] 161,]] 162,]]

mutation, x,]] 4,]] 32,]] 34,]] 35,]] 43–55,]]

176–78,]] 180–84,]] 186,]] 188,]] [^189]

58,]] 60,]] 61,]] 64,]] 67–76,]] 78–83,]]

_φ_ X174, 11,]] 12,]] [^161]

85–90,]] 105,]] 108,]] 109,]] 112,]] 114,]]

156,]] 159,]] 161,]] 169,]] 171,]] 173–76,]]

Q _β_, 33,]] [^34]

194,]] 195,]] 197,]] 198,]] [^200]

quasispecies, x]], 44,]] 45,]] 47–49,]] 51,]]

mutation rate, x,]] 4,]] 43,]] 44–46,]]

52,]] 54,]] 58,]] 64,]] 77–80,]] 105,]] 112,]]

49–55,]] 78,]] 79,]] 81,]] 82,]] 88–90,]]

114,]] 195,]] 197,]] 199,]] [^200]

105,]] [^198]

random drift, [^45]

NCLDV, [^42]

recombination, 68,]] [^86]

neutral mutations, 85,]] 88,]] [^156]

Red Queen, 63,]] 66,]] [^67]

neutral network, 62,]] 78,]] 84,]] 87–89]]

replication, 4,]] 10,]] 12–14,]] 21–25,]]

Novella, Isabel S., 62,]] [^156]

32–37,]] 39,]] 40,]] 42–45,]] 47,]]

Nowak, Martin A., 100,]] 108–10,]]

51–53,]] 55,]] 58,]] 63,]] 67,]] 77,]] 78,]] 81,]]

114,]] 115,]] 199,]] [^200]

83,]] 86–89,]] 105,]] 109,]] 119,]] 160,]]

outbreak 7,]] 16,]] 119–23,]] 128–30,]]

174,]] 180,]] 182,]] 186,]] 191,]] 193,]]

139,]] 152,]] 154,]] 163–65]]

195,]] [^197]

replicator, xi,]] 23,]] 33,]] 35–41,]] 45,]] 50,]]

pandemic, ix,]] 4,]] 5,]] 98,]] 121,]] 122,]]

63,]] 64,]] 82,]] 90,]] 174,]] 175,]] 189,]]

124,]] 129,]] 140,]] 141,]] 147,]] 148,]] [^163]

190,]] 198,]] [^200]

**222**

Index

retrotransposon, 39,]] 117,]] 177,]] [^178]

software, ix,]] 19,]] 20,]] 23,]] 24,]] 32,]] 36,]]

retrovirus, xi,]] 14,]] 15,]] 95,]] 96,]] 117,]]

42,]] 43,]] 117,]] 191–96]]

178,]] 182,]] 187,]] [^196]

Solé, Ricard V., 52–54,]] 67,]] 68,]] 92,]]

ribosome,13,]] 14,]] 22,]] 23,]] 181,]] [^189]

99,]] 134,]] 197–200]]

RNA, x–xii,]] 5,]] 10,]] 12–15,]] 21,]] 23,]] 27,]]

spherical viruses, 25,]] 26,]] [^28]

28,]] 33–36,]] 38,]] 43,]] 44–46,]] 53–55,]]

Spiegelman, Sol, 33,]] 35,]] [^36]

56,]] 62,]] 68,]] 69,]] 71–74,]] 83,]] 84,]] 86,]]

spillover, 151,]] [^167]

87,]] 94–97,]] 102,]] 103,]] 108,]] 153,]]

stamping-machine, [^86]

176,]] 177,]] 179–83,]] 185,]] 186,]] 188,]]

survival of the flattest, 77–79,]]

189,]] 194,]] 197–99]]

81–83,]] [^85]

RNA polymerase, 21,]] 43,]] [^45]

Suttle, Curtis A., [^7], [^8]

RNA World, 181,]] 183,]] [^185]

symbiosis, 116,]] 117,]] [^119]

robustness, 61,]] 68,]] 82,]] 83,]] 85–89]]

rugged landscape, 60,]] [^62]

TEV, 74–77,]] 158,]] [^161]

ruggedness, 60,]] 68,]] 70,]] 73,]] 75,]]

TMV, 9,]] 12,]] 14,]] 27,]] [^28]

90,]] [^109]

trade-off, 156–62]]

transcription, 12,]] 14,]] 21,]] 22,]] 42,]]

Sanjuán, Rafael, xii,]] 43,]] 44,]] 71,]] 72,]]

93,]] [^94]

78,]] [^108]

translation, 13,]] 21,]] 22,]] 56,]] 57,]] 94,]]

Sardanyés, Josep, xii,]] 81,]] [^82]

183,]] 186,]] [^187]

satellite, 11,]] 12,]] 42,]] 182,]] [^183]

transposons, 38,]] 39,]] 117,]] 169,]] 177,]]

scale-free networks, 141–43,]] [^145]

178,]] [^187]

Schuster, Peter, xii,]] 44,]] 45,]] 47,]] 50,]]

transpovirons, [^42]

53,]] 54,]] 57,]] 78,]] 79,]] [^84]

Turing, Alan M., 19–21,]] [^196]

selection, 33,]] 34,]] 43–45,]] 47,]] 56,]] 70,]]

Turing machine, 20,]] 21,]] [^196]

77,]] 82,]] 83,]] 85–89,]] 118,]] 156,]] 158,]]

Turner, Paul E., xii,]] 156,]] [^158]

159,]] 169,]] 170,]] 180,]] 190,]] 194,]]

198,]] [^200]

self-assembly, x,]] 26,]] 27,]] 28,]]

Van Nimwegen, Eric, 78,]] [^85]

30–32

Villarreal, Luis P., 168,]] [^188]

selfishness, 37–39]]

viroids, 10,]] 38,]] 45,]] 46,]] 78,]] 79,]]

self-organization, x,]] [^33]

181–83

self-replication, 22,]] [^33]

virome, 3,8]]

sequence space, 56–58,]] 60,]] 62,]] 67,]]

virophage, 42,]] 182,]] [^183]

78,]] 84,]] [^85]

virosphere, 1,]] [^4], 6–10,]] 12–14,]] 16,]]

SINV, 156,]] [^159]

18,]] [^181]

SIR model, 126,]] [^163]

virulence, 39,]] 152,]] [^158]

SIS model, 125–31,]] 133–35,]] 137,]]

virus dynamics, 56,]] 60,]] 92,]] 94,]]

143,]] 146,]] [^163]

96,]] 98,]] 100,]] 102,]] 104,]] 106,]]

Index

**223**

108,]] 110,]] 112,]] 114,]] 116,]] 118,]]

Weitz, Joshua S., [^7], [^16]

170,]] [^190]

wild-type, 62,]] 64,]] 68,]] 69,]] 71,]] 72,]] 74,]]

virus factories, [^188]

76,]] [^162]

Von Neumann, John, 22–24,]] 31,]] 32,]]

Wilke, Claus O., 78,]] 87,]] [^89]

36,]] 37,]] 171,]] [^191]

Wright, Sewall, [^57]

VSV, 62–64,]] 67,]] 71,]] 72,]] 78,]] 156,]]

158,]] [^159]

zoonotic, 153,]] 166,]] [^167]

