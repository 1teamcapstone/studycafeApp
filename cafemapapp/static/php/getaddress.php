<?php

    header("Content-Type: application/json");
    include "db.php";
    $db=new MysqliDb('localhost','root','0000','studycafe');
    
    $users = $db->getValue('studycafes','address',null); //contains an Array of all users 

    echo json_encode($users);


?>
