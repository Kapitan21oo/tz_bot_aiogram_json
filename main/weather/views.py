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
                "Москва": {"температура": random.randint(-10, 30), "скорость_ветра": random.randint(0, 20),
                           "осадки": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Берлин": {"температура": random.randint(-5, 25), "скорость_ветра": random.randint(0, 15),
                           "осадки": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Лондон": {"температура": random.randint(5, 20), "скорость_ветра": random.randint(5, 25),
                           "осадки": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Нью-Йорк": {"температура": random.randint(0, 30), "скорость_ветра": random.randint(0, 20),
                             "осадки": random.choice(["Ясно", "Облачно", "Дождь"])},
                "Токио": {"температура": random.randint(10, 35), "скорость_ветра": random.randint(0, 10),
                          "осадки": random.choice(["Ясно", "Облачно", "Дождь"])},
            }

            # Получаем данные о погоде для указанного города (если он существует)
            city_data = weather_data.get(city.capitalize())

            if city_data:
                # Если данные о погоде для города найдены, возвращаем их в формате JSON
                return JsonResponse(city_data)
            else:
                # Если город не найден, возвращаем сообщение об ошибке с кодом 404
                return JsonResponse({"error": "Город не найден"}, status=404)
        else:
            # Если параметр 'city' отсутствует в запросе, возвращаем сообщение об ошибке с кодом 400
            return JsonResponse({"error": "Отсутствует параметр 'city'"}, status=400)
