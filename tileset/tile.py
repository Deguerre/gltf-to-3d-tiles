from .b3dm import B3dm
from .i3dm import I3dm
from functools import cached_property
from utils import Box3, Matrix4
from enum import Enum

FOOT_TO_METER_MULTIPLIER = 0.3084


class Measure(str, Enum):
    METER = "meter"
    FOOT = "foot"


# "extensions":{"3DTILES_batch_table_hierarchy":{"instancesLength":7,"classes":[{"name":"3pJ76nj9n83RbqhUZBfhIy","length":1,"instances":{"_bbox":["[-2253029.39765054,4770915.644159853,-3571619.976734421,-2253028.798549994,4770916.802204468,-3571618.566224917]"]}},{"name":"3pJ76nj9n83RbqhUZBfhUn","length":1,"instances":{"_bbox":["[-2253030.470970784,4770915.128510029,-3571619.9817472426,-2253029.8820565795,4770916.308040005,-3571618.571455689]"]}},{"name":"3pJ76nj9n83RbqhUZBfhPn","length":1,"instances":{"_bbox":["[-2253030.1515143127,4770915.1499954425,-3571620.166195554,-2253028.8436961025,4770916.215109578,-3571619.524952785]"]}},{"name":"3pJ76nj9n83RbqhUZBfhOf","length":1,"instances":{"_bbox":["[-2253030.4360111337,4770915.738067527,-3571619.207685483,-2253029.1281928946,4770916.803181752,-3571618.5664428673]"]}},{"name":"3pJ76nj9n83RbqhUhBfhOD","length":1,"instances":{"_bbox":["[-2253030.078873601,4770916.137833561,-3571620.28133959,-2253028.9103676286,4770916.897018406,-3571618.844854497]"]}},{"name":"3pJ76nj9n83RbqhUlBfhOD","length":1,"instances":{"_bbox":["[-2253030.585788592,4770915.514756631,-3571620.28133959,-2253029.712689874,4770916.897018406,-3571618.8511750125]"]}},{"name":"3pJ76nj9n83RbqhUZBfgZ3","length":1,"instances":{"_bbox":["[-2253030.3387800627,4770914.997482321,-3571619.654564682,-2253028.666088733,4770916.372731941,-3571618.45500102]"]}}],"classIds":[0,1,2,3,4,5,6]}}}

class Tile:
    measure = Measure.METER
    BATCH_DATA = {
      "3pJ76nj9n83RbqhUZBfhIy": {
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
      },
      "3pJ76nj9n83RbqhUZBfhUn": {
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
      },
      "3pJ76nj9n83RbqhUZBfhPn": {
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
    },
    "3pJ76nj9n83RbqhUZBfhOf": {
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
    },
    "3pJ76nj9n83RbqhUhBfhOD": {
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
    },
    "3pJ76nj9n83RbqhUlBfhOD":{
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
    },
    "3pJ76nj9n83RbqhUZBfgZ3": {
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
      }
    }

    def __init__(self, *, content_id=None, refine=None, matrix=Matrix4(), box=Box3(), instance_box=Box3(), instances_matrices=None, gltf=None, extras=None, name=None) -> None:
        self.refine = refine
        self.__content_id = content_id
        # self.__content = None
        self.__matrix = matrix.clone()
        self.__content_matrices = instances_matrices
        self.__instance_box = instance_box
        self.__box = box.clone()
        self.__children = []
        self.__gltf = gltf
        self.__extras = extras
        self.__name = name
        self.__batch_data = Tile.BATCH_DATA.get(name, None)
        # self.__parse_children()

    def add_child(self, tile):
        if not tile:
            return self

        self.__children.append(tile)
        self.__box.union(tile.box_world)
        return self

    def add_children(self, children):
        if not children:
            return self

        for child in children:
            self.add_child(child)
        return self

    def add_content_matrix(self, matrix):
        self.__content_matrices.append(matrix)

    @property
    def content(self):
        if 1 < len(self.__content_matrices):
            return I3dm(str(self.__content_id),
                        self.__gltf, self.__content_matrices, extras=self.__extras)
        else:
            return B3dm(str(self.__content_id), self.__gltf, extras=self.__extras, batch_data=self.__batch_data)

    @property
    def __content_matrix(self):
        if self.__content_matrices and 1 == len(self.__content_matrices):
            return self.__content_matrices[0]

        return Matrix4()

    @property
    def __content_box(self):
        box = Box3()
        if 1 < len(self.__content_matrices):
            for matrix in self.__content_matrices:
                box.union(
                    self.__instance_box.clone().apply_matrix4(matrix.matrix))
            return box

        return self.__instance_box

    @property
    def size(self):
        return self.box.size

    @property
    def centroid(self):
        return self.box.center

    @property
    def matrix(self):
        return self.__matrix.clone().multiply(self.__content_matrix)

    def apply_matrix4(self, matrix):
        self.__matrix.premultiply(matrix)
        return self

    @property
    def children(self):
        return self.__children

    @property
    def box(self):
        return self.__box if self.__content_id is None else self.__box.clone().union(self.__content_box)

    @cached_property
    def box_world(self):
        return self.box.clone().apply_matrix4(self.matrix.matrix)

    @property
    def centroid_world(self):
        return self.box_world.center

    @property
    def geometric_error(self):
        if self.__content_id is None:
            return max(list(map(lambda tile: tile.geometric_error, self.__children)))

        if Tile.measure is Measure.FOOT:
            return self.__instance_box.diagonal * FOOT_TO_METER_MULTIPLIER

        return self.__instance_box.diagonal

    @property
    def dict(self):
        ret = {
            "boundingVolume": {"box": self.box.list},
            "geometricError": self.geometric_error,
            "refine": self.refine}

        if not self.matrix.is_identity:
            ret["transform"] = self.matrix.list

        if self.__content_id is not None:
            ret["content"] = self.content.dict

        if self.children:
            ret["children"] = [
                child.dict for child in self.children]

        return {k: v for k, v in ret.items() if v is not None}
