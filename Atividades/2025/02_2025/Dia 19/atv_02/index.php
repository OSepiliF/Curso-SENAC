<!-- Estruturas Condicionais -->

<?php 
    $idade = $_POST["anos"];

    if ($idade >= 18 & $idade < 60) {
        echo "Maior de Idade";

    } elseif ($idade >= 60) {
        echo "Idoso";
        
    } else echo "Menor de Idade";

?>