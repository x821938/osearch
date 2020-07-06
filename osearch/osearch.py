import re


def osFindValue(obj, searchTerm, searchMethod):
    """Internal helper method!
    Generic search method to search a string or int for a searchTerm. Different search methods can be
    provided for different ways of searching.

    Args:
        obj (str|int): The object that is being searched in
        searchTerm (str|int): The thing we want to find
        searchMethod (str): If searching in strings, it can be "exact", "contains", "regex" or "regex-case"
                            If searching in integers it can only be "exact"

    Raises:
        ValueError: If an invalid searchmethod is provided

    Returns:
        bool: If the searchterm is found then True is returned, otherwise False
    """
    if type(obj) == int and type(searchTerm) == int:
        if searchMethod == "exact":
            return searchTerm == obj
        else:
            raise ValueError("When searching integers the method should be: exact")

    if type(obj) == str and type(searchTerm) == str:
        if searchMethod == "exact":
            return searchTerm == obj
        elif searchMethod == "contains":
            return searchTerm in obj
        elif searchMethod == "regex":
            return re.search(searchTerm, obj) is not None
        elif searchMethod == "regex-case":
            return re.search(searchTerm, obj, re.IGNORECASE) is not None
        raise ValueError("Search method should be one of: exact, contains, regex, regex-case")
    return False


def osRawSearch(obj, searchTerm, path="", ret=None, method="exact"):
    """Internal helper method
    Recursive function that traverses throug an object (nested list/dict thingy).
    It searches through the entire structure and returns the found terms.

    Args:
        obj (dict|list): The object to be searched
        searchTerm (str|int): The thing we want to find
        path (str, optional): Used for recursion to keep a static var with the path of the object found
        ret ([type], optional): Used for recursion to keep track of the list of found objects.
        method (str, optional): The way of searching. See findValue() for description

    Returns:
        [str]: A list of places in the object where the searchTerm was found
    """
    if ret is None:  # First time we are called, initialize the result list to nothing
        ret = []
    if type(obj) == dict:
        for key, val in obj.items():  # When looking at a dict, we need to go through each key and value
            skey = repr(key)  # Make a human readable path representation
            sval = repr(val)

            # Search the key and value for our term, and add result to list if found
            if osFindValue(key, searchTerm, method):
                ret.append(f"{path}[{skey}]")
            if osFindValue(val, searchTerm, method):
                ret.append(f"{path}[{skey}]={sval}")

            # Handle sub-structure via recursive calls
            if type(val) == dict:
                osRawSearch(val, searchTerm, f"{path}[{skey}]", ret, method)
            elif type(val) == list:
                osRawSearch(val, searchTerm, f"{path}[{skey}]", ret, method)
        return ret

    if type(obj) == list:
        for idx, val in enumerate(obj):  # Ehne looking at a list, we need to go through each value
            if type(val) == dict:  # Handle sub-structure via recursive calls
                osRawSearch(val, searchTerm, f"{path}[{idx}]", ret, method)
            elif type(val) == list:  # Handle sub-structure via recursive calls
                osRawSearch(val, searchTerm, f"{path}[{idx}]", ret, method)
            else:
                sval = repr(val)  # Make a human readable path representation

                # Search the value for our term, and add result to list if found
                if osFindValue(val, searchTerm, method):
                    ret.append(f"{path}[{idx}]={sval}")
        return ret


def osearch(obj, searchTerm, method="exact", prettyprint=False):
    """ Public method
    Searches through a nested object of dicts and lists and returns or prints the found items

    Args:
        obj (dict|list): A nested object you want to search in
        searchTerm (str|int): The thing you want to find
        method (str, optional): The way of searching. Defaults to "exact". It can be:
                                "exact": Only the exact stringmatch is returned
                                "contains": Returns elements which contains searchTerm somewhere in string
                                "regex": A regular expression search
                                "regex-case": Same, but case-insensitive
        prettyprint (bool, optional): Defaults to False. If set to true the the results are printed to screen.

    Returns:
        [str]: A list of found searchTerms in the object.
    """
    searchResult = osRawSearch(obj, searchTerm, method=method)
    if prettyprint:
        for found in searchResult:
            print(found)
    return searchResult
