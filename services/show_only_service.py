from typing import List

def show_only(data: List, show_only: List[str]):
    if show_only == None:
        return data

    data_show_only = []
    print(data)
    for c, d in enumerate(data):
        print(d)
        data_show_only.append({})
        for k, v in d.items():
            if k in show_only:
                data_show_only[c][k] = v
    
    return data_show_only