def entryToKVal(entry):
    if not isinstance(entry, dict):
        return entry, None
    if not "vartype" in entry:
        return None, None
    if entry["vartype"] == "compound" or entry["vartype"] == "template":
        d = dict()
        iterval = entry["compounds"] if "compounds" in entry else entry["varvalue"]
        for e in iterval:
            k,v = entryToKVal(e)
            if v == None:
                continue
            if v == {}:
                continue
            if k in d:
                if not isinstance(d[k], list):
                    d[k] = [d[k], v]
                else:
                    d[k].append(v)
            else:
                d[k]=v
        return entry["varid"], d
    else:
        return entry["varid"], entry["varvalue"]

def listToDict(entries):
    d = dict()
    for ent in entries:
        k,v = entryToKVal(ent)
        if v == None:
            continue
        if v == {}:
            continue
        if k in d:
            if not isinstance(d[k], list):
                d[k] = [d[k], v]
            else:
                d[k].append(v)
        else:
            d[k]=v
    return d
