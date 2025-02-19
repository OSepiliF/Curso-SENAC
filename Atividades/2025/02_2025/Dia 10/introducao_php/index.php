<?php 
    $primeiro_nome = 'Bilau';
    $ultimo_nome = 'Gigante';
    
    echo '<div class="teste_2"> Ex. </div>';
    echo '<div class="teste"> 01. </div>';
    echo 'Bem 10 disse: '.$primeiro_nome.' '. $ultimo_nome;
    echo '<br>'.$primeiro_nome.' tem '.strlen(string: $primeiro_nome).' caracteres - '.$ultimo_nome.' tem '.strlen(string: $ultimo_nome).' caracteres.';

    echo '<hr>';

    $primeiroNome = 'Jão';
    $segundoNome = 'de';
    $ultimoNome = 'Oliva';

    $nomeCompleto = $primeiroNome.' '.$segundoNome.' '.$ultimoNome;

    echo '<div class="teste"> 02. </div>';
    echo 'Seu nome é ' .$nomeCompleto. ', ele tem '.strlen(string: $nomeCompleto ). ' caracteres.';

    echo '<hr>';

    $nome = 'Rafael';
    $idade = 62;
    $curso = 'TI';
    $cidade = 'Campo Grande';
    $estado = 'Mato Grosso do Sul';
    $filme = 'Barbie';

    echo '<div class="teste"> 03. </div>';
    echo 'Meu nome é '.$nome.' tenho '.$idade.' anos de idade. Estou cursando um curso de '.$curso.' e moro na cidade de '.$cidade.' no estado de '.$estado.', onde nos fins de semana saio para assistir '.$filme.'. 0_0';   
    
    echo '<hr>';

    echo '<div class="teste_2"> Atividades </div>';
    echo '<div class="teste"> 01. </div>';

    $nota1 = 45;
    $nota2 = 81;
    $nota3 = 99;

    $mediaDasProvas = ($nota1 + $nota2 + $nota3) / 3;

    echo "Notas:
        <p> 1°: $nota1
        <br> 2°: $nota2
        <br> 3°: $nota3 
        <p> Média: $mediaDasProvas";


    echo '<hr>';
    echo '<div class="teste"> 02. </div>';

    $custo_bruto = 78;
    $desconto = 10;

    $custo_final = 78 - ($custo_bruto * $desconto) / 100;

    echo "Um produto custa R$ $custo_bruto, mas com o desconto de 10% fica: $custo_final ";

    echo '<hr>';
    echo '<div class="teste"> 03. </div>';

    $idade1 = 18; //Enzo
    $idade2 = 19;
    $idade3 = 21; //Rafael
    $idade4 = 19;   
    $idade5 = 50; //Felipe

    $mediaDasIdades = ($idade1 + $idade2 + $idade3 + $idade4 + $idade5) / 5;

    echo "Notas:
        <p> 1°: $idade1
        <br> 2°: $idade2
        <br> 3°: $idade3 
        <br> 4°: $idade4 
        <br> 5°: $idade5 

        <p> Média: $mediaDasIdades";
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style> 
        .teste {
            color: blue;
            font-size: 40px;
        }

        .teste_2 {
            color: red;
            font-size: 50px;
        }
    </style>
</body>
</html>