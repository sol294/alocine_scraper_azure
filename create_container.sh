set -o allexport
source .env
set +o allexport
az storage container create \
    --account-name $storageAccountName \
    --name $containerNameB \
    --auth-mode login
#chmod +x create_container.sh
# ./create_container.sh 

az storage container create \
    --account-name $storageAccountName \
    --name $containerNameC \
    --auth-mode login