from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_id: str = None) -> None:
        self.stream_id = "UNKNOWN" if not stream_id else stream_id
        self.n_process = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: 
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    @staticmethod
    def get_stats(stream_id, type) -> Dict[str, Union[str, int, float]]:
        print(f"Stream ID: {stream_id}, Type: {type}")
        return {"Stream ID": stream_id, "Type": type}


class SensorStream(DataStream):
    def __init__(self, stream_id = None):
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
            return f"Processing sensor batch: {data_batch}".replace("'", "").replace("{", "").replace("}", "")
            
        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if self.n_process == 0:
            return "Sensor analysis: No readings processed"
        for data in data_batch:
            for key in data:
                if key == criteria:
                    return (f"Sensor analysis: {self.n_process} readings "
                            f"processed, avg {data}{'Cº' if key == 'temp' else ''}\n".replace("'", "")
                    )
        return f"Sensor analysis: {self.n_process} readings processed, don't found the keyword\n"

    def get_stats(self):
        return super().get_stats(self.stream_id, "Environmental Data")


class TransactionStream(DataStream):
    def __init__(self, stream_id = None):
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
            return f"Processing transaction batch: {data_batch}".replace("'", "").replace("{", "").replace("}", "")

        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if self.n_process == 0:
            return "No transation analysis!!"
        for data in data_batch:
            for key, val in data.items():
                if key == criteria:
                    return f"Transaction analysis: {self.n_process} operations, net flow: +{val - 125} units\n"
        return  f"Transation analysis: {self.n_process} operations, don't found the keyword\n"

    def get_stats(self):
        return super().get_stats(self.stream_id, "Financial Data")


class EventStream(DataStream):
    def __init__(self, stream_id = None):
        super().__init__(stream_id)

    def get_stats(self):
        return super().get_stats(self.stream_id, "System Event")

    def process_batch(self, data_batch: List[Any] = None):
        try:
            self.data_batch = data_batch
            for data in data_batch:
                if not isinstance(data, str):
                    raise ValueError("Error: Each item has to be a string!!")
                self.n_process += 1
            return f"Processing event batch: {data_batch}".replace("'", "")

        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch, criteria = None):
        try:
            count = 0
            if data_batch != self.data_batch:
                raise ValueError("The data provided has to be equal than data process")
            for data in data_batch:
                if data == criteria:
                    count += 1
            return f"Event analysis: {self.n_process} events, {count} {criteria} detected"

        except ValueError as e:
            print(e)
            raise


class StreamProcessor():
    def __init__(self, streams: List) -> None:
        self.streams = streams

    def all_process(self):

        


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    
    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    
    data_sensor = [{"temp":22.5}, {"humidity":65}, {"pressure": 1013}]
    data_trans = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    data_event = ["login", "error", "logout"]

    manager = StreamProcessor([sensor, trans, event])
    manager.all_process()

"""         print("Initialize Sensor Stream...")
        sensor.get_stats()
        data_sensor = [{"temp":22.5}, {"humidity":65}, {"pressure": 1013}]
        print(sensor.process_batch(data_sensor))
        print(sensor.filter_data(data_sensor, "humidity"))

        print("Initialize TransactionStream...")
        trans.get_stats()
        data_trans = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
        print(trans.process_batch(data_trans))
        print(trans.filter_data(data_trans, "sell"))

        print("Initialize Event Stream...")
        event.get_stats()
        data_event = ["login", "error", "logout"]
        print(event.process_batch(data_event))
        print(event.filter_data(data_event, "error"))

    except ValueError:
        print("\n=== Fatal error: Programs has stopped ===\n")
 """

if __name__ == "__main__":
    main()
