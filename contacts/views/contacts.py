from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from contacts.models import Contact
from contacts.serializers import ContactSerializer


@api_view(['GET'])
def getContacts(request):
    contact = Contact.objects.filter(
        user=request.user).all().order_by('-created_at')
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getContact(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
        serializer = ContactSerializer(contact, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Contact.DoesNotExist:
        return Response(f"The contact #{pk} don't exist!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def addContact(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = ContactSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response('Error with the contact save!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateContact(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ContactSerializer(instance=contact, data=data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Contact.DoesNotExist:
        return Response(f"The contact #{pk} don't exist!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def deleteContact(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
        if (contact.delete()):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('Problem with delete the contact', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Contact.DoesNotExist:
        return Response(f"The contact #{pk} don't exist!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
