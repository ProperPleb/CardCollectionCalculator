import sys
import logging
import json
import jsonpickle
import util

from rest import Rest
from python.request_dto import *


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

        detail_view = util.DetailViewUtil.instantiateDetailViewDTO()

        json_str: str = util.JSONUtil.overrideVariableNames(jsonpickle.encode(grid, unpicklable=False))
        query = "diabellstar the black witch"
        logger.info(json_str)
        # logger.info(r.getGrid(json_str, query).content)

        json_str: str = util.JSONUtil.overrideVariableNames(jsonpickle.encode(detail_view, unpicklable=False))
        logger.info(json_str)
        # logger.info(r.getDetailView(json_str, str(558188)).content)

        util.ExcelUtil.excelMapper()
    except Exception as e:
        logger.exception(e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
