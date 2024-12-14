import numpy as np
from scipy.ndimage import label


def plantGarden(in1):
    """returns a detailed plot for each plant.
    For each plant, an array of all the separate
    plots"""
    A = np.array([[x for x in y] for y in in1.splitlines()], dtype=str)
    plantset = set(A.flatten())
    garden = []
    detailedgarden = []
    for plant in plantset:
        garden.append(np.array(A == plant, dtype=int))
    for planttype in garden:
        labels, _ = label(planttype)
        plantsections = set(labels.flatten())
        plantsections.remove(0)
        plots = []
        for plant in plantsections:
            plots.append(np.array(labels == plant, dtype=int))
        detailedgarden.append((planttype, plots))

    return detailedgarden


def perimeter(arr):
    """only counts perimeter above and below.
    to get perimeter of the whole shape,
    get sum of perimeter(arr) + perimeter(arr.T)"""
    count = 0
    x, y = arr.shape
    for i in range(x):
        for j in range(y):
            if arr[i][j]:
                # look up
                if i == 0:
                    count += 1
                elif not arr[i - 1][j]:
                    count += 1
                else:
                    pass
                # look down
                if i == x - 1:
                    count += 1
                elif not arr[i + 1][j]:
                    count += 1
                else:
                    pass

    return count


def getPerimeter(arr):
    return perimeter(arr) + perimeter(arr.T)


def sides(arr):
    """only gets sides above and below.
    to get total number of sides,
    get sum of sides(arr) + sides(arr.T)"""
    count = 0
    x, y = arr.shape
    for i in range(x):
        upOn = False
        downOn = False
        for j in range(y):
            if arr[i][j]:
                # look up
                if i == 0:
                    if not upOn:
                        count += 1
                        upOn = True
                elif not arr[i - 1][j]:
                    if not upOn:
                        count += 1
                        upOn = True
                else:
                    upOn = False
                # look down
                if i == x - 1:
                    if not downOn:
                        count += 1
                        downOn = True
                elif not arr[i + 1][j]:
                    if not downOn:
                        count += 1
                        downOn = True
                else:
                    downOn = False
            else:
                upOn = False
                downOn = False
    return count


def getSides(arr):
    return sides(arr) + sides(arr.T)


def part1():
    with open("/Users/kartheek/Development/AdventOfCode/AOC2024/Day12/input", "r") as fp:
        blah = fp.read()
    garden = plantGarden(blah)
    summa = 0
    for plant in garden:
        for plot in plant[1]:
            summa += getPerimeter(plot) * plot.flatten().sum()
    return summa


def part2():
    with open("/Users/kartheek/Development/AdventOfCode/AOC2024/Day12/input", "r") as fp:
        blah = fp.read()
    garden = plantGarden(blah)
    summa = 0
    for plant in garden:
        for plot in plant[1]:
            summa += getSides(plot) * plot.flatten().sum()
    return summa


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")