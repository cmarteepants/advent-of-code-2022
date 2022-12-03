def main():
    with open("input.txt") as f:
        data = f.read()

    elf_meals = data.split("\n\n")
    elf_calories = sorted([sum(map(int, elf.splitlines())) for elf in elf_meals])

    # part 1
    print(f"The highest number of calories an elf is carrying is: {elf_calories[-1]}")
    # part 2
    print(f"The sum of calories that the top three elves are carrying is {sum(elf_calories[-3:])}")
