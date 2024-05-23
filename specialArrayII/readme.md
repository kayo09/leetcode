Special Array II 
____________________

nums-> 
    1-D array 
queries->
    2-D array 

special->
    if the parity of adjacent cells are different

To do:
    -check if subarray is special or not  
    -subarray is based on elements of queries such that: $$0<len(queries_i)<=2  $$


e.g 
```
queries=[[0,2],
         [0,3]]
``****`

Algorithm: 
    -Traverse the queries 2-D array and get the respective postions of start and end for the subarray 
    -Traverse the subarray to check for special condition