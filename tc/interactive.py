import tbot

@tbot.testcase
def test_uboot_dhcp() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        ub.exec0("dhcp")
