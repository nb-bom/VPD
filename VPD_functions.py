"""Vapour pressure deficit functions"""

import xarray as xr
import pandas as pd
import numpy as np

#function to compute VPD from tasmax and rh datasets
#input: are datasets of rh and tasmax, and chosen_gwl (string)
#output: datasets of vpd and monthly_mean_vpd

def vpd_calc(ds_rh, ds_tasmax, chosen_gwl):
#    vpd = (1 - ds_rh/100) * 0.61094 * np.exp((17.652 * ds_tasmax)/(243.04 + ds_tasmax)) #originally used funtion
    vpd = (1 - ds_rh/100) * 6.1094 * np.exp ((17.625 * ds_tasmax)/(243.04 + ds_tasmax)) #the formula that Blair uses from http://www.bom.gov.au/research/publications/cawcrreports/CTR_024.pdf
    monthly_mean_vpd = vpd.groupby('time.month').mean('time', keep_attrs=True)
    
    vpd.attrs = {
        'long_name': 'Daily maximum vapour dressure deficit computed from tasmax and hursmin',
        'standard_name': 'vpd',
        'units': 'hPa',
        'program' : 'Australian Climate Service (ACS)',
        'summary' : f'Fire weather metric: vapour dressure deficit for Global Warming Level {chosen_gwl} C',
        'naming_authority' : "Bureau of Meteorology",
        'publisher_type' : "group",
        'publisher_type' : "group" ,
        'publisher_institution' : "Bureau of Meteorology",
        'publisher_name' : "Bureau of Meteorology",
        'publisher_url' : "http://www.bom.gov.au",
        'creator_type' : "institution" ,
        'creator_institution' : "Bureau of Meteorology" ,
        'contact' : "Naomi Benger (naomi.benger@bom.gov.au)" ,
        'institute_id' : "BOM" ,
        'institution' : "Bureau of Meteorology",
        'acknowledgement' : "Development of data supported with funding from the Australian Climate Service.",
    }
    ds_vpd = xr.Dataset({'vpd' : vpd})
    ds_rh.close()
    ds_tasmax.close()
    
    monthly_mean_vpd.attrs = {
        'long_name': 'Monthly mean vapour dressure deficit computed from tasmax and hursmin',
        'standard_name': 'monthly_mean_vpd',
        'units': 'hPa',
        'program' : 'Australian Climate Service (ACS)',
        'summary' : f'Fire weather metric: monthly mean vapour dressure deficit for Global Warming Level {chosen_gwl} C',
        'naming_authority' : "Bureau of Meteorology",
        'publisher_type' : "group",
        'publisher_type' : "group" ,
        'publisher_institution' : "Bureau of Meteorology",
        'publisher_name' : "Bureau of Meteorology",
        'publisher_url' : "http://www.bom.gov.au",
        'creator_type' : "institution" ,
        'creator_institution' : "Bureau of Meteorology" ,
        'contact' : "Naomi Benger (naomi.benger@bom.gov.au)" ,
        'institute_id' : "BOM" ,
        'institution' : "Bureau of Meteorology",
        'acknowledgement' : "Development of data supported with funding from the Australian Climate Service.",
    }
    }
    ds_monthly_mean_vpd = xr.Dataset({'monthly_mean_vpd' : monthly_mean_vpd})
    return ds_vpd, ds_monthly_mean_vpd
