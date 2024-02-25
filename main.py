import itertools
import math
import random


def to_array(tuple):
    arr = []
    for i in tuple:
        arr.append(i)
    return arr


def evaluate(state):
    middle = math.floor(len(state) / 2)
    # [1,2,3,4,5,6]
    left = 0
    right = 0
    for num in state[:middle]:
        left += num
    for next_num in state[middle + 1:]:
        right += next_num
    return abs(right - left)


def boat_brute_force(*items):
    items_arr = to_array(items)
    result = dict()
    for perm in itertools.permutations(items_arr):
        eval = evaluate(perm)
        hashable = tuple(perm)
        result[hashable] = eval
    return result


def boat_monte_carlo(*items):
    items_arr = to_array(items)
    result = dict()
    times_to_shuffle = math.floor(len(items_arr) / 2) + 1
    for i in range(1, times_to_shuffle):
        shuffled = items_arr.copy()
        random.shuffle(shuffled)
        shuffled_tuple = tuple(shuffled)
        try:
            result[shuffled_tuple] = 0
        except:
            continue
        eval = evaluate(shuffled)
        result[shuffled_tuple] = eval
    return result


def boat_heuristic(*items):
    items_arr = to_array(items)
    result = dict()
    quarter_arr = math.floor((math.factorial(len(items_arr)) / 2) / 2)
    index = 0
    for perm in itertools.permutations(items_arr):
        index += 1
        if index > quarter_arr:
            break
        hashable = tuple(perm)
        try:
            result[hashable] = 0
        except:
            continue
        eval = evaluate(perm)
        result[hashable] = eval
    items_arr.reverse()
    index = 0
    for perm in itertools.permutations(items_arr):
        index += 1
        if index > quarter_arr:
            break
        hashable = tuple(perm)
        try:
            result[hashable] = 0
        except:
            continue
        eval = evaluate(perm)
        result[hashable] = eval
    return result


if __name__ == "__main__":
    testing_array = []
    print(min(boat_brute_force(1000, 31, 2, 10, 12).values()))
    # print(boat_monte_carlo(12, 31, 521))
    print(min(boat_heuristic(1000, 31, 2, 10, 12).values()))

# {(12, 31, 521, 123): 80, (12, 31, 123, 521): 478, (12, 521, 31, 123): 410, (12, 521, 123, 31): 502, (12, 123, 31, 521): 386, (12, 123, 521, 31): 104, (31, 12, 521, 123): 80, (31, 12, 123, 521): 478, (31, 521, 12, 123): 429, (31, 521, 123, 12): 540, (31, 123, 12, 521): 367, (31, 123, 521, 12): 142, (521, 12, 31, 123): 410 |||, (521, 12, 123, 31): 502, (521, 31, 12, 123): 429, (521, 31, 123, 12): 540, (521, 123, 12, 31): 613, (521, 123, 31, 12): 632, (123, 12, 31, 521): 386, (123, 12, 521, 31): 104, (123, 31, 12, 521): 367, (123, 31, 521, 12): 142, (123, 521, 12, 31): 613, (123, 521, 31, 12): 632}


# 10
