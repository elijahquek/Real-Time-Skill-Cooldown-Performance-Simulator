<?php
$config = [
  "cooldown_time" => $_POST["cooldown_time"],
  "stamina_cost" => $_POST["stamina_cost"]
];

file_put_contents(
  "../backend-python/config.json",
  json_encode($config, JSON_PRETTY_PRINT)
);

echo "Saved";
?>
