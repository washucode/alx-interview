#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """

    Args:
        boxes ([array]): array of boxes with keys

    Returns:
        [boolean]: [Return true or false]
    """
    boxes_opened = [0]
    boxes_keys = boxes[0]

    while boxes_keys:
        key = boxes_keys.pop()

        if 0 <= key <= len(boxes) - 1 and key not in boxes_opened:
            boxes_opened.append(key)
            boxes_keys.extend(boxes[key])

    return len(boxes_opened) == len(boxes)
