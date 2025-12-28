import requests
from datetime import datetime

KAP_API = "https://www.kap.org.tr/tr/api/disclosures"


def fetch_kap_disclosures(stock_code, page_size=50):
    """
    Holt KAP-Meldungen für einen Aktiencode (z.B. ASELS).
    """
    params = {
        "stockCodes": stock_code,
        "pageIndex": 0,
        "pageSize": page_size
    }
    r = requests.get(KAP_API, params=params, timeout=15)
    if r.status_code != 200:
        raise Exception("KAP Daten nicht abrufbar")
    return r.json()


def normalize_disclosures(raw):
    """
    Vereinheitlicht wichtige Felder für spätere Bewertung/Analyse.
    """
    items = []
    for d in raw:
        items.append({
            "datum": d.get("disclosureDate"),
            "titel": d.get("title"),
            "typ": d.get("disclosureType"),
            "firma": d.get("companyName"),
            "url": f"https://www.kap.org.tr/tr/Bildirim/{d.get('disclosureIndex')}"
        })
    return items


if __name__ == "__main__":
    code = "ASELS"
    raw = fetch_kap_disclosures(code)
    data = normalize_disclosures(raw)

    print(f"{len(data)} KAP-Meldungen gefunden für {code}")
    for x in data[:5]:
        print(f"- {x['datum']} | {x['titel']}")
