Network-Traffic-Anomaly-Detection/
├── data/
│   ├── raw/
│   │   └── *.pcap                  # Raw packet capture files
│   ├── processed/
│   │   └── *.csv                   # Processed data files (e.g., CSV files after preprocessing)
│   └── models/
│       └── model.pkl               # Trained machine learning models
├── src/
│   ├── cpp/
│   │   ├── CMakeLists.txt          # CMake configuration file for building C++ code
│   │   ├── PacketSniffer.cpp       # Main packet sniffer implementation
│   │   ├── PacketSniffer.h         # Header file for packet sniffer
│   │   ├── Makefile                # Makefile for building the C++ code
│   │   └── libpcap/                # Directory for libpcap related files
│   │       └── ...
│   ├── python/
│   │   ├── preprocessing.py        # Script for data preprocessing
│   │   ├── feature_extraction.py   # Script for feature extraction
│   │   ├── anomaly_detection.py    # Script for training and evaluating anomaly detection models
│   │   ├── utils.py                # Utility functions
│   │   ├── requirements.txt        # Python dependencies
│   │   ├── model_deployment.py     # Script for deploying models on AWS Lambda
│   │   └── notebooks/
│   │       └── exploratory_data_analysis.ipynb # Jupyter notebook for initial data analysis
│   ├── aws/
│   │   ├── lambda_function.py      # AWS Lambda function code
│   │   ├── deploy.sh               # Shell script for deploying Lambda function
│   │   ├── iot_config.json         # Configuration file for AWS IoT
│   │   ├── sns_alerts.py           # Script for setting up AWS SNS alerts
│   │   └── visualization/
│   │       ├── dashboard.py        # Dash app for data visualization
│   │       ├── app.py              # Flask app to serve the Dash application
│   │       ├── s3_upload.py        # Script to upload dashboard to AWS S3
│   │       └── requirements.txt    # Python dependencies for visualization
├── tests/
│   ├── test_preprocessing.py       # Unit tests for preprocessing
│   ├── test_feature_extraction.py  # Unit tests for feature extraction
│   ├── test_anomaly_detection.py   # Unit tests for anomaly detection
│   ├── test_packet_sniffer.cpp     # Unit tests for C++ packet sniffer
│   └── test_lambda_function.py     # Unit tests for AWS Lambda function
├── scripts/
│   ├── setup_env.sh                # Script to set up the development environment
│   ├── data_download.sh            # Script to download sample data for testing
│   ├── run_pipeline.sh             # Script to run the entire data processing pipeline
│   └── clean_up.sh                 # Script to clean up temporary files and data
├── docs/
│   ├── README.md                   # Project overview and setup instructions
│   ├── DESIGN.md                   # Detailed design document
│   ├── INSTALL.md                  # Installation instructions
│   └── USAGE.md                    # Usage guide and examples
└── .gitignore                      # Git ignore file
