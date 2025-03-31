import requests
from django.http import JsonResponse

API_KEY = "503e7ef2e71e7014781a5a28"
EXCHANGE_RATE_API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def convert_currency(request):
    base_currency = request.GET.get("from")
    target_currency = request.GET.get("to")
    amount = request.GET.get("amount")

    if not base_currency or not target_currency or not amount:
        return JsonResponse({"error": "Missing required parameters"}, status=400)

    try:
        amount = float(amount)
    except ValueError:
        return JsonResponse({"error": "Invalid amount value"}, status=400)

    try:
        response = requests.get(EXCHANGE_RATE_API_URL)
        data = response.json()
    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch exchange rates: {str(e)}"}, status=500)

    if data.get("result") != "success":
        return JsonResponse({"error": "Failed to fetch exchange rates"}, status=500)

    rates = data.get("conversion_rates", {})

    if base_currency not in rates or target_currency not in rates:
        return JsonResponse({"error": "Invalid currency code"}, status=400)

    # Convert currency using USD as an intermediate
    if base_currency == "USD":
        converted_amount = amount * rates[target_currency]
    else:
        usd_amount = amount / rates[base_currency]  # Convert to USD
        converted_amount = usd_amount * rates[target_currency]  # Convert USD to target currency

    return JsonResponse({
        "base_currency": base_currency,
        "target_currency": target_currency,
        "amount": amount,
        "converted_amount": round(converted_amount, 2)
    })
