#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-FILE2LINK > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-FILE2LINKC/blob/master/LICENSE >
#
# All rights reserved.

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /DV-FILE2LINK
WORKDIR /DV-FILE2LINK
COPY . /DV-FILE2LINK
CMD ["python", "bot.py"]

