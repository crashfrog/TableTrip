from functools import wraps


def tabletrip(cls=None):
    """
    Two-mode decorator to annotate model classes that should have an editable table representation.

    @tabletrip
    class MyModel(Orm.Model):

        

    """