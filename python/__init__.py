import sys
import logging
import json
import jsonpickle
import util

from rest import Rest
from data_model.dto.request_dto import *


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
        logger.info(util.JSONUtil.overrideVariableNames(json_str))
        logger.info(json_str)

        detail_view = util.DetailViewUtil.instantiateDetailViewDTO()
        json_str = jsonpickle.encode(detail_view, unpicklable=False)
        logger.info(util.JSONUtil.overrideVariableNames(json_str))
        logger.info(json_str)

        logger.info(r.urlSetup("host.action.query.prefix", "host.action.query.suffix"))
        logger.info(r.urlSetup("host.action.query.prefix", "host.action.query.suffix", "diabellstar the black witch".replace(" ", "+")))
        logger.info(r.urlSetup("host.action.list.prefix", "host.action.list.suffix", str(558188)))

        json_str: str = util.JSONUtil.overrideVariableNames(jsonpickle.encode(grid, unpicklable=False))
        query = "diabellstar the black witch"
        logger.info(json_str)
        logger.info(query.replace(" ", "+"))
        logger.info(json.loads(json_str))
        logger.info(r.getGrid(json_str, query).content)
    except Exception as e:
        logger.exception(e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
