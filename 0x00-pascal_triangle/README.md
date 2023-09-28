## Pascal's Triangle problem

- Pascal’s triangle is a pattern of the triangle which is based on nCr.
- Generally, it takes this format:

```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
```

- To solve the problem, I created a function `def pascal_triangle(n):` that uses a while loop to compute each row based on the previous row's values, following the pattern of summing the two adjacent values.
