def study_schedule(permanence_period, target_time):
    if target_time is None and type(target_time) != int:
        return None

    count_students = 0
    for time in permanence_period:
        if type(time[0]) != int or type(time[1]) != int:
            return None
        if time[0] <= target_time <= time[1]:
            count_students += 1

    return count_students
