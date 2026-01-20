<?php
$cooldown = $_POST["cooldown"];
file_put_contents("config.txt", $cooldown);
echo "Saved!";
?>
