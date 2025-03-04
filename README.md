# VPD
Create vapour pressure deficit projections

Code to create vapour pressure deficit (VPD) projections from daily tasmax and hursmin projections.

Equations saturation vapour pressure http://www.bom.gov.au/climate/how/newproducts/images/IDCJHC02_notes.txt

ea = Vapour pressure = exp (1.8096 + (17.269425 * Dew_Point)/(237.3 + Dew_Point)) (units hPa)

es = Saturated Vapour pressure = exp (1.8096 + (17.269425 * Air_Temperature)/(237.3 + Air_Temperature)) (units hPa)

Relative Humidity = Vapour pressure / Saturated vapour pressure * 100 (units percent %)

Rearrange the formulae to get:

Vapour pressure = rh * 0.0061094 * exp((17.652 * t)/(243.04 + t))

Vapour pressure deficit is the difference between the saturation vapour pressure and the actual vapour pressure:

vpd 
= es - ea = es - (RH * es /100) = (1 - RH/100) * es 
= (1 - RH/100) * exp (1.8096 + (17.269425 * Air_Temperature)/(237.3 + Air_Temperature)) (units hPa)

A nice explainer about the relevance of VPD to fire: https://blog.ucsusa.org/carly-phillips/what-is-vapor-pressure-deficit-vpd-and-what-is-its-connection-to-wildfires/
