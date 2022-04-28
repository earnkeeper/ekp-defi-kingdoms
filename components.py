# https://betterprogramming.pub/how-to-remove-null-none-values-from-a-dictionary-in-python-1bedf1aab5e4
def cleanNullTerms(d):
    clean = {}
    for k, v in d.items():
        if isinstance(v, dict):
            nested = cleanNullTerms(v)
            if len(nested.keys()) > 0:
                clean[k] = nested
        elif v is not None:
            clean[k] = v
    return clean

def Span(content, className=None):
    return {
        "_type": "Span",
        "props": cleanNullTerms({
            "className": className,
            "content": content,
        })
    }


def Container(children, className=None):
    return {
        "_type": "Container",
        "props": cleanNullTerms({
            "className": className,
            "children": children
        })
    }


def Row(children, className=None):
    return {
        "_type": "Row",
        "props": cleanNullTerms({
            "className": className,
            "children": children
        })
    }


def Col(children, className=None):
    return {
        "_type": "Col",
        "props": cleanNullTerms({
            "className": className,
            "children": children
        })
    }


def Icon(name, className=None, size=None):
    return {
        "_type": "Icon",
        "props": cleanNullTerms({
            "className": className,
            "name": name,
            "size": size
        })
    }


def Datatable(data, columns, className=None):
    return {
        "_type": "Datatable",
        "props": cleanNullTerms({
            "className": className,
            "columns": columns,
            "data": data,
        })
    }


def Column(id, title=None):
    return cleanNullTerms({
        "id": id,
        "title": title,
    })

def documents(collectionName):
    return f'$["{collectionName}"].*'