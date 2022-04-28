import time


def calc_rarity(id, rarity, fusion_materials, commons, boxes, costs, rate, fiat_symbol):
    normal_cost = costs[0] * rate
    normal_total_cost = normal_cost * boxes[0]
    normal_color = "danger"

    premium_cost = costs[1] * rate
    premium_total_cost = premium_cost * boxes[1]
    premium_color = "danger"

    if (normal_total_cost < premium_total_cost):
        normal_color = "success"
    else:
        premium_color = "success"

    return {
        "id": id,
        "updated": time.time(),
        "commonsNeeded": commons,
        "fiatSymbol": fiat_symbol,
        "fusionMaterials": fusion_materials,
        "normalBoxes": boxes[0],
        "normalColor": normal_color,
        "normalCost": normal_cost,
        "normalTotalCost": normal_total_cost,
        "premiumBoxes": boxes[1],
        "premiumColor": premium_color,
        "premiumCost": premium_cost,
        "premiumTotalCost": premium_total_cost,
        "rarity": rarity,
    }


def documents(rate, fiat_symbol):
    return [
        calc_rarity(
            "rare", "Rare", "2 x Common @ Lv 2",
                    4, [4, 4], [20, 100], rate, fiat_symbol
        ),
        calc_rarity(
            "epic", "Epic", "2 x Rare @ Lv 3",
                    24, [19, 9], [20, 100], rate, fiat_symbol
        ),
        calc_rarity(
            "legend", "Legend", "2 x Epic @ Lv 4",
            192, [148, 73], [20, 100], rate, fiat_symbol
        ),
        calc_rarity(
            "mythic", "Mythic", "2 x Legend @ Lv 5",
            1920, [1477, 738], [20, 100], rate, fiat_symbol
        ),
        calc_rarity(
            "meta", "Meta", "2 x Mythic @ Lv 6",
                    23040, [17723, 8800], [20, 100], rate, fiat_symbol
        ),
    ]
