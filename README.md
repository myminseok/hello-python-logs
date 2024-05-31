Sample Python Web application for generating logs.
=============================

The sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [Pivotal's Cloud Foundry](https://run.pivotal.io/).

Deploy to Cloud Foundry
-----------------------
```
pip3 download -r requirements.txt --no-binary=:none: -d vendor
```
https://docs.cloudfoundry.org/buildpacks/python/#vendoring

```
cf push
```

to start emitting logs, call the api, then it will spin up a seperated thread for emitting logs. the more calls, the more logs.
```
curl -k https://this-app-domain/start
curl -k https://this-app-domain/start
curl -k https://this-app-domain/start

```
scale out for more logs.

```
cf scale my-app -i 10
```

to stop generating logs.
```
curl -k https://this-app-domain/stop
curl -k https://this-app-domain/stop
curl -k https://this-app-domain/stop
```
