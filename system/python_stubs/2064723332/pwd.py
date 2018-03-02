# encoding: utf-8
# module pwd
# from (built-in)
# by generator 1.145
"""
This module provides access to the Unix password database.
It is available on all Unix versions.

Password database entries are reported as 7-tuples containing the following
items from the password database (see `<pwd.h>'), in order:
pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell.
The uid and gid items are integers, all others are strings. An
exception is raised if the entry asked for cannot be found.
"""
# no imports

# functions

def getpwall(): # real signature unknown; restored from __doc__
    """
    getpwall() -> list_of_entries
    Return a list of all available password database entries, in arbitrary order.
    See help(pwd) for more on password database entries.
    """
    pass

def getpwnam(name): # real signature unknown; restored from __doc__
    """
    getpwnam(name) -> (pw_name,pw_passwd,pw_uid,
                        pw_gid,pw_gecos,pw_dir,pw_shell)
    Return the password database entry for the given user name.
    See help(pwd) for more on password database entries.
    """
    pass

def getpwuid(uid): # real signature unknown; restored from __doc__
    """
    getpwuid(uid) -> (pw_name,pw_passwd,pw_uid,
                      pw_gid,pw_gecos,pw_dir,pw_shell)
    Return the password database entry for the given numeric user ID.
    See help(pwd) for more on password database entries.
    """
    pass

# classes

class struct_passwd(tuple):
    """
    pwd.struct_passwd: Results from getpw*() routines.
    
    This object may be accessed either as a tuple of
      (pw_name,pw_passwd,pw_uid,pw_gid,pw_gecos,pw_dir,pw_shell)
    or via the object attributes as named in the above tuple.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    pw_dir = property(lambda self: '')
    """home directory

    :type: string
    """

    pw_gecos = property(lambda self: '')
    """real name

    :type: string
    """

    pw_gid = property(lambda self: 0)
    """group id

    :type: int
    """

    pw_name = property(lambda self: '')
    """user name

    :type: string
    """

    pw_passwd = property(lambda self: '')
    """password

    :type: string
    """

    pw_shell = property(lambda self: '')
    """shell program

    :type: string
    """

    pw_uid = property(lambda self: 0)
    """user id

    :type: int
    """


    n_fields = 7
    n_sequence_fields = 7
    n_unnamed_fields = 0


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """ Load a built-in module. """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

