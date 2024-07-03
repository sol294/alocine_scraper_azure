set -o allexport
source .env
set +o allexport
#chmod +x create_account_storage.sh
#./create_account_storage.sh 
az storage account create \
--name $storageAccountName \
--resource-group $RESOURCE_GROUP \
--location $LOCATION \
--sku Standard_ZRS \
--encryption-services blob