from app.services.csv_processor import read_csv_rows

def calculate_pnl(file_path):

    strategy_pnl = {}
    
    # Track both quantity and total cost for average price
    buy_inventory = {}  # (strategy, symbol) -> {"qty": total_qty, "cost": total_cost}
    
    for trade in read_csv_rows(file_path):

        strategy = trade["strategy"]
        symbol = trade["symbol"]
        side = trade["side"].lower()
        qty = int(
            trade["quantity"]
        )
        price = float(
            trade["price"]
        )
        key = (
            strategy,
            symbol
        )

        if side == "buy":
            # Track cumulative buy quantity and cost
            if key not in buy_inventory:
                buy_inventory[key] = {"qty": 0, "cost": 0}
            
            buy_inventory[key]["qty"] += qty
            buy_inventory[key]["cost"] += qty * price

        elif side == "sell":
            # Only calculate PnL if we have bought this symbol
            if key in buy_inventory and buy_inventory[key]["qty"] > 0:
                
                # Calculate average buy price
                avg_buy_price = buy_inventory[key]["cost"] / buy_inventory[key]["qty"]
                
                # Only count PnL for quantity actually bought
                sellable_qty = min(qty, buy_inventory[key]["qty"])
                
                pnl = (
                    price - avg_buy_price
                ) * sellable_qty
                
                strategy_pnl[
                    strategy
                ] = (
                    strategy_pnl.get(
                        strategy,
                        0
                    ) + pnl
                )
                
                # Reduce inventory after sell
                buy_inventory[key]["qty"] -= sellable_qty

    return strategy_pnl