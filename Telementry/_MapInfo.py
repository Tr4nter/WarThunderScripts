
from ._BaseDataClass import BaseDataClass
from dataclasses import dataclass, field


@dataclass
class MapInfo:
    grid_size: list[int] = field(default_factory=list)
    grid_steps: list[int] = field(default_factory=list)
    grid_zero: list[int] = field(default_factory=list)
    hud_type: int = -1
    map_generation: int = -1
    map_max: list[int]= field(default_factory=list)
    map_min: list[int]= field(default_factory=list)
    valid: bool = False


class __MapInfo(BaseDataClass):
    def __init__(self):
        self._mapInfo: MapInfo = MapInfo()


    @property
    def data(self) -> MapInfo:
        return self._mapInfo


    def submit_data(self, data):
        self._mapInfo = MapInfo(**data)



_MapInfo = __MapInfo()

