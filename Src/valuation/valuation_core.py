def calculate_pe_ratio(price, eps):
    """ KGV = aktueller Preis / Gewinn je Aktie """
    if eps == 0:
        return None
    return round(price / eps, 2)


def calculate_fair_value(pe, eps, target_pe=12):
    """ Einfaches Fair-Value Modell """
    if eps == 0:
        return None
    return round(eps * target_pe, 2)


def evaluate_stock(price, eps):
    """ Einfache Bewertung für Start – später erweitern wir Ranking Systeme """
    pe = calculate_pe_ratio(price, eps)
    fair_value = calculate_fair_value(pe, eps)

    result = {
        "KGV": pe,
        "FairValue": fair_value,
        "Upside (%)": None if fair_value is None else round(((fair_value - price) / price) * 100, 2)
    }
    
    return result


if __name__ == "__main__":
    print(evaluate_stock(price=40, eps=3))
