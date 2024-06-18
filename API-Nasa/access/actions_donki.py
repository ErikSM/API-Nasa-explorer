source_address = "https://api.nasa.gov/DONKI/"
key_demo = "&api_key=DEMO_KEY"


donki_dict = dict()


def _setter_date(start_date, end_date):
    date = f"startDate={start_date}&endDate={end_date}"
    return date


def coronal_mass_ejection(set_date):
    address = f"CME?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['cme'] = address, parameters


def coronal_mass_ejection_analysis(set_date, most_accurate_only='true', speed='500', half_angle='30', catalog='ALL'):
    address = (f"CMEAnalysis?{set_date}&"
               f"mostAccurateOnly={most_accurate_only}&"
               f"speed={speed}&"
               f"halfAngle={half_angle}&"
               f"catalog={catalog}")

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
        "mostAccurateOnly: default is set to true",
        "completeEntryOnly: default is set to true",
        "speed (lower limit): default is set to 0",
        "halfAngle (lower limit): default is set to 0",
        "catalog: default is set to ALL (choices: ALL, SWRC_CATALOG, JANG_ET_AL_CATALOG)",
        "keyword: default is set to NONE (example choices: swpc_annex)"
    ]

    donki_dict['cme_analysis'] = address, parameters


def geomagnetic_storm_gst(set_date):
    address = f"GST?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['gst'] = address, parameters


def interplanetary_shock_ips(set_date, location='LOCATION', catalog='CATALOG'):
    address = f"IPS?{set_date}&location={location}&catalog={catalog}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
        "location: default to ALL (choices: Earth, MESSENGER, STEREO A, STEREO B)",
        "catalog: default to ALL (choices: SWRC_CATALOG, WINSLOW_MESSENGER_ICME_CATALOG)"
    ]

    donki_dict['ips'] = address, parameters


def solar_flare_flr(set_date):
    address = f"FLR?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['flr'] = address, parameters


def solar_energetic_particle_sep(set_date):
    address = f"SEP?{set_date}"
    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['sep'] = address, parameters


def magnetopause_crossing_mpc(set_date):
    address = f"MPC?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['mpc'] = address, parameters


def radiation_belt_enhancement_rbe(set_date):
    address = f"RBE?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['rbe'] = address, parameters


def hight_speed_stream_hss(set_date):
    address = f"HSS?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 30 days prior to current UTC date",
        "endDate: default to current UTC date"""
    ]

    donki_dict['hss'] = address, parameters


def wsa_and_enlil_simulation(set_date):
    address = f"WSAEnlilSimulations?{set_date}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "startDate: default to 7 days prior to current UTC date",
        "endDate: default to current UTC date"
    ]

    donki_dict['wsa + enlil_simulation'] = address, parameters


def notifications(set_date, type='all'):
    address = f"notifications?{set_date}&type={type}"

    parameters = [
        "'startDate' and 'endDate' are in format 'yyyy-MM-dd' UT",
        "'startDate' if left out would default to 7 days prior to the current UT date",
        "'type' could be: all, FLR, SEP, CME, IPS, MPC, GST, RBE, report",
        "'endDate' if left out would default to current UT date",
        "'type' if left out would default to 'all'",
        """The request date range is limit to 30 days. If the request range is greater than 30 days, 
    it would limit your request range to (endDate-30) to endDate."""
    ]

    donki_dict['notifications'] = address, parameters
