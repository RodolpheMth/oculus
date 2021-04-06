import regex as re

url_pattern = r'(https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}[-a-zA-Z0-9()@:%_+.~#?&/=]*)'
url_matcher = re.compile(url_pattern)

str_money_pattern = r'\p{Sc}\s?\d+(?:\.\d+)?\s?(?:million|billion|M|m|B|b|Million|Billion)?(?:\s(?:dollars|euros|pounds|USD|EUR|GBP))?'
money_matcher = re.compile(str_money_pattern)

str_series_regex = 'seed|series [A-Z]|mezzanine|IPO|public'
serie_matcher = re.compile(str_series_regex)