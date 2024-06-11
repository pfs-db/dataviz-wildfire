"""This script will be to show how extract information from the dwd database"""

from wetterdienst import Wetterdienst, Resolution, Period
from wetterdienst.provider.dwd.observation import (
    DwdObservationRequest,
    DwdObservationDataset,
    DwdObservationResolution,
)
from wetterdienst.provider.dwd.observation import (
    DwdObservationRequest,
    DwdObservationPeriod,
)

Wetterdienst.discover()

stations = DwdObservationRequest(
    parameter=DwdObservationDataset.PRECIPITATION_MORE,
    resolution=Resolution.DAILY,
    period=Period.HISTORICAL,
)

# print(stations.all())
# weather_data = stations.filter_by_station_id(station_id).values.all().df
print(stations.filter_by_station_id(1).values.all().df)
