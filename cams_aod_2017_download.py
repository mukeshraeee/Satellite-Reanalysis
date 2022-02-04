import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-reanalysis-eac4',
    {
        'date': '2017-09-01/2017-11-30',
        'format': 'netcdf',
        'variable': 'total_aerosol_optical_depth_550nm',
        'time': '12:00',
 'area':'60/15/45/100',   
 },
    '2017_pengfei.grib')
