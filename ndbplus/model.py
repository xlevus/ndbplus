from google.appengine.ext import ndb

from . import signals


__all__ = ['Model', 'Expando']


class Model(signals._SignalsMixin, ndb.Model):
    pass


class Expando(signals._SignalsMixin, ndb.Expando):
    pass

