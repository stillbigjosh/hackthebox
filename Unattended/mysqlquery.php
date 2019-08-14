<?php
$servername = "localhost";
$username = "nestedflanders";
$password = "1036913cf7d38d4ea4f79b050f171e9fbf3f5e";
$db = "neddy";
$link = new mysqli($servername, $username, $password, $db);
$sql = "SHOW TABLES";
$result = mysqli_query($link, $sql);
while($row = mysqli_fetch_row($result)){
           echo $row[0]."\r\n";
    }
?>
