#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear: O(n) --> Loops based on n

b) Polynomial O(n^2) --> Loops until it's equal to

c) Linear O(n) --> Recursion calling on itself

## Exercise II
Determine the value of f in a way that breaks the least amount of eggs (least amount of attempts).
- Where n = stories in building 
- Where f is the highest floor where eggs are not broken when dropped.
- If at or above floor f, egg breaks, else egg does not break.

This could be a binary search runtime: O(log(n))

How to solve this:
- Go to floor n/2 (the middle of the building). 
- Drop the egg. 
- If egg breaks, you the move halfway down the building (halfway between the current floor and the bottom). 
- If it didn't break, you'd move halfway up the building (halfway between the current floor and the top). 
- Then repeat over and over each time eliminating half the options until you find the exact floor the egg doesn't break.

Pseudocode:
The Function
    Move to n//2
        if f == 1
            return 1
        drop egg
        if egg breaks
            repeat at new floor determined by current floor//2 (lower half)
        if egg not broken
            repeat at new floor determined by n-current floor//2 (upper half)



