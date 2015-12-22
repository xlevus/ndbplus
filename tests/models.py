import ndbplus as ndb


class Model(ndb.Model):
    a = ndb.IntegerProperty()


class Expando(ndb.Expando):
    a = ndb.IntegerProperty()


