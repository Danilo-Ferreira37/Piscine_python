from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER ="officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(max_length=12, min_length=1)
    #VERIFICA SE A LISTA TEM QUE SER OBRIGATORIAMENTE FORMADA POR CREW MEMBERS!!!!!
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)
    #TESTA SE É OBRIGATORIO UM METODO RETORNAR SELF
    @model_validator(mode='after')
    def mission_validator_rules(self) -> object:
        leadership = False
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                leadership = True
        if not leadership:
            raise ValueError("The mission must have at least "
                             "one Commander or Captain")
        return self

    @model_validator(mode='after')
    def mission_experience(self) -> object:
        qnty = len(self.crew)
        xp = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience > 5:
                    xp += 1
            if xp < (qnty / 2):
                raise ValueError("In long missions (> 365 days) "
                "need 50% experienced crew (5+ years)")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    m1 = CrewMember()
    m2 = CrewMember()
    m3 = CrewMember()

    mission = SpaceMission()


if __name__ == "__main__":
    main()
