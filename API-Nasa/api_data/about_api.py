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

about_open_science_data_repository_public_api = """

 --  ****  (About: Open Science Data Repository Public API )  --

NASA OSDR provides a RESTful Application Programming Interface (API) to its full-text 
search, data file retrieval, and metadata retrieval capabilities. The API provides a choice 
of standard web output formats, either JavaScript Object Notation (JSON) or Hyper Text 
Markup Language (HTML), of query results. The Data File API returns metadata on data files 
associated with dataset(s), including the location of these files for download via https. 
The Metadata API returns entire sets of metadata for input study dataset accession numbers. 
The Search API can be used to search dataset metadata by keywords and/or metadata. It can 
also be used to provide search of three other omics databases: the National Institutes of 
Health (NIH) / National Center for Biotechnology Information's (NCBI) Gene Expression 
Omnibus (GEO); the European Bioinformatics Institute's (EBI) Proteomics Identification 
(PRIDE); the Argonne National Laboratory's (ANL) Metagenomics Rapid Annotations using 
Subsystems Technology (MG-RAST).

In addition to study datasets, NASA OSDR also hosts metadata for 7 other data types: 
experiments, payloads, subjects, biospecimens, missions, vehicles, and hardware. The API for 
these data types is listed separately and uniform throughout, to make for easy metadata 
exploration.


**(Study)
Study Data File API:
Syntax = https://osdr.nasa.gov/osdr/data/osd/files/{OSD_STUDY_IDs}/?page={CURRENT_PAGE_NUMBER}&size=
{RESULTS_PER_PAGE}?all_files={ALL_FILES}

**(Experiments, Missions, Payloads, Hardware, Vehicles, Subjects, Biospecimens)
Format:
follow the  same API format. The "All" call returns a list of all objects within that data type, 
while the "Single" call returns an expanded version of a specific object. The endpoint for any 
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

Examples:
Single Mission Call
https://osdr.nasa.gov/geode-py/ws/api/mission/SpaceX-12


** (Resources)
For more information on making API requests with python, 
visit https://www.dataquest.io/blog/python-api-tutorial/.
"""

about_donki = """

    --  **** (The Space Weather Database Of Notifications, Knowledge, Information (DONKI))  ---
    
is a comprehensive on-line tool for space weather forecasters, scientists, and the general 
space science community. DONKI chronicles the daily interpretations of space weather observations, 
analysis, models, forecasts, and notifications provided by the Space Weather Research Center (SWRC), 
comprehensive knowledge-base search functionality to support anomaly resolution and space science 
research, intelligent linkages, relationships, cause-and-effects between space weather activities 
and comprehensive webservice API access to information stored in DONKI.

This API consists of the following component services:
Coronal Mass Ejection (CME), Coronal Mass Ejection (CME) Analysis, Geomagnetic Storm (GST),
Interplanetary Shock (IPS), Solar Flare (FLR), Solar Energetic Particle (SEP), Magnetopause Crossing (MPC),
Radiation Belt Enhancement (RBE), Hight Speed Stream (HSS), WSA+EnlilSimulation, Notifications.
"""
