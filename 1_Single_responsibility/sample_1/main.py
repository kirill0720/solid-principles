from code_before import CalorieTracker


def main():
    calorie_tracker = CalorieTracker(2000)
    calorie_tracker.track_calories(500)
    calorie_tracker.track_calories(1000)
    calorie_tracker.track_calories(700)


if __name__ == '__main__':
    main()
