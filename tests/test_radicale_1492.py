# -*- coding: utf-8 -*-

import pytest

import vobject

# From: https://github.com/Kozea/Radicale/issues/1492

vcs = (
    # First cited example, embedded in a constructed valid vCard 3.0.
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN: Example #1\r\n"
    "N:Stevenson;John;Philip, Paul;Dr.;Jr., M.D., A.C.P.\r\n"
    'X-APPLE-END-LOCATION;VALUE=URI;X-ADDRESS="Airport Location, Address, Country";\r\n'
    ' X-APPLE-MAPKIT-HANDLE=BASE64encodedSOMETHING=;X-TITLE=Airport \\"Location\\":geo:1.23456,1.23456\r\n'
    "END:VCARD\r\n"
    # Second cited example, embedded in a constructed valid vCard 3.0.
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN: Example #1\r\n"
    "N:Stevenson;John;Philip, Paul;Dr.;Jr., M.D., A.C.P.\r\n"
    "X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-ADDRESS=Αεροδρόμιο Θεσσαλονίκης\r\n"
    ' \\"Μακεδονία\\" 551 03 Thessaloniki Greece;X-TITLE=Thessaloniki Internatio\r\n'
    " nal Airport:geo:40.520833,22.972222\r\n"
    "END:VCARD\r\n"
)


@pytest.mark.skip(reason="needs quirks-mode (#111)")
def test_radicale_1492():
    """This bug report from Radicale is caused by the illegal use of DQUOTE
    characters in the parameter value.  They are backslash-quoted, but this
    is not supported by vCard 3.0.  This should be rejected by a strict-mode
    parsing, but could be accepted by a quirks-mode parser."""

    components = vobject.readComponents(vcs)
    for vo in components:
        assert vo is not None
