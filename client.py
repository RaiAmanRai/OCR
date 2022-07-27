from __future__ import print_function
from cmath import log

import logging

import grpc
from protos.ocr_pb2 import OCRRequest
from protos.ocr_pb2_grpc import OCRServiceStub


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = OCRServiceStub(channel)
        
        r = stub.OCR(OCRRequest(uuid = 'default',  language = "en", image = bytes(4)))
        print("Client received: ", r)


if __name__ == '__main__':
    logging.basicConfig()
    run()