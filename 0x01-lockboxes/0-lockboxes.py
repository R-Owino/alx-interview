#!/usr/bin/python3
'''
Function that solves the lockboxes problem
'''


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes(list of lists): the boxes to check keys for
    
    Returns:
        True if all boxes can be opened, otherwise false
    """
    box_0 = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in box_0 and key != box_id:
                box_0.append(key)
    
    if len(box_0) == len(boxes):
        return True
    return False

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))