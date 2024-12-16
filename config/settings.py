# Configuration for the stock alert app

# Email settings
EMAIL_SENDER = "@gmail.com"
EMAIL_PASSWORD = ""  # Use app passwords for Gmail or secure equivalents
EMAIL_RECEIVER = "@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Coins and thresholds
COINS = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT"]
RSI_UPPER_THRESHOLD = 70  # RSI threshold for overbought
RSI_LOWER_THRESHOLD = 30  # RSI threshold for oversold


# Binance settings
BINANCE_API_KEY = ""  # Leave empty for public data
BINANCE_API_SECRET = ""  # Leave empty for public data
