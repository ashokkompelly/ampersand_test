import csv
from datetime import datetime, timedelta
import random

# Define different strategies and symbols with realistic data
strategies = ["Momentum", "Mean Reversion", "Arbitrage", "Grid Trading"]
symbols = {
    "AAPL": {"base_price": 150, "range": 30},
    "TSLA": {"base_price": 250, "range": 60},
    "GOOGL": {"base_price": 140, "range": 35},
    "MSFT": {"base_price": 380, "range": 50},
    "AMZN": {"base_price": 170, "range": 40},
}

with open("large_trades.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "trade_id",
        "strategy",
        "symbol",
        "side",
        "quantity",
        "price",
        "timestamp"
    ])

    trade_id = 1
    base_date = datetime(2025, 1, 1, 9, 0, 0)

    # Generate 100k trades with variety
    for i in range(100000):
        # Randomly select strategy, symbol, and side
        strategy = random.choice(strategies)
        symbol = random.choice(list(symbols.keys()))
        side = random.choice(["buy", "sell"])
        
        # Get symbol-specific price range
        symbol_data = symbols[symbol]
        base_price = symbol_data["base_price"]
        price_range = symbol_data["range"]
        
        # Generate price with some variation
        price = base_price + random.uniform(-price_range/2, price_range/2)
        
        # Vary quantity based on strategy
        if strategy == "Grid Trading":
            quantity = random.randint(5, 20)  # Smaller quantities for grid
        elif strategy == "Arbitrage":
            quantity = random.randint(50, 200)  # Larger quantities for arbitrage
        else:
            quantity = random.randint(10, 100)
        
        # Increment timestamp slightly for each trade
        timestamp = base_date + timedelta(seconds=i * 5)
        
        writer.writerow([
            trade_id,
            strategy,
            symbol,
            side,
            quantity,
            round(price, 2),
            timestamp.strftime("%Y-%m-%dT%H:%M:%S")
        ])
        
        trade_id += 1

print("✅ Generated 100,000 trades with multiple strategies and symbols!")
print("   Strategies: Momentum, Mean Reversion, Arbitrage, Grid Trading")
print("   Symbols: AAPL, TSLA, GOOGL, MSFT, AMZN")