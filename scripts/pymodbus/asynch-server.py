#!/usr/bin/env python2

# use /usr/bin/env python to run it on ubuntu
# taken from the official doc pdf

# import the various server implementations
from pymodbus.server.async import StartTcpServer
from pymodbus.server.async import StartUdpServer
from pymodbus.server.async import StartSerialServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# configure the service logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# initialize your data store
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17] * 100),
    co=ModbusSequentialDataBlock(0, [17] * 100),
    hr=ModbusSequentialDataBlock(0, [17] * 100),
    ir=ModbusSequentialDataBlock(0, [17] * 100))
context = ModbusServerContext(slaves=store, single=True)

# run the server you want
StartTcpServer(context)
# StartUdpServer(context)
# StartSerialServer(context, port='/tmp/tty1')
