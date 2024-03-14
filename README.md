# Algorithms
# encontrar_sublista_suma_mayor

This Python script finds the contiguous sublist within a list that has the largest sum of elements.

## How it Works

The script works by iterating through the input list and maintaining a record of the sublist with the largest sum found so far. It follows these logical steps:

1. **Initialization of Variables:** Several variables are initialized to keep track of the largest sum found (`largest_sum`), the starting and ending indices of the sublist with the largest sum (`start_sublist` and `end_sublist`), the current sum of the sublist being considered (`current_sum`), and the starting index of the best sublist found so far (`best_sublist_start`).

2. **Iterating through the List:** The script loops through each element of the list, tracking both the value and the index.

3. **Updating the Current Sum:** For each element in the list, its value is added to `current_sum`, updating the sum of the current sublist being considered.

4. **Comparison with Largest Sum:** After updating `current_sum`, the script compares it with `largest_sum`. If `current_sum` is greater than `largest_sum`, it updates `largest_sum`, `start_sublist`, and `end_sublist` to reflect the new largest sum and its corresponding sublist indices.

5. **Resetting Current Sum:** If `current_sum` becomes negative during the iteration, it indicates that the current sublist does not contribute positively to the overall sum. Thus, `current_sum` is reset to 0, and `best_sublist_start` is updated to the index of the next element.

6. **Returning the Sublist with the Largest Sum:** Once the iteration through the list is complete, the script returns the sublist with the largest sum found.

## Usage

To use the script, simply call the `find_largest_sum_sublist()` function and pass the list of integers as an argument. For example:

```python
result =encontrar_sublista_suma_mayor([1, -3, 2, 1, -1])
print("Sublist with the largest sum:", result)
```

This will output:

```
Sublist with the largest sum: [2, 1]
```
