
def find_start_of_packet_marker(string, num_chars):

    count = 0
    for _ in string:
        count += 1

        # check if the last n characters are all different and return the count
        if count >= num_chars and len(set(string[count - num_chars:count])) == num_chars:
            return count


def main():
    with open("input.txt") as f:
        string = f.read()

    result = find_start_of_packet_marker(string, 4)
    print(result)

    result = find_start_of_packet_marker(string, 14)
    print(result)


if __name__ == "__main__":
    main()


