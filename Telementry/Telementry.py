import math
from ._MapObjects import MapObjects, Object
from ._Indicators import _Indicators
from ._State import _State
from ._MapInfo import _MapInfo
from ._call import _call
class _Telementry:
    def __init__(self):

        self.fetch_thread = _call()
        self.fetch_thread.start_fetch_thread()

        self.MapObjects = MapObjects
        self.Indicators = _Indicators
        self.State = _State
        self.MapInfo = _MapInfo


    def real_distance(self, x, y):
        map_max = self.MapInfo.data.map_max
        map_min = self.MapInfo.data.map_min
        wx = map_min[0] + x * (map_max[0] - map_min[0])
        wy = map_min[1] + y * (map_max[1] - map_min[1])
        return wx, wy


    def distance_2_points(self, x1, y1 ,x2,y2):
        p1r = self.real_distance(x1, y1)
        p2r = self.real_distance(x2, y2)
        return math.dist(p1r, p2r)


    def distance_2_object(self, object_1: Object, object_2: Object):
        return self.distance_2_points(object_1.x, object_1.y, object_2.x, object_2.y)


Telementry = _Telementry()
        




