<?php
require("C:\\xampp\PHPMailer\src\PHPMailer.php");               #Load PHP Mailer Class
require("C:\\xampp\PHPMailer\src\SMTP.php");
use PHPMailer\PHPMailer\PHPMailer;

$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';                                 #smtp servers
$mail->SMTPAuth = false;                                        #no need to use a real account with SMTPAuth off
$SMTPSecure = 'tls';

$mail->From = 'ThisIsTheSendersEmail@gmail.com';
$mail->FromName = 'Senders Name';
$mail->addAddress('ThisIsTheReceiversEmail@gmail.com', 'Receivers Name');     #who it emails

$mail->WordWrap = 50;
$mail->isHTML(true);
                                                                #Defines PHP Mail Information
$emailSent = False;
$x = 0;

function doesContain($str, $part){                              #Used to search ping results for a string
    if(strpos($str,$part)!== False){
        return True;
    }else{
        return False;
    }
}


while (True){
    $output = null;

    $ip = "127.0.0.1";                                          #IP Address pinging to check if its online
    exec("ping -n 1 $ip", $output, $status);
    $unreachable = doesContain($output[2], "Destination host unreachable.");
    $timeOut = doesContain($output[2], "Request timed out.");

    $outputLine = $output[5];                                   #Grabs the 5th array in the ping result
    $outputLineList = explode("=", $outputLine);                #Parses ping result after the "="

    $sent = $outputLineList[1];
    $received = $outputLineList[2];
    $lost = substr($outputLineList[3], 1,2);                    #Grabs first letter in the third array of the ping result
    print_r($output);

    if((int)$lost >= 1 || $unreachable || $timeOut){            #1 packet is lost, the destination is unreachable or timed out send email after 20 attempts
        echo "The host is unable to be reached, Attempt # ";
        $x++;
        echo $x;
        if($x < 20){
            continue;
        }
        $mail->Subject = 'host has gone offline';
        $mail->Body = 'host is <b>unable</b> to respond to pings and is <b>offline</b>';

        if($emailSent == False){
            if(!$mail->send()){
                echo 'Message could not be sent.';
                echo 'Mailer Error: ' . $mail->ErrorInfo;
            }else{
                $emailSent = True;
                echo "Email has been sent." . PHP_EOL;
            }
            }
    }else{
        $emailSent = False;
        $x = 0;
        echo "the host is online";
        sleep(10);
    }
}
?>