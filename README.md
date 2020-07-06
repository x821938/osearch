# Osearch - The tool for finding information in nested dicts/lists

When you are working with imported JSON in python, it's often hard to get an overview of the datastructure. I created `osearch` to help you with this. It allows you to search for strings or integers in huge nested structures.
Here is an example of a messy test structure:
```
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
```
first we import the `osearch` lib: 
```
from osearch import osearch
```
Now we can do some funny searches for strings containing the part "val":
```
>> osearch(tstObj, "val", method="contains", prettyprint=True)
[3]='listval2'
[4]='listval5'
[5]['dict1']='dictval1'
[5]['dict2']='dictval2'
```

Or we could search for an integer:
```
>> osearch(tstObj, 100, prettyprint=True)
[5][100]
```

Or maybe even a regular expression search that is non-case sensitive. Here we search for all occurances of keys/values that ends in val1 or val5:
```
>> osearch(tstObj, r"val[15]$", method="regex-case", prettyprint=True)
[4]='listval5'
[5]['dict1']='dictval1'
```
Have fun

/ Alex Skov Jensen