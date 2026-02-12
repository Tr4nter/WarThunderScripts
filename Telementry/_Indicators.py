import typing
from dataclasses import dataclass, asdict
from ._BaseDataClass import BaseDataClass

@dataclass
class TankIndicators:
    valid: bool = False
    army: str = "tank"
    type: str = ""
    stabilizer: float = 0.0
    gear: float = 0.0
    gear_neutral: float = 0.0
    speed: float = 0.0
    has_speed_warning: float = 0.0
    rpm: float = 0.0
    driving_direction_mode: float  = 0.0
    cruise_control: float = 0.0
    lws: float = 0.0
    ircm: float = 0.0
    roll_indicators_is_available: float = 0.0
    first_stage_ammo: float = 0.0
    crew_total: float = 0.0
    crew_current: float = 0.0
    crew_distance: float = 0.0
    gunner_state: float = 0.0
    driver_state: float = 0.0

# copied from the index and chagpted this, i cant be bothered typing all of this out
@dataclass
class AirIndicators:
    # Meta
    valid: bool = False
    army: str = "air"
    type: str = ""

    # Flight / Controls
    speed: float = 0.0
    speed_01: float = 0.0
    speed_02: float = 0.0

    pedals: float = 0.0
    pedals0: float = 0.0
    pedals1: float = 0.0
    pedals2: float = 0.0
    pedals3: float = 0.0
    pedals4: float = 0.0
    pedals5: float = 0.0
    pedals6: float = 0.0
    pedals7: float = 0.0
    pedals8: float = 0.0

    stick_elevator: float = 0.0
    stick_ailerons: float = 0.0
    trimmer: float = 0.0

    vario: float = 0.0

    # Altitude / Attitude
    altitude_hour: float = 0.0
    altitude_min: float = 0.0
    altitude_10k: float = 0.0

    aviahorizon_roll: float = 0.0
    aviahorizon_pitch: float = 0.0
    aviahorizon_roll1: float = 0.0
    aviahorizon_pitch1: float = 0.0

    bank: float = 0.0
    bank1: float = 0.0
    bank2: float = 0.0

    turn: float = 0.0
    turn1: float = 0.0
    turn2: float = 0.0

    # Navigation
    compass: float = 0.0
    compass1: float = 0.0
    compass2: float = 0.0
    compass3: float = 0.0
    compass4: float = 0.0

    clock_hour: float = 0.0
    clock_min: float = 0.0
    clock_sec: float = 0.0

    g_meter: float = 0.0

    # Engine / Power
    manifold_pressure: float = 0.0
    manifold_pressure1: float = 0.0
    manifold_pressure2: float = 0.0
    manifold_pressure3: float = 0.0

    rpm: float = 0.0
    rpm1: float = 0.0
    rpm2: float = 0.0
    rpm3: float = 0.0
    rpm_min: float = 0.0
    rpm1_min: float = 0.0
    rpm2_min: float = 0.0
    rpm3_min: float = 0.0
    rpm_hour: float = 0.0
    rpm1_hour: float = 0.0
    rpm2_hour: float = 0.0
    rpm3_hour: float = 0.0

    oil_pressure: float = 0.0
    oil_pressure1: float = 0.0
    oil_pressure2: float = 0.0
    oil_pressure3: float = 0.0

    oil_temperature: float = 0.0
    oil_temperature1: float = 0.0
    oil_temperature2: float = 0.0
    oil_temperature3: float = 0.0

    water_temperature: float = 0.0
    water_temperature1: float = 0.0
    water_temperature2: float = 0.0
    water_temperature3: float = 0.0

    carb_temperature: float = 0.0
    carb_temperature1: float = 0.0
    carb_temperature2: float = 0.0
    carb_temperature3: float = 0.0

    mixture: float = 0.0
    mixture1: float = 0.0
    mixture2: float = 0.0
    mixture3: float = 0.0

    fuel: float = 0.0
    fuel1: float = 0.0
    fuel2: float = 0.0

    fuel_pressure: float = 0.0
    fuel_pressure1: float = 0.0
    fuel_pressure2: float = 0.0
    fuel_pressure3: float = 0.0
    fuel_consume: float = 0.0

    throttle: float = 0.0
    throttle1: float = 0.0
    throttle2: float = 0.0

    supercharger: float = 0.0
    supercharger1: float = 0.0
    supercharger2: float = 0.0

    prop_pitch: float = 0.0
    prop_pitch_hour: float = 0.0
    prop_pitch_hour1: float = 0.0
    prop_pitch_hour2: float = 0.0
    prop_pitch_hour3: float = 0.0
    prop_pitch_min: float = 0.0
    prop_pitch_min1: float = 0.0
    prop_pitch_min2: float = 0.0
    prop_pitch_min3: float = 0.0

    # Gear / Flaps
    gears: float = 0.0
    gears1: float = 0.0
    gears2: float = 0.0
    gears_lamp: float = 0.0
    flaps: float = 0.0
    flaps_indicator: float = 0.0
    gears_indicator: float = 0.0
    radiator: float = 0.0

    # Weapons / Ammo
    weapon1: float = 0.0
    weapon2: float = 0.0
    weapon3: float = 0.0

    ammo_counter: float = 0.0
    ammo_counter1: float = 0.0
    ammo_counter2: float = 0.0
    ammo_counter3: float = 0.0
    ammo_counter4: float = 0.0
    ammo_counter5: float = 0.0
    ammo_counter6: float = 0.0
    ammo_counter7: float = 0.0

    oxygen: float = 0.0

valid_properties = []
for k in (list(asdict(AirIndicators())) + list(asdict(TankIndicators()))):
    valid_properties.append(k)

indicatorType = typing.Union[AirIndicators,TankIndicators]
class __Indicators(BaseDataClass):
    
    def __init__(self):
        self._indicators: indicatorType = AirIndicators()


    @property 
    def data(self) -> indicatorType:
        return self._indicators


    def submit_data(self, data):
        valid = {k: v for k, v in data.items() if k in valid_properties}
        try:
            self._indicators = TankIndicators(**valid)
        except TypeError:
            self._indicators = AirIndicators(**valid)


_Indicators = __Indicators()








