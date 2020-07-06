from osearch import osFindValue, osearch
import pytest

# Some random data that should provide some good testcases
tstObj = [
    1,
    2,
    3,
    "listval2",
    "listval5",
    {
        "dict1": "dictval1",
        "dict2": "dictval2",
        "dict3": 3,
        "dict4": ["item1", "A long string here", 1000, "another string"],
        100: 222,
    },
]


def test_rawSearch():
    # Exact search for string
    assert osearch(tstObj, "dict") == []
    assert osearch(tstObj, "dict1") == ["[5]['dict1']"]
    assert osearch(tstObj, "item1") == ["[5]['dict4'][0]='item1'"]

    # String contains. Result both in keys and values
    assert osearch(tstObj, "2", method="contains") == [
        "[3]='listval2'",
        "[5]['dict2']",
        "[5]['dict2']='dictval2'",
    ]

    # Search integer
    assert osearch(tstObj, 222) == ["[5][100]=222"]


def test_findValue():
    # Search in strings
    assert osFindValue("teststring", "teststring", "exact") is True
    assert osFindValue("teststring", "teststrinG", "exact") is False

    assert osFindValue("teststring", "str", "contains") is True
    assert osFindValue("teststring", "xxx", "contains") is False

    assert osFindValue("teststring", r"str.ng", "regex") is True
    assert osFindValue("teststring", r"str..ng", "regex") is False

    assert osFindValue("teststring", r"S.RiNg", "regex-case") is True
    assert osFindValue("teststring", r"StR..NG", "regex-case") is False

    with pytest.raises(ValueError):
        osFindValue("teststring", "string", "bad-parameter")

    # Search in integer
    assert osFindValue(1, 1, "exact") is True
    assert osFindValue(1, 2, "exact") is False

    with pytest.raises(ValueError):
        osFindValue(1, 2, "contains")

    # Mixed search
    assert osFindValue(1, "1", "exact") is False
    assert osFindValue("1", 1, "exact") is False
