class GeoModel:

    def  __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        if not self.latitude: return "Missing latitude."
        if not self.longitude: return "Missing longitude."
        if float(self.latitude) < -90 or float(self.latitude) > 90: return "Latitude must be between -90 and 90."
        if float(self.longitude) < -180 or float(self.longitude) > 180: return "Longitude must be between -180 and 180."
        return None