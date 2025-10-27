"""
Mission API placeholder.
Eventually, this will let you define missions like:

from mission_api import Mission, send_to_backend

mission = Mission("Patrol Alpha", route=[(0,0), (10,0), (10,10)])
send_to_backend(mission)
"""

class Mission:
    def __init__(self, name, route=None):
        self.name = name
        self.route = route or []

    def __repr__(self):
        return f"<Mission name={self.name}, waypoints={len(self.route)}>"

def send_to_backend(mission: Mission):
    print(f"Sending mission '{mission.name}' with {len(mission.route)} waypoints...")

if __name__ == "__main__":
    test_mission = Mission("Patrol Alpha", route=[(0, 0), (10, 10), (20, 5)])
    print(test_mission)
    send_to_backend(test_mission)
