wget https://github.com/Biubush/AHU-netlogin/releases/download/AHU-netlogin/AHU-netlogin.py -O /etc/AHU-netlogin.py
chmod 777 /etc/AHU-netlogin.py
wget https://github.com/Biubush/AHU-netlogin/releases/download/AHU-netlogin/AHU-netlogin.service -O /etc/AHU-netlogin.service
chmod 777 /etc/AHU-netlogin.service
systemctl daemon-reload
systemctl enable AHU-netlogin
systemctl start AHU-netlogin
