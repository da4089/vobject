# -*- coding: utf-8 -*-

import codecs
import datetime

import vobject


def test_unicode_in_vcard():
    card = vobject.vCard()
    card.add("fn").value = "Hello\u1234 World!"
    card.add("n").value = vobject.vcard.Name("World", "Hello\u1234")
    card.add("adr").value = vobject.vcard.Address("5\u1234 Nowhere, Apt 1", "Berkeley", "CA", "94704", "USA")
    assert card.adr.value != vobject.vcard.Address("Just a street")
    assert card.adr.value == vobject.vcard.Address("5\u1234 Nowhere, Apt 1", "Berkeley", "CA", "94704", "USA")
    serialized = card.adr.serialize()
    assert serialized.strip() == "ADR:;;5ሴ Nowhere\\, Apt 1;Berkeley;CA;94704;USA"


def test_organizational_unit_in_vcard():
    card = vobject.vCard()
    card.add("fn").value = "example"
    card.add("org").value = ["Company, Inc.", "main unit", "sub-unit"]

    serialized = card.org.serialize()
    assert serialized.strip() == "ORG:Company\\, Inc.;main unit;sub-unit"


def test_quoted_printable():
    given = "Jörg"
    family = "Schüler"
    qp_n = codecs.encode(f"{family};{given}".encode("utf-8"), "quotedprintable").decode("ascii")
    qp_fn = codecs.encode(f"{given} {family}".encode("utf-8"), "quotedprintable").decode("ascii")

    vcf = (
        "BEGIN:VCARD\r\n"
        "VERSION:2.1\r\n"
        f"N;ENCODING=QUOTED-PRINTABLE:{qp_n}\r\n"
        f"FN;ENCODING=QUOTED-PRINTABLE:{qp_fn}\r\n"
        "TEL;HOME:0111111111\r\n"
        "END:VCARD\r\n"
    )

    card = vobject.readOne(vcf)
    assert card.n.value.given == given
    assert card.n.value.family == family

    # FIXME: given this card is VERSION:2.1, it should be serialized using v2.1 rules: no \n, non-ASCII values
    # FIXME: encoded using Quoted Printable, and we maybe want to give some thought to round-tripping both the
    # FIXME: byte encoding and the charset: should the serialized form match the input?
    # FIXME: Regardless, current behaviour seems to ignore the v2.1, and emit a v3.0 card using UTF-8 charset,
    # FIXME: which isn't ideal.
    serialized = card.serialize()
    assert len(serialized) > 0
    # FIXME: what should we actually expect here?
    # assert serialized == "BEGIN:VCARD\r\nVERSION:2.1\r\nFN:\xc3\xa9\r\nN:;\xc3\xa9;;;\r\nTEL:0111111111\r\nEND:VCARD\r\n"

    ics = (
        "BEGIN:VCALENDAR\r\n"
        "PRODID:-//OpenSync//NONSGML OpenSync vformat 0.3//EN\r\n"
        "VERSION:1.0\r\n"
        "BEGIN:VEVENT\r\n"
        "DESCRIPTION;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:foo =C3=A5=0Abar =C3=A4=\r\n=0Abaz =C3=B6\r\n"
        "UID:20080406T152030Z-7822\r\n"
        "END:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )

    calendar = vobject.readOne(ics, allowQP=True)
    serialized = calendar.serialize()
    assert len(serialized) > 0

    # FIXME: see above discussion
    # assert serialized == (
    #     "BEGIN:VCALENDAR\r\n"
    #     "VERSION:1.0\r\n"
    #     "PRODID:-//OpenSync//NONSGML OpenSync vformat 0.3//EN\r\n"
    #     "BEGIN:VEVENT\r\n"
    #     "UID:20080406T152030Z-7822\r\n"
    #     "DESCRIPTION:foo \xc3\xa5\\nbar \xc3\xa4\\nbaz \xc3\xb6\r\n"
    #     "END:VEVENT\r\n"
    #     "END:VCALENDAR\r\n"
    # )


def test_unicode_in_tzid():
    ics = (
        "BEGIN:VCALENDAR\r\n"
        "PRODID:- // Microsoft Corporation // Outlook 12.0 MIMEDIR // EN\r\n"
        "VERSION:2.0\r\n"
        "BEGIN:VTIMEZONE\r\n"
        "TZID:Екатеринбург\r\n"
        "BEGIN:STANDARD\r\n"
        "DTSTART:16011028T030000\r\n"
        "RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10\r\n"
        "TZOFFSETFROM:+0600\r\n"
        "TZOFFSETTO:+0500\r\n"
        "END:STANDARD\r\n"
        "BEGIN:DAYLIGHT\r\n"
        "DTSTART:16010325T020000\r\n"
        "RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3\r\n"
        "TZOFFSETFROM:+0500\r\n"
        "TZOFFSETTO:+0600\r\n"
        "END:DAYLIGHT\r\n"
        "END:VTIMEZONE\r\n"
        "BEGIN:VEVENT\r\n"
        "UID:CyrillicTest\r\n"
        "DTSTART;TZID=Екатеринбург:20080530T150000\r\n"
        "END:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )

    calendar = vobject.readOne(ics)
    event_start = calendar.vevent.dtstart.value
    assert type(event_start) is datetime.datetime
    assert event_start.year == 2008
    assert event_start.month == 5
    assert event_start.day == 30
    assert event_start.hour == 15
    assert event_start.minute == 0
    assert event_start.second == 0
    assert event_start.tzinfo.utcoffset(event_start) == datetime.timedelta(hours=6)
    assert event_start.tzinfo._tzid == "Екатеринбург"

    serialized = calendar.vevent.dtstart.serialize()
    assert serialized.strip() == "DTSTART;TZID=Екатеринбург:20080530T150000"


def test_commas_in_tzid():
    ics = (
        "BEGIN:VCALENDAR\r\n"
        "PRODID:-//Microsoft Corporation//Outlook 12.0 MIMEDIR//EN\r\n"
        "VERSION:2.0\r\n"
        "BEGIN:VTIMEZONE\r\n"
        "TZID:Canberra, Melbourne, Sydney\r\n"
        "BEGIN:STANDARD\r\n"
        "DTSTART:20010325T020000\r\n"
        "RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=3;UNTIL=20050327T070000Z\r\n"
        "TZOFFSETFROM:+1100\r\n"
        "TZOFFSETTO:+1000\r\n"
        "TZNAME:Standard Time\r\n"
        "END:STANDARD\r\n"
        "BEGIN:STANDARD\r\n"
        "DTSTART:20060402T020000\r\n"
        "RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=4;UNTIL=20060402T070000Z\r\n"
        "TZOFFSETFROM:+1100\r\n"
        "TZOFFSETTO:+1000\r\n"
        "TZNAME:Standard Time\r\n"
        "END:STANDARD\r\n"
        "BEGIN:STANDARD\r\n"
        "DTSTART:20070325T020000\r\n"
        "RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=3\r\n"
        "TZOFFSETFROM:+1100\r\n"
        "TZOFFSETTO:+1000\r\n"
        "TZNAME:Standard Time\r\n"
        "END:STANDARD\r\n"
        "BEGIN:DAYLIGHT\r\n"
        "DTSTART:20001029T020000\r\n"
        "RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=10\r\n"
        "TZOFFSETFROM:+1000\r\n"
        "TZOFFSETTO:+1100\r\n"
        "TZNAME:Daylight Savings Time\r\n"
        "END:DAYLIGHT\r\n"
        "END:VTIMEZONE\r\n"
        "BEGIN:VEVENT\r\n"
        "UID:CommaTest\r\n"
        'DTSTART;TZID="Canberra, Melbourne, Sydney":20080530T150000\r\n'
        "END:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )

    calendar = vobject.readOne(ics)
    event_start = calendar.vevent.dtstart.value
    assert type(event_start) is datetime.datetime
    assert event_start.year == 2008
    assert event_start.month == 5
    assert event_start.day == 30
    assert event_start.hour == 15
    assert event_start.minute == 0
    assert event_start.second == 0
    assert event_start.tzinfo.utcoffset(event_start) == datetime.timedelta(hours=10)


def test_ruby_escaped_semicolon_in_rrule():
    ics = (
        "BEGIN:VCALENDAR\r\n"
        "VERSION:2.0\r\n"
        "CALSCALE:GREGORIAN\r\n"
        "METHOD:PUBLISH\r\n"
        "PRODID:-//LinkeSOFT GmbH//NONSGML DIMEX//EN\r\n"
        "BEGIN:VEVENT\r\n"
        "SEQUENCE:0\r\n"
        "RRULE:FREQ=DAILY\\;COUNT=10\r\n"
        "DTEND:20030101T080000\r\n"
        "UID:2008-05-29T17:31:42+02:00_865561242\r\n"
        "CATEGORIES:Unfiled\r\n"
        "SUMMARY:Something\r\n"
        "DTSTART:20030101T070000\r\n"
        "DTSTAMP:20080529T152100\r\n"
        "END:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )

    calendar = vobject.readOne(ics)
    assert calendar.vevent.rruleset.count() == 10

    events = list(calendar.vevent.rruleset)
    first = events[0]
    assert first.year == 2003
    assert first.month == 1
    assert first.day == 1
    assert first.hour == 7
    assert first.minute == 0
    assert first.second == 0

    last = events[9]
    assert last.year == 2003
    assert last.month == 1
    assert last.day == 10
    assert last.hour == 7
    assert last.minute == 0
    assert last.second == 0
