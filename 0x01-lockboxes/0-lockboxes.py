#!/usr/bin/python3
"""
0-lockboxes.py contains a function canUnlockAll that takes a list of list as input and returns a true
or false value if all the boxes(sub lists) can be unlocked using the keys in them.
"""


def canUnlockAll(boxes):
    """
    Determines if a list of boxes with keys in them can be all be opened, each box may contains keys, the
    first box is always opened.
    """
    keys = boxes[0]
    visited = {}

    for key in keys:
        if key in visited:
            continue
        keys.extend((boxes[key]))
        visited[key] = 1

    keys = set(keys)
    boxes = set([item for box in boxes for item in box])

    return True if len(keys) == len(boxes) else False
