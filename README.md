# ELK Stack Experiments

This repository contains experiments using the ELK (Elasticsearch, Logstash, Kibana) stack. The experiments focus on two primary areas:

1. **Parsing Different Types of Log Files**:
   - Parsing example log files (`example2.log` and `example3.log`).
   - Configuring Logstash to process and structure the log data.
   - Visualizing the parsed log data in Kibana.

2. **Fetching and Parsing GitLab Repository Information**:
   - Fetching repository information from GitLab using a Python script.
   - Parsing the resulting JSON file with Logstash.
   - Displaying the parsed information in Kibana.

## Repository Structure

```
.
├── Gitlab Repo Parsing/
│   ├── fetch_gitlab_repo_info.py
│   ├── logstash.conf
│   ├── project_data.json
│   ├── requirements.txt
│   └── screenshots/
│       ├── ss1.png
│       └── ss2.png
├── Log file Parsing/
│   ├── example2.log
│   ├── example3.log
│   ├── logstash.conf
│   └── screenshots/
│       ├── ss1.png
│       ├── ss2.png
│       └── ss3.png
├── docker-compose.yaml
└── README.md
```

### Parsing Log Files

When I began working on log parsing, I had to first understand how to write effective Grok patterns. This involved a lot of learning and analysis of the log files to extract meaningful data. After much experimentation, I successfully crafted the following Grok filters:

- **For `example3.log`:** 
  - Filter: `(?<date>\d{1,2}/\d{1,2}) %{TIME:time} %{LOGLEVEL:loglevel} %{DATA:ignore}%{WORD:process}: %{GREEDYDATA:message}`
  - This pattern allowed me to extract the date, time, log level, process name, and the message from each log entry.

- **For `example2.log`:**
  - Filter: `%{YEAR:year}-%{MONTHNUM:month}-%{MONTHDAY:day}T%{HOUR:hour}:%{MINUTE:minute}:%{SECOND:second}Z %{LOGLEVEL:loglevel} %{GREEDYDATA:message}`
  - With this pattern, I could parse the timestamp, log level, and the message content from the log data.

### Fetching and Parsing GitLab Repository Information

For the GitLab repository parsing, I decided to leverage Logstash's JSON parsing capabilities. After fetching the repository information using a Python script, I processed the resulting JSON file with Logstash. This allowed me to structure the data effectively, making it easy to visualize and analyze within Kibana.

## Screenshots

### GitLab Repository Parsing
![GitLab Repo Parsing 1](Gitlab%20Repo%20Parsing/screenshots/ss1.png)
![GitLab Repo Parsing 2](Gitlab%20Repo%20Parsing/screenshots/ss2.png)

### Log File Parsing
![Log File Parsing 1](Log%20file%20Parsing/screenshots/ss1.png)
![Log File Parsing 2](Log%20file%20Parsing/screenshots/ss2.png)
![Log File Parsing 3](Log%20file%20Parsing/screenshots/ss3.png)

Author: Bora Fenari Köstem