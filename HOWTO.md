# 🚀 How to Deploy the Azure Resources with Bicep

This guide walks you through deploying Azure resources using Azure CLI.

## 📋 Prerequisites

- Azure CLI installed and logged in to your Azure account. [Install Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli)
- An Azure subscription where you have permissions to create resources.
- An Azure Open AI resource with gpt model deployed
- An Azure Postgres database 

2. **Set up connections:**
```bash
pf connection create --file core/connections/AOAILAB03.yaml --set api_key=<your_api_key> api_base=<your_api_base> --name AOAILAB03
```

```bash
pf connection create --file core/connections/SQL_CONN.yaml --set secrets.conn=<your_db_conn> --name SQL_CONN
```

3. **Build flow as docker format**
```bash
pf flow build --source core/flow/ --output core/dist --format docker
```

4. **Build Docker image**
```bash 
docker build -f core/dist/Dockerfile -t nl2sql core/dist
```