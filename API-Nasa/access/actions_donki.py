from access.api_request import make_request, api_key

source_address = "https://api.nasa.gov/DONKI/"

donki_dict = dict()

all_acronyms = ["CME", "CMA", "GST", "IPS", "FLR", "SEP",
                "MPC", "RBE", "HSS", "WSA+ES", "NTF"]


def _setter_date(start_date, end_date):
    date = f"startDate={start_date}&endDate={end_date}"

    return date


def open_donki(donki_address):
    address = source_address + donki_address

    requested = make_request(address, api_key)

    return requested


def coronal_mass_ejection(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"CME?{set_date}"

    parameters = [
        "'startDate' and 'endDate': are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = "CME"

    return address, parameters, acronym


donki_dict['Coronal Mass Ejection (CME)'] = coronal_mass_ejection


def coronal_mass_ejection_analysis(start_date, end_date,
                                   most_accurate_only='true', speed='500', half_angle='30', catalog='ALL'):
    set_date = _setter_date(start_date, end_date)

    address = (f"CMEAnalysis?{set_date}&"
               f"mostAccurateOnly={most_accurate_only}&"
               f"speed={speed}&"
               f"halfAngle={half_angle}&"
               f"catalog={catalog}")

    parameters = [
        "'startDate' and 'endDate': are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
        "mostAccurateOnly: default is set to true",
        "completeEntryOnly: default is set to true",
        "speed (lower limit): default is set to 0",
        "halfAngle (lower limit): default is set to 0",
        "catalog: default is set to ALL (choices: ALL, SWRC_CATALOG, JANG_ET_AL_CATALOG)",
        "keyword: default is set to NONE (example choices: swpc_annex)"
    ]

    acronym = 'CMA'

    return address, parameters, acronym


donki_dict['Coronal Mass Ejection (CME) Analysis'] = coronal_mass_ejection_analysis


def geomagnetic_storm(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"GST?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'GST'

    return address, parameters, acronym


donki_dict['Geomagnetic Storm (GST)'] = geomagnetic_storm


def interplanetary_shock(start_date, end_date,
                         location='LOCATION', catalog='CATALOG'):
    set_date = _setter_date(start_date, end_date)

    address = f"IPS?{set_date}&location={location}&catalog={catalog}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
        "location: default to ALL (choices: Earth, MESSENGER, STEREO A, STEREO B)",
        "catalog: default to ALL (choices: SWRC_CATALOG, WINSLOW_MESSENGER_ICME_CATALOG)"
    ]

    acronym = 'IPS'

    return address, parameters, acronym


donki_dict['Interplanetary Shock (IPS)'] = interplanetary_shock


def solar_flare(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"FLR?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'FLR'

    return address, parameters, acronym


donki_dict['Solar Flare (FLR)'] = solar_flare


def solar_energetic_particle(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"SEP?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'SEP'

    return address, parameters, acronym


donki_dict['Solar Energetic Particle (SEP)'] = solar_energetic_particle


def magneto_pause_crossing(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"MPC?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'MPC'

    return address, parameters, acronym


donki_dict['Magnetopause Crossing (MPC)'] = magneto_pause_crossing


def radiation_belt_enhancement(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"RBE?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'RBE'

    return address, parameters, acronym


donki_dict['Radiation Belt Enhancement (RBE)'] = radiation_belt_enhancement


def hight_speed_stream(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"HSS?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    acronym = 'HSS'

    return address, parameters, acronym


donki_dict['Hight Speed Stream (HSS)'] = hight_speed_stream


def wsa_and_enlil_simulation(start_date, end_date):
    set_date = _setter_date(start_date, end_date)

    address = f"WSAEnlilSimulations?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 7 days prior to current UTC date",
        "endDate: default to current UTC date"
    ]

    acronym = 'WSA+ES'

    return address, parameters, acronym


donki_dict['WSA+EnlilSimulation'] = wsa_and_enlil_simulation


def donki_notices(start_date, end_date,
                  type_n='all'):
    set_date = _setter_date(start_date, end_date)
    address = f"notifications?{set_date}&type={type_n}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "'startDate' if left out would default to 7 days prior to the current UT date",
        "'endDate' if left out would default to current UT date",
        "'type' could be: all, FLR, SEP, CME, IPS, MPC, GST, RBE, report",
        "'type' if left out would default to 'all'",
        """The request date range is limit to 30 days. If the request range is greater than 30 days, 
    it would limit your request range to (endDate-30) to endDate."""
    ]

    acronym = 'NTF'

    return address, parameters, acronym


def test_donki(donki):
    cme = donki("2015-08-01", "2015-09-01")

    test = open_donki(cme[0])

    print(f"(({len(test)} {type(test)}))\n")
    for i in test:
        print(f'**{len(i)}{type(i)}')


test_donki(coronal_mass_ejection)

