"""There are two reasons to change CalorieTracker class:
1. We want to change how we calculate calories
2. We want to change how we notify user, e.g. change to email
THAT's WRONG!
"""


class CalorieTracker:
    def __init__(self, max_calories):
        self.max_calories = max_calories
        self.current_calories = 0

    def track_calories(self, calorie_count):
        """How we calculate calories"""
        self.current_calories += calorie_count
        if self.current_calories > self.max_calories:
            self.log_calorie_surplus()

    def log_calorie_surplus(self):
        """How we notify user about calorie exceed"""
        print('Max calories exceeded')


if __name__ == '__main__':
    calorie_tracker = CalorieTracker(2000)
    calorie_tracker.track_calories(500)
    calorie_tracker.track_calories(1000)
    calorie_tracker.track_calories(700)
