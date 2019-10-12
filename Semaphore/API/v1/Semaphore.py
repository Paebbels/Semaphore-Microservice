from pyHTTPRequestRouter.Attributes import POSTRoute, DELETERoute, GETRoute, PUTRoute

from . import BaseAPINode


class Semaphore(BaseAPINode):
	def __init__(self):
		super().__init__()

	@POSTRoute("api/v1/semaphore")
	def registerSemaphore(self, request):
		name = ""
		resources = 5

	@DELETERoute("api/v1/semaphore")
	@DELETERoute("api/v1/semaphore/<int:id>")
	def unregisterSemaphore(self, request, id=None):
		if (id is None):
			name = ""
			id = int(name)

	@GETRoute("api/v1/semaphore")
	def listSemaphores(self, request):
		pass

	@GETRoute("api/v1/semaphore/<int:id>")
	def getStatus(self, request, id):
		pass

	@PUTRoute("api/v1/semaphore/<int:id>")
	def acquireResource(self, request, id):
		pass

	@PUTRoute("api/v1/semaphore/<int:id>")
	def releaseResource(self, request, id):
		pass

	def resetAll(self):
		pass


# - status(name)
# - status(id)
#
# - acquire(name)
# - acquireOrWait(name, timeout)
# - acquireOrCallback(name, url, timeout)
#
# - release(name)
# - release(id)
#
# - reset(name, value)
# - reset(id, value)
#
# - clear(name)
# - clear(id)
#
# - ClearAll
