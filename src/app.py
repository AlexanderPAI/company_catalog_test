import logging

import uvicorn

from src.interfaces.api.endpoints import app

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
