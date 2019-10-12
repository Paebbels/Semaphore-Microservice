![PyPI - License](https://img.shields.io/pypi/l/Semaphore-Microservice)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Paebbels/Semaphore-Microservice) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Paebbels/Semaphore-Microservice)
[![Documentation Status](https://readthedocs.org/projects/semaphore-microservice/badge/?version=latest)](https://semaphore-microservice.readthedocs.io/en/latest/?badge=latest)  
[![PyPI](https://img.shields.io/pypi/v/Semaphore-Microservice)](https://pypi.org/project/Semaphore-Microservice/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Semaphore-Microservice)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/Semaphore-Microservice)
![PyPI - Status](https://img.shields.io/pypi/status/Semaphore-Microservice)

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
