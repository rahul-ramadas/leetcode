import collections


class Solution:

    def find_itinerary(self, current_airport, destinations, ticket_used, num_tickets_left, itinerary):
        if not num_tickets_left:
            return True

        current_stop_index = len(itinerary) - num_tickets_left
        for i, destination in enumerate(destinations[current_airport]):
            if ticket_used[current_airport][i]:
                continue

            ticket_used[current_airport][i] = True
            itinerary[current_stop_index] = destination
            if self.find_itinerary(destination, destinations, ticket_used, num_tickets_left - 1, itinerary):
                return True
            ticket_used[current_airport][i] = False
            itinerary[current_stop_index] = None

        return False

    def findItinerary(self, tickets):
        destinations = collections.defaultdict(list)

        for ticket in tickets:
            destinations[ticket[0]].append(ticket[1])

        for source in destinations.keys():
            destinations[source].sort()

        ticket_used = { source: [False] * len(destinations[source]) for source in destinations.keys()}

        itinerary = [None] * (len(tickets) + 1)
        itinerary[0] = "JFK"
        self.find_itinerary("JFK", destinations, ticket_used, len(tickets), itinerary)
        return itinerary
