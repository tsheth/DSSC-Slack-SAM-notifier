# Deep security Smart check slack notifier 

Made with ❤️ by  Trend Micro (tejas_s@trendmicro.com). Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

   After deployment of application customer need to add 3 environment variables in deployed lambda function. 
   
          1) SLACK_WEBHOOK_URL: "<add-your-slack-incomming-webhook-url>"
          2) SLACK_CHANNEL: "<slack-channel-name>"
          3) DSSC_URL: "<smartcheck dashboard url e.g. dssc.example.com>"

  After deployment it will generate API gateway URL that need to be added to DS smart check web console. To add api gateway URL navigate to web hooks in DSSC console and create eb hook and add URL.

  NOTE: kindly select option to send notification when image scan completed. other wise it will keep on sending unnecessary messages to this serverless application. 
  
  #### Steps to configure DSSC slack notification application.
 
![alt text](https://github.com/tsheth/Deep-Security-unified-ssm/blob/master/git-snaps/1.PNG)



we appreciate your feedback for any enhancement need to be done

## License

Apache License 2.0 (undefined)
