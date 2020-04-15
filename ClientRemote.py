from paramiko import client
import paramiko

class ClientRemote():
    __client_ssh = None
    __stdin =  None
    __stdout = None
    __stderr = None

    def __init__(self, ip, username, password):
        self.__client_ssh = client.SSHClient()
        self.__client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.__client_ssh.connect(ip, username=username,password=password)
        paramiko.util.log_to_file('paramiko.log')


    def close(self):
        self.__client_ssh.close()

    def execute_commander(self, commander):
        self.__stdin, self.__stdout, self.__stderr = self.__client_ssh.exec_command(commander)

    def get_result(self):
        return self.__stdout.readlines()

    def realice_ping(self, nro_package, ip_destino):
        ping = 'ping -c '+nro_package+' '+ip_destino
        self.__stdin, self.__stdout, self.__stderr = self.__client_ssh.exec_command(ping)

    def realice_traceroute(self, ip_destino):
        traceroute = 'traceroute '+ip_destino
        self.__stdin, self.__stdout, self.__stderr = self.__client_ssh.exec_command(traceroute)
