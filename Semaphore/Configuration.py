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
