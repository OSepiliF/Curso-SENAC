<!-- Laços de Repetição -->

<?php
    for ($i = 0; $i <= 100; $i++) {
        
        if ($i % 3 == 0 && $i % 5 == 0) {
            echo "<br>|$i|: AB ";
            
        } elseif ($i % 3 == 0) {
            echo "<br>|$i|: A ";  
            
        } elseif ($i % 5 == 0) {
            echo "<br>|$i|: B ";  
            
        } else {
            echo "<br>|$i|: $i ";  
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>03</title>
</head>
<body>
    
</body>
</html>