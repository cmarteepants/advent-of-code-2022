import textwrap


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    priority_rules = {}
    for i, ordinal in enumerate(range(ord('a'), ord('z') + 1), start=1):
        priority_rules[chr(ordinal)] = i
    for i, ordinal in enumerate(range(ord('A'), ord('Z') + 1), start=27):
        priority_rules[chr(ordinal)] = i

    rucksacks = [textwrap.wrap(rucksack, len(rucksack)//2) for rucksack in data]

    priorities = []
    for rucksack in rucksacks:
        common = set(rucksack[0]) & set(rucksack[1])
        for item in common:
            priorities.append(priority_rules[item])

    print(f"The sum of the priority items are {sum(priorities)}")

    new_priorities = []
    grouped_rucksacks = list(zip(*[iter(rucksacks)]*3))
    for rucksack_group in grouped_rucksacks:
        sets = []
        for rucksack in rucksack_group:
            items = set(rucksack[0]) | set(rucksack[1])
            sets.append(items)
        common = sets[0] & sets[1] & sets[2]
        for i in common:
            new_priorities.append(priority_rules[i])

    print(f"The sum of the item types that corresponds to the badges of each three-Elf group are {sum(new_priorities)}")


if __name__ == "__main__":
    main()
