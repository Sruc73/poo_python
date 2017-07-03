import json
import math

class Agent():
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180

class Zone:
    MIN_LONGITUDE_DEGREES = - 180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # Degrees of longitude
    HEIGHT_DEGREES = 1 # Degrees of latitude
    ZONES = []

    def initialize_zones(self):
        for latitude in range(self.MIN_LATITUDE_DEGREES, self.MAX_LATITUDE_DEGREES, self.HEIGHT_DEGREES):
            for longitude in range(self.MIN_LONGITUDE_DEGREES, self.MAX_LONGITUDE_DEGREES, self.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, 1)
                top_right_corner = Position(longitude + self.WIDTH_DEGREES, 1 + self.WIDTH_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)

    def  __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0


def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)

        print(agent.position.longitude)

main()
