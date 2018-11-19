import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sshd_service(host):
    s = host.service('sshd')

    assert s.is_running
    assert s.is_enabled


def test_sshd_config(host):
    f = host.file('/etc/ssh/sshd_config')

    assert f.exists
    assert f.contains('PermitRootLogin no')
    assert f.contains('PasswordAuthentication no')
