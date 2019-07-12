# websitedemo
Demo of website to Codeship and CircleCI

The html is checked for correctness. 

CircleCI:  deploying on demo2.d1g.nl http://demo2.d1g.nl.s3-website-us-east-1.amazonaws.com

If you want to use your own bucket, you need to specify so in .circlei/config.yml and create an AWS IAM User with the policy mentioned in policy.txt (and give CircleCI its API keys).

Codeship: S3 Bucket:demo.d1g.nl http://s3.eu-central-1.amazonaws.com/demo.d1g.nl/index.html 

Buildstatus on CircleCI: [![CircleCI](https://circleci.com/gh/pve/websitedemo.svg?style=svg)](https://circleci.com/gh/pve/websitedemo)

Buildstatus on Codeship: [ ![Codeship Status for pve/websitedemo](https://app.codeship.com/projects/6fe0baa0-b6ab-0132-49dc-364f89ca8665/status?branch=master)](https://app.codeship.com/projects/71096)

[![Known Vulnerabilities](https://snyk.io/test/github/pve/websitedemo/badge.svg)](https://snyk.io/test/github/pve/websitedemo)
