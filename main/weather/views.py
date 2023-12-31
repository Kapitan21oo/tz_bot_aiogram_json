from django.http import JsonResponse
from django.views import View
import random

class WeatherView(View):
    def get(self, request, *args, **kwargs):
        # Получаем значение параметра 'city' из GET-запроса
        city = request.GET.get('city')

        if city:
            # Здесь определяем данные о погоде для различных городов
            weather_data = {
                "Москва": {"temperature": random.randint(-10, 30), "wind_speed": random.randint(0, 20),
                           "precipitation": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Берлин": {"temperature": random.randint(-5, 25), "wind_speed": random.randint(0, 15),
                           "precipitation": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Лондон": {"temperature": random.randint(5, 20), "wind_speed": random.randint(5, 25),
                           "precipitation": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Нью-Йорк": {"temperature": random.randint(0, 30), "wind_speed": random.randint(0, 20),
                             "precipitation": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Токио": {"temperature": random.randint(10, 35), "wind_speed": random.randint(0, 10),
                          "precipitation": random.choice(["Ясно", "Облачно", "Дождь"])},
            }

            # Получаем данные о погоде для указанного города (если он существует)
            city_data = weather_data.get(city)

            if city_data:
                # Если данные о погоде для города найдены, возвращаем их в формате JSON
                return JsonResponse(city_data, json_dumps_params={'ensure_ascii': False})
            else:
                # Если город не найден, возвращаем сообщение об ошибке с кодом 404
                return JsonResponse({"error": "City not found"}, status=404, json_dumps_params={'ensure_ascii': False})
        else:
            # Если параметр 'city' отсутствует в запросе, возвращаем сообщение об ошибке с кодом 400
            return JsonResponse({"error": "Отсутствует параметр 'city'"}, status=400, json_dumps_params={'ensure_ascii': False})
