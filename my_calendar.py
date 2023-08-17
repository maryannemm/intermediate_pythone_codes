import calendar

cal=calendar.TextCalendar(calendar.MONDAY)
months=[
    (2023,8),
    (2023,9),
    (2023,10),
    (2023,11),
    (2023,12),
]
for month, year in months:
    m=cal.formatmonth(month, year)
    print (m)
    