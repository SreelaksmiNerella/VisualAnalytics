<?php
include('connection.php');

//$con=mysqli_connect("localhost","root","","india");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

  //replace csv file with $deacde.".csv"
$handle = fopen("latestnews.csv", "r");
// Read first (headers) record only)
$data = fgetcsv($handle, 1000, ",");
$sql= 'CREATE TABLE IF NOT EXISTS news(';
for($i=0;$i<count($data); $i++) {
$sql .= $data[$i].' VARCHAR(50), ';
}
//The line below gets rid of the comma
$sql = substr($sql,0,strlen($sql)-2);
$sql .= ')';
$sql .=';';
//echo $sql;
$res=mysql_query($sql);
echo"hello";
if(!$res)
    {
      echo mysql_error();
    }

fclose($handle);


$query1  = "LOAD DATA INFILE 'latestnews.csv' INTO TABLE news FIELDS TERMINATED BY ','";
$res1=mysql_query($query1);
if(!$res1)
    {
      echo "error is ".mysql_error();
    }
	
	?>