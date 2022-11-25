def get_formatted_name(f_name, l_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f_name + ' '+ middle_name + ' ' + l_name
    else:
        full_name = f_name + ' ' + l_name

    return full_name.title()

musciana = get_formatted_name('jimi', 'handrix', 'lee')
print(musciana)
musciana = get_formatted_name('jimi','handrix')
print(musciana)
