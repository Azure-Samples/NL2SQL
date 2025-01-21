---
name: Natural Language to SQL - Solution Accelerator (Python)
description: Convert natural language text into SQL queries using Azure's Prompt Flow, automating the generation of SQL query outputs from natural language inputs.
languages:
- python
- azure-prompt-flow
- markdown
products:
- azure-openai
- azure-functions
- azure-sql-database
- azure
page_type: sample
urlFragment: natural-language-to-sql-solution-accelerator

---
<!-- YAML front-matter schema: https://review.learn.microsoft.com/en-us/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->

# Natural Language to SQL - Solution accelerator


 ##### Table of Contents
- [Natural Language to SQL - Solution accelerator](#natural-language-to-sql---solution-accelerator)
        - [Table of Contents](#table-of-contents)
  - [User story](#user-story)
    - [Key features](#key-features)
    - [About this repo](#about-this-repo)
    - [When should you use this?](#when-should-you-use-this)
    - [Example](#example)
    - [Target end users](#target-end-users)
  - [Deploy](#deploy)
    - [Pre-requisites](#pre-requisites)
    - [Products used](#products-used)
    - [Required licenses](#required-licenses)
    - [Pricing Considerations](#pricing-considerations)
    - [Deploy instructions](#deploy-instructions)
    - [Testing the deployment](#testing-the-deployment)
  - [Supporting documentation](#supporting-documentation)
    - [Resource links](#resource-links)
    - [Licensing](#licensing)
  - [Disclaimers](#disclaimers)


# Welcome to the *Natural Language to SQL* Solution Accelerator

The *Natural Language to SQL* project uses Azure's Prompt Flow to automatically generate SQL queries based on natural language inputs. This solution simplifies the process of converting natural language into SQL queries, ensuring accuracy and efficiency.

![Solution Architecture](/docs/images/architecture.png)

## Key Features

- **Automated Query Generation**: Automatically translates natural language into SQL queries, making data retrieval more intuitive.
- **Consistency**: Delivers standardized queries based on predefined templates, reducing errors and enhancing reliability.
- **Efficiency**: Saves time by eliminating the manual process of writing SQL queries, allowing users to focus on data analysis and decision-making.

Integrate this solution to streamline the generation of SQL queries from natural language, improving productivity and data handling accuracy.


Certainly! Here are the sections "About This Repo" and "When Should I Use This" for your `README.md`:

---

## About This Repo

This repository contains a powerful tool for transforming natural language descriptions into SQL queries. By leveraging Azure's Prompt Flow, it automatically generates SQL `SELECT` statements based on a predefined database schema and executes them on a PostgreSQL database. The primary focus of this project is to streamline the process of querying databases without requiring users to have an in-depth knowledge of SQL syntax.

The codebase is organized to facilitate easy integration, customization, and extension. Whether you're a developer looking to integrate natural language query capabilities into your application or a data analyst seeking to simplify your workflow, this repository provides the foundation you need.

## When Should I Use This

You should consider using this tool in the following scenarios:

1. **Natural Language Querying**: If you want to enable users to query a PostgreSQL database using natural language descriptions, this tool is ideal for bridging the gap between user intent and database querying.

2. **Automating SQL Query Generation**: When you need to automate the process of translating business requirements or user inputs into accurate SQL queries, this tool saves time and reduces errors.

3. **Context-Aware Query Generation**: If your use case involves generating SQL queries that adapt based on previous interactions or context, this tool provides adaptive query generation capabilities.

4. **Simplifying Data Access**: For data analysts or non-technical stakeholders who need to access data without writing complex SQL queries, this tool provides a user-friendly interface.

5. **Educational Purposes**: If you’re teaching or learning SQL and want to explore how natural language can be transformed into SQL queries, this repository offers practical examples and a robust system to experiment with.

## Tables Structure

![Tables Structure](/docs/images/tables_structure.png)

## Example

**Input:**
```
Give me the seller name with the best sales performance
```

**Generated SQL Query:**
```sql
SELECT s.seller_name
FROM sellers s
JOIN sales_transaction st ON s.seller_id = st.seller_id
GROUP BY s.seller_name
ORDER BY SUM(st.quantity) DESC
LIMIT 1;
```

**Result:**
```
<table>
  <tr>
    <th>seller_name</th>
  </tr>\n<tr>
    <td>Jane Smith</td>
  </tr>
</table>
```

## Target End Users

- **Data Analysts:** Convert natural language queries into SQL for quick data extraction.
- **Database Administrators:** Generate SQL queries from plain text for efficient data access.
- **BI Professionals:** Create SQL queries from natural language for interactive dashboards.
- **Developers & Solution Architects:** Integrate natural language-to-SQL functionality into apps.
- **Non-Technical Users:** Formulate SQL queries using plain language for data analysis.


![One-click Deploy](/docs/images/oneClickDeploy.png)
## Deploy
### Pre-requisites
- Azure subscription - [Create one for free](https://azure.microsoft.com/free/) with owner access.
- Approval to use Azure OpenAI services with your Azure subcription. To apply for approval, see [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai).


### Products used
- Azure Container Registry: For storing and managing Docker container images.
- Azure Container Apps: For deploying and running containerized applications.
- Azure CLI: For interacting with Azure services from the command line.
- Docker: For building and pushing the container images.
- Azure Functions: For any serverless functions used in the project.
- Azure SQL Database: For managing SQL databases connected to the project.

### Required licenses
- Microsoft 365 (optional: Teams extension only)

### Pricing Considerations

This solution accelerator deploys multiple resources. Evaluate the cost of each component prior to deployment.

The following are links to the pricing details for some of the resources:
- [Azure OpenAI service pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). GPT and embedding models are charged separately.
- [Azure Web App Pricing](https://azure.microsoft.com/pricing/details/app-service/windows/)

### Deploy instructions

There are two choices; the "Deploy to Azure" offers a one click deployment where you don't have to clone the code, alternatively if you would like a developer experience, follow the [Local deployment instructions](./docs/LOCAL_DEPLOYMENT.md).

### Testing the deployment

#### Streamlit Application
```bash streamlit run frontend/app.py  ```

#### Prompt Flow API
```bash pf flow serve --source ./core/flow --port 8080 --host localhost ``` 

## Supporting documentation

### Build a custom Prompt Flow environment with PostgreSQL driver
In case you want to try using a PostgreSQL database you will need to install some libraries to be able to use PGSQL.
Below are some guidance to build a Docker image using Prompt Flow image a base image (see the Dockerfile) and push it to an Azure Container Registry.
In this way, we can use it as a custom image in our Prompt Flow environment (on Azure AI Foundry).

```
# Build the docker image
docker build -t prompt_flow_pgsql .

# Set the variables

export ACR_NAME="<your-acr-name>"
export TENANT_ID="<your-tenant-id>"

export IMAGE_NAME="prompt_flow_pgsql"
export IMAGE_TAG="latest"

# Login to Azure
az login --tenant $TENANT_ID

# Login to ACR
az acr login --name $ACR_NAME

# Build the Docker image
docker build -t $ACR_NAME.azurecr.io/$IMAGE_NAME:$IMAGE_TAG .

# Push the Docker image to ACR
docker push $ACR_NAME.azurecr.io/$IMAGE_NAME:$IMAGE_TAG

echo "Docker image pushed to ACR successfully."
```

## Resource links

## Licensing

This repository is licensed under the [MIT License](LICENSE.md).


## Disclaimers
