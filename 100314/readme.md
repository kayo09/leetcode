**Block Placement Queries**
_______________________

There exsists an infinite number line, with its origin at 0 and extending
towards the positive x-axis.

queries->
    -2-D array 
    -Two types:
        -type 1: queriese[i]=[1,x]
            note:Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query isaasked.
        
        -type 2: queries[i]=[2,x,sz]
            note: Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.

To do: 
    -return a bool array results, where results[i] is **true** if you can place
the block specified in the ith query of type 2 and false otherwise 
