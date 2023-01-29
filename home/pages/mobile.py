# -*- coding: utf-8 -*-

import pynecone as pc
from home.templates import webpage
from home import constants
import pandas as pd
from home.base_state import State
from home.pages import projects


def mobile():
    return pc.text("mobile")
