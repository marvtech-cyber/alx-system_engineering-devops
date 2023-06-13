# Execute a command
exec { 'KILLMENOW':
  command => 'pkill -f killmenow',
  path    => '/usr/local/bin/:/bin/',
}
