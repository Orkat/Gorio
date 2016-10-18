import json
import sys

import definitions


def read_hidden_data():

    hidden_data = open(definitions.ROOT_DIR + "/" + definitions.HIDDEN_DATA_FILENAME)
    line = hidden_data.readline()
    return json.loads(line)
