$password='36mEAhz/B8xQ~2VM'|convertto-securestring -asplaintext -force;
$cred=new-object -typename system.management.automation.pscredential('SNIPER\chris',$password);
Invoke-Command -computer SNIPER -credential $cred {type c:\users\chris\desktop\user.txt};
