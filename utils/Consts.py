
mass_bins1 = [1350., 1650., 2017., 2465., 3013., 3682., 4500., 5500., 99999.]
mass_bins2 = [1492., 1824., 2230., 2725., 3331., 4071., 4975., 6081., 99999.]


mass_bin_idxs = list(range(1,7)) + list(range(11,17))

mass_bin_sig_mass_map_sparse = {
        0: [1600.,],
        1: [1800.,],
        2: [2200.,],
        3: [2700.,],
        4: [3300.,],
        5: [4100.,],
        6: [5000.,],
        10: [1600.,],
        11: [2000.,],
        12: [2500.,],
        13: [3000.,],
        14: [3700.,],
        15: [4500.,],
        16: [5500.,],
}

mass_bin_sig_mass_map = {
        0: [1600.,],
        1: [1800., 1900.],
        2: [2200., 2300.],
        3: [2600., 2700., 2800.],
        4: [3200., 3300., 3400.],
        5: [3900., 4100., 4200., 4300.],
        6: [4800.,  5000.,  5200.],
        10: [1600.,],
        11: [2000., 2100.],
        12: [2400., 2500.,],
        13: [2900., 3000., 3100.],
        14: [3600., 3700., 3800.],
        15: [4400., 4500., 4600., 4700.],
        16: [5400., 5600., 5800.],
}

#From the h5 maker, maps between different systematics and their index
sys_weights_map = {
        'nom_weight' : 0,
        'pdf_up' : 1,
        'pdf_down': 2,
        'prefire_up': 3,
        'prefire_down' : 4,
        'pileup_up' : 5 ,
        'pileup_down' : 6,
        'btag_up' : 7,
        'btag_down' : 8,
        'PS_ISR_up' : 9,
        'PS_ISR_down' : 10,
        'PS_FSR_up' : 11,
        'PS_FSR_down' : 12,
        'F_up' : 13,
        'F_down' : 14,
        'R_up' : 15,
        'R_down' : 16,
        'RF_up' : 17,
        'RF_down' : 18
        }

JME_vars = { 'JES_up', 'JES_down', 'JER_up',   'JER_down', 'JMS_up',  'JMS_down', 'JMR_up',  'JMR_down' }

JME_vars_map = {
        'pt_JES_up' : 0,
        'm_JES_up' : 1,
        'pt_JES_down' : 2,
        'm_JES_down' : 3,
        'pt_JER_up' : 4,
        'm_JER_up' : 5,
        'pt_JER_down' : 6,
        'm_JER_down' : 7,
        'm_JMS_up' : 8,
        'm_JMS_down' : 9,
        'm_JMR_up' : 10,
        'm_JMR_down' : 11
        }

sys_list = sorted((set(sys_weights_map.keys()) | JME_vars))
sys_list.remove("nom_weight")
sys_weight_list = sorted(set(sys_weights_map.keys()))
sys_weight_list.remove("nom_weight")

sys_list_clean = { sys.replace("_up", "").replace("_down", "") for sys in sys_list}
sys_weight_list_clean = { sys.replace("_up", "").replace("_down", "") for sys in sys_weight_list}

JME_vars_clean = { sys.replace("_up", "").replace("_down", "") for sys in JME_vars}

