# λ selenium-chromium-lambda

How to run automated (Selenium) Headless Chromium in AWS Lambda.
Please refer the article to understand how the selenium driver is handled on aws lambda:-
Read full article [https://www.vittorionardone.it/en/2020/06/04/chromium-and-selenium-in-aws-lambda](https://www.vittorionardone.it/en/2020/06/04/chromium-and-selenium-in-aws-lambda)
authors git : https://github.com/vittorio-nardone/selenium-chromium-lambda

## SAM Deploy
Run these commands in sequence:
`make lambda-layer-build` to prepare archive for AWS Lambda Layer deploy (layer.zip)
`make lambda-function-build` to prepare archive for AWS Lambda deploy (deploy.zip)
`make BUCKET=<your_bucket_name> create-stack` to create CloudFormation stack (lambda function, layer and IAM role)

## Lambda Update
update your lambda and add remaining dependancies as layers if any:
update lambda handler to `src/main.handler`

## Credits
Inspired by : [this awesome project](https://github.com/vittorio-nardone/selenium-chromium-lambda)
Inspired by : [this awesome project](https://github.com/21Buttons/pychromeless)
Inspired by : [this awesome project](https://github.com/srinjoychakravarty/authentikos)
