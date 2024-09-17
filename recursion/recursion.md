# Python - Recursion #
___

Recursion is a fundamental programming concept where a function calls itself in order to solve a problem. This technique breaks down a complex problem into smaller and more manageable sub-problems of the same type. In Python, recursion is implemented by defining a function that makes one or more calls to itself within its own body.

### Components of Recursion ###

As we discussed before Recursion is a technique where a function calls itself. Here for understanding recursion, it's required to know its key components. Following are the primary components of the recursion −

* Base Case
* Recursive Case

#### Base Case ####

The Base case is a fundamental concept in recursion, if serving as the condition under which a recursive function stops calling itself. It is essential for preventing infinite recursion and subsequent stack overflow errors.

The base case provides a direct solution to the simplest instance of the problem ensuring that each recursive call gets closer to this terminating condition.

The most popular example of recursion is calculation of factorial. Mathematically factorial is defined as −
>n! = n x (n-1)!

It can be seen that we use factorial itself to define factorial. Hence this is a fit case to write a recursive function. Let us expand above definition for calculation of factorial value of 5.
>5! = 5 x 4!<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 x 4 x 3!<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 x 4 x 3 x 2!<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 x 4 x 3 x 2 x 1!<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 x 4 x 3 x 2 x 1<br>
>= 120

While we can perform this calculation using a loop, its recursive function involves successively calling it by decrementing the number till it reaches 1.

#### Recursive Case ####
The recursive case is the part of a recursive function where the function calls itself to solve a smaller or simpler instance of the same problem. This mechanism allows a complex problem to be broken down into more manageable sub-problems where each them is a smaller version of the original problem.

The recursive case is essential for progressing towards the base case, ensuring that the recursion will eventually terminate.