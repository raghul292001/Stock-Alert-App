import ccxt
import pandas as pd

def fetch_coin_rsi(coin: str, timeframe: str = "1h", period: int = 14) -> float:
    """
    Fetch the RSI for a given coin using Binance data.

    :param coin: The cryptocurrency pair (e.g., "BTC/USDT").
    :param timeframe: The Binance timeframe (e.g., "1m", "1h", "1d").
    :param period: The RSI calculation period.
    :return: The RSI value as a float.
    """
    try:
        # Initialize Binance API
        exchange = ccxt.binance()
        
        # Fetch historical OHLCV data
        ohlcv = exchange.fetch_ohlcv(coin, timeframe)
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        
        # Calculate RSI
        delta = df["close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi.iloc[-1]  # Return the latest RSI value
    except Exception as e:
        raise RuntimeError(f"Error fetching RSI for {coin}: {str(e)}")
