#!/usr/bin/python3

def magic_string(values= []):
    if values is None:
        values = ['BestSchool']
    else:
        values.append('BestSchool')
    return ', '.join(values)
