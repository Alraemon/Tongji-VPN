#! /bin/sh
# 利用cookie连接同济VPN

cookie=$(python /home/erwin/Telegram/TJVPN/tjvpnCookie.py 2>&1)
echo "获得Cookie: $cookie"
sudo openconnect -q -b --juniper --no-dtls --cookie "DSID=${cookie}" vpn.tongji.cn
echo "已连接"
