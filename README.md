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

Unlimit app logging
-----------------------

To quickly allow App1's logging to be unblocked from the limit we could use the cf CLI to scale the log limit: 
```
cf scale App1 -l -1
```

Emitting logs
-----------------------
to start emitting logs, call the api, then it will spin up a seperated thread for emitting logs. the more calls, the more logs.
```
curl -k https://this-app-domain/start
curl -k https://this-app-domain/start
curl -k https://this-app-domain/start
...
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
...
```
