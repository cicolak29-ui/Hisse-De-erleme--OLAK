from Src.fetch.kap_fetch import fetch_kap_disclosures
from Src.valuation.valuation_core import calculate_valuation

def main():
    stock = input("Aktienkürzel (z.B. ASELS): ").upper()

    print("\nKAP-Meldungen werden geladen...")
    kap_data = fetch_kap_disclosures(stock)
    print(f"{len(kap_data)} Meldungen gefunden")

    for k in kap_data[:3]:
        print("-", k["title"])

    print("\nBewertung wird berechnet...")

    financials = {
        "price": 45,
        "eps": 6,
        "book_value": 30,
        "equity": 120_000_000,
        "net_profit": 22_000_000
    }

    result = calculate_valuation(financials)

    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

