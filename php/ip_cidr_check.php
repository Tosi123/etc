<?php
function ip_cidr($src_ip, $allow_ip) {
  foreach ($allow_ip as $ip) {
    $cidr = explode('/', $ip);
    if (count($cidr) != 2) {
        $cidr[1] = 32;
    }
    // IP 형태
    $min = long2ip((ip2long($cidr[0])) & ((-1 << (32 - (int)$cidr[1]))));
    $max = long2ip((ip2long($min)) + pow(2, (32 - (int)$cidr[1])) - 1);
    if (ip2long($src_ip) <= ip2long($max) && ip2long($src_ip) >= ip2long($min)){
        return true;
    }
  }
  return false;
}

$allow_ip = array("192.168.40.0/32");

var_dump(ip_cidr("192.168.40.55", $allow_ip));