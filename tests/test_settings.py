from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_settings(File):
    settings_file = File('/home/test_usr/.config/Code/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.user == 'test_usr'
    assert settings_file.group == 'test_usr'
    assert oct(settings_file.mode) == '0600'
    assert settings_file.contains('"Vagrantfile": "ruby"')
