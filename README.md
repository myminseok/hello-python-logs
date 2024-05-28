Sample Python Web application
=============================

The sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [Pivotal's Cloud Foundry](https://run.pivotal.io/).

Deploy to Cloud Foundry
-----------------------
```
pip3 download -r requirements.txt -d vendor
```

```
cf push
```

to start emitting logs
```
curl -k https://this-app-domain/start
```

```
curl -k https://this-app-domain/stop
```
