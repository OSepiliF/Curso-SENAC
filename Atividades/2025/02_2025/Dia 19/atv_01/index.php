<!-- Manipulação de Variáveis e Tipos de Dados -->

<?php

    $num1 = $_POST["n1"];
    $num2 = $_POST["n2"];

    $soma = $num1 + $num2;
    $sub = $num1 - $num2;
    $div = $num1 / $num2;
    $mult = $num1 * $num2;

    echo "<h2>Calculo:</h2> <p>";
    echo "Soma: " . $soma . "<br>";
    echo "Subtração: " . $sub . "<br>";
    echo "Divisão: " . $div . "<br>";
    echo "Multiplicação: " . $mult . "<br>";

?>
