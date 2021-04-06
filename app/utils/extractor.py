from resources.regex import *
from resources.const import *

import regex

def money_extractor(text, money_matcher=money_matcher):
    try:
        return money_matcher.findall(text)[0]
    except:
        return ""

def serie_extractor(text, serie_matcher=serie_matcher):
    try:
        return serie_matcher.findall(text)[0]
    except:
        return ""

def extract_funds_invest(text, str_money_pattern=str_money_pattern):
    list_sent = []
    invest = []
    funds = []

    about_doc = nlp(text)
    sentences = about_doc.sents

    for sentence in sentences:
        list_sent.append(sentence)

    for i in range(len(list_sent)):

        test = list_sent[i].text


        matches = regex.findall(str_money_pattern, test)
        if matches:
            spacy_label = [ent.text.strip() for ent in nlp(test).ents if ent.label_ in ["ORG", "PERSON"]]
            if spacy_label:
                for first_element_invest in spacy_label[0:1]:
                    invest = first_element_invest
                for first_element_fund in matches[0:1]:
                    funds = first_element_fund
    return invest, funds