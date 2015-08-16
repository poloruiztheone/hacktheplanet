<?php

include '../connection.php';

$res = array();
$aux = array();

//consultation: 
$query = "SELECT id_tr, currency_pair, date, time, amount, midRate
			FROM TRANSACTION"; 

//execute the query. 

$result = $link->query($query); 

if (!$result) {
	$res["result"] = "error";
	$res["message"] = "Impossible to execute query";
	print_r(json_encode($res));
	die();
}

//display information: 
while($row = mysqli_fetch_array($result)) {
	$aux=array();
  	$aux["idOperacion"] = $row["id_tr"];
  	$aux["currencyPair"] = $row["currency_pair"];
	$aux["date"] = $row["date"];
	$aux["time"] = $row["time"]; 
	$aux["amount"] = $row["amount"];
	$aux["midRate"] = $row["midRate"]; 
} 

array_push($res, $aux);

mysqli_close($link);

print_r(json_encode($res));

?>