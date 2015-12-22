import mock
import pytest

import ndbplus


@pytest.yield_fixture
def pre_put_signal():
    m = mock.Mock()
    with ndbplus.signals.pre_put.connected_to(m):
        yield m


@pytest.yield_fixture
def post_put_signal():
    m = mock.Mock()
    with ndbplus.signals.post_put.connected_to(m):
        yield m


@pytest.yield_fixture
def pre_get_signal():
    m = mock.Mock()
    with ndbplus.signals.pre_get.connected_to(m):
        yield m


@pytest.yield_fixture
def post_get_signal():
    m = mock.Mock()
    with ndbplus.signals.post_get.connected_to(m):
        yield m


@pytest.yield_fixture
def pre_delete_signal():
    m = mock.Mock()
    with ndbplus.signals.pre_delete.connected_to(m):
        yield m


@pytest.yield_fixture
def post_delete_signal():
    m = mock.Mock()
    with ndbplus.signals.post_delete.connected_to(m):
        yield m


@pytest.yield_fixture
def pre_allocate_ids_signal():
    m = mock.Mock()
    with ndbplus.signals.pre_allocate_ids.connected_to(m):
        yield m


@pytest.yield_fixture
def post_allocate_ids_signal():
    m = mock.Mock()
    with ndbplus.signals.post_allocate_ids.connected_to(m):
        yield m


ALLOCATE_ID_KWARGS = [
    {'size': 10, 'max': None, 'parent': None},
    {'size': None, 'max': 10, 'parent': None},
    {'size': None, 'max': None, 'parent': ndbplus.Key('BogusModel', 'foo')}
]


@pytest.mark.usefixtures('ndb')
class TestSignals(object):
    def test_pre_put_signal(self, instance, pre_put_signal):
        instance.put()

        pre_put_signal.assert_called_once_with(
            instance.__class__,
            instance=instance)

    def test_post_put_signal(self, instance, post_put_signal):
        instance.put()

        post_put_signal.assert_called_once_with(
            instance.__class__,
            instance=instance,
            future=mock.ANY)

    def test_pre_get_signal(self, key, pre_get_signal):
        if key is None:
            # Byproduct of genrating tests with fixtures
            return

        instance = key.get()

        pre_get_signal.assert_called_once_with(
            instance.__class__,
            key=key)

    def test_post_get_signal(self, key, post_get_signal):
        if key is None:
            # Byproduct of genrating tests with fixtures
            return

        instance = key.get()

        post_get_signal.assert_called_once_with(
            instance.__class__,
            key=key,
            future=mock.ANY)

    @pytest.mark.parametrize('kwargs', ALLOCATE_ID_KWARGS)
    def test_pre_allocate_ids_signal(self, kwargs,
                                     Model, pre_allocate_ids_signal):
        Model.allocate_ids(**kwargs)

        pre_allocate_ids_signal.assert_called_once_with(
            Model,
            **kwargs)

    @pytest.mark.parametrize('kwargs', ALLOCATE_ID_KWARGS)
    def test_post_allocate_ids_signal(self, kwargs, Model,
                                      post_allocate_ids_signal):
        Model.allocate_ids(**kwargs)

        post_allocate_ids_signal.assert_called_once_with(
            Model,
            future=mock.ANY,
            **kwargs)

