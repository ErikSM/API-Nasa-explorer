from access.actions_donki import *

donki_dict = dict()

donki_dict['Coronal Mass Ejection (CME)'] = coronal_mass_ejection, parameters_of_cme
donki_dict['Coronal Mass Ejection (CME) Analysis'] = coronal_mass_ejection_analysis, parameter_of_cma
donki_dict['Geomagnetic Storm (GST)'] = geomagnetic_storm, parameter_of_gst
donki_dict['Interplanetary Shock (IPS)'] = interplanetary_shock, parameters_of_ips
donki_dict['Solar Flare (FLR)'] = solar_flare, parameter_of_flr
donki_dict['Solar Energetic Particle (SEP)'] = solar_energetic_particle, parameter_of_sep
donki_dict['Magnetopause Crossing (MPC)'] = magneto_pause_crossing, parameter_of_mpc
donki_dict['Radiation Belt Enhancement (RBE)'] = radiation_belt_enhancement, parameter_of_rbe
donki_dict['Hight Speed Stream (HSS)'] = hight_speed_stream, parameter_of_hss
donki_dict['WSA+EnlilSimulation'] = wsa_and_enlil_simulation, parameter_of_wsa_es
donki_dict['Notifications'] = donki_notices, parameter_of_ntf
