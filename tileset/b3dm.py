import json
from .content import Content

class B3dm(Content):
    __MAGIC = b'b3dm'
    __HEADER_LEN = 28

    def __init__(self, *args, **kwargs) -> None:
        super(B3dm, self).__init__(*args, **kwargs)
        self._batch_data = [{
            "GUID":"3pJ76nj9n83RbqhUZBfhIy",
            "IFC Type":"IfcWall",
            "name":"Basic Wall:Kennel Wall 50mm:3538",
            "ObjectPlacement":"0 -1 0 0 1 0 0 0 0 0 1 0 124.0172505308301 1310.128241636344 50.171319348236203 1",
            "ObjectType":"Basic Wall:Kennel Wall 50mm",
            "PredefinedType":"NOTDEFINED",
            "Tag":"3538",
            "layers":["A-WALL-____-OTLN"],
            "materials":["IfcMaterial_329"],
            "propertySets":["3XRvp$lR1CNeXaFUbN51A5","28VWihCDPEx8X3$UowqiYi","3pJ76nj9n83RbqfXNBfhIy"],
            "types":["3pJ76nj9n83RbqhUZBfhTD"]
        }, {
            "GUID":"3pJ76nj9n83RbqhUZBfhUn",
            "IFC Type":"IfcWall",
            "name":"Basic Wall:Kennel Wall 50mm:3807",
            "ObjectPlacement":"0 -1 0 0 1 0 0 0 0 0 1 0 1324.0172505308196 1310.128241636334 50.171319348236203 1",
            "ObjectType":"Basic Wall:Kennel Wall 50mm",
            "PredefinedType":"NOTDEFINED",
            "Tag":"3807",
            "layers":["A-WALL-____-OTLN"],
            "materials":["IfcMaterial_329"],
            "propertySets":["2OzdGuIpH2kenpU8MAO5nE","3foYTuTZzEhezfcg7wVird","3pJ76nj9n83RbqfXNBfhUn"],
            "types":["3pJ76nj9n83RbqhUZBfhTD"],
        }, {
            "GUID":"3pJ76nj9n83RbqhUZBfhPn",
            "IFC Type":"IfcWall",
            "name":"Basic Wall:Kennel Wall 50mm:3871",
            "ObjectPlacement":"-1 0 0 0 0 -1 0 0 0 0 1 0 1299.0172505308196 125.128241636339 50.171319348236203 1",
            "ObjectType":"Basic Wall:Kennel Wall 50mm",
            "PredefinedType":"NOTDEFINED",
            "Tag":"3871",
            "layers":["A-WALL-____-OTLN"],
            "materials":["IfcMaterial_329"],
            "propertySets":["12GPu5ghDEG9O45LGSVVhw","0Imrv5egD1kgAli8VQVJoV","3pJ76nj9n83RbqfXNBfhPn"],
            "types":["3pJ76nj9n83RbqhUZBfhTD"],
        }, {
            "GUID":"3pJ76nj9n83RbqhUZBfhOf",
            "IFC Type":"IfcWall",
            "name":"Basic Wall:Kennel Wall 50mm:3911",
            "ObjectPlacement":"1 0 0 0 0 1 0 0 0 0 1 0 149.0172505308301 1285.128241636344 50.171319348236203 1",
            "ObjectType":"Basic Wall:Kennel Wall 50mm",
            "PredefinedType":"NOTDEFINED",
            "Tag":"3911",
            "layers":["A-WALL-____-OTLN"],
            "materials":["IfcMaterial_329"],
            "propertySets":["13rj8rkfn9SvpGBT8wcF5K","3o5J9RrM57kgp4hHeHZC9y","3pJ76nj9n83RbqfXNBfhOf"],
            "types":["3pJ76nj9n83RbqhUZBfhTD"],
        }, {
            "GUID":"3pJ76nj9n83RbqhUhBfhOD",
            "IFC Type":"IfcSlab",
            "name":"Basic Roof:Kennel Roof:3939",
            "ObjectPlacement":"1 0 0 0 0 1 0 0 0 0 1 0 -0.98274946917990746 0.12824163633899843 692.43629242927329 1",
            "ObjectType":"Basic Roof:Kennel Roof",
            "PredefinedType":"ROOF",
            "Tag":"3939",
            "layers":["A-ROOF-____-OTLN"],
            "materials":["IfcMaterial_850"],
            "propertySets":["3TNNssrWj37RffDHwiYd__","1jfdDckJX5oul5EpFFvigM","3pJ76nj9n83RbqfXFBfhOD"],
            "types":["3pJ76nj9n83RbqhUZBfhR8"],
        }, {
            "GUID":"3pJ76nj9n83RbqhUlBfhOD",
            "IFC Type":"IfcSlab",
            "name":"Basic Roof:Kennel Roof:3939",
            "ObjectPlacement":"1 0 0 0 0 1 0 0 0 0 1 0 -0.98274946917990746 0.12824163633899843 692.43629242927329 1",
            "ObjectType":"Basic Roof:Kennel Roof",
            "PredefinedType":"ROOF",
            "Tag":"3939",
            "layers":["A-ROOF-____-OTLN"],
            "materials":["IfcMaterial_850"],
            "propertySets":["2t$xonxg96bRWsYxh5FgK9","33gN0MOBbCD8Ar8XnVaw_O","3F3JyxDUrFtwP0ZaZ5RBc$"],
            "types":["3$5vpeOK134emwhsMJcrfu"],
        }, {
            "GUID":"3pJ76nj9n83RbqhUZBfgZ3",
            "IFC Type":"IfcSlab",
            "name":"Floor:Kennel Floor 50mm:4525",
            "ObjectPlacement":"1 0 0 0 0 1 0 0 0 0 1 0 -2903.68741305088 -547.36571511348598 50.171319348236203 1",
            "ObjectType":"Floor:Kennel Floor 50mm",
            "PredefinedType":"FLOOR",
            "Tag":"4525",
            "layers":["A-FLOR-____-OTLN"],
            "materials":["IfcMaterial_995"],
            "propertySets":["370u2wdPDAYvRZVTHGIs8N","0vYigZ2lrCsw5lyPRJI2He","3pJ76nj9n83RbqfXFBfgZ3"],
            "types":["3pJ76nj9n83RbqhUZBfgYh"]
        }]

# "extensions":{"3DTILES_batch_table_hierarchy":{"instancesLength":7,"classes":[{"name":"3pJ76nj9n83RbqhUZBfhIy","length":1,"instances":{"_bbox":["[-2253029.39765054,4770915.644159853,-3571619.976734421,-2253028.798549994,4770916.802204468,-3571618.566224917]"]}},{"name":"3pJ76nj9n83RbqhUZBfhUn","length":1,"instances":{"_bbox":["[-2253030.470970784,4770915.128510029,-3571619.9817472426,-2253029.8820565795,4770916.308040005,-3571618.571455689]"]}},{"name":"3pJ76nj9n83RbqhUZBfhPn","length":1,"instances":{"_bbox":["[-2253030.1515143127,4770915.1499954425,-3571620.166195554,-2253028.8436961025,4770916.215109578,-3571619.524952785]"]}},{"name":"3pJ76nj9n83RbqhUZBfhOf","length":1,"instances":{"_bbox":["[-2253030.4360111337,4770915.738067527,-3571619.207685483,-2253029.1281928946,4770916.803181752,-3571618.5664428673]"]}},{"name":"3pJ76nj9n83RbqhUhBfhOD","length":1,"instances":{"_bbox":["[-2253030.078873601,4770916.137833561,-3571620.28133959,-2253028.9103676286,4770916.897018406,-3571618.844854497]"]}},{"name":"3pJ76nj9n83RbqhUlBfhOD","length":1,"instances":{"_bbox":["[-2253030.585788592,4770915.514756631,-3571620.28133959,-2253029.712689874,4770916.897018406,-3571618.8511750125]"]}},{"name":"3pJ76nj9n83RbqhUZBfgZ3","length":1,"instances":{"_bbox":["[-2253030.3387800627,4770914.997482321,-3571619.654564682,-2253028.666088733,4770916.372731941,-3571618.45500102]"]}}],"classIds":[0,1,2,3,4,5,6]}}}

    def _magic(self):
        return B3dm.__MAGIC

    def _header_len(self):
        return B3dm.__HEADER_LEN

    @ property
    def uri(self):
        return self._name + ".b3dm"

    def _batch_json(self):
        batch_json_data = super()._batch_json()
        return batch_json_data

    def feature_json(self):
        return json.dumps(
            {"BATCH_LENGTH": self._batch_json_len()},
            separators=(",", ":")).encode("utf-8")

    def as_bytes(self) -> bytes:
        return self._header() + self._body()
