**Sum of Digit Differences of All Pairs**
_____________________________________

nums->
    -1-D array
    -Positive integers where all integers have the same number of **digits**

Note->
    $$
    nums_i-nums_i+1=diff_i\\
    nums_i-nums_i+2=diff_i\\
    while\:\:i<=len(nums)$$

e.g
```
nums=[13,23,12]
Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
```