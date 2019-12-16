#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  This will run in O(n) time. As the input value for N grows linearly, so will the time complexity.


b)  This will run in O(n^2) time. Both the outer and inner loop will grow as N increases, and nested loops mean that this algorithm will have quadratic time.


c) This will run in O(n) time. The function recursively calls itself and decrements the bunnies by one after each call. 

## Exercise II

The best approach here is to use binary search to find floor F, this will take log n time. First, we search floor n/2 and check if an egg thrown from there will crack. if it does, we are too high and we search from the floor we're currently on divided by 2. if the egg doesnt crack, we know that everything beneath is good and we need to find our cieling so we move to the halfway point between our previous step and where we currently are.

We are constantly searching and cutting our bound in half at each search. This will minimize the number of eggs we have to crack to find our safe point.


A bad approach would be for floor in range(floors), throw an egg off and check if it cracks up until we find a floor where the egg cracks when dropped.
