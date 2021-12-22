import logging
import json
from io import StringIO
import azure.functions as func
import sys


def main(myblob: func.InputStream, collection1: func.Out[str], collection2: func.Out[str]):

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    logging.info(f"blob type {type(myblob)}")

    bytes = myblob.read()                        # bytes
    doc = json.loads(bytes.decode('utf-8'))      # json object
    logging.info(f"doc type {type(doc)}")

    # doc contains escaped json objects that are strings
    logging.info(f"item 'fullDocument' type {type(doc['fullDocument'])}")  # string
    logging.info(f"item 'namespace' type {type(doc['namespace'])}")  # string


    # we can load these into objects
    fullDocument = json.loads(doc['fullDocument'])
    logging.info(f"fullDocument type {type(fullDocument)}")  # object
    namespace = json.loads(doc['namespace'])
    logging.info(f"namespace type {type(namespace)}")  # object

    # optionally we can manipulate these objects or extract items from them
    collection = namespace['collectionName']

    # write the document into a json formatted string
    docstr = json.dumps(fullDocument)

    # write that string to the relevant output binding
    if collection == 'collection1':
        collection1.set(docstr)
    elif collection == 'collection2':
        collection2.set(docstr)


