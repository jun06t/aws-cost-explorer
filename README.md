# aws-cost-explorer

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

Then run docker container with some environmental variables.
```
$ docker run --name cost_explorer \
 -e ACCOUNT_ID=wwwwwwwwww \
 -e USERNAME=xxxxxxxxxxxx \
 -e PASSWORD=yyyyyyyyyyyy \
 -e TARGET_DATE=1 \
 -e WEBHOOK_URL=https://hooks.slack.com/services/xxxxxxx/yyyyyyyyyy/zzzzzzzzzzzzzzzzzzzzzzzzz \
 aws-cost-explorer
```

After that you'll get the following message.

<img width="508" alt="slack_-_awa" src="https://user-images.githubusercontent.com/4252009/33522752-62fef618-d837-11e7-888d-dba85085ace4.png">

Click the link, and you'll go to the cost explorer page.

<img width="690" alt="2017-12-03 14 33 43" src="https://user-images.githubusercontent.com/4252009/33522759-7ba4dda4-d837-11e7-951c-ac09a458c6bc.png">


## Environmental variable

|variable|description|
|---|---|
|ACCOUNT_ID|your aws account id.|
|USERNAME|IAM username who has ``Billing`` policy.|
|PASSWORD|IAM user's password.|
|TARGET_DATE|The report target date. Default to one (= yesterday)|
|WEBHOOK_URL|slack's incoming webhook url.|
