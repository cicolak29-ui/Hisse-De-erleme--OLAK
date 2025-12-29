from Src.fetch.kap_fetch import fetch_kap_disclosures, normalize_disclosures
from Src.fetch.fundamentals import get_fundamentals
from Src.valuation.valuation_core import evaluate_stock

def main():
    aktie = input("Aktiencode eingeben (z.B. ASELS): ").strip().upper()

    # 1) Fundamentaldaten abrufen
    f = get_fundamentals(aktie)
    print("\n📌 Fundamentaldaten:")
    print(f"Preis: {f.get('price')} ₺")
    print(f"EPS: {f.get('eps')} ₺")
    print(f"BVPS: {f.get('bvps')} ₺")
    print(f"ROE: {f.get('roe')} %")

    # 2) Bewertung ausrechnen
    val = evaluate_stock(price=f.get('price'), eps=f.get('eps'))
    print("\n📊 Bewertungsergebnis:")
    for k, v in val.items():
        print(f"{k}: {v}")

    # 3) News / KAP Meldungen
    raw = fetch_kap_disclosures(aktie)
    meldungen = normalize_disclosures(raw)

    print("\n📰 Letzte 5 KAP Meldungen:")
    for m in meldungen[:5]:
        print(f"- {m['datum']} | {m['firma']} | {m['titel']}")
        print(f"  {m['url']}")

if __name__ == "__main__":
    main()
