"""See https://github.com/Kozea/Radicale/issues/1316"""

import vobject


def test_ical_with_different_type_elements():
    vobjs = vobject.readComponents(cal_data, allowQP=True)
    for vo in vobjs:
        assert vo is not None


# In this case, I think the issue report is confusing the iCalendar
# specification requirements (where you can mix the component types
# within a calendar at will, and CalDAV, where a specific "resource"
# (I assume in a HTTP sense) can include only a single type of
# component (except for timezones), even if there are
# multiple, e.g. VEVENTs describing that single "resource" (like a
# repeating meeting with an override, to use their example).
#
# Consequently, I think vobject should just make sure that it can
# parse and validate multiple component types.

cal_data = (
    "BEGIN:VCALENDAR\r\n"
    "VERSION:2.0\r\n"
    "PRODID:-//mozilla.org/Mozilla Thunderbird//EN\r\n"
    "BEGIN:VTIMEZONE\r\n"
    "TZID:US/Pacific\r\n"
    "BEGIN:STANDARD\r\n"
    "DTSTART:19671029T020000\r\n"
    "RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10\r\n"
    "TZOFFSETFROM:-0700\r\n"
    "TZOFFSETTO:-0800\r\n"
    "TZNAME:PST\r\n"
    "END:STANDARD\r\n"
    "BEGIN:DAYLIGHT\r\n"
    "DTSTART:19870405T020000\r\n"
    "RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4\r\n"
    "TZOFFSETFROM:-0800\r\n"
    "TZOFFSETTO:-0700\r\n"
    "TZNAME:PDT\r\n"
    "END:DAYLIGHT\r\n"
    "END:VTIMEZONE\r\n"
    "BEGIN:VEVENT\r\n"
    "SEQUENCE:0\r\n"
    "DTSTART;TZID=US/Pacific:20021028T140000\r\n"
    "RRULE:FREQ=Weekly;COUNT=10\r\n"
    "DTSTAMP:20021028T011706Z\r\n"
    "SUMMARY:Coffee with Jason\r\n"
    "UID:EC9439B1-FF65-11D6-9973-003065F99D04\r\n"
    "DTEND;TZID=US/Pacific:20021028T150000\r\n"
    "BEGIN:VALARM\r\n"
    "TRIGGER;VALUE=DURATION:-P1D\r\n"
    "ACTION:DISPLAY\r\n"
    "DESCRIPTION:Event reminder\\, with comma\\nand line feed\r\n"
    "END:VALARM\r\n"
    "END:VEVENT\r\n"
    "BEGIN:VJOURNAL\r\n"
    "UID:19970901T130000Z-123405@example.com\r\n"
    "DTSTAMP:19970901T130000Z\r\n"
    "DTSTART;VALUE=DATE:19970317\r\n"
    "SUMMARY:Staff meeting minutes\r\n"
    "DESCRIPTION:1. Staff meeting: Participants include Joe\\,\r\n"
    "  Lisa\\, and Bob. Aurora project plans were reviewed.\r\n"
    "  There is currently no budget reserves for this project.\r\n"
    "  Lisa will escalate to management. Next meeting on Tuesday.\\n\r\n"
    " 2. Telephone Conference: ABC Corp. sales representative\r\n"
    "  called to discuss new printer. Promised to get us a demo by\r\n"
    "  Friday.\\n3. Henry Miller (Handsoff Insurance): Car was\r\n"
    "  totaled by tree. Is looking into a loaner car. 555-2323\r\n"
    "  (tel).\r\n"
    "END:VJOURNAL\r\n"
    "END:VCALENDAR\r\n"
)
