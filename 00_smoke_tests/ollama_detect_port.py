import subprocess
import re

# Ejecutamos ps aux para buscar el proceso llama-server
output = subprocess.check_output("ps aux | grep llama-server", shell=True).decode()

# Buscamos el parámetro --port XXXXX
match = re.search(r"--port (\d+)", output)

if match:
    port = match.group(1)
    print(f"Puerto detectado: {port}")
else:
    print("No se pudo detectar el puerto de Ollama")
