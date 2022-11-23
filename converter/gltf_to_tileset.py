import json
import numpy as np
import math
from gltf.gltf import Axis, Gltf
from tileset import Tile, Tileset, Measure
from pathlib import Path
from gltf import Slicer, io
from utils import Box3, Matrix4


def build_bvh(tiles):
    split = -1
    min_cost = math.inf
    split_axis = -1

    if len(tiles) < 3:
        return Tile().add_children(tiles)

    for axis in range(3):
        sorted_tiles = sorted(
            tiles, key=lambda tile: tile.centroid_world[axis])
        left_box = Box3()
        right_box = Box3()
        left_cost = [0] * (len(sorted_tiles) - 1)
        right_cost = [0] * (len(sorted_tiles) - 1)
        for i in range(len(sorted_tiles)-1):
            left_box.union(sorted_tiles[i].box_world)
            right_box.union(sorted_tiles[-i-1].box_world)
            left_cost[i] = sah_cost(left_box.size, i + 1)
            right_cost[-i-1] = sah_cost(right_box.size, i + 1)
        costs = list(
            map(lambda l, r: l + r, left_cost, right_cost))
        min_cost_axis = min(costs)
        if min_cost_axis < min_cost:
            min_cost = min_cost_axis
            split = np.argmin(costs) + 1
            split_axis = axis

    sorted_tiles = sorted(
        tiles, key=lambda tile: tile.centroid_world[split_axis])
    return Tile().add_child(build_bvh(sorted_tiles[:split])).add_child(build_bvh(sorted_tiles[split:]))


def sah_cost(size, count):
    return (size[0] * size[1] + size[1] * size[2] + size[2] * size[0]) * count


def split_group(source):
    tiles = source[:]
    length = len(tiles)
    if 1 == length:
        return [tiles[0]]

    if 2 == length:
        return [Tile().add_child(tiles.pop()).add_child(tiles.pop())]

    groups = []
    while tiles:
        box = tiles[-1].box_world
        group = list(filter(lambda tile: box.contains(tile.box_world), tiles))
        tile = Tile().add_child(group.pop())
        if group:
            tile.add_children(split_group(group))

        groups.append(tile)

        tiles = list(
            filter(lambda tile: not box.contains(tile.box_world), tiles))

    return groups

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
# "extensions":{"3DTILES_batch_table_hierarchy":{"instancesLength":7,"classes":[{"name":"3pJ76nj9n83RbqhUZBfhIy","length":1,"instances":{"_bbox":["[-2253029.39765054,4770915.644159853,-3571619.976734421,-2253028.798549994,4770916.802204468,-3571618.566224917]"]}},{"name":"3pJ76nj9n83RbqhUZBfhUn","length":1,"instances":{"_bbox":["[-2253030.470970784,4770915.128510029,-3571619.9817472426,-2253029.8820565795,4770916.308040005,-3571618.571455689]"]}},{"name":"3pJ76nj9n83RbqhUZBfhPn","length":1,"instances":{"_bbox":["[-2253030.1515143127,4770915.1499954425,-3571620.166195554,-2253028.8436961025,4770916.215109578,-3571619.524952785]"]}},{"name":"3pJ76nj9n83RbqhUZBfhOf","length":1,"instances":{"_bbox":["[-2253030.4360111337,4770915.738067527,-3571619.207685483,-2253029.1281928946,4770916.803181752,-3571618.5664428673]"]}},{"name":"3pJ76nj9n83RbqhUhBfhOD","length":1,"instances":{"_bbox":["[-2253030.078873601,4770916.137833561,-3571620.28133959,-2253028.9103676286,4770916.897018406,-3571618.844854497]"]}},{"name":"3pJ76nj9n83RbqhUlBfhOD","length":1,"instances":{"_bbox":["[-2253030.585788592,4770915.514756631,-3571620.28133959,-2253029.712689874,4770916.897018406,-3571618.8511750125]"]}},{"name":"3pJ76nj9n83RbqhUZBfgZ3","length":1,"instances":{"_bbox":["[-2253030.3387800627,4770914.997482321,-3571619.654564682,-2253028.666088733,4770916.372731941,-3571618.45500102]"]}}],"classIds":[0,1,2,3,4,5,6]}}}

def gltf_to_tileset(fin, fout, measure: Measure = Measure.METER, up_direction: Axis = Axis.Y, batch_data_table = {}):
    Gltf.up_direction = up_direction
    gltf, buffers = io.read_gltf(fin)
    Path(fout).parent.mkdir(parents=True, exist_ok=True)
    gltf_slicer = Slicer(gltf, buffers=buffers)
    Tile.measure = measure
    tiles = list(map(lambda id: Tile(content_id=id, instance_box=gltf_slicer.get_bounding_box(
        id), instances_matrices=gltf_slicer.get_matrices(id), matrix=Matrix4(), gltf=gltf_slicer.slice_mesh(id).as_bytes(), batch_data=BATCH_DATA.get(gltf_slicer.get_name(id), None), extras=gltf_slicer.get_extras(id)), range(gltf_slicer.meshes_count)))
    tiles.sort(key=lambda tile: tile.box_world.diagonal)
    grouped_tiles = split_group(tiles)
    root = build_bvh(grouped_tiles)

    root.refine = "ADD"
    tileset = Tileset(root)
    with open(fout, "w") as f:
        json.dump(tileset.dict, f, separators=(",", ":"))

    for tile in tiles:
        with open(Path(fout).parent / tile.content.uri, "wb") as f:
            f.write(tile.content.as_bytes())

    io.copy_textures(fin, fout, gltf.images)
