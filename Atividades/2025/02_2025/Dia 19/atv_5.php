<?php
    function Sequencia() {
        $fib = [0,1];
        for ($i = 2; $i < 10; $i++){
            $fib[] = $fib[$i - 1] + $fib[$i - 2];
        }  

        foreach ($fib as $print) {
            echo $print. '<br>';
        }
    }

    Sequencia();
?>