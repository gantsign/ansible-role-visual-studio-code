def test_visual_studio_code(host):
    assert host.run('which code').rc == 0


def test_visual_studio_code_signed_by(host):
    repo_file = host.file('/etc/apt/sources.list.d/vscode.list')

    assert repo_file.contains(
        'signed-by=/usr/share/keyrings/packages.microsoft.gpg')
