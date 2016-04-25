<?php
//include('connection.php');

$con=mysqli_connect("localhost","root","","india");

if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }


 explode($_POST);
 $decade = $_POST["decade"];
 $criteria = $_POST["criteria"];
 //print_r($_POST);

//replace attacktype1_txt as $criteria
//replace nine1 wrt table name:$decade
$sql="SELECT $criteria as name,count(*) as count FROM  $decade WHERE $criteria NOT LIKE 'Unknown' and $criteria NOT LIKE '$criteria' and $criteria NOT LIKE '2' and $criteria NOT LIKE '' GROUP BY $criteria LIMIT 0,20 ";

if ($result=mysqli_query($con,$sql))
  {
  // Fetch one and one row 
  $jsonarray = array();
  
 /* while ($row=mysqli_fetch_row($result))
    {
    printf ("%s (%s)\n",$row[0],$row[1]);
  echo "<br/>"; //printf();
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
