from rest_framework.views import APIView
from rest_framework.response import Response

class DynamicResponse(APIView):
    # Variable to hold the response
    response_value = True

    # GET request returns the current value
    def get(self, request):
        return Response(self.response_value)

class ChangeResponse(APIView):
    # POST request to change the response
    def post(self, request):
        new_value = request.data.get('value')
        if new_value is not None:
            DynamicResponse.response_value = new_value
            return Response(f"Response value changed to: {new_value}")
        return Response("Please provide a value (True or False) to update the response.")

