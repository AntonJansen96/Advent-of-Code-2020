#!/bin/python3

import numpy as np

instructions = open('input.txt').read().split('\n')

example = ['F10', 'N3', 'F7', 'R90', 'F11']

def process1(instruction, x, y, direction):
    char, value = instruction[0], int(instruction[1:])

    # NORTH
    if char == 'N':
        y += value
    
    # SOUTH
    elif char == 'S':
        y -= value

    # EAST
    elif char == 'E':
        x += value

    # WEST
    elif char == 'W':
        x -= value

    # FORWARD
    elif char == 'F':
        if direction == 0 or direction == 360:
            y += value
    
        elif direction == 180:
            y -= value

        elif direction == 90:
            x += value

        elif direction == 270:
            x -= value

    # RIGHT
    elif char == 'L':
        direction = (direction - value) % 360
    
    elif char == 'R':
        direction = (direction + value) % 360

    return x, y, direction

def process2(instruction, x, y, f, g):
    char, value = instruction[0], int(instruction[1:])

    # MOVE WAYPOINT NORTH
    if char == 'N':
        f += value
    
    # MOVE WAYPOINT SOUTH
    elif char == 'S':
        f -= value

    # MOVE WAYPOINT EAST
    elif char == 'E':
        g += value

    # MOVE WAYPOINT WEST
    elif char == 'W':
        g -= value

    # FORWARD
    elif char == 'F':
        x_old = x
        y_old = y
        x += value * (f - x)
        y += value * (g - y)
        f += x - x_old
        g += y - y_old

    # RIGHT
    if char == 'R':
        f_relative = f - x
        g_relative = g - y
        # print(f_relative, g_relative)

        f_relative, g_relative = f_relative * np.cos(np.deg2rad(value)) - g_relative * np.sin(np.deg2rad(value)), f_relative * np.sin(np.deg2rad(value)) + g_relative * np.cos(np.deg2rad(value))

        f = x + f_relative
        g = y + g_relative

    # LEFT
    if char == 'L':
        f_relative = f - x
        g_relative = g - y
        # print(f_relative, g_relative)

        f_relative, g_relative = g_relative * np.cos(np.deg2rad(value)) - g_relative * np.sin(np.deg2rad(value)), - f_relative * np.sin(np.deg2rad(value)) + f_relative * np.cos(np.deg2rad(value))

        f = x + f_relative
        g = y + g_relative

    return x, y, f, g

def manhattan(x, y):
    return abs(x) + abs(y)

x = 0
y = 0
f = 1       # waypoint is 1 unit north
g = 10      # and 10 units east of ship

for instruction in instructions:
    print(instruction)
    x, y, f, g = process2(instruction, x, y, f, g)
    print('ship = (%s, %s), waypoint = (%s, %s)' % (x, y, f, g))

print(manhattan(x, y))
