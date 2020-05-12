Technical Interview Best Practices
Brief summary of everything covered in SPD 1.01 in summer 2019.

Communication
Restate the problem
Ask clarifying questions
State your assumptions
Think out loud
Brainstorm solutions
Explain your rationale
Discuss tradeoffs
Suggest improvements

Problem Solving Strategy
Generate reasonable test inputs
Understand the problem – solve it by hand
Simplify the problem if needed
Find a pattern in your solution
Make a plan – write pseudocode
Follow your plan – write real code
Check your work – test your code

Test Cases and Debugging
Good or normal input
Edge case input
Step through code carefully to find and fix any bugs

Syntax Errors and Coding Conventions
Is the code syntactically correct or does it have syntax errors?
Does the code use the language and standard library correctly and effectively?
Does the code adhere to or violate coding conventions of the language?

Algorithm Complexity Analysis
Avoid redundant or repeated work
Analyze time complexity (operations)
Analyze space complexity (memory)
Define all variables used in analysis
Use this analysis to generate ideas for improved solutions

Whiteboard Usage
Use entire whiteboard effectively in an organized way
Draw diagrams that represent data structures effectively
Run test cases by stepping through code carefully and keep track of variable values

Toolbelt of Ideas for Brainstorming Solutions
Although seemingly unremarkable in appearance, Batman's utility belt is one of his most important tools in fighting crime crushing technical interviews. Each of its ten pouches or cylinders contains various tools integral to Batman's war on crime successful job search. Through the years, Batman has added many tools to his belt to accommodate various crime-fighting scenarios programming problems. Elements of the utility belt include, but are not limited to, the following:
Use for loop
Iterate over array values – for value in array
Iterate over array indexes – for index in range(len(array))
Iterate over indexes and values – for index, value in enumerate(array)
Iterate over array from front to back – show above
Iterate over array from back to front – for value in reversed(array)
Use while loop
Iterate over one array with two indexes – while i < len(a) and j < len(a)
Iterate over two arrays with two indexes – while i < len(a) and j < len(b)
Iterate until unusual stopping condition – while left <= right  (binary search)
Traverse linked list or tree nodes – while node is not None
Sort array values
In ascending order – array.sort()
In descending order – array.sort(reverse=True)
By mutating original array – array.sort()
By making a copy of array – sorted(array)
Search for value in array
Linear search – array can be in arbitrary order
Binary search – array must be in sorted order
Use data properties
Calculate mean or median to help narrow down which part of input to consider
Use recursion
Helpful to avoid repetitive nested logic
Identify subproblem that can be solved in a similar way, call function recursively
Try using divide-and-conquer strategy – solve subproblems, then combine results
Create a new data structure
Create a set with array values as elements – unique elements, fast lookup
Create a dictionary with array values as keys and indexes as values – fast lookup
Create a linked list with array values as elements – avoid slow array shifting
Create a binary search tree with array values as elements – kept in sorted order
Create a min/max heap with array values as elements – find min/max value fast
Decide whether to create entire data structure of all elements right away or to put elements in one at a time as they encountered
Generate more ideas and add them here!


Simplify, Simplify, Simplify!
Come up with at least 3 different ways to simplify the problem given below, then share your ideas with other students and borrow their ideas that you think would be helpful.
Create a Plan
Then create a plan for how you’ll solve the problem from the absolute simplest possible version as step 1, then remove one of the simplifications in step 2, then another in step 3, and finally remove all simplifications so you are solving the full version of the problem in your final step. DO NOT attempt to solve the full version of the problem right away.
The goal of this activity is to break the problem down into smaller, simpler steps to create an incremental path from the simplest version to the full problem. Practicing this will help you during real interviews, especially when you hear a new problem and think to yourself “OMG this is hard!” – This is to develop a strategy for how to move past those thoughts.


Write your answers to these in your notebook:
What clarifying questions would you ask?
What reasonable assumptions could you state?
What are 2-3 ways you can simplify the problem?
Brainstorm 2-3 ways to approach the problem.
Choose one idea and write pseudocode for it.

Activity
Choose a problem below at the appropriate difficulty level for your own experience.
What are edge case inputs that could be challenging to handle in your solution?
How can you simplify the problem to ensure you make progress and don’t get stuck?


Warmup
Grab a whiteboard and marker.
Draw a diagram of a binary search tree containing 6 strings inserted in the following order: 'red', 'orange', 'yellow', 'green', 'blue', 'purple'.
Label the root node and its references that link to its children. Label all leaf nodes.
Compare your diagram to 2 other students’ diagrams. Are your structures identical?

Activity
Write your answers to these in your notebook:
Choose a problem below at the appropriate difficulty level for your own experience.
Draw a diagram of a normal or simple input case that you should attempt to solve first.
What are edge case inputs that could be more challenging to handle in your solution? Write these down (or draw a small diagram) to identify them and not worry about them.
Can you break the problem down into smaller pieces and solve each part separately?
Can you simplify any of the parts so you can make progress and then expand it later?

Binary Tree Problems
Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
Given a binary search tree containing integers and a target integer, come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.
Given a binary tree containing numbers, find the maximum sum path (the path that has the largest sum of node values). The path may start and end at any node in the tree.
Let’s say a binary tree is "superbalanced" if the difference between the depths of any two leaf nodes is at most one. Write a function to check if a binary tree is "superbalanced".

Fully solve at least two of the above binary tree problems in real working code. Use your idea sketches and pseudocode, type it in your code editor, run some test cases, and debug your code so it works correctly. Implement at least one solution for 2 or more of the problems above.

Warmup (Round 1)
Find a partner to pair with, plus a whiteboard and at least 2 markers of different colors
Choose a problem below you’re familiar with and fairly confident you can solve in 15 min
Try to apply the best practices we’ve covered in a 15-minute mock interview then swap

Reflect on the best practices below and write down which you want to better utilize in round 2.
Tips & Best Practices
Communication: Restate the problem; Ask clarifying questions; State your assumptions
Problem Solving: Break the problem into parts; Simplify each part; Brainstorm solutions
Programming: Make a plan (write pseudocode); Focus on normal input, not edge cases
Testing & Debugging: Step through each line of code carefully to find and fix any bugs
Complexity Analysis: Analyze time and space complexity; Define all variables you use

Activity (Round 2)
Find a new partner for round 2, plus a whiteboard and 2+ markers of different colors
Choose a new problem below (or a problem that you’re less familiar with) and not that confident you can solve in 30 minutes
Better utilize the best practices we’ve covered in a 30-minute mock interview then swap


Tips & Best Practices
Programming: Make a plan (write pseudocode); Focus on normal input, not edge cases
Testing & Debugging: Step through each line of code carefully to find and fix any bugs

Recursion Activity
Let’s practice a couple of more challenging technical interview problems that involve recursion.
Find a new partner, plus a large whiteboard and at least 2 markers of different colors
Choose a problem below at an appropriate challenge level for you to solve in 30 minutes
Try to apply the best practices we’ve covered in a 30-minute mock interview, then swap


