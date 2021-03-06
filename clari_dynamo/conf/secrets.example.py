# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range, zip, round, input, int, pow, object)
import os
import json

# Template file for secrets.py, copy to secrets.py in the same directory
# and fill in the values for local dev.
# Populate these environment variables in your OS system environment
# for deployments per 12factorapp.com

os.environ['CLARI_DYNAMO_AWS_KMS_S3_BUCKET_NAME'] = 'x'
os.environ['CLARI_DYNAMO_AWS_KMS_KEY_ARN_ID']     = 'x'
# os.environ['CLARI_DYNAMO_AUTH_WEB_HOOK']          = 'https://example.com/authed_for?tenant_id=%s'
os.environ['CLARI_DYNAMO_BASIC_AUTH_USERNAME']    = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
os.environ['CLARI_DYNAMO_BASIC_AUTH_PASSWORD']    = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

################################################################################
# Crypto key ###################################################################
"""
Populate with:

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

"""

# TODO: Use KMS to encrypt crypto key or do all encryption.
os.environ['CLARI_DYNAMO_CRYPTO_KEY'] = None

################################################################################
################################################################################