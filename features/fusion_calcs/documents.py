import time
import math

def format_document(rarity, rate, fiat_symbol):
    box_stats = [
        {
            "name": "Normal",
            "cost": 20,
            "probability": [0.9, 0.09, 0.01, 0, 0]
        },
        {
            "name": "Premium",
            "cost": 100,
            "probability": [0.3, 0.5, 0.19, 0.01, 0]
        },
        {
            "name": "Ultra",
            "cost": 500,
            "probability": [0, 0.4, 0.5, 0.095, 0.005]
        }
    ]

    rarities = [
        {
            "name": "Common",
            "fusion_commons": 1
        },
        {
            "name": "Rare",
            "fusion_commons": 4
        },
        {
            "name": "Epic",
            "fusion_commons": 24
        },
        {
            "name": "Legend",
            "fusion_commons": 192
        },
        {
            "name": "Mythic",
            "fusion_commons": 1920
        },
        {
            "name": "Meta",
            "fusion_commons": 23040
        }
    ]

    commons_needed = rarities[rarity]["fusion_commons"]

    box_calcs = {}
    costs = []

    for box_i in range(0, 3):
        box_stat = box_stats[box_i]
        box_commons = 0
        for rarity_i in range(0, 5):
            box_commons += box_stat["probability"][rarity_i] * \
                rarities[rarity_i]["fusion_commons"]

        boxes_to_this_rarity = math.ceil(commons_needed / box_commons)

        total_cost = boxes_to_this_rarity * box_stat["cost"]

        costs.append(total_cost)

        box_calcs[box_stat["name"].lower()] = {
            "name": box_stat["name"],
            "cost": box_stat["cost"] * rate,
            "boxes": boxes_to_this_rarity,
            "total_cost": total_cost * rate,
            "color": "danger"
        }

    costs.sort()

    for box_i in range(0,3):
        box_stat = box_stats[box_i]
        total_cost = box_calcs[box_stat["name"].lower()]["total_cost"]

        if total_cost == costs[0]:
            box_calcs[box_stat["name"].lower()]["color"] = "success"

        if total_cost == costs[1]:
            box_calcs[box_stat["name"].lower()]["color"] = "warning"


    fusion_materials = f'2 x {rarities[rarity - 1]["name"]} @ Lv {rarity + 1}'

    return {
        "id": rarities[rarity]["name"].lower(),
        "updated": time.time(),
        "commonsNeeded": commons_needed,
        "fiatSymbol": fiat_symbol,
        "fusionMaterials": fusion_materials,
        "calcs": box_calcs,
        "rarity": rarities[rarity]["name"],
    }


def documents(rate, fiat_symbol):
    return list(
        map(
            lambda rarity: format_document(rarity, rate, fiat_symbol),
            range(1, 6)
        )
    )
