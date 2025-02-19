<?php
    function Calculo() {
        $comp = $_POST["comprimento"];
        $larg = $_POST["largura"];

        $calcular_area = $comp * $larg;

        echo "<h2>Cálculo:</h2>";
        echo "<p><strong>Comprimento:</strong> " . $comp . " px</p>";
        echo "<p><strong>Largura:</strong> " . $larg . " px</p>";
        echo "<p><strong>Área:</strong> " . $calcular_area . " px²</p>";

        echo '<div class="area_box" style="width: ' . $larg . 'px; height: ' . $comp . 'px;">
                <span>' . $calcular_area . ' px²</span>
            </div>';
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>04</title>
</head>
<body>
    <form action="./index.php" method="post">
        <div class="coluna_input">
            <label for="text_n1">Comprimento</label>
            <input type="number" name="comprimento" id="comprimento" required>
        </div>
        <div class="coluna_input">
            <label for="text_n2">Largura</label>
            <input type="number" name="largura" id="largura" required>
        </div>
        <button type="submit">CALCULAR</button>
    </form>

    <?php Calculo() ?>

    <style>
        .coluna_input {
            display: flex;
            flex-direction: column;
            max-width: 200px;
        }

        h2 {
            color: #333;
        }

        .result p {
            font-size: 18px;
            color: #555;
        }

        .area_box {
            margin-top: 20px;
            display: flex;
            justify-content: start;

            border: 2px solid #000;
            background-color: green;
        }

        .area_box span {
            color: white;
            font-weight: bold;
        }

    </style>
</body>
</html>
