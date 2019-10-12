from pyHTTPRequestRouter import GETRoute

from . import BaseAPINode


class Service(BaseAPINode):
	def __init__(self):
		super().__init__()

	@GETRoute("api/v1/service")
	def getServiceStatus(self, request):
		pass
