set -o allexport
source .env
set +o allexport

az postgres flexible-server db create --resource-group $RESOURCE_GROUP --server-name $NAMESERVER --database-name $dbname

#chmod +x create_db_flexible_server.sh
#./create_db_flexible_server.sh