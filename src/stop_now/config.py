from mcdreforged.api.utils.serializer import Serializable

class Configuration(Serializable):
    timeout: int = 5
    pattern: str = 'All dimensions are saved$'
