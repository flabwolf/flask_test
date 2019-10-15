<?php

$cmd = "python -V";
exec($cmd,$res,$out);
echo $res;
echo "\n";
echo $res[0];
echo "\n";

?>