---
name: SQL to Natural Language - Solution Accelerator (Python)
description: Generate natural language responses from SQL query outputs using Azure's Prompt Flow.
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

# SQL to Natural Language - Solution accelerator


 ##### Table of Contents
- [SQL to Natural Language - Solution accelerator](#chat-with-your-data---solution-accelerator)
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
## User story

Welcome to the *SQL to Natural Language* Solution accelerator repository! The nl2sql project leverages Azure's Prompt Flow to automatically generate natural language responses based on SQL query outputs. By providing a SQL query and its corresponding database output, the system:

- Automates Interpretation: Automatically interprets and formats SQL query results into clear, concise, and easy-to-understand natural language responses.
- Ensures Consistency: Delivers consistent responses by following a standardized template, reducing the risk of miscommunication or data misinterpretation.
- Saves Time: Eliminates the need for manual translation of SQL results into natural language, allowing professionals to focus on higher-level tasks.

![Solution Architecture]()

### About this repo



### Key features



### Target End Users

- **Data Analysts:** Automate SQL output translation into clear insights for reports.
- **Database Administrators:** Provide accessible data insights to non-technical stakeholders.
- **BI Professionals:** Integrate natural language explanations into dashboards.
- **Developers & Solution Architects:** Enhance apps with natural language processing for SQL data.
- **Non-Technical Business Users:** Understand data insights without deep SQL knowledge.


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
- Azure Functions: (If applicable) For any serverless functions used in the project.
- Azure SQL Database: (If applicable) For managing SQL databases connected to the project.

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
