def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    round_survivors = {0:set(arrays[0])}
    current = 1
    while current < len(arrays):
        # print(current)
        round_survivors[current] = set()
        for num in arrays[current]:
            if num in round_survivors[current - 1]:
                round_survivors[current].add(num)
        current += 1
    return list(round_survivors[current - 1])


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
