set -o allexport
source .env
set +o allexport
az postgres flexible-server create \
    --location $LOCATION \
    --resource-group $RESOURCE_GROUP \
    --name $NAMESERVER \
    --admin-user $adminname \
    --admin-password $adminpassword \
    --sku-name $skuname \
    --tier Burstable \
    --public-access $adresseip \
    --storage-size 32 \
    --tags $TAGS \
    --version 13 \
    --high-availability $availability 
#--zone 1 \
#--standby-zone 3

#chmod +x create_server_flexible.sh
#./create_server_flexible.sh 