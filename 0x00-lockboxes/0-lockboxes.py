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
    num_box = set(range(0, len(boxes)))
    num_keys = set(boxes[0])
    num_box_called = set({0})
    '''
    current box sublist index index box with closed key
    '''
    current_box = (num_keys - num_box_called).pop()
    num_box_called.add(current_box)
    try:
        num_keys.update(boxes[current_box])
    except:
        pass
    if len(num_box - num_box_called) == 0:
        return True
    else:
        return False
