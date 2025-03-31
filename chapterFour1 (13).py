def seconds_since_midnight(hour_in_seconds, minutes_in_seconds, seconds):
  if hour_in_seconds:
      if hour_in_seconds >= 0 or hour_in_seconds <= 23:
       if minutes_in_seconds >= 0 or minutes_in_seconds <= 59:
           if seconds >= 0 or seconds <= 59:
               return (hour_in_seconds * 3600) + (minutes_in_seconds * 60 ) + seconds



print(seconds_since_midnight(13, 30, 45))
