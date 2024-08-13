#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 -resource <Resource name> -location <Region> -apikey <API_KEY> -apiurl <API_BASE_URL>"
    exit 1
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -resource) RESOURCE_NAME="$2"; shift ;;
        -location) REGION="$2"; shift ;;
        -apikey) API_KEY="$2"; shift ;;
        -apiurl) API_URL="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
done

# Check if all required arguments are provided
if [ -z "$RESOURCE_NAME" ] || [ -z "$REGION" ] || [ -z "$API_KEY" ] || [ -z "$API_URL" ]; then
    usage
fi


# Build the Docker image
docker build -f ./frontend/Dockerfile -t frontnl2sql ./frontend

# Create an azure container registry
ACR_NAME="crnl2sql"
az acr create --resource-group $RESOURCE_NAME --name $ACR_NAME --sku Basic --location $REGION --admin-enabled true

# Get the Azure Container Registry name from the resource group
az acr login --name $ACR_NAME 

# Tag the Docker image
docker tag frontnl2sql:latest $ACR_NAME.azurecr.io/insight_engine/frontnl2sql:latest

# Push the Docker image to the Azure Container Registry
docker push $ACR_NAME.azurecr.io/insight_engine/frontnl2sql:latest

# Get ACR credentials
az acr update -n $ACR_NAME --admin-enabled true
ACR_USERNAME=$(az acr credential show --name $ACR_NAME --query "username" --output tsv)
ACR_PASSWORD=$(az acr credential show --name $ACR_NAME --query "passwords[0].value" --output tsv)
ACR_LOCATION=$(az acr show --name $ACR_NAME --query "location" --output tsv)

# Deploy the container to Azure Container App Service
env_name=cae-frontnl2sql
app_name=ca-frontnl2sql

az containerapp env create \
    --name $env_name \
    --resource-group $RESOURCE_NAME \
    --location $ACR_LOCATION \

az containerapp create \
    --resource-group $RESOURCE_NAME \
    --name $app_name \
    --image $ACR_NAME.azurecr.io/insight_engine/frontnl2sql:latest \
    --cpu 3 \
    --memory 6 \
    --registry-server $ACR_NAME.azurecr.io \
    --registry-username $ACR_USERNAME \
    --registry-password $ACR_PASSWORD \
    --environment $env_name \
    --ingress external \
    --target-port 8501 \
    --env-vars API_BASE_URL=$API_BASE_URL API_KEY=$API_KEY