"""See https://github.com/Kozea/Radicale/issues/1274"""

import vobject


def test_radicale_1274():
    vobjs = vobject.readComponents(cal_data, allowQP=True)
    for vo in vobjs:
        assert vo is not None


cal_data = (
    "BEGIN:VCALENDAR\r\n"
    "PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN\r\n"
    "VERSION:2.0\r\n"
    "BEGIN:VTIMEZONE\r\n"
    "TZID:Europe/Berlin\r\n"
    "BEGIN:DAYLIGHT\r\n"
    "TZOFFSETFROM:+0100\r\n"
    "TZOFFSETTO:+0200\r\n"
    "TZNAME:CEST\r\n"
    "DTSTART:19700329T020000\r\n"
    "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\r\n"
    "END:DAYLIGHT\r\n"
    "BEGIN:STANDARD\r\n"
    "TZOFFSETFROM:+0200\r\n"
    "TZOFFSETTO:+0100\r\n"
    "TZNAME:CET\r\n"
    "DTSTART:19701025T030000\r\n"
    "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\r\n"
    "END:STANDARD\r\n"
    "END:VTIMEZONE\r\n"
    "BEGIN:VEVENT\r\n"
    "CREATED:20221216T080616Z\r\n"
    "LAST-MODIFIED:20221216T080618Z\r\n"
    "DTSTAMP:20221216T080618Z\r\n"
    "UID:a05ae5f9-6932-4acb-b918-c7e340352388\r\n"
    "SUMMARY:Testtermin\r\n"
    "DTSTART;TZID=Europe/Berlin:20221216T100000\r\n"
    "DTEND;TZID=Europe/Berlin:20221216T110000\r\n"
    "DESCRIPTION:test#015\\n#015\\ntest#015\\n#015\\n#015\\n#015\\n#015\\ntest\r\n"
    "URL:mid:5a13abf3-4e11-f524-4bf1-b10d35dd8bb1@foo.bar\r\n"
    "END:VEVENT\r\n"
    "END:VCALENDAR\r\n"
)
