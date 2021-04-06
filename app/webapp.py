# pylint: disable=invalid-name
import pandas as pd
from flask import Flask
from flask import render_template, send_from_directory

from utils.get_tweet import *
from utils.get_url import *
from utils.body_extractor import *
from utils.extractor import *
from utils.edited_data import *

df = pd.read_csv(r"C:\Users\rodol\Documents\2020-2021\Projet 4\oculus_monitoring\oculus_webapp\app\datas\brouillon.csv")
app = Flask(__name__, static_url_path="/templates")
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)


# @app.route("/reboot")
# def reboot():
# if __name__ == "__main__":
#     df_inter = get_tweet()
#     df_inter["urls"] = df_inter.text.apply(get_url)
#     df_inter = df_inter.drop(['id', 'created_at', 'text'], axis = 1)

#     df_inter = df_inter['urls'][:2]

#     list_finale = []
#     get_extractor = body_extractor(df_inter)
#     list_finale['Date'] = get_extractor[0]
#     list_finale['Title'] = get_extractor[1]
#     list_finale['Body Content'] = get_extractor[2]
#     list_finale['Company Name'] = get_extractor[3]


#     # print(list_finale)

#     # df_final = pd.DataFrame(list_finale)
#     # df_final = df_final.dropna()
#     # df_final = df_final[df_final.astype(str)['Company Name'] != '[]']
#     # df_final = df_final.reset_index(drop=True)
    
#     # inter = df_final['Body Content'].apply(extract_funds_invest)

#     # df_final['Investors'] = [x[0] for x in inter]
#     # df_final['Funds'] = [x[1] for x in inter]
#     # df_final = df_final[df_final.astype(str)['Investors'] != '[]']
#     # df_final = df_final[df_final.astype(str)['Funds'] != '[]']
#     # df_final['Funds'] = money_convert(df_final['Funds'])
#     # df_final['Serie'] = df_final['Body Content'].apply(serie_extractor)
    
#     df_final.to_csv(path_to_csv, index=False, sep=";")


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/statics/<path:path>")
def statics(path):
    return send_from_directory('statics', path)

@app.route("/lda")
def lda():
    return render_template('lda.html')

@app.route("/wordcloud")
def wdcl():
    return render_template('wordcloud.html')

@app.route("/total")
def total():
    return df.to_csv()

if __name__ == "__main__":
   
    app.run()