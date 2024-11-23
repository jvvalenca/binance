from binance.client import Client
import locale
import os

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Substitua pelas suas chaves
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

# Inicializa o cliente da Binance
client = Client(api_key, api_secret)

# Função para obter o preço atual do Bitcoin
def get_btc_price():
    try:
        ticker = client.get_ticker(symbol="BTCUSDT")  # Par Bitcoin para dólar
        price = float(ticker['lastPrice'])
        formatted_price = locale.format_string('%.2f', price, grouping=True)
        ##print(f"O preço atual do Bitcoin é: ${price:.2f}")
        if price >= 100000:
            print(f"O preço atual do Bitcoin é: R${formatted_price} dólares. Está na hora de vender!")
            return price
        elif price <= 90000:
            print(f"O preço atual do Bitcoin é: R${formatted_price} dólares. Houve uma queda significativa, cuidado!")
            return price
        else:
            print(f"O preço atual do Bitcoin é: R${formatted_price} dólares.")
            return price
    except Exception as e:
        print(f"Erro ao obter o preço: {e}")

# Chamando a função
get_btc_price()
