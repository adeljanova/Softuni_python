exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes
if arrival_in_minutes > exam_in_minutes:
    print("Late")
elif exam_in_minutes - 30 <= arrival_in_minutes <= exam_in_minutes:
    print("On time")
else:
    print("Early")
difference = abs(exam_in_minutes - arrival_in_minutes)
if exam_in_minutes - 60 < arrival_in_minutes < exam_in_minutes:
    print(f"{difference} minutes before the start" )
elif arrival_in_minutes <= exam_in_minutes - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start" )
    else:
        print(f"{hours}:{minutes} hours before the start")
elif exam_in_minutes < arrival_in_minutes < exam_in_minutes + 60:
    print(f"{difference} minutes after the start" )
elif arrival_in_minutes >= exam_in_minutes + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
