import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-reanalysis-eac4',
    {
        'date': '2017-01-01/2017-12-31',
        'format': 'netcdf',
        'variable': 'particulate_matter_10um',
        'time': '12:00',
'area':'60/30/05/135',   
 },
    'pm_10_2017.nc')
