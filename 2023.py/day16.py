from collections import deque
import utils
from typing import TypeAlias

Coord: TypeAlias = tuple[int, int]
Direction: TypeAlias = tuple[int, int]
Node: TypeAlias = tuple[Coord, Direction]


def change_direction(current_coord: Coord, direction: Direction) -> Node:
    return (current_coord[0] + direction[0], current_coord[1] + direction[1]), direction


def expand_explore(grid: utils.Grid, current: Node) -> list[Node]:
    current_coord, current_direction = current

    if current_coord in grid:
        match grid[current_coord]:
            case '.':
                return [change_direction(current_coord, current_direction)]
            case '/':
                match utils.DELTA_TO_NESW[current_direction]:
                    case 'N':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['E'])]
                    case 'S':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['W'])]
                    case 'E':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['N'])]
                    case 'W':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['S'])]
            case '\\':
                match utils.DELTA_TO_NESW[current_direction]:
                    case 'N':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['W'])]
                    case 'S':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['E'])]
                    case 'E':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['S'])]
                    case 'W':
                        return [change_direction(current_coord, utils.CHAR_TO_DELTA['N'])]
            case '|':
                if utils.DELTA_TO_NESW[current_direction] in ['N', 'S']:
                    return [change_direction(current_coord, current_direction)]
                else:
                    return [
                        change_direction(current_coord, utils.CHAR_TO_DELTA['N']),
                        change_direction(current_coord, utils.CHAR_TO_DELTA['S'])
                    ]
            case '-':
                if utils.DELTA_TO_NESW[current_direction] in ['W', 'E']:
                    return [change_direction(current_coord, current_direction)]
                else:
                    return [
                        change_direction(current_coord, utils.CHAR_TO_DELTA['W']),
                        change_direction(current_coord, utils.CHAR_TO_DELTA['E'])
                    ]
    else:
        return []
    

def simulate_beam(grid: utils.Grid, initial: Node) -> int:
    explore = deque([initial])
    energized = set()

    while explore:
        current = explore.pop()
        energized.add(current)
        explore.extend(filter(lambda x: x not in energized and x[0] in grid, expand_explore(grid, current)))

    return len(set([i[0] for i in energized]))


def main():
    with open("input16.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [[i for i in line] for line in lines]
    grid = utils.Grid(lines)

    # part 1
    print(simulate_beam(grid, ((0, 0), utils.CHAR_TO_DELTA['R'])))
      
    # part 2
    max_energized = 0
    for i in range(grid.rows):
        max_energized = max(max_energized, simulate_beam(grid, ((i, 0), utils.CHAR_TO_DELTA['R'])))
        max_energized = max(max_energized, simulate_beam(grid, ((i, grid.rows - 1), utils.CHAR_TO_DELTA['L'])))

    for i in range(grid.cols):
        max_energized = max(max_energized, simulate_beam(grid, ((0, i), utils.CHAR_TO_DELTA['D'])))
        max_energized = max(max_energized, simulate_beam(grid, ((grid.cols - 1, i), utils.CHAR_TO_DELTA['U'])))

    print(max_energized)
    return

main()
