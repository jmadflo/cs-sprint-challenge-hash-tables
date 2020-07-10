def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    records = {}
    for index, num in enumerate(weights):
        if limit - num in records:
            return (index, records[limit - num])
        else:
            records[num] = index
    return None
