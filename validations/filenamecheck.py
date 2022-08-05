import re

def checkImageType(filename):

    dry = ["dry", "Dry", "DRY"]
    wet = ["wet", "Wet", "WET"]

    if any(dry in filename for dry in dry):
        imageType = 'Dry'
    elif any(wet in filename for wet in wet):
        imageType = 'Wet'
    else:
        imageType = ''

    return (imageType)

def checkStartEndDepth(filename):
    decimal_expression = r'(\d+\.\d+)'

    result = re.findall(decimal_expression, filename)
    
    try:
        start_depth = result[0]
    except:
        start_depth = ''
    try:
        end_depth = result[-1]
    except:
        end_depth = ''
    if start_depth == end_depth:
        end_depth = ''

    return ([start_depth, end_depth])
