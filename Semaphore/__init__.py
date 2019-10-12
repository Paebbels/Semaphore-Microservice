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
