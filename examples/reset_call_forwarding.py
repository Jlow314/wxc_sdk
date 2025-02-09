#!/usr/bin/env python
"""
Example script
Reset call forwarding to default for all users in the org
"""

import logging
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv

from wxc_sdk import WebexSimpleApi
from wxc_sdk.types import PersonForwardingSetting

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

# set to DEBUG to see the actual requests
logging.getLogger('wxc_sdk.rest').setLevel(logging.INFO)

api = WebexSimpleApi()

# get all calling users
calling_users = [user for user in api.people.list(calling_data=True)
                 if user.location_id]

# set call forwarding to default for all users
with ThreadPoolExecutor() as pool:
    # default call forwarding settings
    forwarding = PersonForwardingSetting.default()

    # schedule update for each user and wait for completion
    list(pool.map(
        lambda user: api.person_settings.forwarding.configure(person_id=user.person_id,
                                                              forwarding=forwarding),
        calling_users))
