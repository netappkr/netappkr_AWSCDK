#rendom /endの実行
rendom /end
#DNS Serverの追加設定
Add-DnsServerPrimaryZone -Name _msdcs.demoXX.netapp.com -ReplicationScope Domain -DynamicUpdate NonsecureAndSecure -PassThru
Start-Sleep 5
#DNS Suffixの変更
Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name 'NV Domain' -Value 'demoXX.netapp.com'
#終了メッセージ
write "Deploy Process is End. Computer will Reboot Automatically. Please re-login. Then Let's start Lab!"
sleep 8
#再起動
Restart-Computer -Force