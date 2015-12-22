import ndbplus


class TestPolymodel(object):
    def test_kind(self):
        """
        Check that our extra level of inheritance from PolyModel
        doesn't mess with how PolyModel should work.
        """

        assert ndbplus.polymodel.PolyModel._get_kind() == 'PolyModel'

        class MyPolyModel(ndbplus.polymodel.PolyModel):
            pass

        assert MyPolyModel._get_kind() == 'MyPolyModel'

        class MyOtherPolyModel(MyPolyModel):
            pass

        assert MyOtherPolyModel._get_kind() == 'MyPolyModel'

