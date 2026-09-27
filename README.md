# LeetCode 306 - Additive Number

## Problem Statement

Given a string containing only digits, determine whether it can form an additive sequence.

An additive sequence is a sequence where every number is the sum of the previous two numbers.

## Example 1

### Input

```text
num = "112358"
```

### Output

```text
true
```

### Explanation

`1, 1, 2, 3, 5, 8` is an additive sequence.

## Example 2

### Input

```text
num = "199100199"
```

### Output

```text
true
```

### Explanation

`1, 99, 100, 199` is an additive sequence.

## Approach

Try every possible pair of first and second numbers. Then repeatedly calculate their sum and check whether the resulting number appears next in the string.

Leading zeros are not allowed unless the number itself is `0`.

## Algorithm

1. Choose the first number.
2. Choose the second number.
3. Calculate their sum.
4. Check whether the sum matches the next part of the string.
5. Continue using the previous two numbers.
6. Return `True` if the complete string forms an additive sequence.
7. Otherwise, try another pair.

## Time Complexity

`O(n^3)`

## Space Complexity

`O(n)`

## Key Concepts

* String Manipulation
* Backtracking
* Number Formation
* Sequence Validation

## Language

Python

## LeetCode Details

* **Problem:** 306
* **Title:** Additive Number
* **Difficulty:** Medium

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
