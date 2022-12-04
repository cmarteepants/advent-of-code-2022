def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    assignments = [[tuple(map(int, pair.split("-"))) for pair in assignment.split(",")] for assignment in data]
    assignment_sets = [[set(range(assignment[0], (assignment[1]+1))) if assignment[0] != assignment[1] else set([assignment[0]]) for assignment in assignment_pair] for assignment_pair in assignments]

    overlapping_assignments = 0

    for assignment_set in assignment_sets:
        if assignment_set[0].issubset(assignment_set[1]) or assignment_set[1].issubset(assignment_set[0]):
            overlapping_assignments += 1

    print(f"The number of fully overlapping assignments is {overlapping_assignments}")

    intersecting_assignments = 0
    for assignment_set in assignment_sets:
        if assignment_set[0].intersection(assignment_set[1]):
            intersecting_assignments += 1

    print(f"The number of intersecting assignments is {intersecting_assignments}")





    # print(assignments)
    # for assignment in assignments:
    #     ranges = [tuple(map(int, assignment_range.split("-"))) for assignment_range in assignment]
    #
    #     print(ranges)




if __name__ == "__main__":
    main()