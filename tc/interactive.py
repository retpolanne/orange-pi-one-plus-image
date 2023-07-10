import tbot
import time


@tbot.testcase
def test_uboot_mdio_contains_phy() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        mdio = ub.exec0("mdio", "list")
        assert "Generic PHY" in mdio

@tbot.testcase
def test_uboot_gmac_regulator() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        # This line will probe both regulators!
        ub.exec0("regulator", "status")
        ub.exec0("regulator", "dev", "vcc-gmac-3v3")
        reg_status = ub.exec0("regulator", "status")
        assert "enable" in reg_status
        reg_status_enabled = False
        for line in reg_status.split("\n"):
            if "enable" in line:
                reg_status_enabled = True
        assert reg_status_enabled

@tbot.testcase
def test_uboot_gmac_regulator_dm() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        dm_tree = ub.exec0("dm", "tree")
        assert "3v3" in dm_tree
        reg_5v5_probed = False
        reg_3v3_probed = False
        for line in dm_tree.split("\n"):
            if "vcc5v" in line:
                reg_5v5_probed = ("+" in line)
            if "gmac-3v3" in line:
                reg_3v3_probed = ("+" in line)
        assert reg_5v5_probed
        assert reg_3v3_probed

@tbot.testcase
def test_uboot_pinmux_pd6() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        pinmux = ub.exec0("pinmux", "status", "PD6")
        assert "gpio output" in pinmux

@tbot.testcase
def test_uboot_dhcp() -> None:
    with tbot.ctx.request(tbot.role.BoardUBoot) as ub:
        ub.exec0("dhcp")
