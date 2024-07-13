import sys
import logging
import json
import jsonpickle
import util

from rest import Rest
from data_model.dto.grid_dto import *


def main() -> int:
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    try:
        r = Rest()
        grid = util.GridUtil.instantiateGridDTO()
        json_str: str = jsonpickle.encode(grid, unpicklable=False)
        logger.info(util.JSONUtil.removeNameUnderscores(json_str))
        logger.info(json_str)
        # logger.info(r.ping("https://google.com"))
    except Exception as e:
        logger.exception(e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
