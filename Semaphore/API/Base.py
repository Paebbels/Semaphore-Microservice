from pyHTTPRequestRouter.Attributes import ReSTAPIMixin


class BaseAPINode(ReSTAPIMixin):
	_children = None # type: List[BaseAPINode]

	def __init__(self, children=[]):
		super().__init__()

		self._children = children

	@property
	def ChildNodes(self):
		return self._children
