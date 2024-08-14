---
name: Natural Language to SQL - Solution Accelerator (Python)
description: Generate SQL query outputs natural language responses from SQL query outputs using Azure's Prompt Flow.
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
urlFragment: sql-to-natural-language-solution-accelerator

---
<!-- YAML front-matter schema: https://review.learn.microsoft.com/en-us/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->

# Natural Language to SQL - Solution accelerator


 ##### Table of Contents
- [Natural Language to SQL - Solution accelerator](#chat-with-your-data---solution-accelerator)
        - [Table of Contents](#table-of-contents)
  - [User story](#user-story)
    - [About this repo](#about-this-repo)
    - [When should you use this repo?](#when-should-you-use-this-repo)
    - [Key features](#key-features)
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

The *Natural Language to SQL* project leverages Azure's Prompt Flow to seamlessly translate SQL query results into clear, understandable natural language responses. This solution automates the interpretation of SQL outputs, ensuring consistency and efficiency in communication.

## Key Features

- **Automated Interpretation**: Automatically converts SQL query results into natural language responses, making complex data easier to understand.
- **Consistency**: Provides standardized responses based on predefined templates, minimizing errors and ensuring clarity.
- **Time Savings**: Eliminates the manual effort required to interpret SQL results, freeing up time for more strategic tasks.

By integrating this solution, you can streamline the process of generating natural language responses from SQL queries, enhancing both productivity and accuracy in data communication.


### About this repo



### Target End Users

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

## Supporting documentation

### Resource links

### Licensing

This repository is licensed under the [MIT License](LICENSE.md).


## Disclaimers
