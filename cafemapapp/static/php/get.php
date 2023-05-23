<?php
    $host = "localhost";
    $user = "root";
    $pw = "0000";
    $dbName = "studycafe";

    $conn = new mysqli($host, $user, $pw, $dbName);
    
    /* DB 연결 확인 */
    if($conn){ echo "Connection established"."<br>"; }
    else{ die( 'Could not connect: ' . mysqli_error($conn) ); }

    
    /* SELECT 예제 */
    $sql = "SELECT name, address FROM studycafes";
    $result = mysqli_query($conn, $sql);

    $arr = array();

    while($row = mysqli_fetch_array($result)){
        array_push($arr, [$row['name'], $row['address']]);        
    }
    //echo var_dump($arr);

    mysqli_close($conn);
?>