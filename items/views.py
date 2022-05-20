from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, User
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


@api_view(['POST'])
@parser_classes([JSONParser])
def add_items(request):
    if not request.user.is_authenticated:
        return Response({"message": "This function is restricted"})
    else:
        data = request.data
        name = data.get('name')
        color = data.get('color')
        amount = data.get('amount')
        user_id = data.get('user')

        users = User.objects.filter(id=user_id)
        if len(users) == 0:
            return Response({"message": "User not founded"})
        else:
            user = users[0]
            item = Item(name=name, color=color, amount=amount, user=user)
            if Item.objects.filter(name=name, color=color, amount=amount, user=user):
                return Response({"message": "Item is already existed"})
            else:
                item.save()
                return Response(item.to_dict())


@api_view(['GET'])
@parser_classes([JSONParser])
def view_items(request):
    if not request.user.is_authenticated:
        return Response({"message": "This function is restricted"})
    else:
        items = [item.to_dict() for item in Item.objects.all()]
        return Response(items)


@api_view(['PUT'])
@parser_classes([JSONParser])
def update_items(request, id):
    if not request.user.is_authenticated:
        return Response({"message": "This function is restricted"})
    else:
        item = Item.objects.get(id=id)

        data = request.data
        item.name = data['name']
        item.color = data['color']
        item.amount = data['amount']
        item.save()
        return Response(item.to_dict())


@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_items(request, id):
    if not request.user.is_authenticated:
        return Response({"message": "This function is restricted"})
    else:
        item = Item.objects.filter(id=id)
        item.delete()
        return Response({"message": "item deleted"})


@api_view(['GET'])
@parser_classes([JSONParser])
def find_items(request, user):
    if not request.user.is_authenticated:
        return Response({"message": "This function is restricted"})
    else:
        items = [item.to_dict() for item in Item.objects.filter(user=user)]
        return Response(items)
