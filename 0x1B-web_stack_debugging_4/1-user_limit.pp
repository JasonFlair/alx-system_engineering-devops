# puppet manifest to make changes to the holberton user limits configuration

exec {'hard nofile change':
  command  => 'sed -i "s/nofile 5/nofile 6000/" /etc/security/limits.conf',
  provider => 'shell',
  before   => Exec['soft nofile change'],
}
exec {'soft nofile change':
  command  => 'sed -i "s/nofile 4/nofile 5000/" /etc/security/limits.conf',
  provider => 'shell',
}