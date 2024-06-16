source_address = "https://api.nasa.gov/DONKI/"
key_demo = "&api_key=DEMO_KEY"


def define_date(start_date, end_date):
    start_and_end_date = f"startDate={start_date}&endDate={end_date}"
    return start_and_end_date


def all_donki_addresses(definded_date):

    donki_dict = dict()

    coronal_mass_ejection_cme = f"CME?{definded_date}"
    donki_dict['cme'] = coronal_mass_ejection_cme

    coronal_mass_ejection_cme_analysis = (f"CMEAnalysis?{definded_date}&"
                                          "mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL")
    donki_dict['cme_analysis'] = coronal_mass_ejection_cme_analysis

    geomagnetic_storm_gst = f"GST?{definded_date}"
    donki_dict['gst'] = geomagnetic_storm_gst

    imterplanetary_shock_ips = (f"IPS?{definded_date}&"
                                "location=LOCATION&catalog=CATALOG")
    donki_dict['ips'] = imterplanetary_shock_ips

    solar_flare_flr = f"FLR?{definded_date}"
    donki_dict['flr'] = solar_flare_flr

    solar_energetic_particle_sep = f"SEP?{definded_date}"
    donki_dict['sep'] = solar_energetic_particle_sep

    magnetopause_crossing_mpc = f"MPC?{definded_date}"
    donki_dict['mpc'] = magnetopause_crossing_mpc

    radiation_belt_enhancement_rbe = f"RBE?{definded_date}"
    donki_dict['rbe'] = radiation_belt_enhancement_rbe

    hight_speed_stream_hss = f"HSS?{definded_date}"
    donki_dict['hss'] = hight_speed_stream_hss

    wsa_and_enlil_simulation = f"WSAEnlilSimulations?{definded_date}"
    donki_dict['wsa + enlil_simulation'] = wsa_and_enlil_simulation

    notifications = (f"notifications?{definded_date}"
                     "&type=all")
    donki_dict['notifications'] = notifications

