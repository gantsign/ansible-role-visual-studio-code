import pytest


@pytest.mark.parametrize('extension', [
    'ms-python.python',
    'wholroyd.jinja'
])
def test_visual_studio_code(host, extension):
    output = host.check_output('sudo --user test_usr -H code %s %s',
                               '--install-extension', extension)
    assert 'already installed' in output


@pytest.mark.parametrize('extension', [
    'ms-python.python',
    'wholroyd.jinja'
])
def test_visual_studio_code_insiders(host, extension):
    output = host.check_output('sudo --user test_usr -H code-insiders %s %s',
                               '--install-extension', extension)
    assert 'already installed' in output
