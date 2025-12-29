import requests

def fetch_fundamentals(stock_code):
    """
    Holt fundamentale Finanzdaten einer Aktie (Gewinn, Umsatz, Verschuldung usw.)
    Quelle: https://financialmodelingprep.com/
    Du brauchst später einen kostenlosen API-Key.
    """
    
    API_KEY = "DEIN_API_KEY_HIER"  # wir setzen später gemeinsam einen ein
    url = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock_code}?apikey={API_KEY}"

    r = requests.get(url, timeout=15)

    if r.status_code != 200:
        raise Exception("Fundamentaldaten nicht abrufbar")

    return r.json()


if __name__ == "__main__":
    data = fetch_fundamentals("ASELS")
    print(data)
