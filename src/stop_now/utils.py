from mcdreforged.api.types import ServerInterface


def tr(key, *args, **kwargs):
    return psi.rtr(f'foo_bar.{key}', *args, **kwargs)


psi = ServerInterface.get_instance().as_plugin_server_interface()
