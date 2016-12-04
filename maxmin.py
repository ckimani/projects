def find_max_min(list):
    new_list=[]
    mn=min(list)
    mx=max(list)
    if max(list)== min(list):
        new_list.append(len(list))
    else:
        new_list.append(mn)
        new_list.append(mx)
    return new_list

