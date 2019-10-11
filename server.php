<?php

$cmd = "python test.py";
exec("cd work");
exec($cmd. " > /dev/null &",$res,$out);
echo "hello world";
echo $res[0];
echo $out;

?>