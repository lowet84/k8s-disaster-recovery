winscp.com /command "open sftp://root@home.kube" "put ./*.py /root/python/" "exit" /privatekey=Z:\Dokument\SSH\fredrik.ppk
ssh -i Z:\Dokument\SSH\fredrik root@home.kube python3 /root/python/main.py master home.kube