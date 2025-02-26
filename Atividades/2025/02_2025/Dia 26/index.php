<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
   $nome = $_POST["nome"];
   $data_nasc = $_POST["data_nasc"];
   $sexo = $_POST["sexo"];
   $cpf = $_POST["cpf"];
   $rg = $_POST["rg"];
   $email = $_POST["email"];
   $confirm_email = $_POST["confirm_email"];
   $senha = $_POST["senha"];
   $confirm_senha = $_POST["confirm_senha"];
   $endereco = $_POST["endereco"];
   $cidade = $_POST["cidade"];
   $estado = $_POST["estado"];
   $celular = $_POST["celular"];
}

?>