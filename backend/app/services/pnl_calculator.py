from app.services.csv_processor import read_csv_rows

def calculate_pnl(file_path):

    strategy_pnl = {}

    buy_prices = {}

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

            buy_prices[key] = price

        elif side == "sell":

            if key in buy_prices:

                pnl = (
                    price -
                    buy_prices[key]
                ) * qty

                strategy_pnl[
                    strategy
                ] = (
                    strategy_pnl.get(
                        strategy,
                        0
                    ) + pnl
                )

    return strategy_pnl