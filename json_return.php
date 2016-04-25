<?php
header('Content-type: application/json');
$data1 = array( 'a', 'b', 'c' );
$data2 = array( 'name' => 'God', 'age' => -1 );
$option = 1; 
$data = '[{"name":"Armed Assault","value":9},
{"name":"Assassination","value":5},
{"name":"Bombing/Explosion","value":5},
{"name":"Facility/Infrastructure Attack","value":2},
{"name":"Hijacking","value":2},
{"name":"Unknown","value":1}]';


  echo json_encode($data);
 
?>