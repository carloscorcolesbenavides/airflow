from crewai_tools import ScrapeWebsiteTool, FileWriterTool, TXTSearchTool
import requests

# Inicializar la herramienta, pasando la sesión si hace falta
tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence')

# Extraer el texto
text = tool.run()
print(text)