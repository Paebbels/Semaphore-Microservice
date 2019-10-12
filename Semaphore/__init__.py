from typing import Dict

from .    import Configuration
from .API import API


class Semaphore:
	_initialValue: int = 0
	_maximumValue: int = 0

	def __init__(self, initialValue, maximumValue):
		self._initialValue = initialValue
		self._maximumValue = maximumValue

	def acquire(self):
		pass

	def release(self):
		pass


class Service:
	_config:     Configuration        = None
	_semaphores: Dict[str, Semaphore] = None
	api : API = None

	def __init__(self, config: Configuration):
		self._config = config

		self.__initSemaphores()
		self.__initAPI()

	def __initSemaphores(self):
		print("Creating semaphores...")
		self._semaphores = {}
		for semaphore in self._config.semaphores:
			print("  {name: <20}{min}  max={max}".format(name=semaphore.name, min=semaphore.initialValue, max=semaphore.maximumValue))
			self._semaphores[semaphore.name] = Semaphore(semaphore.initialValue, semaphore.maximumValue)

	def __initAPI(self):
		print("Initializing API...")
		self.api = API()
