import pdmt.api

'''
This is the a null cache handler handler
It does not have a cache...:)
'''

class NullCache(Cache):
    def has_checksum(self, checksum):
        return False
    def get_filename(self, checksum, filename):
        pass
    def put_filename(self, checksum, filename):
        pass
