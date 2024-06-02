about_neows = """Asteroids - NeoWs

NeoWs (Near Earth Object Web Service) is a RESTful web service for
near earth Asteroid information. With NeoWs a user can: search
for Asteroids based on their closest approach date to Earth, lookup a
specific Asteroid with its NASA JPL small body id, as well as browse
the overall data-set.

Data-set: All the data is from the NASA JPL 
Asteroid team (http://neo.jpl.nasa.gov/).

This API is maintained by SpaceRocks Team: David Greenfield, Arezu 
Sarvestani, Jason English and Peter Baunach."""


neows_keys = [
    "is_potentially_hazardous_asteroid",
    "neo_reference_id",
    "id",
    "absolute_magnitude_h",
    "nasa_jpl_url",
    "orbital_data",
    "name",
    "links",
    "name_limited",
    "is_sentry_object",
    "estimated_diameter",
    "designation",
    "close_approach_data"
]


Open_Science_Data_Repository_Public_APIb = """Experiments, Missions, Payloads, Hardware, Vehicles, 
Subjects, Biospecimens

Format:
Experiments, Missions, Payloads, Hardware, Vehicles, Subjects, and Biospecimens follow the 
same API format. The "All" call returns a list of all objects within that data type, while 
the "Single" call returns an expanded version of a specific object. The endpoint for any 
single object can be selected from the "All" call. Some objects may include links to other 
objects within the API, such as a vehicle within a mission.

Experiment:
All: https://osdr.nasa.gov/geode-py/ws/api/experiments
Single: https://osdr.nasa.gov/geode-py/ws/api/experiment/ + identifier
Mission:
All: https://osdr.nasa.gov/geode-py/ws/api/missions
Single: https://osdr.nasa.gov/geode-py/ws/api/mission/ + identifier
Payload:
All: https://osdr.nasa.gov/geode-py/ws/api/payloads
Single: https://osdr.nasa.gov/geode-py/ws/api/payload/ + identifier
Hardware:
All: https://osdr.nasa.gov/geode-py/ws/api/hardware
Single: https://osdr.nasa.gov/geode-py/ws/api/hardware/ + identifier
Vehicle:
All: https://osdr.nasa.gov/geode-py/ws/api/vehicles
Single: https://osdr.nasa.gov/geode-py/ws/api/vehicle/ + identifier
Subject:
All: https://osdr.nasa.gov/geode-py/ws/api/subjects
Single: https://osdr.nasa.gov/geode-py/ws/api/subject/ + identifier
Biospecimen:
All: https://osdr.nasa.gov/geode-py/ws/api/biospecimens
Single: https://osdr.nasa.gov/geode-py/ws/api/biospecimen/ + identifier

*Examples:
Single Mission Call
https://osdr.nasa.gov/geode-py/ws/api/mission/SpaceX-12"""

