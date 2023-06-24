#execute command
exec { 'pkill killmenow':
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep killmenow',
}

