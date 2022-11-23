import json
from .content import Content

class B3dm(Content):
    __MAGIC = b'b3dm'
    __HEADER_LEN = 28

    def __init__(self, **kwargs) -> None:
        self._batch_data = []
        super().__init__(False, **kwargs)

    def _magic(self):
        return B3dm.__MAGIC

    def _header_len(self):
        return B3dm.__HEADER_LEN

    @ property
    def uri(self):
        return self._name + ".b3dm"

    def _batch_json(self):
        var batch_json_data = super()._batch_json()
        return batch_json_data

    def feature_json(self):
        return json.dumps(
            {"BATCH_LENGTH": self._batch_json_len()},
            separators=(",", ":")).encode("utf-8")

    def as_bytes(self) -> bytes:
        return self._header() + self._body()
