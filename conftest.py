import pytest
import tbot
from tbot import newbot

def pytest_addoption(parser, pluginmanager):
    parser.addoption("--tbot-config", action="append", default=[], dest="tbot_configs")
    parser.addoption("--tbot-flag", action="append", default=[], dest="tbot_flags")

def pytest_configure(config):
    # Only register configuration when nobody else did so already.
    if not tbot.ctx.is_active():
        # Register flags
        for tbot_flag in config.option.tbot_flags:
            tbot.flags.add(tbot_flag)
        # Register configurations
        for tbot_config in config.option.tbot_configs:
            newbot.load_config(tbot_config, tbot.ctx)

@pytest.fixture(scope="session", autouse=True)
def tbot_ctx(pytestconfig):
    with tbot.ctx:
        # Configure the context for keep_alive (so machines can be reused
        # between tests).  reset_on_error_by_default will make sure test
        # failures lead to a powercycle of the DUT anyway.
        with tbot.ctx.reconfigure(keep_alive=True, reset_on_error_by_default=True):
            # Tweak the standard output logging options
            with tbot.log.with_verbosity(tbot.log.Verbosity.STDOUT, nesting=1):
                yield tbot.ctx
