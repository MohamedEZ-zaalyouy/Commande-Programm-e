from django.shortcuts import render
from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from rest_framework import status
from rest_framework.response import Response
from checkout.mutations import orderCreateFromCheckoutMutation
from checkout.settings import SALEOR_API, SALEOR_API_TOKEN




transport = RequestsHTTPTransport(
    url=SALEOR_API,
    headers={'Authorization': f"Bearer {SALEOR_API_TOKEN}"},
    verify=True,
    retries=3,
)


# Create your views here.


client = Client(transport=transport, fetch_schema_from_transport=True)



def CreateOrderProFromCheckout(checkoutID):
    remove_checkout = True
    data = client.execute(orderCreateFromCheckoutMutation, variable_values={
        "id": checkoutID,
        "removeCheckout": remove_checkout
    })
    return Response(data, status=status.HTTP_200_OK)

