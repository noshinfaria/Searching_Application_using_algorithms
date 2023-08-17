from django.shortcuts import render
from django.contrib import messages
import heapq
from .models import InputData
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserInputSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes


def sort_array_descending_order(arr):
    minHeap = []
    for num in arr:
        heapq.heappush(minHeap, num)

    result = []
    while minHeap:
        top = heapq.heappop(minHeap)
        result.insert(0, top)

    return result


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return True

        # If element is smaller than mid, then it
        # can only be present in right subarray
        elif arr[mid] > x:
            return binarySearch(arr, mid + 1, r, x)

        # Else the element can only be present
        # in left subarray
        else:
            return binarySearch(arr, l, mid - 1, x)

    # Element is not present in the array
    else:
        return False


def search_element(request):
    if request.method == "POST":
        input_values = request.POST.get('input_values', '')
        search_value = request.POST.get('search_value', '')

        if input_values == '' or not search_value:
            messages.error(request, "Please fill the form correctly")
        else:
            # -------changing data type & format-------------------
            search_value = int(search_value)
            input_values = list(input_values.split(","))
            input_values = map(int, input_values)

            # -------Sort and Search-------------------
            sorted_array = sort_array_descending_order(input_values)
            result = binarySearch(sorted_array, 0, len(sorted_array) - 1, search_value)

            # -------save input values-------------------
            input_info = InputData(input_values=sorted_array, user_id=request.user)
            input_info.save()
            return render(request, "searchApp/search_element.html", {'result': result})

    return render(request, "searchApp/search_element.html")


# class ListUserInput(generics.ListAPIView):
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
#
#     serializer_class = UserInputSerializer
#     # queryset = InputData.objects.all()
#
#     def get(self, request, format=None):
#         queryset = InputData.objects.filter(user_id=request.user)
#         return render(request, "searchApp/list_view.html",  {'queryset': queryset})


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def list_user_input(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')
        user_name = request.GET.get('user_id', '')

        if not start_date or not end_date or not user_name:
            messages.error(request, "Please fill the box correctly")
        else:
            queryset = InputData.objects.filter(user_id=user_name,
                                                input_time__gte=start_date,
                                                input_time__lte=end_date)
            return render(request, "searchApp/list_view.html", {'queryset': queryset})

    return render(request, "searchApp/list_view.html")
