---
source: github.com
url: https://github.com/nomyx/Nomyx
---

[![Build Status](https://camo.githubusercontent.com/67f41d01f47643262a51853e07101f5ad7bc62a48cc4968d78e8af27cd692f5a/68747470733a2f2f7472617669732d63692e6f72672f636475706f6e742f4e6f6d79782e706e673f6272616e63683d6d6173746572)](https://travis-ci.org/cdupont/Nomyx) [![Hackage](https://camo.githubusercontent.com/2b2132e7b0aa59716cdb559a25ab4c66638f1d1c583f3abd64e1d6a13f5ab1fd/68747470733a2f2f627564756562612e636f6d2f6861636b6167652f4e6f6d7978)](https://hackage.haskell.org/package/Nomyx)

## Nomyx

A [Nomic game](https://en.wikipedia.org/wiki/Nomic) in Haskell

Nomyx is a strange game where you can change the rules of the game, while playing! In fact, changing the rules is the goal of the game. Changing a rule is considered as a move. Of course even that can be changed! In this game, the player can enter new rules in a dedicated language, modify existing ones, thus changing completely the behaviour of the game through time.

More info on this [blog post](https://www.corentindupont.info/blog/posts/Programming/2014-09-23-first-Nomyx-tutorial.html)

## Installation

First install Haskell Stack:

```
$ sudo apt-get update
$ curl -sSL https://get.haskellstack.org/ | sh
```

To install from the GitHub repo:

```
$ git clone --recursive https://github.com/nomyx/Nomyx.git
$ cd Nomyx/nomyx-server
$ stack setup
$ stack install
```

## Execution

Launch with the command:

```
$ stack exec nomyx-server
```

and follow the instructions. You may connect using a web browser to the provided address. You can play with the GUI and propose some rules!

## Cloud deploy

```
docker build -t cdupont2/nomyx .
docker push cdupont2/nomyx
ecs-cli compose down
ecs-cli compose up
```

## Troubleshooting

See the [issues](https://github.com/cdupont/Nomyx/issues) for known bugs.

Run tests with:
