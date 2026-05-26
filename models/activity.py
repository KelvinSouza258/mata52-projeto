class Activity:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def __str__(self):
        return f"Activity(name={self.name}, description={self.description}, difficulty={self.difficulty})"
        