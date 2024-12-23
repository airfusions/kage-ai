from typing import List, Dict
from phi.tools import Toolkit
from phi.utils.log import logger
import json
class PortfolioTools(Toolkit):
    def __init__(self):
        super().__init__(name="shell_tools")
        self.register(self.get_dummy_data)

    def get_dummy_data(self) -> str:

        dummy_data = {
            "name": "Dummy User",
            "age": 30,
            "city": "Exampleville",
            "crypto_portfolio": {
                "tokens": [
                    {"symbol": "BTC", "amount": 0.5, "value_usd": 30000},
                    {"symbol": "ETH", "amount": 3.0, "value_usd": 5000},
                    {"symbol": "ADA", "amount": 1000, "value_usd": 500},
                     {"symbol": "SOL", "amount": 100, "value_usd": 1500},
                     {"symbol": "DOGE", "amount": 10000, "value_usd": 900}
                ],
                "total_value_usd": 37900,
            },
            "hobbies": ["coding", "reading", "hiking"],
        }
        return json.dumps(dummy_data, indent=2)