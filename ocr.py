import easyocr



def get_text(image, lang, cust_id):
    """Driver pipeline for ocr

    param
        image : byte array
        lang : language for recognition
        cust_id : cutomer id

    """
    # yield "STEP 1/4 : - Download Data Finished", flag

    reader = easyocr.Reader([lang])             # this needs to run only once to load the model into memory
    result = reader.readtext('/home/OCR/examples/english.png')
    # result = [list(i) for i in result ]

    return result