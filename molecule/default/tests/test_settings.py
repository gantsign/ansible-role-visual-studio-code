def test_settings(host):
    settings_file = host.file('/home/test_usr/.config/Code/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert settings_file.mode == 0o600
    assert settings_file.contains('"Vagrantfile": "ruby"')


def test_settings_insiders(host):
    settings_file = host.file(
        '/home/test_usr/.config/Code - Insiders/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert settings_file.mode == 0o600
    assert settings_file.contains('"Vagrantfile": "ruby"')


def test_settings_overwrite(host):
    settings_file = host.file(
        '/home/test_usr4/.config/Code/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr4'
    assert settings_file.group == 'test_usr4'
    assert settings_file.mode == 0o600
    assert not settings_file.contains('remove_me')


def test_keybindings(host):
    settings_file = host.file(
        '/home/test_usr/.config/Code/User/keybindings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert settings_file.mode == 0o600
    assert settings_file.contains(
        '"command": "workbench.action.terminal.focus"')


def test_keybindings_overwrite(host):
    settings_file = host.file(
        '/home/test_usr4/.config/Code/User/keybindings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr4'
    assert settings_file.group == 'test_usr4'
    assert settings_file.mode == 0o600
    assert not settings_file.contains('remove_me')


def test_keybindings_insiders(host):
    settings_file = host.file(
        '/home/test_usr/.config/Code - Insiders/User/keybindings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert settings_file.mode == 0o600
    assert settings_file.contains(
        '"command": "workbench.action.terminal.focus"')
