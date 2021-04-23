#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    or not:
    if can be opened: return True
    else: return False
    """
    numBoxes = len(boxes)
    if numBoxes == 0:
        return false
    openBoxes = [1]
    keys = []
    for i in range(1, numBoxes):
        openBoxes.append(0)
    for box in boxes[0]:
        if box >= numBoxes:
            continue
        keys.append(box)
        openBoxes[box] = 1
    posBox = 1
    while posBox < numBoxes:
        if posBox in keys:
            for key in boxes[posBox]:
                if key >= numBoxes:
                    continue
                keys.append(key)
                if openBoxes[key] == 0 and key < posBox:
                    openBoxes[key] = 1
                    posBox = key - 1
                    break
                openBoxes[key] = 1
        posBox += 1
    if 0 in openBoxes:
        return False
    return True
