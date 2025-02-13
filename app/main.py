class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7  # Rounds up to the next whole week

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)

    def __repr__(self) -> str:
        return (f"OnlineCourse(name='{self.name}'"
                f", description='{self.description}'"
                f", weeks={self.weeks})")
