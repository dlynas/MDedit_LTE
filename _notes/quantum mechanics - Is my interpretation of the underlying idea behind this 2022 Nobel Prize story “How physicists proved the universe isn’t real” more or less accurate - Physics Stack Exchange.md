---
source: physics.stackexchange.com
url: https://physics.stackexchange.com/questions/733500/is-my-interpretation-of-the-underlying-idea-behind-this-2022-nobel-prize-story
---

First, it's important to clarify two definitions.

1.  The [principle of locality](https://en.wikipedia.org/wiki/Principle_of_locality) loosely says that interactions occur at individual points in space. If you say that one charged particle at a point x exerts a force on a second charged particle at a point y, then that would be a _non-local interaction_. On the other hand, if you say that one charged particle at x creates a distortion in the electromagnetic field which permeates all of space and that a particle at y feels a force due to that electric field, then you are describing a _local interaction_. If a theory obeys the principle of locality, it is called local.
2.  [Realism](https://en.wikipedia.org/wiki/Principle_of_locality#Local_realism) is the idea that the observable quantities of a system take definite values at each moment in time. Classical (non-statistical) physics is unambiguously real, insofar as the observables of a system (position, energy, momentum, angular momentum, etc) all have definite values at all times. Most formulations of quantum mechanics (with exceptions like [de Broglie-Bohm](https://en.wikipedia.org/wiki/De_Broglie%E2%80%93Bohm_theory)) dispense with this principle and in a generic state of the system, the observables exist in superposition and do not take definite values.

With those two definitions out of the way, one may ask whether it is possible that nature can be described by a theory which features both of these properties - such theories are called _locally real_. Classical mechanics is an example of a locally real theory, but it is known to disagree with experiment. The standard formulation of quantum mechanics is _not_ locally real, but perhaps there is a locally real theory which underlies it, or at least produces the same predictions.

The [Bell theorem(s)](https://en.wikipedia.org/wiki/Bell%27s_theorem) answer this question in the negative. Given some fairly reasonable assumptions, it tells us that **if** a theory is locally real, then there exist experiments in which they **must** produce predictions which unambiguously disagree with the predictions made by quantum theory. If such an experiment were performed and the results _agree_ with the predictions of quantum theory, then it follows that _whatever_ theory ultimately describes nature **cannot** be locally real.

The [2022 Nobel prize in Physics](https://www.nobelprize.org/prizes/physics/2022/press-release/) was awarded to Clauser, Aspect, and Zeilinger for respectively performing the first practical Bell-type experiment, improving the experiment by closing a potential loophole, and developing more sophisticated experiments which utilize and illustrate the properties of the so-called _entangled states_ which are the origin of the disagreement with any locally real predictions.

> Is that more or less accurate?

I would say that your definition of "real" isn't quite right. One way to think about it is that _realism_ means that when you make a measurement of a system, you are simply revealing the definite values of observable quantities which already existed before the measurement. If you measure the energy of a particle to be 10 eV, then its energy of the particle was 10 eV _before you measured it_, and your measurement simply revealed that fact.

On the other hand, the standard formulation of quantum mechanics would say that the energy of the particle was (generally) _indefinite_ before your measurement, and only assumed a definite value when the measurement was performed. Whether this is due to some kind of wavefunction collapse, entanglement between the system and the measurement device, or something else is not important; the point is that the energy of the particle did not exist as a definite value before the measurement took place.

> So some immeasurably tiny interaction must occur between all particles. Yet, we can conduct the double slit experiment, so there is some threshold at which the interaction is so small that two distinct behaviors occur.

Yes, that's true. Entanglement is not binary; the degree of entanglement of a system is quantified by the [entanglement entropy](https://en.wikipedia.org/wiki/Entropy_of_entanglement), and can take a continuous range of values between totally unentangled and maximally entangled. Tiny interactions between particles produce correspondingly small degrees of entanglement, which may be able to be safely ignored. On the other hand, ostensibly small interactions may cause entangled states to [decohere](https://en.wikipedia.org/wiki/Quantum_decoherence), so they can be very important in understanding how a particular system behaves.

---

> So, since the wave function collapse occurs from the perspective of each respective observer (observer not being a human, but rather an individual particle), and the entanglement can occur as some non-binary gradient space of "degrees", to use your term, could we then carry out a double-slit experiment wherein the result is equally non-binary?

In a sense, yes. Let's imagine that we perform a double slit experiment with electrons as per [Feynman's thought experiment](https://www.feynmanlectures.caltech.edu/III_01.html) (sec. 1-6, "Watching the Electrons"). We can label the slits A and B, and we can imagine directing a laser toward slit B in such a way that an electron going through slit B will scatter a photon into a detector, thus confirming which route it took to the screen.

If the photon energy is high, then the wavelength of the photon will be short. You can imagine that the photon itself is correspondingly small, like a bullet. In this case, a scattered photon almost certainly means an electron going through slit B.

On the other hand, if the photon energy is low, then the wavelength of the photon will be large and you can imagine the photon to resemble a big, fuzzy ball. In this case, the photon can't resolve the difference between an electron going through slit B and one going through slit A; either one is just as likely to scatter.

One loose way to think about entanglement between an electron and the measuring device is that it quantifies how much information the state of the detector gives you about the state of the photon. If the interaction between the two is such that knowing the state of the detector is enough to completely specify the state of the electron, then they are maximally entangled and have high entanglement entropy. On the other hand, if knowing the state of the detector tells you nothing whatsoever about the state of the electron, then they are completely unentangled.

In a general case, our double slit experiment will be somewhere in between these two extremes, so we will not see a perfectly pure interference pattern (as we'd expect with no electron/detector entanglement) nor will we see two broad bright spots and no interference pattern (as we'd expect with complete electron/detector entanglement). Feynman's thought experiment is very well explained in the link above, so I would encourage you to read it thoroughly to get more information and intuition than I am providing here (though he does not frame the issue precisely in terms of entanglement).
