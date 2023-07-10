import re
import tbot
import time
from tbot.machine import board, connector

class OrangePi(
    connector.ConsoleConnector,
    board.Board
):
    baudrate = 115200
    serial_port = "/dev/ttyUSB0"

    def connect(self, mach):
        return mach.open_channel("picocom", "-b", str(self.baudrate), self.serial_port)


class OrangePiUBoot(
    board.Connector,
    board.PowerControl,
    board.UBootAutobootIntercept,
    board.UBootShell
):
    prompt = "=> "

    def poweron(self):
        time.sleep(1)
        self.ch.sendline("reset")

    def poweroff(self):
        pass


def register_machines(ctx):
    ctx.register(OrangePi, tbot.role.Board)
    ctx.register(OrangePiUBoot, tbot.role.BoardUBoot)
