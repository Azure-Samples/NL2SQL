# Initialize variables
RESOURCE_NAME=""
REGION=""
API_KEY=""
API_BASE_URL=""

# Parse named parameters
while getopts ":r:k:u:" opt; do
  case $opt in
    resource) RESOURCE_NAME="$OPTARG"
    ;;
    location) REGION="$OPTARG"
    ;;
    apikey) API_KEY="$OPTARG"
    ;;
    apiurl) API_BASE_URL="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

# Check if all required parameters are set
if [ -z "$RESOURCE_NAME" ] || [ -z "$API_KEY" ] || [ -z "$API_BASE_URL" ]; then
  echo "Usage: $0 -r <Resource name> -k <API_KEY> -u <API_BASE_URL>"
  exit 1
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
env_name=cae-frontchatwithpdf
app_name=ca-frontchatwithpdf

# Retrieve the API_BASE_URL and API_KEY from keyvault 
API_BASE_URL=https://nl2sql.swedencentral.inference.ml.azure.com/scor
API_KEY=JJUl2NB3giSckF6AJE6mAfQDRzT6tGIM

az containerapp env create \
    --name $env_name \
    --resource-group $RESOURCE_NAME \
    --location $ACR_LOCATION \

az containerapp create \
    --resource-group $RESOURCE_NAME \
    --name $app_name \
    --image $ACR_NAME.azurecr.io/insight_engine/frontchatwithpdf:latest \
    --cpu 3 \
    --memory 6 \
    --registry-server $ACR_NAME.azurecr.io \
    --registry-username $ACR_USERNAME \
    --registry-password $ACR_PASSWORD \
    --environment $env_name \
    --ingress external \
    --target-port 8501 \
    --env-vars API_BASE_URL=$API_BASE_URL API_KEY=$API_KEY