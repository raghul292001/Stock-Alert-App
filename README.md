# Crypto RSI Alert Bot 📈🚀

**Crypto RSI Alert Bot** is a Python-based application that monitors the Relative Strength Index (RSI) of selected cryptocurrencies using the Binance API and sends email alerts when RSI values cross predefined thresholds. This helps traders stay informed about overbought or oversold conditions in real-time.

---

## Features

- 🛠 **Customizable RSI Thresholds**: Configure upper and lower RSI thresholds for alerts.
- 📊 **Supports Multiple Cryptocurrencies**: Track RSI values for pairs like BTC/USDT, ETH/USDT, and more.
- 📭 **Email Notifications**: Receive consolidated email alerts for multiple coins that breach thresholds.
- 🔄 **Continuous Monitoring**: Automatically checks RSI values every 45 seconds.
- 🔒 **Free & Open-Source**: Completely free to use with no restrictions.

---

## How It Works

1. The app fetches RSI values for selected cryptocurrency pairs using the Binance API.
2. Compares the RSI values against user-defined thresholds:
   - **Overbought**: RSI exceeds the upper threshold.
   - **Oversold**: RSI falls below the lower threshold.
3. Sends a single email notification if one or more coins breach the thresholds.
4. Runs continuously, checking RSI values every 45 seconds.

---

## Folder Structure

```plaintext
project/
├── config/
│   └── settings.py       # Configure RSI thresholds, coins, and email settings
├── logs/
│   └── app.log           # Log file for monitoring
├── main.py               # Entry point for the app
├── utils/
│   ├── binance_data.py   # Fetch RSI data from Binance
│   ├── email_utils.py    # Utility to send email alerts
└── requirements.txt      # List of dependencies
```

---

## Configuration

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-rsi-alert-bot.git
   cd crypto-rsi-alert-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your settings in `config/settings.py`:
   - Add the cryptocurrency pairs (e.g., `"BTC/USDT"`, `"ETH/USDT"`).
   - Set RSI thresholds (`RSI_UPPER_THRESHOLD`, `RSI_LOWER_THRESHOLD`).
   - Enter your email credentials for notifications.

---

## Usage

Run the application with:

```bash
python main.py
```

The app will continuously monitor RSI values and log real-time data in the console and `logs/app.log`.

---

## Example Email Alert

**Subject**: RSI Alert  
**Body**:

```plaintext
Overbought coins:
BTC/USDT (RSI: 72.35)
ETH/USDT (RSI: 71.22)

Oversold coins:
LTC/USDT (RSI: 28.45)
```

---

## Dependencies

- `ccxt` (Binance API integration)
- `pandas` (Data processing)
- `smtplib` (Email functionality)

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality.

---

## License

This project is licensed under the **MIT License**.
