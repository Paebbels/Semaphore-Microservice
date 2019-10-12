from pathlib                 import Path

from pyHTTPServer.HTTPServer  import Server
from pyHTTPRequestRouter      import Router

from Semaphore.Configuration  import Configuration
from Semaphore                import Service


def main():

	configFilePath = Path("Semaphore.yaml")
	config = Configuration(configFilePath)
	service = Service(config)

	print("Preparing ReST API Router...")
	router = Router(service.api)

	httpServerConfig = config.httpServer

	print("Preparing HTTP Server...")
	print("  http://{host}:{port}/".format(host=httpServerConfig.hostname, port=httpServerConfig.port))
	server = Server(httpServerConfig, router)

	print("Serving HTTP requests...")
	server.run()

if (__name__ == "__main__"):
	main()
