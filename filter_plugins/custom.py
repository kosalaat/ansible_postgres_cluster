__author__ = 'kosala atapattu'
from ansible import errors

def get_pg_revision(values=[]):
    pg_maj_ver = str(values).split(".")[0]
    if pg_maj_ver == "9":
        return 3
    elif pg_maj_ver == "10":
        return 2
    elif pg_maj_ver == "11":
        return 1

class FilterModule(object):
    def filters(self):
        return {
            'get_pg_revision': get_pg_revision
            }
        
