import re
import time

from mcdreforged.api.decorator import new_thread, spam_proof
from mcdreforged.api.types import Info, PluginServerInterface

import stop_now.constants as constants
from stop_now.config import Configuration
from stop_now.utils import psi, tr

config: Configuration
server_stopped = False


@new_thread(constants.PLUGIN_ID)
def on_info(server: PluginServerInterface, info: Info):
    if not info.is_user and re.match(config.pattern, info.content):
        kill_server()


@spam_proof
def kill_server():
    timeout = config.timeout * 5
    with timeout and not server_stopped:
        timeout -= 1
        time.sleep(0.2)
        psi.start
    psi.kill()


def on_server_start(server: PluginServerInterface):
    global server_stopped
    server_stopped = False


def on_server_stop(server: PluginServerInterface, server_return_code: int):
    global server_stopped
    server_stopped = True


def on_load(server: PluginServerInterface, prev_module):
    global config, server_stopped
    server_stopped = not server.is_server_running()
    config = server.load_config_simple(target_class=Configuration)
