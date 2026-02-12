import typing
from dataclasses import dataclass

hex = typing.NewType("hex", str)

@dataclass
class Object:
    type: str = ""
    color: hex = hex("") 
    color3: str = ""
    blink: int= -1
    icon: str = ""
    icon_bg: str = ""
    x: float = 0.0
    y: float = 0.0
    dx: float = -0.0
    dy: float = -0.0
    sx: float = -0.0
    sy: float = -0.0
    ex: float = -0.0
    ey: float = -0.0


class MapObjects:
    objects: list[Object] = []
    _point_of_interest: Object = Object()


    @classmethod
    def clear(cls):
        cls.objects = []


    @classmethod
    def submit_data(cls, data: dict):
        newList = []
        for object in data:
            object["color3"] = object["color[]"]
            del object["color[]"]
            newObject = Object(**object)
            newList.append(newObject)

        cls.objects = newList

        for object in cls.objects:
            if object.type == "point_of_interest":
                cls._point_of_interest = object
                break

    @classmethod
    def get_player(cls):
        for object in cls.objects:
            if object.icon == 'Player': return object


    @classmethod
    def get_player_tank(cls):
        for object in cls.objects:
            if object.color == "#faC81E": return object


    @classmethod
    def get_objects_not_player(cls):
        return [i for i in cls.objects if i.icon != 'Player']


    
    @classmethod
    def get_point_of_interest(cls):
        return cls._point_of_interest


    @classmethod
    def clear_point_of_interest(cls):
        _point_of_interest = Object()

    
