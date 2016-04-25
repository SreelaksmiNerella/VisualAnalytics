<?php
//include('connection.php');

$con=mysqli_connect("localhost","root","","india");

if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }


  
//replace attacktype1_txt as $criteria
//replace nine1 wrt table name:$decade
$sql="SELECT attacktype1_txt as name,count(*) as count FROM  nine1 WHERE attacktype1_txt NOT LIKE 'Unknown' and attacktype1_txt NOT LIKE 'attacktype1_txt' and attacktype1_txt NOT LIKE '2' GROUP BY attacktype1_txt LIMIT 0,20 ";

if ($result=mysqli_query($con,$sql))
  {
  // Fetch one and one row 
  $jsonarray = array();
  
 /* while ($row=mysqli_fetch_row($result))
    {
    printf ("%s (%s)\n",$row[0],$row[1]);
	echo "<br/>";	//printf();
    }*/
  
  while ($row=mysqli_fetch_object($result))
    {
    $jsonarray[]=$row;
    }
  
  echo json_encode($jsonarray);
  // Free result set
  
  mysqli_free_result($result);
}

mysqli_close($con);

?>
