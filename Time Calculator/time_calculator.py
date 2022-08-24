def add_time(start, duration, start_day = None):
  days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
  new_day = 0
  day_index = -1

  #calculate time even if the string 'start_day' dosn't match
  if start_day != None:
    start_day = start_day.lower()
    if start_day not in days:
      start_day = None
    else:
      day_index = days.index(start_day)

  #split the string and get what we need
  time, ampm = start.split(' ')
  s_hour,s_min = time.split(':')
  d_hour,d_min = duration.split(':')

  ampm.upper()
  
  new_min = (int(s_min) + int(d_min)) % 60
  min_to_hr = (int(s_min) + int(d_min)) // 60
  
  new_hr = (int(s_hour) + int(d_hour) + min_to_hr) % 12
  hr_to_ampm = (int(s_hour) + int(d_hour) + min_to_hr) // 12

  if new_hr == 0:
    new_hr = 12

  #change between AM/PM and increase days
  for i in range(hr_to_ampm):
    if ampm == 'PM':
      new_day+=1
      if day_index == 6:
        day_index=0
      else:
        day_index+=1
      ampm = 'AM'
    elif ampm == 'AM':
      ampm = 'PM'
  
  #with starting day
  if start_day != None:
    if new_day == 0:
      new_time = f'{new_hr}:{new_min:02} {ampm}, {days[day_index].capitalize()}'
    elif new_day == 1:
      new_time = f'{new_hr}:{new_min:02} {ampm}, {days[day_index].capitalize()} (next day)'
    elif new_day >1:
      new_time = f'{new_hr}:{new_min:02} {ampm}, {days[day_index].capitalize()} ({new_day} days later)'
  #without starting day
  else:
    if new_day == 0:
      new_time = f'{new_hr}:{new_min:02} {ampm}'
    elif new_day == 1:
      new_time = f'{new_hr}:{new_min:02} {ampm} (next day)'
    elif new_day >1:
      new_time = f'{new_hr}:{new_min:02} {ampm} ({new_day} days later)'

#  for python 3.10
#  match new_day:
#    case 0:
#      new_time = f'{new_hr}:{new_min:02} {ampm}'
#    case 1:
#      new_time = f'{new_hr}:{new_min:02} {ampm} (next day)'
#    case _:
#      new_time = f'{new_hr}:{new_min:02} {ampm} ({new_day} days later)'

  return new_time

