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
    best = dict()
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
    dic_brute = boat_brute_force(4, 3, 2, 1, 1, 3, 20, 42, 15)
    dic_heuristic = boat_heuristic(4, 3, 2, 1, 1, 3, 20, 42, 15)
    dic_random = boat_monte_carlo(4, 3, 2, 1, 1, 3, 20, 42, 15)
    best_brute = min(dic_brute.values())
    best_heur = min(dic_heuristic.values())
    best_rand = min(dic_random.values())
    print(f"brute: {best_brute}, heuristic: {best_heur}, random: {best_rand}")

# 10
