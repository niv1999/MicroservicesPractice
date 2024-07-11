from geopy.distance import geodesic
from utils.open_areas import open_areas

class DecisionLogic:

    def launch_missile(self, attack_location):
        for open_area in open_areas:
            if self.is_100_meter_proximity(attack_location, open_area):
                return False
        return True

    def is_100_meter_proximity(self, geo1, geo2):
        tuple1 = (geo1.latitude, geo1.longitude)
        tuple2 = (geo2.latitude, geo2.longitude)
        distance = geodesic(tuple1, tuple2).meters
        return distance <= 100