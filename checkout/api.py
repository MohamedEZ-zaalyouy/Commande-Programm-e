from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .mutations import orderCreateFromCheckoutMutation
from .settings import SALEOR_API, SALEOR_API_TOKEN


#Order Pro
from OrderPro.models import OrderCheckoutTasks


transport = RequestsHTTPTransport(
    url=SALEOR_API,
    headers={'Authorization': f"Bearer {SALEOR_API_TOKEN}"},
    verify=True,
    retries=3,
)


client = Client(transport=transport, fetch_schema_from_transport=True)


class CreateOrderFromCheckout(APIView):

    def post(self, request):
        
        checkout_id = request.data.get('checkoutID')
        execution_time = request.data.get('DateTime')

        
        if not execution_time :

            remove_checkout = True
            data = client.execute(orderCreateFromCheckoutMutation, variable_values={
                "id": checkout_id,
                "removeCheckout": remove_checkout
            })

            return Response(data, status=status.HTTP_200_OK)
        
        else:

            OrderPro = OrderCheckoutTasks(checkoutID = checkout_id, execution_time = execution_time )
            OrderPro.save()
            #   - Quantité her
            return Response({"status": "Order is reserved"}, status=status.HTTP_200_OK)