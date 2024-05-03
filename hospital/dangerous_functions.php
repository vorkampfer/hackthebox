<?php
	$dangerous_functions = array("exec", "passthru", "system", "shell_exec", "popen", "pcntl_exec");
	foreach ($dangerous_functions as $f){
		if (function_exists($f)){
			echo "\n[+] " . $f . " - PHP Function Exists";
		}
	}
?>