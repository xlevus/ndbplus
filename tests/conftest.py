import pytest

import models


@pytest.fixture(scope='module',
                params=[models.Model, models.Expando, models.Polymodel],
                ids=lambda x: x._get_kind())
def Model(request):
    return request.param


@pytest.fixture(params=[True, False], ids=['WithKey', 'WithoutKey'])
def instance(request, Model):
    instance = Model(a=1)

    if request.param:
        instance.put()

    return instance


@pytest.fixture
def key(request, instance):
    return instance.key


