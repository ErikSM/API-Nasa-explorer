from access.api_request import make_request, api_key

source_address = "https://api.nasa.gov/DONKI/"

all_acronyms = [
    "CME", "CMEAnalysis", "GST", "IPS", "FLR", "SEP", "MPC", "RBE", "HSS", "WSAEnlilSimulation", "Notifications"
]

all_parameters = {
    'generic': ["Start date", "End date"],
    'cme_a': ["Start date", "End date", "Most accurate only", "completeEntryOnly", "Speed", "Half angle", "Catalog"],
    'ips': ["Start date", "End date", "Location", "Catalog"],
    'notification': ["Start date", "End date", "Type"]
}

generic_rules = [
    "Parameters rules: **",
    "> 'startDate' and 'endDate': are in format 'yyyy-MM-dd' UT",
    "> startDate: default to 30 days prior to current UTC date",
    "> endDate: default to current UTC date"
]

cme_a_rules = [
    "Parameters rules: **",
    "> 'startDate' and 'endDate': are in format 'yyyy-MM-dd' UT",
    "> startDate: default to 30 days prior to current UTC date",
    "> endDate: default to current UTC date"""
    "> mostAccurateOnly: default is set to true",
    "> completeEntryOnly: default is set to true",
    "> speed (lower limit): default is set to 0",
    "> halfAngle (lower limit): default is set to 0",
    "> catalog: default is set to ALL (choices: ALL, SWRC_CATALOG, "
    "JANG_ET_AL_CATALOG)",
    "> keyword: default is set to NONE (example choices: swpc_annex)"
]

ips_rules = [
    "Parameters rules: **",
    "> 'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
    "> startDate: default to 30 days prior to current UTC date",
    "> endDate: default to current UTC date",
    "> location: default to ALL (choices: Earth, MESSENGER, "
    "STEREO A, STEREO B)",
    "> catalog: default to ALL (choices: SWRC_CATALOG, "
    "WINSLOW_MESSENGER_ICME_CATALOG)"
]

wsa_e_s_rules = [
    "Parameters rules: **",
    "> 'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
    "> startDate: default to 7 days prior to current UTC date",
    "> endDate: default to current UTC date"
]

notification_rules = [
    "Parameters rules: **",
    "> 'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
    "> 'startDate' if left out would default to 7 days prior to the "
    "current UT date",
    "> 'endDate' if left out would default to current UT date",
    "> 'type' could be: all, FLR, SEP, CME, IPS, MPC, GST, RBE, "
    "report",
    "> 'type' if left out would default to 'all'",
    """obs: The request date range is limit to 30 days. If the request 
    range is greater than 30 days,  it would limit your request range 
    to (endDate-30) to endDate."""
]


def get_donki(donki_address):
    address = source_address + donki_address

    print(address + api_key)

    requested = make_request(address, api_key)

    return requested


def _setter_date(start_date='default', end_date='default'):
    date = f"startDate={start_date}&endDate={end_date}"

    return date


def coronal_mass_ejection(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"CME?{set_date}"

    return address


def parameters_of_cme():
    data_name = "Coronal Mass Ejection"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = "CME"

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def coronal_mass_ejection_analysis(start_date='default', end_date='default',
                                   most_accurate_only='default', complete_entry_only='default',
                                   speed='0', half_angle='0', catalog='ALL'):
    set_date = _setter_date(start_date, end_date)

    address = (f"CMEAnalysis?{set_date}&"
               f"mostAccurateOnly={most_accurate_only}&"
               f"completeEntryOnly={complete_entry_only}&"
               f"speed={speed}&"
               f"halfAngle={half_angle}&"
               f"catalog={catalog}")

    return address


def parameter_of_cme_analysis():
    data_name = "Coronal Mass Ejection Analysis"

    parameters = cme_a_rules, 7, all_parameters['cme_a']

    acronym = 'CMEAnalysis'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def geomagnetic_storm(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"GST?{set_date}"

    return address


def parameter_of_gst():
    data_name = "Geomagnetic Storm"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = 'GST'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def interplanetary_shock(start_date='default', end_date='default',
                         location='ALL', catalog='ALL'):
    set_date = _setter_date(start_date, end_date)

    address = f"IPS?{set_date}&location={location}&catalog={catalog}"

    return address


def parameters_of_ips():
    data_name = "Interplanetary Shock"

    parameters = ips_rules, 4, all_parameters['ips']

    acronym = 'IPS'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def solar_flare(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"FLR?{set_date}"

    return address


def parameter_of_flr():
    data_name = "Solar Flare"

    parameters = generic_rules, 2, all_parameters['generic']
    acronym = 'FLR'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def solar_energetic_particle(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"SEP?{set_date}"

    return address


def parameter_of_sep():
    data_name = "Solar Energetic Particle"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = 'SEP'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def magneto_pause_crossing(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"MPC?{set_date}"

    return address


def parameter_of_mpc():
    data_name = "Magnetopause Crossing"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = 'MPC'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def radiation_belt_enhancement(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"RBE?{set_date}"

    return address


def parameter_of_rbe():
    data_name = "Radiation Belt Enhancement"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = 'RBE'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def hight_speed_stream(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"HSS?{set_date}"

    return address


def parameter_of_hss():
    data_name = "Hight Speed Stream"

    parameters = generic_rules, 2, all_parameters['generic']

    acronym = 'HSS'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def wsa_and_enlil_simulation(start_date='default', end_date='default'):
    set_date = _setter_date(start_date, end_date)

    address = f"WSAEnlilSimulations?{set_date}"

    return address


def parameter_of_wsa_es():
    data_name = "WSA + Enlil Simulation"

    parameters = wsa_e_s_rules, 2, all_parameters['generic']

    acronym = 'WSAEnlilSimulation'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}


def donki_notifications(start_date='default', end_date='default',
                        type_n='all'):
    set_date = _setter_date(start_date, end_date)
    address = f"notifications?{set_date}&type={type_n}"

    return address


def parameter_of_notifications():
    data_name = "Notifications"

    parameters = notification_rules, 3, all_parameters['notification']

    acronym = 'Notifications'

    return {'data name': data_name, 'parameters': parameters, 'acronym': acronym}
