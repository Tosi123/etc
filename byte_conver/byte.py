def conver_byte(size, flag=True):
    units = {1000: ['KB', 'MB', 'GB', 'TB', 'PB'],
            1024: ['KiB', 'MiB', 'GiB', 'TIB', 'PIB']}
    mult = 1024 if flag else 1000
    for unit in units[mult]:
        size = size / mult
        if size < mult:
            return f'{round(size, 1)} {unit}'
    return size
