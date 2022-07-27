from concurrent import futures
import grpc
from protos.ocr_pb2 import OCRResponse, Coordinates, OCRText
from protos.ocr_pb2_grpc import OCRServiceServicer, add_OCRServiceServicer_to_server

from ocr import get_text


class OCRService(OCRServiceServicer):
    def OCR(self, request, context):
        cust_id = request.uuid
        image = request.image
        lang = request.language

        m = get_text(image, lang, cust_id)

        res = []
        for n in m:
            res.append( OCRText( text = n[1], confidence = n[2], coordinates =  [ Coordinates( i = n[0][0] ), Coordinates( i = n[0][1] ), Coordinates( i = n[0][2] ), Coordinates( i = n[0][3] ) ]) )
        return OCRResponse(uuid = cust_id, language = lang, text = res)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    add_OCRServiceServicer_to_server(OCRService(), server)
    server.add_insecure_port('0.0.0.0'+':'+'8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()