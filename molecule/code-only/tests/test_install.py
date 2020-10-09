def test_visual_studio_code(host):
    assert host.run('which code').rc == 0
