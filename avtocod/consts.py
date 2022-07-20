from typing import Dict, Final

AVTOCOD_URI: Final[str] = "https://profi.avtocod.ru/"
AVTOCOD_API: Final[str] = "https://api-profi.avtocod.ru/rpc"
HEADERS: Final[Dict[str, str]] = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": AVTOCOD_URI,
    "Referer": AVTOCOD_API,
}
