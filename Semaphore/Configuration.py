from pathlib      import Path
from typing       import Union, List

from flags        import Flags
from ruamel.yaml  import YAML


class SemaphoreKinds(Flags):
	NaturalRangeLimited = 1


class Base():
	root = None
	parent = None

	def __init__(self, root, parent):
		self.root = root
		self.parent = parent


class TLS(Base):
	certificatePath: Path = None

	def __init__(self, root, parent, settings):
		super().__init__(root, parent)

		self.certificatePath = Path(settings['certificate'])


class HTTPServer(Base):
	hostname: str = None
	port:     int = None
	tls:      Union[bool, TLS] = None

	def __init__(self, root, parent, settings):
		super().__init__(root, parent)

		self.hostname = settings['hostname']
		self.port =     settings['port']

		if ('tls' in settings):
			self.tls = settings['tls']

		if (self.tls is not False):
			self.tls = TLS(root, self, settings['tls'])


class Semaphore(Base):
	name:         str =            None
	kind:         SemaphoreKinds = None
	initialValue: int =            None
	maximumValue: int =            None

	def __init__(self, root, parent, settings, name):
		super().__init__(root, parent)

		self.name =         name
		self.kind =         SemaphoreKinds.from_str(settings['kind'])
		self.initialValue = settings['initialValue']
		self.maximumValue = settings['maximumValue']


class Configuration():
	httpServer: HTTPServer =      None
	semaphores: List[Semaphore] = None

	def __init__(self, configFile):
		yaml =   YAML()
		config = yaml.load(configFile)

		self.httpServer = HTTPServer(self, self, config['httpServer'])

		self.semaphores = []
		sema = config['semaphores']
		for name, semaphore in sema.items():
			self.semaphores.append(Semaphore(self, self, semaphore, name))
