from __future__ import annotations

from models.activity import Activity


class ScheduleResult:
    def __init__(self, label: str, items: list[Activity], elapsed_ms: float):
        self.label = label
        self.items = items
        self.elapsed_ms = elapsed_ms

    @property
    def total_weight(self) -> int:
        return sum(a.weight for a in self.items)

    @property
    def count(self) -> int:
        return len(self.items)
