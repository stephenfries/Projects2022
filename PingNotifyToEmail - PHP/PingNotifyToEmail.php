<?php                                                                           #https://stackoverflow.com/questions/5335273/how-can-i-send-an-email-using-php
require("C:\\xampp\PHPMailer\src\PHPMailer.php");                               #Load PHP Mailer Class
require("C:\\xampp\PHPMailer\src\SMTP.php");                                    #Load PHP Mailer STMP
use PHPMailer\PHPMailer\PHPMailer;                                              #PHP Mailer Namespace

$mail = new PHPMailer;                                                          #Initializes PHP Mailer function 
$mail->isSMTP();                                                                #Sets PHPMailer to use SMTP
$mail->Host = 'smtp.gmail.com';                                                 #Specify SMTP servers
$mail->SMTPAuth = false;                                                        #Disables SMTP authentication which allows us to use any account to mail from
$SMTPSecure = 'tls';                                                            #Enables TLS encryption

$mail->From = 'ThisIsTheSendersEmail@gmail.com';                                #Sender's Email Address
$mail->FromName = 'Senders Name';                                               #Sender's Name
$mail->addAddress('ThisIsTheReceiversEmail@gmail.com', 'Receivers Name');       #Receiver's Name

$mail->WordWrap = 50;                                                           #Word wraps at 50 characters
$mail->isHTML(true);                                                            #Use of HTML in email body
                            //Above Defines PHP Mail Information
$emailSent = False;                                                             #Initalizes emailSent to False
$x = 0;                                                                         #Initalizes failed pings to 0

function doesContain($str, $part){                                              #Function to search for strings
    if(strpos($str,$part)!== False){
        return True;
    }else{
        return False;
    }
}


while (True){
    error_reporting(E_ERROR | E_PARSE);                                         #Stops error codes from displaying
    $output = null;                                                             #Clears output variable so the array resets back to 0
                                                                                #https://stackoverflow.com/questions/13283674/how-to-ping-ip-addresses-in-php-and-give-results
    $ip = "127.0.0.1";                                                          #IP Address to ping
    exec("ping -n 1 $ip", $output, $status);                                    #Ping command, output from the ping and status
    $unreachable = doesContain($output[2], "Destination host unreachable.");    #Checks if ping array[2] displays destination host unreachable
    $timeOut = doesContain($output[2], "Request timed out.");                   #Checks if ping array[2] displays request timed out

    $outputLine = $output[5];                                                   #Parases the entire output into just array 5
    $outputLineList = explode("=", $outputLine);                                #Parses all information after the "=" in the ping

    $sent = $outputLineList[1];                                                 #This is the ping sent amount
    $received = $outputLineList[2];                                             #This is the ping received amount
    $lost = substr($outputLineList[3], 1,2);                                    #Grabs first letter in the third array of ping result

    if((int)$lost >= 1 || $unreachable || $timeOut){                            #If packets lost is greater than 1, or host unreachable or timed out
        echo "The host is unable to be reached, Attempt # ";
        $x++;                                                                   #$x is the amount of unsuccessful pings
        echo "$x" . PHP_EOL;                                                    #Display the unsuccessful amount number
        if($x < 120){                                                           #Keep running the ping until 120 unsuccessful pings happen
            continue;
        }
        $mail->Subject = 'host has gone offline';                                           #Sends email with this subject
        $mail->Body = 'host is <b>unable</b> to respond to pings and is <b>offline</b>';    #Sends email with this body

        if($emailSent == False){                                                #If Email was not sent, display error
            if(!$mail->send()){
                echo 'Message could not be sent.';
                echo 'Mailer Error: ' . $mail->ErrorInfo;
            }else{
                $emailSent = True;
                echo "Email has been sent." . PHP_EOL;                          #If Email was sent, display that it has
            }
            }
    }else{                                                                      #Ping was successful
        $emailSent = False;                                                     #Reset email initialization
        $x = 0;                                                                 #Reset ping unsuccessful counter
        echo "the host is online";                                              #Display device is online
        sleep(10);                                                              #Check status in 10 seconds
    }
}
?>