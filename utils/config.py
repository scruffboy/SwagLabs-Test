class Config:
    """
    Configuration class for SwagLabs UI tests
    """

    # Main link for SwagLabs Tests
    BASE_URL = "https://www.saucedemo.com"
    INVENTORY_URL = f"{BASE_URL}/inventory.html"

    # Timeouts in ms
    DEFAULT_TIMEOUT = 5000
    PERFORMANCE_TIMEOUT = 10000
