import logging
import time
from config.settings import COINS, RSI_UPPER_THRESHOLD, RSI_LOWER_THRESHOLD
from utils.binance_data import fetch_coin_rsi
from utils.email_utils import send_email

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Track sent alerts
sent_alerts = {}

def check_and_alert():
    """
    Check RSI values for coins and send a single email if thresholds are breached.
    """
    global sent_alerts
    overbought = []
    oversold = []
    current_alerts = {}

    for coin in COINS:
        try:
            rsi = fetch_coin_rsi(coin)
            logger.info(f"{coin} RSI: {rsi}")

            if rsi > RSI_UPPER_THRESHOLD:
                overbought.append(f"{coin} (RSI: {rsi:.2f})")
                current_alerts[coin] = "overbought"
            elif rsi < RSI_LOWER_THRESHOLD:
                oversold.append(f"{coin} (RSI: {rsi:.2f})")
                current_alerts[coin] = "oversold"
        except Exception as e:
            logger.error(f"Error fetching RSI for {coin}: {str(e)}")

    if overbought or oversold:
        message_body = ""
        if overbought:
            message_body += "Overbought coins:\n" + "\n".join(overbought) + "\n\n"
        if oversold:
            message_body += "Oversold coins:\n" + "\n".join(oversold)

        if current_alerts != sent_alerts:
            try:
                send_email("RSI Alert", message_body)
                logger.info("Email sent successfully.")
                sent_alerts.update(current_alerts)
            except Exception as e:
                logger.error(f"Error sending email: {str(e)}")

def main():
    """
    Continuously monitor coins and send alerts every 45 seconds.
    """
    while True:
        check_and_alert()
        time.sleep(45)

if __name__ == "__main__":
    main()
