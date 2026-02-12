from dataclasses import dataclass
from ._BaseDataClass import BaseDataClass
import typing

@dataclass
class StateData:
    valid: bool = False

    aileron: int = 0
    elevator: int = 0
    rudder: int = 0
    flaps: int = 0
    gear: int = 0
    airbrake: int = 0

    h_m: int = 0
    tas_km_h: int = 0
    ias_km_h: int = 0
    m: float = 0.0

    aoa_deg: float = 0.0
    aos_deg: float = 0.0
    ny: float = 0.0
    vy_m_s: float = 0.0
    wx_deg_s: float = 0.0

    mfuel_kg: int = 0
    mfuel0_kg: int = 0

    throttle_1: int = 0
    power_1_hp: float = 0.0
    rpm_1: int = 0
    manifold_pressure_1_atm: float = 0.0
    oil_temp_1_c: int = 0
    thrust_1_kgs: int = 0
    efficiency_1: int = 0

    throttle_2: int = 0
    power_2_hp: float = 0.0
    rpm_2: int = 0
    manifold_pressure_2_atm: float = 0.0
    oil_temp_2_c: int = 0
    thrust_2_kgs: int = 0
    efficiency_2: int = 0
def sanitize_key(key: str) -> str:
    key = key.lower()
    key = key.replace(", %", "")
    key = key.replace(",", "")
    key = key.replace(" ", "_")
    key = key.replace("/", "_")
    key = key.replace("-", "_")
    return key

class __State(BaseDataClass):
    def __init__(self):
        self._states: StateData = StateData()


    @property
    def data(self) -> StateData:
        return self._states
    

    def submit_data(self, data):
        cleaned = {sanitize_key(k): v for k,v in data.items()}
        if not cleaned: return
        self._states = StateData(**cleaned)

        

_State = __State()


