def calculate_valuation(fin):
    """
    fin = Dictionary mit Finanzdaten
    Erwartete Keys:
    price, eps, book_value, equity, net_profit
    """

    price = fin.get("price")
    eps = fin.get("eps")
    book = fin.get("book_value")
    equity = fin.get("equity")
    profit = fin.get("net_profit")

    result = {}

    # KGV
    result["KGV"] = price / eps if eps and eps > 0 else None

    # PD/DD
    result["PD_DD"] = price / book if book and book > 0 else None

    # ROE
    result["ROE"] = profit / equity if equity and equity > 0 else None

    # Score
    score = 0
    if result["KGV"] and result["KGV"] < 10:
        score += 1
    if result["PD_DD"] and result["PD_DD"] < 1.5:
        score += 1
    if result["ROE"] and result["ROE"] > 0.15:
        score += 1

    result["Score"] = score
    result["Bewertung"] = (
        "Günstig" if score >= 2 else
        "Neutral" if score == 1 else
        "Teuer"
    )

    return result
