from Telementry.Telementry import Telementry
from misc.ui import UI
from threading import Thread

droneTutorialText = "Launch drone, go into drone view, stabilize it and then go back to tank, distance should be poppin up"
elevationNotice = "Does not take elevation into calculation"

newUI = UI()

def fetch_dist(uiValueRef):
    while True:
        if Telementry.Indicators.data.army == "air": continue
        if not Telementry.MapInfo.data.valid: 
            Telementry.MapObjects.clear_point_of_interest()
            uiValueRef.set(0)
            continue
        player = Telementry.MapObjects.get_player()
        if not player or player.type == "aircraft":  continue
        poi = Telementry.MapObjects.get_point_of_interest()
        if not poi or poi.blink == -1: continue

        uiValueRef.set(str(Telementry.distance_2_object(player, poi)))
        if newUI.get_label(droneTutorialText):
            newUI.destroy_label(droneTutorialText)
            newUI.destroy_label(elevationNotice)


def main():
    newUI.make_label(droneTutorialText)
    newUI.make_label(elevationNotice)

    valueRef = newUI.make_label("Distance")
    valueRef.set("0")
    Thread(target=fetch_dist, args=(valueRef,), daemon=True).start()
    newUI.run()
    


if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        Telementry.fetch_thread.stop()
