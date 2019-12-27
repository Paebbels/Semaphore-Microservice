[![PyPI - License](https://img.shields.io/pypi/l/Semaphore-Microservice?logo=PyPI)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/Semaphore-Microservice?logo=GitHub&include_prereleases)](https://github.com/Paebbels/Semaphore-Microservice/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/Semaphore-Microservice?logo=GitHub&include_prereleases)](https://github.com/Paebbels/Semaphore-Microservice/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/Semaphore-Microservice?logo=GitHub&)](https://github.com/Paebbels/Semaphore-Microservice/releases)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/Semaphore-Microservice)](https://libraries.io/github/Paebbels/Semaphore-Microservice)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/Semaphore-Microservice)](https://requires.io/github/Paebbels/Semaphore-Microservice/requirements/?branch=master)  
[![Travis](https://img.shields.io/travis/com/Paebbels/Semaphore-Microservice?logo=Travis)](https://travis-ci.com/Paebbels/Semaphore-Microservice)
[![PyPI](https://img.shields.io/pypi/v/Semaphore-Microservice?logo=PyPI)](https://pypi.org/project/Semaphore-Microservice/)
![PyPI - Status](https://img.shields.io/pypi/status/Semaphore-Microservice?logo=PyPI)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Semaphore-Microservice?logo=PyPI)
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/Semaphore-Microservice)](https://github.com/Paebbels/Semaphore-Microservice/network/dependents)  
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8acef81b953742639ac21eddee7d9fb5)](https://www.codacy.com/manual/Paebbels/Semaphore-Microservice)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/Semaphore-Microservice)](https://libraries.io/github/Paebbels/Semaphore-Microservice/sourcerank)
[![Read the Docs](https://img.shields.io/readthedocs/semaphore-microservice)](https://Semaphore-Microservice.readthedocs.io/en/latest/)

# Semaphore Microservice

This HTTP-based microservice offers a ReST API to acquire and release resources
that are limited with a *semaphore* semantic.

## Use Cases
### Limited Number of Licenses in an Continuous Integration Environment

Some software uses a global license server to checkout licenses while the software
is executed. By default many license consumers (clients) fail and abort the
execution if no valid license was found or if no license was free for a checkout.
In such cases, a CI pipeline would also fail, because the job is failing caused by
the license error. In many cases there are no retries nor waits for a license to
become valid or available again. More over waiting time would be counted as job
execution time.

This semaphore service allow to acquire a license virtually before asking the actual
license server. If no license is available, it will either wait or register a
callback for the real working job.

## Operations


## Architecture

```
Application => WebServer     => HTTPInterface => Router => API => Semaphore => storage  
Daemon     / \ NGINX + WSGI /
```

## API
### v1.0
