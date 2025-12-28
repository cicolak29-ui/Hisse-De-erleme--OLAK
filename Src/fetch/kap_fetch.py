import requests

def fetch_kap_disclosures(stock_code):
    url = f"https://www.kap.org.tr/tr/api/disclosures?stockCodes={stock_code}"
    r = requests.get(url, timeout=10)

    if r.status_code != 200:
        raise Exception("KAP Daten nicht abrufbar")

    return r.json()


if __name__ == "__main__":
    data = fetch_kap_disclosures("ASELS")
    print(f"{len(data)} KAP-Meldungen gefunden")
