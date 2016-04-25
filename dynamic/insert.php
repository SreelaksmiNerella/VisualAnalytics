<?php
include('connection.php');

//$con=mysqli_connect("localhost","root","","india");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

  //replace csv file with $deacde.".csv"
$handle = fopen("2000-09.csv", "r");
// Read first (headers) record only)
$data = fgetcsv($handle, 1000, ",");
$sql= 'CREATE TABLE IF NOT EXISTS nine1 (';
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


$query1  = "LOAD DATA INFILE '/Temp/2000-09.csv' INTO TABLE nine1 FIELDS TERMINATED BY ','";
$res1=mysql_query($query1);
if(!$res1)
    {
      echo "error is ".mysql_error();
    }
	
	?>