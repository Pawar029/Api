# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from event_api.models import Event
from event_api.serializers import EventSerializer

class EventListView(APIView):
    def get(self, request):
        # event_id = request.GET.get('id')
        event_type = request.GET.get('types')
        limit = int(request.GET.get('limit'))
        page = int(request.GET.get('page'))
        print(event_type)
        print(limit)
        print(page)

        try:
            # Filter events by type
            events = Event.objects.all()
            if event_type == 'latest':
                events = events.order_by('-schedule')

            # Calculate pagtypesination
            total_events = events.count()
            total_pages = (total_events + limit - 1) // limit
            start_index = (page - 1) * limit
            end_index = start_index + limit
            
            if(page>total_pages):
                response_data = {
                    'msg':"You have entered more pages than exist",
                    'total_events': total_events,
                    'total_pages': total_pages
                } 
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            if(limit>total_events):
                response_data = {
                    'msg':"You have entered more limit than exist",
                    'total_events': total_events,
                    'total_pages': total_pages
                } 
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            # Retrieve paginated events
            paginated_events = events[start_index:end_index]

            # Serialize events
            serializer = EventSerializer(paginated_events, many=True)
            
            # Construct response data
            response_data = {
                'msg':"data Successfully got",
                'events': serializer.data,
                'total_events': total_events,
                'total_pages': total_pages,
                'current_page': page
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        print('Request data is : ',request.data)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            Event.objects.create( 
                                name=serializer.data.get("name"),
                                tagline=serializer.data.get("tagline"),
                                schedule=serializer.data.get("schedule"),
                                description=serializer.data.get("description"),
                                moderator=serializer.data.get("moderator"),
                                category=serializer.data.get("category"),
                                sub_category=serializer.data.get("sub_category"),
                                rigor_rank=serializer.data.get("rigor_rank"),
                                types=serializer.data.get("types"),
                                attendees=serializer.data.get("attendees"),
                                # image = serializer.validated_data.get('files').get('image'),
                                  
                                    )
            # event = serializer.save()
            dic = {
                    "msg": "Data Saved Successfully",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED
                }
                # return Response(dic)
            return Response(dic)
            return Response({'id': event.id}, status=status.HTTP_201_CREATED)
        print("In Errors")
        dic = {
                "msg": "Data Failed",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            }
        return Response(dic)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


           


    def put(self, request):
        try:
            event_id = request.GET.get('id')
            event = Event.objects.get(id=event_id)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                res_data={
                    "msg":"Event updated"
                }
                return Response(res_data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            event_id = request.GET.get('id')
            event = Event.objects.get(id=event_id)
            name = event.name
            print(name)
            event.delete()
            res_data = {
                "msg":"Event is Deleted",
                'name':name
            }
            return Response(res_data,status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)


class EventDetailView(APIView):
    def get(self, request):
        try:
            event_id = request.GET.get('id')
            event = Event.objects.get(id=event_id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
