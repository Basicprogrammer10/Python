#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 1
fi
dir=$(pwd)
echo Updateing...
sudo apt update
for REQUIRED_PKG in wget python3 python3-pip screen
do
        PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
        echo Checking for $REQUIRED_PKG: $PKG_OK
        if [ "" = "$PKG_OK" ]; then
        echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
        sudo apt-get --yes install $REQUIRED_PKG
        fi
done
for i in datetime termcolor
do
        echo Installing $i
        pip3 install $i
done
echo 'Installing Web Server!'
mkdir WaterTemp
cd WaterTemp
dir=$(pwd)
wget http://connorcode.com/Downloads/Temp.py && echo 'Server Successfully Installed: 'dir'/Temp.py'
touch autorun.sh && echo "autorun.sh Created"
printf "echo Starting Python Server\nscreen -dmS WaterTemp\nscreen -S WaterTemp -p 0 -X stuff 'sudo python3 Temp.py\\n'" > autorun.sh
chmod +x autorun.sh

touch Config.ini && echo "Config.ini Created"
printf "[Data]\nwaitTimeMin = 1\noutputFile = Data.csv\n[Web Server]\nhostName = 0.0.0.0\nserverPort = 80" > Config.ini

echo 'Would you like me to start the server on boot? (Y/N)'
read start
if [ $start = 'Y' ]; then
    echo "Editing rc.local..."
    cd /etc/
    touch rc.local
    printf "cd /\ncd "$dir"\n./autorun.sh\n" > rc.local
    chmod +x /etc/rc.local
fi
start=0
echo 'The instlation is DONE!'
echo 'Would you like me to start the server? (Y/N)'
read start
if [ $start = 'Y' ]; then
    cd $dir
    sudo ./autorun.sh
fi