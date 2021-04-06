import pandas as pd
import regex

from resources.regex import *

def get_url(text, url_matcher = url_matcher):
    c_text = str(text)
    try:
        return url_matcher.findall(c_text)[0]
    except:
        return ""