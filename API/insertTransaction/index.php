<?php

include '../connection.php';

$client_id = $_REQUEST["client_id"];
$currency_pair = $_REQUEST["currency_pair"];
$profit_loss = $_REQUEST["profit_loss"];
$date = $_REQUEST["date"];
$time = $_REQUEST["time"];
$amount = $_REQUEST["amount"];
$changed = $_REQUEST["changed"];
$midRate = $_REQUEST["midRate"];


$res = array();

if ($client_id == "") {
	$res["result"] = "error";
	$res["message"] = "The client_id is empty";
	print_r(json_encode($res));
	die();
}

if ($currency_pair == "") {
	$res["result"] = "error";
	$res["message"] = "The currency_pair is empty";
	print_r(json_encode($res));
	die();
}

if ($profit_loss == "") {
	$res["result"] = "error";
	$res["message"] = "The profit_loss is empty";
	print_r(json_encode($res));
	die();
}

if ($date == "") {
	$res["result"] = "error";
	$res["message"] = "The date is empty";
	print_r(json_encode($res));
	die();
}

if ($time == "") {
	$res["result"] = "error";
	$res["message"] = "The time is empty";
	print_r(json_encode($res));
	die();
}

if ($amount == "") {
	$res["result"] = "error";
	$res["message"] = "The amount is empty";
	print_r(json_encode($res));
	die();
}

if ($changed == "") {
	$res["result"] = "error";
	$res["message"] = "The changed is empty";
	print_r(json_encode($res));
	die();
}

if ($midRate == "") {
	$res["result"] = "error";
	$res["message"] = "The midRate is empty";
	print_r(json_encode($res));
	die();
}

//consultation: 
$query = "INSERT INTO TRANSACTION (CLIENT_id_cl, currency_pair, profit_loss, date, time, amount, changed, midRate) VALUES ('" . $client_id . "', '" . $currency_pair . "', '" . $profit_loss . "', '" . $date . "', '" . $time . "', '" . $amount . "', '" . $changed . "', '" . $midRate . "') "; 

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