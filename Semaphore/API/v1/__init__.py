# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#   ____                             _                              ____
#  / ___|  ___ _ __ ___   __ _ _ __ | |__   ___  _ __ ___     _   _/ ___|
#  \___ \ / _ \ '_ ` _ \ / _` | '_ \| '_ \ / _ \| '__/ _ \   | | | \___ \
#   ___) |  __/ | | | | | (_| | |_) | | | | (_) | | |  __/   | |_| |___) |
#  |____/ \___|_| |_| |_|\__,_| .__/|_| |_|\___/|_|  \___|   | ._,_|____/
#                             |_|                            |_|
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python package:     Semaphore Microservice
#
# License:
# ==============================================================================
# Copyright 2019-2020 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ==============================================================================
#
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
