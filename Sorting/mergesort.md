## Merge Sort

### Divide and Conquer Based

It is a recursive sort of order ```n*log(n)```
The basic idea is to split the collection into smaller groups
by halving it until the groups only have one element or no
elements (which are both entirely sorted groups).

Then merge the groups back together so that their elements are
in order.

#### Task
Write a function to sort a collection of integers using merge sort.

The merge sort algorithm has two parts:
```
• A sort function, and
• A merge function
```

#### Pseudocode
```
function mergesort(m)
    var list left, right, result
    if length(m) <= 1
        return m
    else
        var middle = length(m) // 2
        for each x in m up to middle - 1
            add x to left
        for each x in m at and after middle
            add x to right
        left = mergesort(left)
        right = mergesort(right)

        if last(left) <= first(right)
            append right to left
            return left
        result = merge(left, right)
        return result

function merge(left, right)
    var list result
    while length(left) > 0 and length(right) > 0
        if first(left) <= first(right)
            append first(left) to result
            left = rest(left)
        else
            append first(right) to result
            right = rest(right)
    if length(left) > 0
        append rest(left) to result
    if length(right) > 0
        append rest(right) to result
    return result

```











