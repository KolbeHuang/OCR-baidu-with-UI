from aip import AipOcr

## My baidu api
# APP_ID = '25194054'
# API_KEY = 'frb7XgojpDGQmBGypaIXgDGP'
# SECRET_KEY = 'My5Ul4c76IF3hC4GeKGR9oVegqmrRBAV'

def ocr_analysis(image_path, APP_ID, API_KEY, SECRET_KEY, model):
    """
    This function can use baidu SDK to recognize and return the characters in the image.
    Parameter model is used to control the ocr mode that is used by SDK.
    model = "general": general mode
    model = "accurate": accurate mode (takes longer)
    model = "location": general mode with locations of characters
    model = "hand": handwritting mode
    The default setup is to recognize both English and Chinese.
    """
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)        # create a new airocr

    # read the image as bits (based 64)
    temp = open(image_path, 'rb')
    image_bits = temp.read()
    temp.close()

    # adding extra general options if necessary
    # options = {}
    # options["language_type"] = "CHN_ENG"

    if model == "general":
        result = client.basicGeneral(image_bits)
    elif model == "accurate":
        result = client.basicAccurate(image_bits)
    elif model == "location":
        result = client.general(image_bits)
    elif model == "hand":
        result = client.handwriting(image_bits)
    else:       # if mode is anything else, use general recognition
        result = client.basicGeneral(image_bits)

    result_neat = ""
    for item in result['words_result']:
        content = item['words']     # recognition word(s)
        result_neat = result_neat + content + "\n"

    return result_neat