def test_visual_studio_code(Command):
    assert Command('which code').rc == 0
