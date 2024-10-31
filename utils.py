#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-FILE2LINK > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-FILE2LINKC/blob/master/LICENSE >
#
# All rights reserved.

from shortzy import Shortzy
from info import SHORTLINK_URL, SHORTLINK_API

class temp(object):
    ME = None
    BOT = None
    U_NAME = None
    B_NAME = None


async def get_shortlink(link):
    shortzy = Shortzy(api_key=SHORTLINK_API, base_site=SHORTLINK_URL)
    link = await shortzy.convert(link)
    return link
