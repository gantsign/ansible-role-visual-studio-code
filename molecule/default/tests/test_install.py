def test_visual_studio_code(host):
    assert host.run('which code').rc == 0


def test_visual_studio_code_insiders(host):
    assert host.run('which code-insiders').rc == 0
