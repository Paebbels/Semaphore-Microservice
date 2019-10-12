from typing import Dict

from pyHTTPRequestRouter.Attributes import GETRoute

from .Base import BaseAPINode
from .v1   import Version1


class API(BaseAPINode):
	_versions: Dict = None

	def __init__(self):

		print("  v1")
		self._versions = {
			"v1": Version1()
		}

		super().__init__(self._versions.values())

	@GETRoute("api")
	def listVersions(self):
		pass
