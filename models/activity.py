import random
from datetime import datetime, timedelta


class Activity:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        start_time: datetime,
        end_time: datetime,
        priority: int,
        participants: int,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.participants = participants
        self.weight = int(self.priority + self.participants / 5)

    def overlaps(self, other: "Activity") -> bool:
        return self.start_time < other.end_time and other.start_time < self.end_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "priority": self.priority,
            "participants": self.participants,
            "weight": self.weight,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            start_time=datetime.fromisoformat(data["start_time"]),
            end_time=datetime.fromisoformat(data["end_time"]),
            priority=data["priority"],
            participants=data["participants"],
        )

    @classmethod
    def random(cls, id: int) -> "Activity":
        base = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        day = random.randint(0, 1)

        if random.random() < 0.85:
            hour = random.choice([9, 10, 11, 13, 14, 15, 16])
        else:
            hour = random.randint(8, 17)

        start_time = base + timedelta(days=day, hours=hour)
        end_time = start_time + timedelta(hours=random.randint(1, 4))

        return cls(
            id=id,
            name=f"Atividade {id}",
            description=f"Descrição aleatória {random.randint(1000, 9999)}",
            start_time=start_time,
            end_time=end_time,
            priority=random.randint(1, 5),
            participants=random.randint(1, 50),
        )

    def __str__(self):
        return f"Activity(name={self.name}, description={self.description})"
