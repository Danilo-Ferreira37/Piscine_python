from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode = 'after')
    def custom_validator_rules(self) -> object:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'.")
        if (self.contact_type == ContactType.PHYSICAL 
            and not self.is_verified):
            raise ValueError("Physical contact reports must be verified.")
        if (self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses.")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) must "
                             "include a received message.")
        return self


def main():
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")
        try:
            ctc = AlienContact(contact_id="AC_2024_001",
                                   timestamp=datetime(2008, 3, 24),
                                   location="agualva-cacem",
                                   contact_type=ContactType.RADIO,
                                   signal_strength= 4,
                                   duration_minutes=1000,
                                   witness_count=80,
                                   is_verified=True
                                   )
            print(f"ID: {ctc.contact_id}")
            print(f"Type: {ctc.contact_type.value}")
            print(f"Location: {ctc.location}")
            print(f"Signal: {ctc.signal_strength}")
            print(f"Duration: {ctc.duration_minutes} minutes")
            print(f"Witnesses: {ctc.witness_count}")
            if ctc.message_received:
                 print(f"Message: {ctc.message_received}")

            print("\n======================================")
            print("Expected validation error:")
            AlienContact(contact_id="AC_2024_001",
                                   timestamp=datetime(2008, 3, 24),
                                   location="agualva-cacem",
                                   contact_type=ContactType.TELEPATHIC,
                                   signal_strength= 4,
                                   duration_minutes=1000,
                                   witness_count=2,
                                   is_verified=True)
        except ValueError as e:
             print(e.errors()[0]['msg'])
        except TypeError as e:
             print(e)


if __name__ == "__main__":
     main()
