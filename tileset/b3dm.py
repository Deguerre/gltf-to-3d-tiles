import json
from .content import Content

class B3dm(Content):
    __MAGIC = b'b3dm'
    __HEADER_LEN = 28

    def __init__(self, *args, **kwargs) -> None:
        super(B3dm, self).__init__(*args, **kwargs)
        if kwargs.get("batch_data", None) is not None:
            self.__batch_data = kwargs["batch_data"]
            del kwargs["batch_data"]
        else:
            self.__batch_data = []

    def _magic(self):
        return B3dm.__MAGIC

    def _header_len(self):
        return B3dm.__HEADER_LEN

    @ property
    def uri(self):
        return self._name + ".b3dm"

    def _batch_json(self):
        batch_json_data = super(B3dm,self)._batch_json()
        for key, value in self.__batch_data:
            batch_json_data[key] = [value]
        return batch_json_data

    def feature_json(self):
        return json.dumps(
            {"BATCH_LENGTH": len(self.__batch_data)},
            separators=(",", ":")).encode("utf-8")

    def as_bytes(self) -> bytes:
        return self._header() + self._body()

