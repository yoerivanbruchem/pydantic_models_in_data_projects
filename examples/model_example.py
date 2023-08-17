from pydantic import BaseModel
import datetime as dt
from typing import List

class CurrentTrafficIntensity(BaseModel):
    road_id: str
    section_id: float
    direction: str
    datetime: dt.datetime
    intensity: float


intensity_A12_35_9 = CurrentTrafficIntensity(road_id="A12", section_id=35.9, direction="L", datetime=dt.datetime(2023, 8, 17, 13, 42), intensity=0.8)

# Result: CurrentTrafficIntensity(road_id='A12', section_id=35.9, direction='L', datetime=datetime.datetime(2023, 8, 17, 13, 42), intensity=0.8)
