from typing import Dict

from pyHTTPRequestRouter.Attributes import GETRoute

from ..Base     import BaseAPINode
from .Service   import Service
from .Semaphore import Semaphore


class Version1(BaseAPINode):
	_nodes: Dict = None

	def __init__(self):
		print("    service")
		print("    semaphore")
		self._nodes = {
			"service":   Service(),
			"semaphore": Semaphore()
		}

		super().__init__(self._nodes.values())

	@GETRoute("api/v1")
	def listEndpoints(self, request):
		pass
