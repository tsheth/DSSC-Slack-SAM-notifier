# Deep security Smart check slack notifier 

Made with ❤️ by  Trend Micro. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

  
  After deployment it will generate API gateway URL that need to be added to DS smart check web console. To add api gateway URL navigate to web hooks in DSSC console and create eb hook and add URL.

  NOTE: kindly select option to send notification when image scan completed. other wise it will keep on sending unnecessary messages to this serverless application. 
  
  #### Steps to configure DSSC slack notification application.
  Go to AWS serverless application repository to naviage to deployment.
  
![alt text](https://github.com/tsheth/DSSC-Slack-SAM-notifier/blob/master/blob/1.PNG)
   Click on deploy button to deploy serverless application.
   
![alt text](https://github.com/tsheth/DSSC-Slack-SAM-notifier/blob/master/blob/3.PNG)

Once application is deployed add bellow environment variables for slack notification.

          1) SLACK_WEBHOOK_URL: "<add-your-slack-incomming-webhook-url>"
          2) SLACK_CHANNEL: "<slack-channel-name>"
          3) DSSC_URL: "<smartcheck dashboard url e.g. dssc.example.com>"

![alt text](https://github.com/tsheth/DSSC-Slack-SAM-notifier/blob/master/blob/4.PNG)

After deployment it will generate API gateway URL that need to be added to DS smart check web console. To add api gateway URL navigate to web hooks in DSSC console and create eb hook and add URL.

![alt text](https://github.com/tsheth/DSSC-Slack-SAM-notifier/blob/master/blob/5.PNG)

Add api gateway URL to DSSC web hook console

![alt text](https://github.com/tsheth/DSSC-Slack-SAM-notifier/blob/master/blob/6.PNG)



we appreciate your feedback for any enhancement need to be done

## License

Apache License 2.0 (undefined)
