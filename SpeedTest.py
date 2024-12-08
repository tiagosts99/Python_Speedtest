import sched
import time
from datetime import datetime
import speedtest

# Inicializa o Speedtest
st = speedtest.Speedtest()
st.get_best_server()

# Inicializa o agendador
scheduler = sched.scheduler(time.time, time.sleep)

# Listas para armazenar os resultados
download = []
upload = []
ping = []
datetimes = []

# Função para definir o intervalo de tempo
def get_delay():
    while True:
        try:
            delay_time = int(input("Digite o intervalo (em segundos) entre cada teste de velocidade da internet: "))
            if delay_time > 0:
                return delay_time
            else:
                print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Digite apenas números inteiros!\n")

# Função para testar a velocidade da internet
def test_internet_speed():
    print("\nTestando a velocidade...\n")
    try:
        # Coleta os dados de velocidade
        download_speed = round(st.download() / (10 ** 6), 2)  # Converte para Mbps
        upload_speed = round(st.upload() / (10 ** 6), 2)      # Converte para Mbps
        ping_value = st.results.ping

        # Armazena os resultados nas listas
        download.append(download_speed)
        upload.append(upload_speed)
        ping.append(ping_value)
        datetimes.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Exibe os resultados no console
        print(f"Velocidade de download: {download_speed} Mbps")
        print(f"Velocidade de upload: {upload_speed} Mbps")
        print(f"Ping: {ping_value} ms")
        print(f"Data e hora do teste: {datetimes[-1]}")

    except Exception as e:
        print(f"Erro ao testar a velocidade da internet: {e}")

    # Agendar o próximo teste
    print(f"\nO próximo teste será realizado em {delay_time} segundos...\n")
    scheduler.enter(delay_time, 1, test_internet_speed)

# Ponto de entrada do programa
if __name__ == "__main__":
    try:
        print("Bem-vindo ao Teste Automático de Velocidade da Internet!")
        delay_time = get_delay()  # Solicita o intervalo de tempo
        scheduler.enter(0, 1, test_internet_speed)  # Agenda o primeiro teste
        scheduler.run()  # Inicia o agendador
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")