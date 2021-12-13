#ex1
Para mesclar os comandos em linux, podemos usar:

Ponto e vírgula (;): Que permite que sejam usados mais de 1 comando, um de cada vez, seguido do outro. 
Por exemplo, "df -h ; iostat ; netstat; free -m". Vou ter a informação de espaço utilizado em disco em unidade de MB, KB, GB; Logo após, 
o relatório de CPU e de entrada/saída dos dispositivos de armazenamento, as informações referentes as conexões de rede e então a informação sobre uso de memória RAM, 
nesse caso, em mbytes (-m).
Ou então pwd ; grep [palavra que será buscada em um texto] [arquivo onde está esse texto] [opções, onde especifico informações sobre essa busca], 
nesse exemplo eu visualizo o diretório que estou atualmente e então, pesquiso/busco uma frase ou palavra em um determinado texto de um determinado arquivo.

Operador lógico OR (| |): Este serve para usarmos um segundo comando no caso de o primeiro não ter sido executado com sucesso. 
Exemplo: top | | htop. No caso do exemplo, eu quero visualizar os programas ativos ou parados que estão utilizando recursos da CPU, 
se esse comando não rodar com sucesso, eu vou visualizar os processos da maneira que seria com o comando top, porém de maneira mais intuitiva
e com uma maior gama de informações.

Operador lógico E (&&): Este é parecido com o ponto e vírgula, porém a diferença é que o segundo só será executado se o primeiro tiver sido executado com sucesso 
e assim sucessivamente. Exemplo: telnet [opção] [ip] [porta]&& sudo fdisk -l && ps -ef. O telnet vai me ajudar a acessar um computador de forma remota, 
eu consigo informar o ip e a porta que quero acessar, bem como a opção, ou seja, o que especificamente quero visualisar. Se eu conseguir esse acesso, 
entra o fdisk, que serve para gerenciar partições, o sudo fdisk -l vai listar as partições identificarmos qual disco usar/gerenciar. 
Seguindo a mesma linha, teremos a visão dos processos que estão sendo executados no computador. Ps -ef é usado para encontrar o id exclusivo do processo, conhecido como PID.
