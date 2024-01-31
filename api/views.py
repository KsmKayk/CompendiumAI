import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.generate_book import generate_book


@csrf_exempt
def generate_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            if "topic" not in data or "target_audience" not in data:
                JsonResponse(
                    {"error": "You must provide a topic and a target_audience"}
                )

            return JsonResponse(data)

        except json.JSONDecodeError:
            JsonResponse({"error": "Invalid JSON"})
