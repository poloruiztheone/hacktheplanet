<?php

include '../connection.php';

$baseCurrency = $_REQUEST["baseCurrency"];
$quoteCurrency = $_REQUEST["quoteCurrency"];
$buyRate = $_REQUEST["buyRate"];
$sellRate = $_REQUEST["sellRate"];

$res = array();

if ($baseCurrency == "") {
	$res["result"] = "error";
	$res["message"] = "The baseCurrency is empty";
	print_r(json_encode($res));
	die();
}

if ($quoteCurrency == "") {
	$res["result"] = "error";
	$res["message"] = "The quoteCurrency is empty";
	print_r(json_encode($res));
	die();
}

if ($buyRate == "") {
	$res["result"] = "error";
	$res["message"] = "The buyRate is empty";
	print_r(json_encode($res));
	die();
}

if ($sellRate == "") {
	$res["result"] = "error";
	$res["message"] = "The sellRate is empty";
	print_r(json_encode($res));
	die();
}

//consultation: 
$query = "INSERT INTO CURRENCY_PAIR (baseCurrency, quoteCurrency, buyRate, sellRate) VALUES ('" . $baseCurrency . "', '" . $quoteCurrency . "', '" . $buyRate . "', '" . $sellRate . "') "; 

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