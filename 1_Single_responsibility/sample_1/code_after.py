import logger


class CalorieTracker:
    def __init__(self, max_calories):
        self.max_calories = max_calories
        self.current_calories = 0

    def track_calories(self, calorie_count):
        """How we calculate calories"""
        self.current_calories += calorie_count
        if self.current_calories > self.max_calories:
            logger.log_calorie_surplus()
