#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ordered_route = []
    routes = {}
    # Your code here
    for ticket in tickets:
        routes[ticket.source] = ticket.destination
    source = 'NONE'
    destination = ''
    while len(ordered_route) < length:
        destination = routes[source]
        ordered_route.append(destination)
        source = destination
    return ordered_route
