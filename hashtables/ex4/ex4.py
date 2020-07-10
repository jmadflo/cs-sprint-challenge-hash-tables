def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    nums = dict(zip(a, [True] * len(a)))
    result = []
    for num in a:
        if -num in nums and num > 0:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
