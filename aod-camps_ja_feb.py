import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-reanalysis-eac4',
    {
        'date': '2017-01-01/2017-02-28',
        'format': 'grib',
        'variable': 'total_aerosol_optical_depth_550nm',
        'time': '12:00',
    },
    'jan_geb.grib')


