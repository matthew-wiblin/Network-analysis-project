# Network-traffic-analysis-pipeline

A project to detect anomalys in network traffic:
 - Data collection - collect network traffic and store packet data using C++, tcpdump and libpcap
 - Data preprocssing - parse and convert data features with storage and versioning in python
 - Anomaly detection - train machine learning models with cross-validation, PCA and performance metrics
 - Integration with AWS IoT - use AWS services to stream data via the cloud
 - Alerts - use AWS SNS, cloudwatch and visualisation techniques and report generation

The docs directory contains instructions on project design, installation and usage