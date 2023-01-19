from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account

# Create your views here.
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)
