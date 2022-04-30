def documents(usdRate, mtbRate, fiat_symbol):
    return [
        {
            "id": 'normal',
            "box": 'Normal',
            "quantity": 5000,
            "staking": 3000,
            "stakeCost": 3000 * mtbRate,
            "cost": 19.99 * usdRate,
            "totalCost": 19.99 * usdRate + 3000 * mtbRate,
            "limit": 4,
            "fiatSymbol": fiat_symbol
        },
        {
            "id": 'premium',
            "box": 'Premium',
            "quantity": 2000,
            "staking": 10000,
            "stakeCost": 10000 * mtbRate,
            "totalCost": 99.99 * usdRate + 10000 * mtbRate,
            "cost": 99.99 * usdRate,
            "limit": 2,
            "fiatSymbol": fiat_symbol
        },
        {
            "id": 'ultra',
            "box": 'Ultra',
            "quantity": 1000,
            "staking": 50000,
            "stakeCost": 50000 * mtbRate,
            "totalCost": 499.99 * usdRate + 50000 * mtbRate,
            "cost": 499.99 * usdRate,
            "limit": 1,
            "fiatSymbol": fiat_symbol
        }
    ]
