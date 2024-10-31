#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-FILE2LINK > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-FILE2LINKC/blob/master/LICENSE >
#
# All rights reserved.

import jinja2
from info import *
from ERASTREAM.bot import ERASTREAMBot
from ERASTREAM.util.human_readable import humanbytes
from ERASTREAM.util.file_properties import get_file_ids
from ERASTREAM.server.exceptions import InvalidHash
import urllib.parse
import logging
import aiohttp


async def render_page(id, secure_hash, src=None):
    file = await ERASTREAMBot.get_messages(int(LOG_CHANNEL), int(id))
    file_data = await get_file_ids(ERASTREAMBot, int(LOG_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f"link hash: {secure_hash} - {file_data.unique_id[:6]}")
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash

    src = urllib.parse.urljoin(
        URL,
        f"{id}/{urllib.parse.quote_plus(file_data.file_name)}?hash={secure_hash}",
    )

    tag = file_data.mime_type.split("/")[0].strip()
    file_size = humanbytes(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "ERASTREAM/template/req.html"
    else:
        template_file = "ERASTREAM/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get("Content-Length")))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = file_data.file_name.replace("_", " ")

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        file_unique_id=file_data.unique_id,
    )
