from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = "UNKNOWN :(" if not stream_id else stream_id
        self.n_process = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: 
        pass
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamProcessor():
    def __init__(self, streams: List) -> None:
        self.streams = streams


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
    
    def process_batch(self, data_batch: List[Any]) -> str: 
        try:
            for item in data_batch:
                if not isinstance(item, dict):
                    raise ValueError("Error: Each item has to be a dictionary!!")
                for key, val in item.items():
                    if not isinstance(key, str) or (not isinstance(val, int) and not isinstance(val, float)):
                        raise ValueError("Error: The key has to be a string and the value has to be a integer!!")
                self.n_process += 1
            return f"Processing sensor batch: {data_batch}"
            
        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if self.n_process == 0:
            return "Sensor analysis: No readings processed"
        for data in data_batch:
            for key in data:
                if key == criteria:
                    return f"Sensor analysis: {self.n_process} readings processed, avg {data}{'Cº' if key == 'temp' else ''}"
        return f"Sensor analysis: {self.n_process} readings processed, don't found the keyword"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        f"Stream ID: {self.stream_id}, Type: Environmental Data\n"


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str: 
        try:
            for item in data_batch:
                if not isinstance(item, dict):
                    raise ValueError("Error: Each item has to be a dictionary!!")
                for key, val in item.items():
                    if not isinstance(key, str) or (not isinstance(val, int) and not isinstance(val, float)):
                        raise ValueError("Error: The key has to be a string and the value has to be a integer!!")
                self.n_process += 1
            return f"Processing transaction batch: {data_batch}"

        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if self.n_process == 0:
            return "No transation analysis!!"
        for data in data_batch:
            for key, val in data.items():
                if key == criteria:
                    return f"Transaction analysis: {self.n_process} operations, net flow: +{val - 125} units"
        return  f"Transation analysis: {self.n_process} operations, don't found the keyword"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return f"Stream ID: {self.stream_id}, Type: Financial Data"


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    manager = StreamProcessor([sensor, trans, event])

    print("Initialize Sensor Stream...")

if __name__ == "__main__":
    main()
