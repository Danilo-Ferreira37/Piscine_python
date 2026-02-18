from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, result: str):
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        self.data = None
        if self.validate(data):
            self.data = data
            return f"Processed {len(data)} numeric values, sum={sum(data)}, avg={(sum(data) / len(data)):.1f}"
        return "Error: Value received is invalid"

    def print_info(self):
            try:
                if self.data == None:
                    raise ValueError
                print(f"Processing data: {self.data}")
                print("Validation: Numeric data verified")
            except ValueError:
                pass

    def validate(self, data: Any) -> bool:
        validation = False
        if type(data) == list or type(data) == set or type(data) == tuple:
            for n in data:
                if type(n) == int or type(n) == float:
                    validation = True
                else:
                    return False
            return validation

    def format_output(self, result: str):
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        self.data = None
        if self.validate(data):
            self.data = data
            return f"Processed text: {len(data)} characters, {len(data.split())} words"
        return "Error: Text is invalid"

    def print_info(self):
            try:
                if self.data == None:
                    raise ValueError
                print(f'Processing data: "{self.data}"')
                print("Validation: Text data verified")
            except ValueError:
                pass

    def validate(self, data: Any) -> bool:
       if type(data) == str:
            return True
       return False

    def format_output(self, result: str):
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        self.data = None
        if self.validate(data):
            self.data = data
            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()
            if "ERROR:" in data:
                return f"[ALERT] {level} level detected: {message}"
            elif "INFO:" in data:
                return f"[INFO] {level} level detected: {message}"
            elif "WARNING:" in data:
                return f"[ALERT] {level} level detected: {message}"
        return "Error: This is a invalid log"

    def print_info(self):
        try:
            if self.data == None:
                raise ValueError
            print(f'Processing data: "{self.data}"')
            print("Validation: Log entry verified")
        except ValueError:
            pass

    def validate(self, data: Any) -> bool:
        if type(data) == str and ("INFO:" in data or "ERROR:" in data or "WARNING:" in data):
            return True
        return False

    def format_output(self, result: str):
        return f"Output: {result}"


def main():
    try:
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
        print("Initializing Numeric Processor...")
        num = NumericProcessor()
        result = num.process([1, 2, 3, 4, 5])
        num.print_info()
        print(num.format_output(result))

        print("\nInitializing Text Processor...")
        text = TextProcessor()
        result = text.process("Hello Nexus World")
        text.print_info()
        print(text.format_output(result))
        
        print("\nInitializing Log Processor...")
        log = LogProcessor()
        result = log.process("WARNING: The variable is not being used.")
        log.print_info()
        print(log.format_output(result))

        print("\n=== Polymorphic Processing Demo ===")
        n = NumericProcessor()
        result = n.process([2, 2, 2])
        print(f"Result 1: {result}")

        t = TextProcessor()
        result = t.process("Daniloo here")
        print(f"Result 2: {result}")

        l = LogProcessor()
        result= l.process("INFO: System ready")
        print(f"Result 3: {result}")
        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except ValueError:
        print("ERROR: General system failure")


if __name__ == "__main__":
    main()
