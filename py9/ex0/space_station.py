from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: bool = Field(default=True)
    notes:str = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(station_id="ID_3737",
                 name="Space Station very nice",
                 crew_size=10,
                 power_level=6.9,
                 oxygen_level=98.3,
                 )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print("Status: Operational")

        print("\n========================================")
        print("Expected validation error:")
        SpaceStation(station_id="ID_3737",
                 name="Space Station very nice",
                 crew_size=50,
                 power_level=6.9,
                 oxygen_level=98.3,)
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
