import logging

import kubernetes
import pytest

import powerkube as pk


EXPECTED_CLUSTER = {'contents': 'foo', 'highlight_groups': ['kubernetes_cluster']}
EXPECTED_NAMESPACE = {'contents': 'bar', 'highlight_groups': ['kubernetes_namespace']}
EXPECTED_USER = {'contents': 'baz', 'highlight_groups': ['kubernetes_user']}


class MockK8sConfig(object):
    def __init__(self):
        self.current_context_dict = {'cluster': 'foo', 'namespace': 'bar', 'user': 'baz'}


@pytest.fixture
def expected_symbol(request):
    return {'contents': pk._KUBE_SYMBOL, 'highlight_groups': [request.param]}


@pytest.fixture
def expected_symbol_highlight_group(hg):
    return pytest.mark.parametrize('expected_symbol', [hg], indirect=True)


@pytest.fixture
def pl():
    ''' Simulate the powerline logger '''
    logging.basicConfig()
    return logging.getLogger()


@pytest.fixture
def segment_info():
    return {'environ': {}}


@pytest.fixture
def setup_mocked_context(monkeypatch):
    monkeypatch.setattr(kubernetes, 'K8sConfig', MockK8sConfig)


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_namespace')
def test_default_arguments(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info)
    assert output == [expected_symbol, EXPECTED_NAMESPACE]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_cluster')
def test_all_items(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=True, show_namespace=True, show_user=True)
    assert output == [expected_symbol, EXPECTED_CLUSTER, EXPECTED_NAMESPACE, EXPECTED_USER]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_cluster')
def test_cluster_namespace(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=True, show_namespace=True, show_user=False)
    assert output == [expected_symbol, EXPECTED_CLUSTER, EXPECTED_NAMESPACE]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_cluster')
def test_cluster_user(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=True, show_namespace=False, show_user=True)
    assert output == [expected_symbol, EXPECTED_CLUSTER, EXPECTED_USER]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_cluster')
def test_only_cluster(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=True, show_namespace=False, show_user=False)
    assert output == [expected_symbol, EXPECTED_CLUSTER]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_namespace')
def test_namespace_user(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=False, show_namespace=True, show_user=True)
    assert output == [expected_symbol, EXPECTED_NAMESPACE, EXPECTED_USER]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_namespace')
def test_only_namespace(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=False, show_namespace=True, show_user=False)
    assert output == [expected_symbol, EXPECTED_NAMESPACE]


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_user')
def test_only_user(pl, segment_info, expected_symbol):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=False, show_namespace=False, show_user=True)
    assert output == [expected_symbol, EXPECTED_USER]


@pytest.mark.usefixtures('setup_mocked_context')
def test_no_items(pl, segment_info):
    output = pk.context(pl=pl, segment_info=segment_info,
                        show_cluster=False, show_namespace=False, show_user=False)
    assert output == []


@pytest.mark.usefixtures('setup_mocked_context')
@expected_symbol_highlight_group('kubernetes_namespace')
def test_shows_if_env_var_is_yes(pl, expected_symbol):
    segment_info = {'environ': {'RENDER_POWERLINE_KUBERNETES': 'YES'}}
    output = pk.context(pl=pl, segment_info=segment_info)
    assert output == [expected_symbol, EXPECTED_NAMESPACE]


@pytest.mark.parametrize('envvar', ['NO', 'GIBBERISH'])
def test_does_not_show_if_env_var_is_not_yes(pl, envvar):
    segment_info = {'environ': {'RENDER_POWERLINE_KUBERNETES': envvar}}
    output = pk.context(pl=pl, segment_info=segment_info)
    assert output == []
