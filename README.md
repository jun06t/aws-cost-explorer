# aws-cost-explorer
======

**aws-cost-explorer** crawls AWS's cost explorer page and gets the report.
Then this sends to slack channel via incoming webhook.

# Quick Start

## Prepare
You need to create IAM user who has ``Billing`` policy.

## Run
Create docker image.
```
$ docker build -t aws-cost-explorer .
```

Then run docker container.
```
```

You should set the following environmental variables.

|variable|description|
|---|---|
|ACCOUNT_ID|your aws account id.|
|USERNAME|IAM username who has ``Billing`` policy.|
|PASSWORD|IAM user's password.|
|TARGET_DATE|The report target date. Default to one (= yesterday)|
|WEBHOOK_URL|slack's incoming webhook url.|
