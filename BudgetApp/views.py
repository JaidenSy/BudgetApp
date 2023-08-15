from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
from .models import Item

class ItemApiView(View):
    def get(self, request, item_id=None):
        if item_id is None:
            items = Item.objects.all()
            data = [{'id': item.id, 'name': item.name, 'price': item.price} for item in items]
        else:
            try:
                item = Item.objects.get(id=item_id)
                data = {'id': item.id, 'name': item.name, 'price': item.price}
            except Item.DoesNotExist:
                return HttpResponseNotFound()

        return JsonResponse(data, safe=False)

    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')

        if name and price:
            item = Item.objects.create(name=name, price=price)
            data = {'id': item.id, 'name': item.name, 'price': item.price}
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest()

    def put(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return HttpResponseNotFound()

        name = request.POST.get('name', item.name)
        price = request.POST.get('price', item.price)

        item.name = name
        item.price = price
        item.save()

        data = {'id': item.id, 'name': item.name, 'price': item.price}
        return JsonResponse(data)

    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return HttpResponseNotFound()

        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})

