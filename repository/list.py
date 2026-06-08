import json
from pathlib import Path

from models.activity import Activity
from services.sort import MergeSort


class ActivityList:
    def __init__(self, filename: str = "activities.json"):
        self.filename = filename
        self.list = self._load()

    def _load(self):
        path = Path(self.filename)
        if not path.exists() or path.stat().st_size == 0:
            self._save([])
            return []

        try:
            with path.open("r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            self._save([])
            return []

        return [Activity.from_dict(activity) for activity in data]

    def _save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def add(self, item):
        self.list.append(item)
        self._save([activity.to_dict() for activity in self.list])

    def sort(self, key: str, reverse: bool = False):
        self.list = MergeSort.sort(self.list, key, reverse)
        self._save([activity.to_dict() for activity in self.list])

    def delete(self, activity_id: int):
        self.list = [activity for activity in self.list if activity.id != activity_id]
        self._save([activity.to_dict() for activity in self.list])

    def clear(self):
        self.list = []
        self._save([])

    def is_empty(self):
        return len(self.list) == 0
