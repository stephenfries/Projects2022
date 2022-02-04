<html>
<body>
ROCK PAPER SCISSORS!
<form name="form" action="" method="post">
<input type="text" name="playerMove">
</form>

<?php
    error_reporting(E_ERROR | E_PARSE); 
    session_start();
    $wins = 0 + $_SESSION["wins"];
    $losses = 0 + $_SESSION["losses"];
    $ties = 0 + $_SESSION["ties"];

    $playerMove = $_POST["playerMove"];
    $start = 0;
    echo("Type one of r, p, or s. (q to quit) <br>");
            
        if($playerMove == "r"){
            echo("<b>ROCK</b> versus...");
            $start = 1;
        }
        elseif($playerMove == "p"){
            echo("<b>PAPER</b> versus...");
            $start = 1;
        }
        elseif($playerMove == "s"){
            echo("<b>SCISSORS</b> versus...");
            $start = 1;
        }
        elseif($playerMove == "q"){
            session_destroy();
            echo ("SCORE: ");
        }
        if($start == 1){
            $randomNum = rand(1,3);
            if($randomNum == 1){
                $computerMove = "r";
                echo("<b>ROCK</b><br>");
            }
            elseif($randomNum == 2){
                $computerMove = "p";
                echo("<b>PAPER</b><br>");
            }
            elseif($randomNum == 3){
                $computerMove = "s";
                echo("<b>SCISSORS</b><br><br>");
            }
            if ($playerMove == $computerMove){
                echo("<h1>It is a <b>tie!</h1></b>");
                $ties = $ties + 1;
            }
            elseif($playerMove == "r" and $computerMove == "s"){
                echo("<h1>You <b>Win!</h1></b>");
                $wins = $wins + 1;
                echo '<img src="https://i.imgur.com/wiJfGA2.gif" width="350" height="150">';
            }
            elseif($playerMove == "p" and $computerMove == "r"){
                echo("<h1>You <b>Win!</h1></b>");
                $wins = $wins + 1;
                echo '<img src="https://i.imgur.com/wiJfGA2.gif" width="350" height="150">';
            }
            elseif($playerMove == "s" and $computerMove == "p"){
                echo("<h1>You <b>Win!</h1></b>");
                $wins = $wins + 1;
                echo '<img src="https://i.imgur.com/wiJfGA2.gif" width="350" height="150">';
            }
            elseif($playerMove == "r" and $computerMove == "p"){
                echo("<h1>You <b>Lose!</h1></b>");
                $losses = $losses + 1;
            }
            elseif($playerMove == "p" and $computerMove == "s"){
                echo("<h1>You <b>Lose!</h1></b>");
                $losses = $losses + 1;
            }
            elseif($playerMove == "s" and $computerMove == "r"){
                echo("<h1>You <b>Lose!</h1></b>");
                $losses = $losses + 1;
            }
        }
    $_SESSION["wins"] = $wins;
    $_SESSION["losses"] = $losses;
    $_SESSION["ties"] = $ties;

    echo("<br>" . $_SESSION["wins"] . " wins, " . $_SESSION["losses"] . " losses, " . $_SESSION["ties"] . " ties<br>");
?>
</body>
</html>