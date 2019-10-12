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
# Package installer:  Semaphore Microservice
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
import setuptools

with open("README.md", "r") as file:
	long_description = file.read()

requirements = []
with open("requirements.txt") as file:
	for line in file.readlines():
		requirements.append(line)

projectName = "Semaphore-Microservice"

github_url =  "https://github.com/Paebbels/" + projectName
rtd_url =     "https://" + projectName + ".readthedocs.io/en/latest/"

setuptools.setup(
	name=projectName,
	version="0.1.1",

	author="Patrick Lehmann",
	author_email="Paebbels@gmail.com",
	# maintainer="Patrick Lehmann",
	# maintainer_email="Paebbels@gmail.com",

	description="A HTTP-based microservice offering a ReST API to acquire and release resources that are limited with a semaphore semantic.",
	long_description=long_description,
	long_description_content_type="text/markdown",

	url=github_url,
	project_urls={
		'Documentation': rtd_url,
		'Source Code':   github_url,
		'Issue Tracker': github_url + "/issues"
	},
	# download_url="",

	packages=setuptools.find_packages(),
	classifiers=[
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3 :: Only",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Development Status :: 2 - Pre-Alpha",
		#		"Development Status :: 3 - Alpha",
		#		"Development Status :: 4 - Beta",
		#		"Development Status :: 5 - Production/Stable",
		"Topic :: Internet :: WWW/HTTP :: HTTP Servers"
	],
	keywords="Python3 Exceptions",

	python_requires='>=3.5',
	install_requires=requirements,
	# provides=
	# obsoletes=
)
