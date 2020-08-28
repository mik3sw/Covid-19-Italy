from covid19italy import covid19

def test1():
    # Small report about latest covid19 data
    c = covid19.Covid()
    print(c.getSmallReport())


def test2():
    # Full report about latest covid19 data
    c = covid19.Covid()
    print(c.getFullReport())