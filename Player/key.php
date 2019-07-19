<?php

$key = '_S0_R@nd0m_P@ss_';
echo base64_decode(strtr($key, '-_', '+/'));
$fp = fopen('b64coded', 'a');
fwrite($fp, base64_decode(strtr($key, '-_', '+/')));
fclose($fp);
?>
