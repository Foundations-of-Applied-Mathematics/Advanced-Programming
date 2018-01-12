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


# Learn and Gos

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

Throughout the semester we held numerous coding competitions to try and practice techniques taught in the Learn and Gos as well as to simulate the environment of the Coding Competition (No googling, only using standard docs as references, up to 3 working together but limited to a single computer).  We had 7 blitzes throughout the semester.
