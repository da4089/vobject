import vobject

radicale_1587 = (
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN:Given Family\r\n"
    "N:Family;Given;Additional;Prefix;Suffix\r\n"
    "GEO:37.386013;-122.082932\r\n"
    "END:VCARD\r\n"
)


def test_radicale_1587():
    vobjs = vobject.readComponents(radicale_1587)
    for vo in vobjs:
        assert vo is not None
        lines = vo.serialize().split("\r\n")
        for line in lines:
            if line.startswith("GEO"):
                assert line == "GEO:37.386013;-122.082932"
