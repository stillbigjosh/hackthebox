$password = get-content C:\Users\leo\Desktop\admin-pass.xml|convertto-securestring -asplaintext -force;
$ptr = system.runtime.interopservices.marshal::securestringtocotaskmemunicode($password);
$result = system.runtime.interopservices.marshal::ptrtostringuni($ptr);
$result
