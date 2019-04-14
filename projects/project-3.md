---
layout: project
type: project
image: images/scrabble-300x300.jpg
title: Scrabble Assistant
permalink: projects/scrabble
# All dates must be YYYY-MM-DD format!
date: 2017-08-20
labels:
  - C++
  - GitHub
summary: A hash table implementation for a dictionary data structure. Implementation is then used to create a tool which assists in finding solutions to tiled word games (such as Scrabble). Provided is a written analysis of the performance of the hash table.
---

As review for data structures, I redid a school project on hash tables. Only the public methods were provided as part of the declaration; Along with a partner, we wrote our own private fields and members. We implemented a separate chaining hash table where one of the constructors allow the user to specify a maximum load factor and the other should uses a sensible default value (e.g. 0.75). All operations on our HashTable (other than getKeys and getItems) run in O(1) average time. We used an array of statically-allocated vector objects to represent the buckets of your HashTable. Statically-allocated vectors are easier to use and less error-prone, especially when stored in an array. 

With a working HashTable, we wrote the Scrabble Assistant. The  application was designed in two parts: a ScrabbleAssistant class (which does all of the interesting work) and a main function (which provides the interface that allows the end user to interact with that object).

The work of the ScrabbleAssistant can be broken into the following parts:
'
1. Keeping track of which words are legal.
2. Finding the anagrams of a particular word.
3. Finding the “power set” of a string.
4. Eliminating duplicate strings in a list.
5. Finding all of the legal plays given a string containing the player’s tiles.
'

My role in the team of two was to design the hash table as well as make choices for the implementation. We initially set out to use arrays, however, I chose to change our plan to involve vectors. The speed properties of vector methods allowed for our functions to run in an appropriate run time. Overall, I gained a better sense of the hash table data structure. Additionally, this project allowed for a fun, active refreshing of building classes on C++.

We ran a peformance analysis on our hash table implementation. The results are shown below:

<img class="ui image" src="../images/graph.png">

The graph shows that our HashTable works well when given a good hashing algorithm and that it can work poorly when given a bad hashing algorithm. Part of my role in the group was determining why. I concluded the reason was more clashes. With a bad hashing functions, you would get more collusions. Collusions slow down the speed of the algorithm. Visualizing our hash table properties taught me clear ways to communicate results, an important part of computer science discourse.

<a href="https://www.cs.swarthmore.edu/~zpalmer/cs35/f16/labs/08/"><i class="large file text icon "></i>Original Lab Page</a>


