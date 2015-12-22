from google.appengine.ext.ndb import polymodel

from .signals import _SignalsMixin


__all__ = ['PolyModel']


class PolyModel(_SignalsMixin, polymodel.PolyModel):

    @classmethod
    def _get_hierarchy(cls):
        """
        Internal helper to return the list of polymorphic base classes.
        This returns a list of class objects, e.g. [Animal, Feline, Cat].

        As this PolyModel needs to behave like the root PolyModel, we need
        to adjust this to take the extra level of subclass into consideration.
        """
        bases = []
        for base in cls.mro():  # pragma: no branch
            if hasattr(base, '_get_hierarchy') and base != polymodel.PolyModel:
                bases.append(base)
        del bases[-1]  # Delete PolyModel itself
        bases.reverse()
        return bases
