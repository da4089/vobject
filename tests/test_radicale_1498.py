# -*- encoding: utf-8 -*-

import vobject

ics = (
    "BEGIN:VCALENDAR\r\n"
    "VERSION:2.0\r\n"
    "PRODID:-//PYVOBJECT//NONSGML Version 1//EN\r\n"
    "BEGIN:VEVENT\r\n"
    "UID:removed@google.com\r\n"
    "DTSTART:20211022T140000Z\r\n"
    "DTEND:20211024T214500Z\r\n"
    "ATTENDEE;CN=removed;EMAIL=removed@removed.com;RSVP=FALSE:mailto:\r\n"
    " removed@removed.com\r\n"
    "ATTENDEE;CN=removed;CUTYPE=INDIVIDUAL;EMAIL=removed@removed.com;PARTSTA\r\n"
    " T=ACCEPTED;X-CALENDARSERVER-DTSTAMP=20221227T172148Z:mailto:removed@removed.co\r\n"
    " m\r\n"
    "CLASS:PUBLIC\r\n"
    "CREATED:20221227T172148Z\r\n"
    'DESCRIPTION;ALTREP="data:text/html,%3Ctable%3E%3Ctbody%3E%3Ctr%3E%3Ctd%3EDi\r\n'
    " e%20Buchungremovednotrelevant\r\n"
    ' A~%3A~%3A~%3A~%3A~%3A~%3A~%3A~%3A~%3A~%3A~%3A~%3A%3A~%3A~%3A%3A-%3Cbr%3E":\r\n'
    "                         \\nDie Buchung für den folgenden Zeitraum wurd\r\n"
    " e geändert\\n22.10.2021 16:00 - 24.10.2021 23:45\\n \\nDas Fahrzeug befindet\r\n"
    " sich am folgenden Standort\\n                                removed\r\n"
    "                  \\n \\nWeitere Buchungsdetails\\n\r\n"
    " \r\n"
    " \r\n"
    " \r\n"
    " \r\n"
    "                                                  \\nBenutzer:       removed\r\n"
    " \\nFahrzeug: Renault Zoe\\nNummernschild:     removed\\nFahrziel:     removed\r\n"
    " \\nFahrzweck:   Privat\\nBenutzungsart:  Privat\\n\\n\\n-::~:~::~:~:~:~:~:~:~:~:~:\r\n"
    " removed\r\n"
    " ~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~::~:~::-\\n\r\n"
    "DTSTAMP:20231231T121233Z\r\n"
    "LAST-MODIFIED:20221227T172148Z\r\n"
    "ORGANIZER;CN=removed@removed.com;EMAIL=removed@removed.com:mailto\r\n"
    " :removed@removed.com\r\n"
    "SEQUENCE:0\r\n"
    'SUMMARY:s Leasing Fahrzeug "Renault Zoe"\r\n'
    "TRANSP:OPAQUE\r\n"
    "END:VEVENT\r\n"
    "END:VCALENDAR\r\n"
)


def test_radicale_1498():
    vobjs = vobject.readComponents(ics)
    for vo in vobjs:
        assert vo is not None
