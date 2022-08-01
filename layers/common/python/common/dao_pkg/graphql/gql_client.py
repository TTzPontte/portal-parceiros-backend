from dataclasses import dataclass
import boto3
import requests

dynamodb = boto3.resource("dynamodb")


class GqlClient():
    url: str = "https://4d6icbogpzfrrpmeaaqcybawfe.appsync-api.us-east-1.amazonaws.com/graphql"

    headers: str = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": "da2-f6cahicmena7tj43grt5zsgcgy"
    }

    def post(self, query):
        return requests.post(self.url, json={'query': query}, headers=self.headers)


