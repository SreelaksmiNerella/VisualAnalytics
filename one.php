<?php
include('connection.php');
//mysql_connect("localhost", "root", "","") or die(mysql_error());
//mysql_select_db("test1") or die(mysql_error());
$query1  = "LOAD DATA INFILE '/Temp/2000-09.csv' INTO TABLE details FIELDS TERMINATED BY ','";
$res=mysql_query($query1);
/*
$query = mysql_query("SELECT DISTINCT gname FROM dup")

or die(mysql_error());
$i = 1;
if($query)
{
while ($row = mysql_fetch_assoc($query))
{
	
    $ins=mysql_query("UPDATE dup SET value = {$i} WHERE gname = '{$row['gname']}'");
   $i++;
}
}
$que  = "SELECT gname,value INTO OUTFILE 'C:/tmp/answer.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' FROM dup";
$res1 = mysql_query($que) or die(mysql_error());*/
?>