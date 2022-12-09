from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Point:
    """ Point class """
    x: int
    y: int


class Grid:
    """ Represents a grid of trees heights """

    def __init__(self, grid_rows: list) -> None:
        """ Expects data in the format... [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], ...] """
        self.rows: list[list[int]] = grid_rows
        self.cols = list(zip(*self.rows))
        self._width = len(self.cols)
        self._height = len(self.rows)
        self.size = self._width * self._height

    def height_at_point(self, point: Point) -> int:
        return self.rows[point.y][point.x]

    def is_visible(self, point: Point) -> bool:
        """ A tree is visible if it is on any edge,
        or if there are no taller trees in the same row or column. """
        visible = False

        # check if it's on an edge
        if point.x == 0 or point.x == self._width - 1:
            return True
        if point.y == 0 or point.y == self._height - 1:
            return True

        value = self.height_at_point(point)
        # Check if taller than any other tree in the row. If so, it is visible.
        if value > max(self.rows[point.y][0:point.x]): return True
        if value > max(self.rows[point.y][point.x + 1:]): return True

        # Now check the column.
        if value > max(self.cols[point.x][0:point.y]): return True
        if value > max(self.cols[point.x][point.y + 1:]): return True

        return visible

    def get_hidden_trees(self) -> set[Point]:
        """ Returns all locations where trees are hidden from view. """
        hidden_trees: set[Point] = set()

        # process across then down
        for y in range(self._width):
            for x in range(self._height):
                point = Point(x, y)
                if not self.is_visible(point):
                    hidden_trees.add(point)

        return hidden_trees

    def get_scenic_scores(self) -> list[int]:
        """ Returns the scenic scores for every tree in the grid """
        scenic_scores = []

        # process across then down
        for y in range(self._width):
            for x in range(self._height):
                point = Point(x, y)
                score = self.get_scenic_score_for_point(point)
                scenic_scores.append(score)

        return scenic_scores

    def get_scenic_score_for_point(self, point: Point) -> int:
        """ Scenic score is given by product of viewing distance in each of the four directions.
        Viewing distance is given by how far away is the nearest tree that is at least as tall as this one.
        Viewing distance is always 0 when looking out from an edge. """

        this_value = self.height_at_point(point)

        # Use generators, since we will just keep getting the next tree
        # until we reach a tree at least as tall. In theory, this is slightly more efficient than lists.
        left = (x for x in reversed(self.rows[point.y][0:point.x]))
        right = (x for x in self.rows[point.y][point.x + 1:])
        up = (y for y in reversed(self.cols[point.x][0:point.y]))
        down = (y for y in self.cols[point.x][point.y + 1:])

        viewing_distances = []  # store our four distances
        for direction in (left, right, up, down):
            distance = 0  # if we're on the edge, this will be the final score.
            for value in direction:
                if value < this_value:
                    distance += 1
                else:  # this tree is at least as tall as our tree. We can't see past it.
                    distance += 1  # This is the last tree we can see
                    break  # exit inner for

            viewing_distances.append(distance)

        return math.prod(viewing_distances)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                + f"(size={self.size}, rows={len(self.rows)}, cols={len(self.cols)})")


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    rows = [[int(x) for x in row] for row in data]
    grid = Grid(rows)
    print(grid)

    # Part 1 - How many visible trees?
    hidden_trees = grid.get_hidden_trees()
    print("Part 1:")
    print(f"Number of hidden trees={len(hidden_trees)}")
    print(f"Number of visible trees={grid.size - len(hidden_trees)}")

    # Part 1 - How many visible trees?
    print("\nPart 2:")
    scenic_scores = grid.get_scenic_scores()
    print(f"Highest score={max(scenic_scores)}")


if __name__ == "__main__":
    main()