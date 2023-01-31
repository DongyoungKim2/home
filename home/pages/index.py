# -*- coding: utf-8 -*-

import pynecone as pc
from home.templates import webpage
from home import constants
import pandas as pd
from home.base_state import State
from home.pages import projects
from home.components.footer import footer
from home.components.navbar import navbar
from home.pages import desktop
from home.pages import mobile
# @webpage(path="/")


def index():
    return pc.box(
        navbar(),
        pc.mobile_only(
            mobile.mobile(),
            width="100%",
        ),
        pc.tablet_and_desktop(
            desktop.desktop(),
        ),
        footer(),
        font_family="Noto Sans KR",
        width="100%",
    )
