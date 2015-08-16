<?php

include '../connection.php';

$full_name = $_REQUEST["name"];
$email = $_REQUEST["email"];

$res = array();

if ($full_name == "") {
	$res["result"] = "error";
	$res["message"] = "The name is empty";
	print_r(json_encode($res));
	die();
}

if ($email == "") {
	$res["result"] = "error";
	$res["message"] = "The email is empty";
	print_r(json_encode($res));
	die();
}

//consultation: 
$query = "INSERT INTO CLIENT (full_name, email) VALUES ('" . $full_name . "', '" . $email . "' ) "; 

//execute the query. 

$result = $link->query($query); 

//display information: 

//while($row = mysqli_fetch_array($result)) { 
  //echo $row["name"] . "<br>"; 
//} 

if (!$result) {
	die("ERROR NO SE PUDO INSERTAR");
}

mysqli_close($link);

$res["result"] = "ok";
$res["message"] = "correct insert";
print_r(json_encode($res));

?>