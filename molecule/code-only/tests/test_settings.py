def test_settings(host):
    settings_file = host.file('/home/test_usr/.config/Code/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert settings_file.mode == 0o600
    assert settings_file.contains('"Vagrantfile": "ruby"')
