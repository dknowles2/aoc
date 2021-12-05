#!/usr/bin/python

def path_to_points(path):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    cur_x = cur_y = step = 0
    points = {}
    for seg in path.split(','):
        dx, dy = directions[seg[0]]
        for _ in range(int(seg[1:])):
            cur_x += dx
            cur_y += dy
            step += 1
            if (cur_x, cur_y) not in points:
                points[(cur_x, cur_y)] = step
    return points


def min_dist(wire1, wire2):
    points1, points2 = path_to_points(wire1), path_to_points(wire2)
    intersections = set(points1.keys()) & set(points2.keys())
    intersections.discard((0, 0))
    return min(abs(x) + abs(y) for x, y in intersections)


def min_path(wire1, wire2):
    points1, points2 = path_to_points(wire1), path_to_points(wire2)
    intersections = set(points1.keys()) & set(points2.keys())
    intersections.discard((0, 0))
    return min(points1[p] + points2[p] for p in intersections)


def run_tests():
    wire1 = 'R8,U5,L5,D3'
    wire2 = 'U7,R6,D4,L4'
    print(wire1)
    print(wire2)
    print('min dist', min_dist(wire1, wire2))
    print('min path', min_path(wire1, wire2))
    print()

    wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
    print(wire1)
    print(wire2)
    print('min dist', min_dist(wire1, wire2))
    print('min path', min_path(wire1, wire2))
    print()

    wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    print(wire1)
    print(wire2)
    print('min dist', min_dist(wire1, wire2))
    print('min path', min_path(wire1, wire2))
    print()


def exe():
    with open('input/day3') as f:
        wire1, wire2 = f.readlines()
        print('min dist', min_dist(wire1, wire2))
        print('min path', min_path(wire1, wire2))


def main():
    run_tests()
    exe()


if __name__ == '__main__':
    main()
