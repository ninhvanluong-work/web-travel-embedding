#!/bin/bash
# dev | prod
ENV=$1
IMAGE_TAG=1
APP_DESTINATION=.

echo $PORT

if [ $ENV == 'dev' ]; then
    CONTAINER_NAME='embedding-cont-dev'
    IMAGE_NAME='embedding-img-dev'
fi

if [ $ENV == 'prod' ]; then
    CONTAINER_NAME='embedding-cont-prod'
    IMAGE_NAME='embedding-img-prod'
fi

echo "Creating docker image..."
docker image build -t $IMAGE_NAME:$IMAGE_TAG -f $APP_DESTINATION/Dockerfile.${ENV} $APP_DESTINATION

if [[ -n $(docker ps -a -q -f name=$CONTAINER_NAME -f publish=$PORT )  && $ENV == 'dev' ]]; then
    echo "Container exists, restarting..."
    docker restart $CONTAINER_NAME
else
    echo "Starting container..."
    docker rm -f $CONTAINER_NAME
    docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG
fi