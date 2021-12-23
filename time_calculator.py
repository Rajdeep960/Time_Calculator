def add_time(startTime, durationTime, startingDay=""):

    week_day_list = [
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
        ]

    global startingTime_hours
    global startingTime_minute
    global time_type

    global durationTime_hours
    global durationTime_minute

    # for starting time
    startingTime_hours = 0
    startingTime_minute = 0
    time_type = ""
    # for duration time
    durationTime_hours = 0
    durationTime_minute = 0


    def startingTimeDivided(time):
        # assign global variable
        global startingTime_hours
        global startingTime_minute
        global time_type
        # function start
        time.strip()
        lst = time.split(" ")
        time_type = str(lst[1])
        hours_minute = lst[0].split(":")
        startingTime_hours = int(hours_minute[0])
        startingTime_minute = int(hours_minute[1])
    

    def durationTimeDivided(duration):
        # assign global variable
        global durationTime_hours
        global durationTime_minute
        # function start
        duration.strip()
        hours_minute = duration.split(":")
        durationTime_hours = int(hours_minute[0])
        durationTime_minute = int(hours_minute[1])


    def calculate_hours(h1, m1, type, h2, m2, today=""):
        t_type = type
        m_sum = m1 + m2
        m_end = m_sum%60
        m_2_h = (m_sum - m_end)/60
        h1 = h1 + m_2_h
        h_quint = 0
        h_reminder = 0
        if t_type == "PM":
            h1 = h1 + 12
        h_end = h1 + h2
        day_count = (h_end - h_end%24)/24
        if h_end >= 12:
            h_reminder = h_end%12
            h_quint = (h_end - h_reminder)/12
            h_end = h_reminder
            if h_end == 0:
                h_end = 12
        
        type_id = pow((-1), h_quint)
        if type_id == 1:
            t_type = "AM"
        else :
            t_type = "PM"

        # for showing day name
        if today == "":
            if day_count == 0:
                return f"{int(h_end)}:{int(m_end):02d} {t_type}"
            elif day_count == 1:
                return f"{int(h_end)}:{int(m_end):02d} {t_type} (next day)"
            else:
                return f"{int(h_end)}:{int(m_end):02d} {t_type} ({int(day_count)} days later)"
        else:
            indexValue = week_day_list.index(today.capitalize())
            resultIndex = indexValue + day_count%7
            if resultIndex == 7:
                resultIndex = 0
            day_name = week_day_list[int(resultIndex)]
            # for printing
            if day_count == 0:
                return f"{int(h_end)}:{int(m_end):02d} {t_type}, {day_name}"
            elif day_count == 1:
                return f"{int(h_end)}:{int(m_end):02d} {t_type}, {day_name} (next day)"
            else:
                return f"{int(h_end)}:{int(m_end):02d} {t_type}, {day_name} ({int(day_count)} days later)"


    
    startingTimeDivided(startTime)
    durationTimeDivided(durationTime)
    new_time = calculate_hours(startingTime_hours, startingTime_minute, time_type, durationTime_hours, durationTime_minute, startingDay)
    return new_time



