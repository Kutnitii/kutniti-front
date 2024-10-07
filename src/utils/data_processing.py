import pandas as pd
import requests

def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json() 
        countries_data = []
        for country, info in data.items():
            if isinstance(info, dict): 
                if (info.get('total_article')!=0):
                    sentiment = info.get('sentiment', None)
                    sentiment_percentage = info.get('sentiment_percentage', {})
                    total_article = info.get('total_article', 0)
                    countries_data.append({
                        'name': country,
                        'sentiment': sentiment, 
                        'positive': sentiment_percentage.get('Good', 0),
                        'neutral': sentiment_percentage.get('Neutral', 0),
                        'negative': sentiment_percentage.get('Bad', 0),
                        'nbr_articles': total_article
                    })
        df_final = pd.DataFrame(countries_data)
        print(df_final)
        return df_final
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


df = load_data('http://192.168.1.11:5000/data')#load_data("./data/donnees_pays.csv")