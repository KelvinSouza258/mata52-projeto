from models.activity import Activity
from models.schedule_result import ScheduleResult
from services.schedule_resolver import greedy_classic, dp_weighted


class Schedule:
    def __init__(self):
        self.classic = ScheduleResult("Guloso Clássico", [], 0.0)
        self.dp = ScheduleResult("Prog. Dinâmica", [], 0.0)

    def rebuild_from(self, activities: list[Activity]):
        items_c, ms_c = greedy_classic(activities)
        self.classic = ScheduleResult("Guloso Clássico", items_c, ms_c)

        items_d, ms_d = dp_weighted(activities)
        self.dp = ScheduleResult("Prog. Dinâmica", items_d, ms_d)

    def clear(self):
        self.classic = ScheduleResult("Guloso Clássico", [], 0.0)
        self.dp = ScheduleResult("Prog. Dinâmica", [], 0.0)

    def is_empty(self) -> bool:
        return self.classic.count == 0
