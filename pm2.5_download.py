import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-reanalysis-eac4-monthly',
    {
        'format': 'netcdf',
        'variable': 'particulate_matter_10um',
        'year': '2017',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'product_type': 'monthly_mean',
'area':'60/30/05/130',
    },
    'pm10_2017.nc')
