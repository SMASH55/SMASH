# from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ""
        for event in events_per_day:
            if event.category == "event":
                d += f"<div id='event'><li> {event.get_html_url} </li></div>"  # pragma: no cover
            elif event.category == "donation":
                d += f"<div id='donation'><li> {event.get_html_url} </li></div>"  # pragma: no cover    
            elif event.category == "volunteer":
                d += f"<div id='volunteer'><li> {event.get_html_url} </li></div>"  # pragma: no cover
            elif event.category == "discount":
                d += f"<div id='discount'><li> {event.get_html_url} </li></div>"  # pragma: no cover
            elif event.category == "free":
                d += f"<div id='free'><li> {event.get_html_url} </li></div>"  # pragma: no cover
            

        if day != 0:
            # return f"<td class='calcell mdl-data-table__cell--non-numeric'><span class='date'>{day}</span><ul> \
            return f"<td class='calcell mdl-data-table__cell--non-numeric'><span class='date'>{day}</span><ul> \
             {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr class='row'> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(
            start_time__year=self.year, start_time__month=self.month
        )

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar mdl-data-table \
        mdl-js-data-table mdl-shadow--2dp">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal
