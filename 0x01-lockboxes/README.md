## LockBoxes Problem

The problem:

```You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened.```

The approach:
- box[0] is unlocked, therefore have access to the keys in that box i.e, if it has keys for boxes 2, 4, and 5, then the boxes can be opened and acess to the keys in those boxes is granted,
- If all the keys are collected, are all boxes opened?
    * Stopping point: 
    - True - all boxes are open, therefore no more  key to be collected.
    - False - No more boxes to be opened with the collected keys.
- A key represents a box position/index.
