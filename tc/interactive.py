import tbot
import time

@tbot.testcase
def test_uboot_dhcp() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        ub.exec0("regulator", "dev", "vcc-gmac-3v3")
        ub.exec0("regulator", "enable")
        ub.exec0("setenv", "autoload", "no")
        time.sleep(5)
        ub.exec0("dhcp")
