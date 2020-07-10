# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    queries_set = dict(zip(queries, [True] * len(queries)))
    result = []

    for file in files:
        current = -1
        while True:
            if file[current] == '/':
                if file[current + 1:] in queries_set:
                    result.append(file)
                break
            current -= 1

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
