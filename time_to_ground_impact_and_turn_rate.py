
from collections import deque
from Telementry.Telementry import Telementry
from misc.ui import UI
from threading import Thread
import math


newUI = UI()
g = 9.81

def pitch_update(pitch_ref, impact_ref, turn_rate_ref):
    global air_data
    while True:
        if not Telementry.MapInfo.data.valid: 
            pitch_ref.set("0")
            impact_ref.set("0")
            turn_rate_ref.set("0")
            continue
        if Telementry.Indicators.data.army != "air": continue
        player = Telementry.MapObjects.get_player()
        if not player or player.type != "aircraft": continue
        pitch = Telementry.Indicators.data.aviahorizon_pitch * -1
        altitude = Telementry.Indicators.data.altitude_hour
        vy = Telementry.State.data.vy_m_s
        tas = Telementry.Indicators.data.speed          
        ny = Telementry.Indicators.data.g_meter         # in G's

        pitch_ref.set(str(round(pitch, 2)))
        if vy < 0:
            discriminant = vy**2 + 2 * g * altitude
            t = (vy + math.sqrt(discriminant)) / g
            impact_ref.set(str(round(t, 2)))
        else:
            impact_ref.set("0.0")

        # VVV powered by chinese deepseek
        if tas is None or tas == 0:
            tas = 0.01
        if ny > 1.0:   
            turn_rate_rad = (g * math.sqrt(ny*ny - 1)) / tas
            turn_rate = math.degrees(turn_rate_rad)     
        else:
            turn_rate = 0.0
        turn_rate_ref.set(str(round(turn_rate,2)))


         



def main():

    pitch_ref = newUI.make_label("Pitch")
    pitch_ref.set("0")

    ttp_ref = newUI.make_label("Time to ground impact")
    pitch_ref.set("0")

    turn_rate = newUI.make_label("Turn rate/deg")
    turn_rate.set("0")
    Thread(target=pitch_update, args=(pitch_ref,ttp_ref,turn_rate), daemon= True).start()
    newUI.run()
    


if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        Telementry.fetch_thread.stop()
