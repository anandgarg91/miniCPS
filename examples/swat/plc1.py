"""
plc1.py

plc init:
    cpppo enip server

plc main loop:
    sequential read/write from/to the state db and its internal cpppo enip
    server.

"""
import sqlite3
import os
import time

from constants import logger
from constants import P1_PLC1_TAGS, LIT_101, LIT_301, FIT_201
from constants import read_single_statedb, update_statedb
from constants import write_cpppo, read_cpppo, init_cpppo_server
from constants import L1_PLCS_IP
from constants import T_PLC_R, T_PLC_W


if __name__ == '__main__':
    """
    Init cpppo enip server.

    Execute an infinite routine loop
        - bla
        - bla
    """

    # init the ENIP server
    tags = []
    tags.extend(P1_PLC1_TAGS)
    # tags.extend(P2_PLC1_TAGS)
    # time.sleep(0.5)
    init_cpppo_server(tags)
    
    write_cpppo(L1_PLCS_IP['plc1'], 'DO_MV_101_CLOSE', '1')

    val = read_cpppo(L1_PLCS_IP['plc1'], 'DO_MV_101_CLOSE', 'examples/swat/plc1_cpppo.cache')
    logger.debug("read_cpppo: %s" % val)

    # synch with plc2, plc3
    # time.sleep(1)

    # look a Stridhar graph
    while True:
        # cmd = read_single_statedb('AI_FIT_101_FLOW', '1')
        logger.debug("plc1 main loop")
        break

