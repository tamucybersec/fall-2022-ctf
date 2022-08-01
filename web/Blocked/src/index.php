<?php
if(isset($_SERVER['HTTP_X_FORWARDED_FOR']) && $_SERVER['HTTP_X_FORWARDED_FOR'] == '127.0.0.1') {
    include('feda5e50c0be175a089ec76fd5eeb4cd.html');
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
    include('eb44136778bf0fa5b4060d5563a90605.html');
}
?>

