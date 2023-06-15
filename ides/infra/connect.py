from opensearchpy import OpenSearch
from opensearch_dsl import Search


class MetaSingleton(type):
    _instances = []
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class OpenSearchConnect(metaclass=MetaSingleton):
    connection = None
    def connect(self, host, port, auth):
        if self.connection is None:
            self.connect = OpenSearch(
                hosts = [{'host': host, 'port': port}],
                http_compress = True, # enables gzip compression for request bodies
                http_auth = auth,
                use_ssl = True,
                )
        return self.connection
