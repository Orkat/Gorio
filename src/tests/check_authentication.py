#!/usr/bin/env python

import requests
import requests.auth

import sys
sys.path.insert(0, '..')

from authentication import oauth2

print(oauth2.get_access_token())
