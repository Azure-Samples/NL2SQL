# Get params
usage() {
    echo "Usage: $0 -workspace <Azure ML workspace> -resource <Resource group> -apiurl <API_BASE_URL> -apikey <API_KEY> -sqlconn <SQL_CONN_CONN>"
    exit 1
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -workspace) WORKSPACE="$2"; shift ;;
        -resource) RESOURCE="$2"; shift ;;
        -apiurl) API_URL="$2"; shift ;;
        -apikey) API_KEY="$2"; shift ;;
        -sqlconn) SQL_CONN="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
done

# Check if all required arguments are provided
if [ -z "$WORKSPACE" ] || [ -z "$RESOURCE" ] || [ -z "$API_URL" ] || [ -z "$API_KEY" ] || [ -z "$SQL_CONN" ]; then
    usage
fi


# Set default workspace
az configure --defaults workspace=$WORKSPACE group=$RESOURCE

# Register the model
az ml model create --file ./core/model.yaml

# create online endpoint
az ml online-endpoint create --file ./core/endpoint.yaml