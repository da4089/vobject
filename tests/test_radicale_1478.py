"""See https://github.com/Kozea/Radicale/issues/1478"""

import datetime

import pytest

import vobject


def test_rrule_date_vs_datetime_parsing():
    vobjs = vobject.readComponents(cal_data, allowQP=True)
    for vo in vobjs:
        assert vo is not None


@pytest.mark.skip("Known issue with dateutil's rrule")
def test_dateutil_rrule_aware_datetimes():
    cal = vobject.readOne(cal_data, allowQP=True)
    rrule_set = cal.vevent.getrruleset()

    # Test using aware datetime values.
    start = datetime.datetime(2024, 4, 1, tzinfo=datetime.timezone.utc)
    stop = datetime.datetime(2025, 4, 17, tzinfo=datetime.timezone.utc)

    recurrences = rrule_set.between(start, stop)

    assert len(recurrences) == 2
    assert recurrences[0] == datetime.datetime(2024, 4, 8)
    assert recurrences[1] == datetime.datetime(2024, 4, 15)


def test_dateutil_rrule_naive_datetimes():
    cal = vobject.readOne(cal_data, allowQP=True)
    rrule_set = cal.vevent.getrruleset()

    # Test using naive datetime values.
    start = datetime.datetime(2024, 4, 1)
    stop = datetime.datetime(2024, 4, 17)

    recurrences = rrule_set.between(start, stop)

    assert len(recurrences) == 2
    assert recurrences[0] == datetime.datetime(2024, 4, 8)
    assert recurrences[1] == datetime.datetime(2024, 4, 15)


@pytest.mark.skip("Known issue with dateutil's rrule")
def test_dateutil_rrule_dates():
    cal = vobject.readOne(cal_data, allowQP=True)
    rrule_set = cal.vevent.getrruleset()

    # Test using date values.
    start = datetime.date(2024, 4, 1)
    stop = datetime.date(2024, 4, 17)

    recurrences = rrule_set.between(start, stop)

    assert len(recurrences) == 2
    assert recurrences[0] == datetime.date(2024, 4, 8)
    assert recurrences[1] == datetime.date(2024, 4, 15)


cal_data = (
    "BEGIN:VCALENDAR\r\n"
    "VERSION:2.0\r\n"
    "PRODID:-//foo//bar//EN\r\n"
    "BEGIN:VEVENT\r\n"
    "UID:fe1da58e-0555-11ef-9770-58ce2a14e2e5\r\n"
    "DTSTART;VALUE=DATE:20240408\r\n"
    "DTEND;VALUE=DATE:20240409\r\n"
    "DTSTAMP:20240428T115356Z\r\n"
    "RRULE:FREQ=WEEKLY;INTERVAL=1\r\n"
    "SEQUENCE:1\r\n"
    "SUMMARY:Test\r\n"
    "END:VEVENT\r\n"
    "END:VCALENDAR\r\n"
)
