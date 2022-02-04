import cdsapi

c = cdsapi.Client()

c.retrieve(
    'derived-near-surface-meteorological-variables',
    {
        'format': 'tgz',
        'variable': 'near_surface_air_temperature',
        'year': '2017',
        'reference_dataset': 'cru',
        'month': [
            '12', 
        ],
    },
    'dec.tar.gz')
