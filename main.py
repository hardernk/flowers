import datetime


def blooming_flowers(month):

    flowers = {'January': ['crocus', 'witch hazel', 'winter jasmine'],
               'February': ['snowdrop', 'iris reticulata', 'hellebore'],
               'March': ['forsythia', 'spring snowflake', 'anemone'], 
               'April': ['daffodils', 'tulip', 'magnolia'],
               'May': ['peonies', 'rhododendrons', 'lilac'],
               'June': ['rose', 'lupine', 'hydrangea'],
               'July': ['phlox', 'lilies', 'aster'],
               'August': ['dahlia', 'poppy', 'sunflower'],
               'September': ['daisies', 'hibiscus', 'sedum'],
               'October': ['aster', 'crysanthemum', 'colchicum'],
               'November': ['pampas grass', 'skimmia', 'photinia'],
               'December': ['hellebore', 'cyclamen', 'viburnum']} 
    if month not in flowers.keys():
        return []
    return flowers[month]

x = datetime.datetime.now()
print(blooming_flowers(x.strftime('%B')))
