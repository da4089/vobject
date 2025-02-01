"""See https://github.com/Kozea/Radicale/issues/1332"""

import vobject


def test_tzid():
    vobjs = vobject.readComponents(cal_data, allowQP=True)
    for vo in vobjs:
        assert vo is not None


cal_data = (
    "BEGIN:VCALENDAR\r\n"
    "PRODID;X-RICAL-TZSOURCE=TZINFO:-//com.denhaven2/NONSGML ri_cal gem//EN\r\n"
    "CALSCALE:GREGORIAN\r\n"
    "VERSION:2.0\r\n"
    "X-WR-CALNAME:Bainbridge Island FC B08 White\r\n"
    "X-WR-CALDESC:The event schedule for the Bainbridge Island FC B08 White So\r\n"
    " ccer team\r\n"
    "X-WR-TIMEZONE:America/Los_Angeles\r\n"
    "X-PUBLISHED-TTL:PT1H\r\n"
    "X-TS-TIMESTAMP:2023-09-19 11:53:05\r\n"
    "BEGIN:VEVENT\r\n"
    "DTEND;TZID=America/Los_Angeles;VALUE=DATE-TIME:20230626T190000\r\n"
    "DTSTART;TZID=America/Los_Angeles;VALUE=DATE-TIME:20230626T173000\r\n"
    "DTSTAMP;VALUE=DATE-TIME:20230611T002230Z\r\n"
    "LAST-MODIFIED;VALUE=DATE-TIME:20230611T002230Z\r\n"
    "DESCRIPTION:(Arrival Time:  5:21 PM (Pacific Time (US & Canada)))\r\n"
    "SUMMARY:Soccer team B08 White - B08 Training\r\n"
    "LOCATION:High School Turf\r\n"
    "SEQUENCE:0\r\n"
    "UID:347d986b3625741bd5bdfbb1b4480f314d31d98e784bb3bd5f1a75bc60d3a26c\r\n"
    "END:VEVENT\r\n"
    "BEGIN:VTIMEZONE\r\n"
    "TZID;X-RICAL-TZSOURCE=TZINFO:America/Los_Angeles\r\n"
    "BEGIN:DAYLIGHT\r\n"
    "DTSTART:20230312T020000\r\n"
    "RDATE:20230312T020000\r\n"
    "TZOFFSETFROM:-0800\r\n"
    "TZOFFSETTO:-0700\r\n"
    "TZNAME:PDT\r\n"
    "END:DAYLIGHT\r\n"
    "BEGIN:STANDARD\r\n"
    "DTSTART:20231105T020000\r\n"
    "RDATE:20231105T020000\r\n"
    "TZOFFSETFROM:-0700\r\n"
    "TZOFFSETTO:-0800\r\n"
    "TZNAME:PST\r\n"
    "END:STANDARD\r\n"
    "END:VTIMEZONE\r\n"
    "END:VCALENDAR\r\n"
)
