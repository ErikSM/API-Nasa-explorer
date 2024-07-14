from access.actions_donki import *

donki_names = dict()

donki_names['Coronal Mass Ejection (CME)'] = coronal_mass_ejection, parameters_of_cme
donki_names['Coronal Mass Ejection (CME) Analysis'] = coronal_mass_ejection_analysis, parameter_of_cme_analysis
donki_names['Geomagnetic Storm (GST)'] = geomagnetic_storm, parameter_of_gst
donki_names['Interplanetary Shock (IPS)'] = interplanetary_shock, parameters_of_ips
donki_names['Solar Flare (FLR)'] = solar_flare, parameter_of_flr
donki_names['Solar Energetic Particle (SEP)'] = solar_energetic_particle, parameter_of_sep
donki_names['Magnetopause Crossing (MPC)'] = magneto_pause_crossing, parameter_of_mpc
donki_names['Radiation Belt Enhancement (RBE)'] = radiation_belt_enhancement, parameter_of_rbe
donki_names['Hight Speed Stream (HSS)'] = hight_speed_stream, parameter_of_hss
donki_names['WSA+EnlilSimulation'] = wsa_and_enlil_simulation, parameter_of_wsa_es
donki_names['Notifications'] = donki_notifications, parameter_of_notifications
