import spacy

path_to_driver = r'C:\webdrivers\chromedriver.exe'
path_to_csv = r"C:\Users\rodol\Documents\2020-2021\Projet 4\oculus_monitoring\data\tweets\TechCrunch_content.csv"


#access token for Tweepy
consumer_key= 'F8SfgcjfSrqCePtC50YBjoh39'
consumer_secret= 'hDrsyRvnvYV68wzCGK0w78V9jBOv8RPtQEofbspiRt5sCNqFQ8'

access_token= '1337705388100169728-4wuMzVebrvbiAqk4uBZ4ICq0rqa2HF'
access_token_secret= 'up1kX8wc15vjZvavNqQCfld9n8SkGQmx3pnSMnpAXP0Yj'

userID = "TechCrunch"

nlp = spacy.load('en_core_web_sm')