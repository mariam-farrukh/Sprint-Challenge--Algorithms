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

This could be a binary search 
Runtime: O(log(n))

How to solve this:
* Go to floor n/2 (the middle of the building). 
* Drop the egg. 
* If egg breaks, you the move halfway down the building (halfway between the current floor and the bottom). 
* If it didn't break, you'd move halfway up the building (halfway between the current floor and the top). 
* Then repeat over and over each time eliminating half the options until you find the exact floor the egg doesn't break.

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


This could also be a linear search: O(n)
How to solve:
* Person goes to each floor (starting from the first one), drops an egg.
* If the egg doesn't break, move to the next floor.
* If the egg breaks, stop and then determine the floor below the current is the last floor where eggs do not break.

Pseudocode:
The Function
    Move to n = 1
    if egg does not break, then n = n+1
    if egg breaks at n, then f = n


** This linear search may be a better strategy because only one egg is broken, while in the binary example, multiple eggs are broken until the floor is determined. The binary example saves time though, but the question is asking for the least amount of eggs that are broken.

