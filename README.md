#### Port Scanning 

Antes de utilizar esse programa, certifique-se de ter a biblioteca socket instalada em seu computador. Você pode instala-la através do comando

> pip3 install socket

Para executar o script você deve fornecer um host, uma porta inicio ou limite (opcional -> Nossa parte limite caso você não informe sempre será 3306 e a inicial será 1) e um timer que pode ir de t1 a t5 (opcional -> nosso timer padrão sempre será de 1) 

Exemplo:

> python3 port_scan.py 127.0.0.1
> python3 port_scan.py 127.0.0.1 1 65535 t1 

 
