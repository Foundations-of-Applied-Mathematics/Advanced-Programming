This folder contains information from the competitive coding class taught by Andrew Carr and Mitchell Probst during the BYU Fall 2017 semester. There is a [Powerpoints](https://github.com/Foundations-of-Applied-Mathematics/Advanced-Programming/tree/master/2017_FallMaterials/Powerpoints) directory that contains the slides shown to classmembers, which we did regularly at the beginning of the semester. However, as the problems became more unwieldly, we switched to working on the problems in class together.

There is also a folder called [PythonFiles](https://github.com/Foundations-of-Applied-Mathematics/Advanced-Programming/tree/master/2017_FallMaterials/PythonFiles) which contain a few specific functions written to help explain some of the Learn and Gos (this is the name used for each topic, *Learn* first together with us as a class, then *Go* and code it up yourself. Last, there is a [BrainTeasers]() folder which contain the brain teasers we asked the students.

# Administration
The class was setup with everything being run through Hackerrank using an e-mail account we created for this purpose:<br>
Username: acme.coding.competition@gmail.com<br>
Password: Ask your ACME professor.

Future classes may choose to re-use the same Learn and Gos, because hackerrank will allow you to modify start/end times of a contest, however we found no way to erase the leaderboard, so it will become critical to closely track each user and their performance on the Learn and Gos.

The class had several core components: Discussing Problem Solving Techniques, Learn and Gos, In-class Blitzes, Interviewing Skills, and Language Projects.

# Problem Solving

We opened the class by asking them to solve several common brain teasers that they might get in an interview class. Some of them are located in the [BrainTeasers]() folder, several people may have seen these problems before, we did not make them up ourselves.

Following the brain teasers, we spent a day teaching the Problem Solving techniques found in [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?ie=UTF8&qid=1515691822&sr=8-1&keywords=cracking+the+coding+interview), a text by Gayle Laakmaan McDowell. The techniques are:

1. Look for BUD (Bottlenecks, Unnecessary Work, Duplication)
2. DIY (Do it Yourself, How would you solve it in real life?)
3. Simplify and Generalize (Start With Extra Assumptions Initially, Then Adapt)
4. Base Case and Build (Start Small and Build Up)
5. Data Structure Brainstorm (Will The Right Structure Simplify The Problem?)

# Learn and Gos (LaG)

We had 10 Learn and Gos throughout the semester, each with its own theme, such as focusing on strings, trees, recursion, grids, ...
Every Learn and Go has at least one tutorial problem that is meant to be solved together in class, then at least 3 other problems varying in difficulty to appease to both novice programmers and experienced ones. For grading purposes, we asked the students to complete at least one non-tutorial problem to receive full credit for a Learn and Go. Each problem is considered *binary* just like the Coding Competitions, you either solve a problem or you do not. No partial credit was given. The number of points they are given reflects how difficult we felt the problems were. Students needed 10 points for full credit (which equates to one non-tutorial problem).

Each problem built by us is available through an [admin page](https://www.hackerrank.com/administration/challenges) on Hackerrank.

## [Learn and Go 0](https://www.hackerrank.com/learn-and-go-0) - Python Essentials

This is a tutorial set meant to help students learn how to use Python, as we assume many juniors take this course and they are not expected to know much about Python. Each problem in this Learn and Go was built by us:

1. Learn and Go 0-0: Lists (This problem introduces how to read input from hackerrank and using Python lists)
2. Learn and Go 0-1: Simple Array Sum (This problem exists in Hackerrank but we re-created it removing the helper code)
3. Learn and Go 0-2: Compare The Triplets (Also already exists but helper code removed)
4. Learn and Go 0-3: Kangaroo (We changed the constraints of this Hackerrank problem to require a Mathematical Solution)

## [Learn and Go 1](https://www.hackerrank.com/learn-and-go-1) - Data Structures

This Learn and Go contains numerous tutorial problems to ease students into competitive coding. Each problem can be solved very simply by just using the correct data structure.

1. Migratory Birds
2. DefaultDict Tutorial
3. Collections.deque()
4. Left Rotation
5. No Idea!
6. Learn and Go 1-2: Sets (This problem was taken from the Rocky Mountain Regional Contest in 2015)
7. Components in a graph (Uses something called disjoint sets)

## [Learn and Go 2](https://www.hackerrank.com/learn-and-go-2) - Parsing

This topic is still full of mostly simple problems, meant to ask students to begin learning how to make multiple pieces of information work together.

1. Zipped! (Very important tutorial because NumPy isn't available in CC, Zipped! teaches you how to iterate over the columns of nested lists)
2. Learn and Go 2-1: Vending Machine 2 (Taken from the 2017 Winter CC hosted at BYU from Pariveda, a great problem for simple maps).
3. Counting Valleys
4. Missing Numbers

## [Learn and Go 3](https://www.hackerrank.com/learn-and-go-3) - Number Theory

This Learn and Go has several problems involving primes, or other mathematical topics that almost should be solved on paper before trying to code up solutions.

1. Project Euler #3: Largest prime factor
2. Project Euler #2: Even Fibonacci numbers
3. Project Euler #16: Power digit sum
4. Leonardo's Prime Factors (lots of students struggled on this one)
5. Beautiful Days at the Movies
6. Learn and Go 3-3: Mixed Bases (A problem asking students to write code to change from one base to another, including a base 1)

## [Learn and Go 4](https://www.hackerrank.com/learn-and-go-4) - Strings

Python can do some neat things in String Manipulation, and strings show up often. We introduce students to some string problems.

1. CamelCase
2. Mars Exploration
3. Super Reduced String
4. Sherlock and the Valid String
5. Learn and Go 4-3: 4th Grade (Problem taken from Pariveda's 2017 BYU Winter CC)*

\* Although many coders warn about eval() in Python, it can be used to solve this problem in one-line.

## [Learn and Go 5](https://www.hackerrank.com/learn-and-go-5) - Abstract

This section was reserved for some of the more abstract CS concepts that ACME students likely haven't been exposed to yet. Things like Bit manipulation or implementing grid searching.

1. Lonely Integer
2. Flipping bits
3. New Year Chaose
4. KnightL on a Chessboard

## [Learn and Go 6](https://www.hackerrank.com/learn-and-go-6) - Grids

Coding Competitions and other interviews often give problems for grids.  Students saw an example that uses color and walks through what a grid challenge is doing. Talking about boundary checking, storing results, and possibly recursing through a grid were all mentioned.

1. Grid Challenge
2. Marking Peaks (An interview question Andrew got from a company. The challenge is to identify "peaks" in a grid where the grid is a representation of a topological map. A position is a peak if and only if it is strictly greater than adjacent points (N/S/E/W are considered adjacent).
3. Connected Cells in a Grid
4. The Grid Search
5. Castle on the Grid

## [Learn and Go 7](https://www.hackerrank.com/learn-and-go-7) - Recursion

We added this Learn and Go that wasn't originally planned because we felt that many students in our class weren't comfortable with recursion. We taught the difference between head recursion and tail recursion.

1. Fancy Printing (A toy recursion problem Andrew built to show the class the difference between head and tail recursion)
2. Tree: Height of a Binary Tree
3. Fibonacci Modifies

## [Learn and Go 8](https://www.hackerrank.com/learn-and-go-8) - BFS/DFS

We saved searching until after ACME students had completed their lab on Breadth-first Search, hoping that we could reinforce principles that they learned in class. Most students struggled on this challenge and only a handful actually completed one of the problems listed here.

1. Snakes and Ladders: The Quickest Way Up
2. Breadth First Search: Shortest Reach
3. PacMan - DFS
4. PacMan - BFS

## [Learn and Go 9](https://www.hackerrank.com/learn-and-go-9) - Dynamic Programming

Many people have a hard time wrapping their heads around Dynamic Programming conceptually. We felt that having a Learn and Go would help students understand its usefulness. Similar to LaG 8, most students did not complete any problem, despite the instruction we gave.

1. The Longeset Common Subsequence
2. Stock Maximize
3. Bricks Game
4. The Longest Increasing Subsequence
5. The Maximum Subarray
6. Knapsack

# Blitzes

Throughout the semester we held numerous coding competitions to try and practice techniques taught in the Learn and Gos as well as to simulate the environment of the Coding Competition (No googling, only using standard docs as references, up to 3 working together but limited to a single computer).  We had 7 blitzes throughout the semester. The problems are not necessarily in order form easy to hard, as we wanted the students to have to practice assessing the difficulty level of a problem. Hackerrank lets you hide the difficulty of the challenges.

## [Blitz0-2](www.hackerrank.com/blitz0-2) - From LaG 0 to LaG 2

Contained several problems, most of which were incredibly simple, the hardest is Balanced Brackets, another common interview question.

1. Breaking the Records
2. CamelCase
3. Balanced Brackets
4. Designer PDF Viewer
5. The Hurdle Race

## [Blitz3-5](www.hackerrank.com/blitz3-5) - From LaG 3 to LaG 5

This blitz came after LaG 5, which included a grid problem in order to assess if the students had any previous exposure to grids, we intentionally put that problem first, along with the other hard problem second to try and trip students up who just try and go down the list one at a time.

1. Marking Peaks (See Learn and Go 6)
2. Separate the Numbers
3. Word Order
4. "Holy" Numbers (Another trick problem, the problem never states that *N* is an integer, just that it is a number. So one test case has a decimal number like 13.46, if students cast it to an int, or round it, they get a run time error, or if they leave it as a string and check each "digit", they will attempt to check ".", which may result in a KeyError)
5. Sum vs XOR

## [Blitz #3](www.hackerrank.com/blitz-3) - Pre-ACM Blitz

The ACM was pushed back a few weeks, so we ended up doing another blitz that was full of problems, lots of primarily simple ones.

1. Summing the N series
2. Equalize the Array
3. Sock Merchant
4. Special Multiple
5. Project Euler #28: Number spiral diagonals
6. Game of THrones - I
7. Athlete Sort

## [Blitz #4](www.hackerrank.com/blitz-4) - Pre-ACM Blitz

We held this blitz on the Thursday before the ACM. Once again loaded with problems in order to encourage the students to spend more time assessing problems and carefully choosing which ones to tackle first. Because of that, many of the challenges have simple solutions

1. Ice Cream Parlor
2. Two Strings
3. Maximizing XOR
4. The Time in Words
5. Weighted Uniform Strings
6. Encryption
7. Missing Numbers
8. Beautiful Triplets
9. Minimum Distances

## [InterviewBlitz](www.hackerrank.com/interviewblitz) - Tackling Interview Questions

This blitz is primarily composed of problems from Cracking the Coding Interview, meant to show students how they can apply their competitive coding skills to interview settings.

1. One Away CtCI (This problem is written in the CtCI book, but we made it a Hackerrank problem)
2. Cycle Detection
3. Is This a Binary Search Tree?
4. Bob and Ben

## [BlitzHard](www.hackerrank.com/blitzhard) - Actual ACM Problems

One of the items of feedback our students gave us post competition was that most of our competitions had "easy" problems, usually composed of one trick and being finished. The students asked for harder problems that reflected 'real ACM problems' during a blitz. Our choice of making them easier was primarily because our blitzes are only one hour long, but we decided to take the easiest problems from the [2017 ICPC](https://icpc.baylor.edu/worldfinals/problems) and put them into a blitz.

1. Need for Speed (solved using binary search)
2. Posterize (solved using Dynamic Programming)
3. Secret Chamber at Mount Rushmore (solved using BFS)

## [SpeedBlitz](www.hackerrank.com/speedblitz) - Coding Quickly

On the last day of class we chose to implement a Speed Blitz. We included what we thought were 12 of the easiest problems from the entire semester, primarily the tutorial problems from our Learn and Gos, but a few other easy ones. We started at the top of the list and began each problem at the same time, and ranked how fast students were able to code solutions to these problems. We wanted to spend ~5 minutes on each problem in order to do many, but probably spent about ~7-8 on each instead, so we only got through 7 or 8 of them.

1. Learn and Go 0-0: Lists (See LaG 0)
2. Learn and Go 1-2: Sets (See LaG 1)
3. Zipped! (See LaG 2)
4. Project Euler #3: Largest prime factor (see LaG 3)
5. CamelCase (See Blitz0-2 or LaG 4)
6. Lonely Integer (See LaG 5)
7. Learn and Go 2-1: Vending Machine 2 (See LaG 2)
8. Left Rotation (See LaG 1)
9. Counting Valleys (See LaG 2)
10. Designer PDF Viewer (See Blitz0-2)
11. "Holy" Numbers (See Blitz3-5)
12. Sum vs XOR (See Blitz3-5)

# Interviewing Skills

We spent two days teaching students about interview skills as suggested from Cracking the Coding Interview. One of the best insights can be found in the [powerpoint](https://github.com/Foundations-of-Applied-Mathematics/Advanced-Programming/blob/master/2017_FallMaterials/Powerpoints/Behavioral%20Components%20to%20a%20Technical%20Interview.pptx) for that day, creating a matrix for answers to common interview questions related to work you have done. We also spent two class days letting students practice technical interviews with us:

1. N time n space array
2. Delete a node in a singly-linked list
3. Khan number, incrementing a number where each digit is stored in a list eg. 4753 = \[4, 7, 5, 3]
4. Determine if a number is a Power of 10
5. Find if a cycle exists in a singly linked list
6. Taking the union of two lists

# Language Projects

Many students in ACME have little to no experience coding, probably did not enjoy CS 142, but now can code well in Python. We wanted to introduce them to some of the more popular languages they may see, and just introduce them to the concept of applying techniques they learned in competitive coding to other languages.  For the class we taught them four different languages. Each language was supposed to have a day of instruction, and a full day of students working, but due to the fact this year's ACM Coding Competition happened on November 4th, we lost several class days. Instead we gave them 25-30 minutes of instruction and then let them work on their own.
The languages covered was JavaScript, C++, Clojure, and R.

For most language projects we expected them to solve easy challenges that they had already seen at the beginning of the semester.

1. Solve Me First
2. Compare the Triplets
3. Migratory Birds

For R, we gave them a chance to play around with the datasets and showed them how to plot data and quickly return the *moments* of the data.

# References:

* [ICPC Previous Problems](https://icpc.baylor.edu/worldfinals/problems)
* [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?ie=UTF8&qid=1515782388&sr=8-1&keywords=cracking+the+coding+interview)
* [2016 Rocky Mountain Regional ACM Contest](http://org.coloradomesa.edu/~wmacevoy/rmrc/2016/index.html)
* [Lucid's 2016 Fall Coding Competition](https://www.hackerrank.com/contests/lccc2016/challenges)
* [Lucid's Repository for 2016 Fall Competition](https://github.com/lucidsoftware/coding-challenge-2016f)
* [Lucid's 2017 Fall Coding Competition](https://www.hackerrank.com/lucid-2017)
* [Lucid's Repository for 2017 Fall Competition](https://github.com/lucidsoftware/lucid-programming-competition-2017)
* [Pariveda's 2017 Winter Coding Competition](https://www.hackerrank.com/byu-winter-2017-programming-competition-by-pariveda)

\* None of these links in this readme are maintained by us, and as such are subject to being broken in the future.
