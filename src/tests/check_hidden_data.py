#!/usr/bin/env python

import sys
sys.path.insert(0, '..')

from authentication import hidden

print(hidden.read_hidden_data())
