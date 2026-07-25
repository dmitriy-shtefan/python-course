class Bicycle:
    def travel_time(self):
        return "30 хвилин"


class Metro:
    def travel_time(self):
        return "15 хвилин"


class Walking:
    def travel_time(self):
        return "50 хвилин"


routes = [Bicycle(), Metro(), Walking()]

for route in routes:
    print(route.travel_time())
