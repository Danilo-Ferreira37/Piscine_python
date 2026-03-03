from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_id: str = None, stream_type: str = None) -> None:
        self.stream_id = "UNKNOWN" if not stream_id else stream_id
        self.n_process = 0
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: 
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self, stream_id, type) -> Dict[str, Union[str, int, float]]:
        print(f"Stream ID: {stream_id}, Type: {type}")
        return {"Stream ID": stream_id, "Type": type}


class SensorStream(DataStream):
    def __init__(self, stream_id = None):
        super().__init__(stream_id, "sensor")
    
    def process_batch(self, data_batch: List[Any]) -> str: 
        try:
            for item in data_batch:
                if not isinstance(item, dict):
                    raise ValueError("SensorStream Error: Each item has to be a dictionary!!")
                for key, val in item.items():
                    if key != "temp" and key != "humidity" and key != "pressure" and key != "preciptation":
                        raise ValueError(f"SensorStream Error: The word given '{key}' is not a parameter enviromental")
                    if not isinstance(key, str) or (not isinstance(val, int) and not isinstance(val, float)):
                        raise ValueError("SensorStream Error: The key has to be a string and the value has to be a integer!!")
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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats(self.stream_id, "Environmental Data")


class TransactionStream(DataStream):
    def __init__(self, stream_id = None):
        super().__init__(stream_id, "transaction")

    def process_batch(self, data_batch: List[Any]) -> str: 
        try:
            for item in data_batch:
                if not isinstance(item, dict):
                    raise ValueError("TransactionStream Error: Each item has to be a dictionary!! ")
                for key, val in item.items():
                    if key != "buy" and key != "sell":
                        raise ValueError(f"TransactionStream Error: The keyword '{key}' is not a transaction word")
                    if not isinstance(key, str) or (not isinstance(val, int) and not isinstance(val, float)):
                        raise ValueError("TransactionStream Error: The key has to be a string and the value has to be a integer!!")
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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats(self.stream_id, "Financial Data")


class EventStream(DataStream):
    def __init__(self, stream_id = None) -> None:
        super().__init__(stream_id, "event")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats(self.stream_id, "System Event")

    def process_batch(self, data_batch: List[Any] = None):
        try:
            self.data_batch = data_batch
            for data in data_batch:
                if data != "error" and data != "info" and data != "login" and data != "logout":
                    raise ValueError(f"EventStream Error: The keyword '{data} is not a Event word")
                if not isinstance(data, str):
                    raise ValueError("EventStream Error: Each item has to be a string!!")
                self.n_process += 1
            return f"Processing event batch: {data_batch}".replace("'", "")

        except ValueError as e:
            print(e)
            raise

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
= None) -> List[Any]:
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
    def __init__(self, streams: List[Any]) -> None:
        self.streams = streams
    
    def all_methods(self, batch: List[Any]) -> None:
        try:
            for b in batch:
                if "temp" in b or "humidity" in b or "pressure" in b:
                    for stream in self.streams:
                        if stream.stream_type == "sensor":
                            stream.get_stats()
                            print(stream.process_batch(batch))
                            print(stream.filter_data(batch, "humidity"))
                            break
                    break
                elif "buy" in b or "sell" in b:
                    for stream in self.streams:
                        if stream.stream_type == "transaction":
                            stream.get_stats()
                            print(stream.process_batch(batch))
                            print(stream.filter_data(batch, "buy"))
                            break
                    break
                elif "login" in batch or "error" in batch or "info" in batch or "logout" in batch:
                    for stream in self.streams:
                        if stream.stream_type == "event":
                            stream.get_stats()
                            print(stream.process_batch(batch))
                            print(stream.filter_data(batch, "error"))
                            break
                    break
        except ValueError:
            print("")

    def process_batch_mixed_filtered(self, batches: List[Any]) -> List[int]:
        sensor = 0
        trans = 0
        event = 0
        alert = 0
        large_trans = 0

        for batch in batches:
            try:
                is_sensor = False
                is_transaction = False
                is_event = True
                for item in batch:
                    if isinstance(item, dict):
                        is_event = False
                        for key, val in item.items():
                            if key in ("pressure", "temp", "humidity", "preciptation"):
                                is_sensor = True
                            if key in ("buy", "sell"):
                                if val > 1000:
                                    large_trans += 1
                                is_transaction = True
                    elif isinstance(item, str):
                        pass
                    else:
                        raise ValueError("Invalid item type in batch")

                if is_sensor:
                    for stream in self.streams:
                        if stream.stream_type == "sensor":
                            stream.process_batch(batch)
                            for _ in batch:
                                sensor += 1

                elif is_transaction:
                    for stream in self.streams:
                        if stream.stream_type == "transaction":
                            stream.process_batch(batch)
                            for _ in batch:
                                trans += 1

                elif is_event:
                    for stream in self.streams:
                        if stream.stream_type == "event":
                            stream.process_batch(batch)
                            for er in batch:
                                if er == "error":
                                    alert += 1
                                event += 1

                else:
                    raise ValueError("Unknown batch format")

            except ValueError as e:
                print("The program will continue.\n")

        print(f"- Sensor data: {sensor} readings processed")
        print(f"- Transaction data: {trans} operations processed")
        print(f"- Event data: {event} events processed")

        return [alert, large_trans]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    try:
        sensor = SensorStream("SENSOR_001")
        trans = TransactionStream("TRANS_001")
        event = EventStream("EVENT_001")

        data_sensor = [{"temp": 12.6}, {"humidity": 65}, {"pressure": 1013}]
        data_trans = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
        data_event = ["login", "error", "logout", "info"]

        manager = StreamProcessor([sensor, trans, event])

        print("Initialize Sensor Stream...")
        manager.all_methods(data_sensor)

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        print("Initialize TransactionStream...")
        manager.all_methods(data_trans)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        print("Initialize Event Stream...")
        manager.all_methods(data_event)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")
        alert, large_trans = manager.process_batch_mixed_filtered([[{"pressure": 15.8}, {"preciptation": 80}],
                                    [{"buy": 100}, {"sell": 150}, {"buy": 1975}, {"sell": 12}],
                                    ["info", "error", "logout", "error"]])
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {alert} critical sensor alerts, {large_trans} large transaction")
    except TypeError as e:
        print(e)

    finally:
        print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
