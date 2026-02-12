import primp
import asyncio
import threading
import time

from ._MapObjects import MapObjects
from ._Indicators import _Indicators
from ._State import _State
from ._MapInfo import _MapInfo

def tick():
    return time.time()

BASE = "http://localhost:8111/"

TASKS = ["map_obj.json", "map_info.json", "indicators", "state"]
REQUESTS_PER_TASK_PER_SEC = 4
WAIT_COOLDOWN = 1/REQUESTS_PER_TASK_PER_SEC
class _call:
    def __init__(self):
        self._loop = asyncio.new_event_loop()
        self._thread = None
        self.client = primp.AsyncClient(impersonate="firefox_135", impersonate_os="macos")
        self._stop_event = threading.Event()

        self._task_fetch_count = {} 
        self._task_fetch_finish = {} 
        self._task_last_fetch = {}
        for task in TASKS:
            self._task_fetch_count[task] = 0
            self._task_fetch_finish[task] = 0
            self._task_last_fetch[task] = 0


    def _submit_data(self, task, data):
        if task == "map_obj.json":
            MapObjects.submit_data(data)
        elif task == "indicators":
            _Indicators.submit_data(data)
        elif task == "state":
            _State.submit_data(data)
        elif task == "map_info.json":
            _MapInfo.submit_data(data)

        self._task_fetch_count[task] -= 1
       
    
    async def _fetch_task(self, task):
        if self._task_fetch_count[task] >= REQUESTS_PER_TASK_PER_SEC:
            return

        TIME_SINCE_LAST_FETCH =(tick()-self._task_last_fetch[task])
        if TIME_SINCE_LAST_FETCH < WAIT_COOLDOWN:
            return

        try:
            url = BASE+task
            self._task_fetch_count[task] += 1
            self._task_last_fetch[task] = tick()
            req = await self.client.get(url)
        except Exception as e:
            self._task_fetch_count[task] -= 1
            return
        if req.status_code != 200: return
        try:
            data = req.json()
            self._submit_data(task, data)
        except Exception as e: 
            self._submit_data(task, {})


    async def fetch_loop(self):
        while True:
            if self._stop_event.is_set():
                for task in asyncio.all_tasks(self._loop):
                    task.cancel()
                break
            for task in TASKS:
                if task != "map_info.json" and not _MapInfo.data.valid: continue #no need to fetch if theres we're not playing in a map
                if task == "state" and _Indicators.data.army == "tank": continue #they dont give you anything as a tank
                asyncio.create_task(self._fetch_task(task))
            await asyncio.sleep(0)


    def _run(self):
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(self.fetch_loop())
        except asyncio.exceptions.CancelledError: 
            pass


    def start_fetch_thread(self):
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()



    def stop(self):
        self._stop_event.set()
