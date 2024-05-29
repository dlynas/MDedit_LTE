---
source: github.com
url: https://github.com/AB-CE/abce
---

abcEconomics: the Agent-Based Computational Economy platform that makes modeling easier //////////////////////////////////////////////////////////////////////////////////////

abcEconomics is a Python based modeling platform for economic simulations. abcEconomics comes with standard functions to simulations of trade, production and consumption. The modeler can concentrate on implementing the logic and decisions of an agents; abcEconomics takes care of all exchange of goods and production and consumption.

[![[ec1285e546c3a96f7e725d781ea8024b_MD5.svg]]](https://zenodo.org/badge/latestdoi/4157636)

[![[b39d903eb65d3b8c57e347c090d4cd35_MD5.svg]]](https://github.com/ab-ce/abce/actions?query=workflow%3Abuild)

[![[df202bb301dbe1e8f5c94c0e467f94fa_MD5.svg]]](https://pypi.python.org/pypi/abcEconomics)

[![[5988c036215da6af63f80eb21c1b487a_MD5.svg]]](https://abceconomics.readthedocs.io/)

[![[97391e4f62b787d5832f19877393aa92_MD5]]](https://raw.githubusercontent.com/AB-CE/abce/master/docs/cheesegrater.png)

In abcEconomics, goods have the physical properties of goods in reality in the sense that if agent A gives a good to agent B, then - unlike information - agent B receives the good and agent B does not have the good anymore. The ownership and transformations (production or consumption) of goods are automatically handled by the platform.

abcEconomics models are programmed in standard Python, stock functions of agents can be inherited from archetype classes (Firm or Household). The only not-so-standard Python is that agents are executed in parallel by the Simulation class (in start.py).

abcEconomics allows the modeler to program agents as ordinary Python class-objects, but run the simulation on a multi-core/processor computer. It takes no effort or intervention from the modeler to run the simulation on a multi-core system. The speed advantages of using abcEconomics with multi-processes enabled. abcEconomics are typically only observed for 10000 agents and more. Below, it might be slower than pure python implementation. abcEconomics supports pypy3, which is approximately 10 times faster than CPython.

abcEconomics is a scheduler and a set of agent classes. According to the schedule the simulation class calls - each sub-round - agents to execute some actions. Each agent executes these actions using some of the build-in functions, such as trade, production and consumption of abcEconomics. The agents can use the full set of commands of the Python general purpose language.

The audience of abcEconomics are economists that want to model agent-based models of trade and production.

abcEconomics does support an accounting framework for financial simulations: abcFinance ([https://github.com/ab-ce/abcFinance](https://github.com/ab-ce/abcFinance)).

abcEconomics runs on macOS, Windows, and Linux. abcEconomics runs 10x faster on pypy!

Install with:

```
pip3 install abcEconomics
```

The documentation is here:

> [http://abce.readthedocs.io/](http://abce.readthedocs.io/)

A code example is here:

> [Jupyter Tutorial](https://github.com/AB-CE/examples/tree/master/examples/jupyter_tutorial)

More code examples are here:

[https://github.com/AB-CE/examples](https://github.com/AB-CE/examples)
