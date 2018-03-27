
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import WalletForm, EditWalletForm
from .models import Wallet, Company, DescriptionCompany, NewsCompany, ImageCompany
from .serializer import WalletSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import quandl
import datetime
import numpy as np
from sklearn.svm import SVR

class WalletListView(APIView):
    serializer_class = WalletSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Wallet.objects.all(), many = True)
        return Response(serializer.data)

class WalletView(APIView):

    def get(self, request, pk, format=None):
        wallet = Wallet.objects.get(pk=pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

def home(request):
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'home/home.html', {'wallets':wallets})

def newwallet(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            companies = form.cleaned_data['companies']
            post.companies = companies
            return redirect('home:home')
    else:
        form = WalletForm()
    return render(request, 'home/newwallet.html', {'form': form})

def wallet(request, name):
    wallet = Wallet.objects.get(name=name)
    companies = Wallet.objects.get(name=name).companies.all()
    image = ImageCompany.objects.all()
    return render(request, 'home/wallet.html', {'wallet': wallet,'companies':companies,'image':image})

def deletewallet(request, name):
    delete = get_object_or_404(Wallet, name=name)
    if request.method == "POST":
        delete.delete()
        return redirect("home:home")
    return render(request, 'home/deletewallet.html', {'delete': delete})

def editwallet(request, name):
    edit = get_object_or_404(Wallet, name=name)
    if request.method == 'POST':
        form = EditWalletForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            form.companies = form.cleaned_data['companies']
            return redirect("home:home")
    else:
        form = EditWalletForm(instance=edit)
    args = {'form': form}
    return render(request, 'home/editwallet.html', args)

def company(request, symbol):
    news = NewsCompany.objects.filter(company=symbol)
    description = DescriptionCompany.objects.filter(company=symbol)
    wallet = Wallet.objects.all()

    quandl.ApiConfig.api_key = "ZdFgZzvMmzfjhidyxuX1"

    #Today and last month datetime
    final_date = datetime.datetime.now().strftime ("%Y-%m-%d")
    last_month = datetime.datetime.now() + datetime.timedelta(days=-30)
    inicial_date = last_month.strftime ("%Y-%m-%d")

    code = symbol

    data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'open', 'close'] }, ticker = code, date = { 'gte': inicial_date, 'lte': final_date }).values

    antepenultimate = data[(len(data)-3)][3]
    penultimate = data[(len(data)-2)][3]
    ultimate = data[(len(data)-1)][3]

    difference = ultimate - penultimate
    percent = (difference/penultimate)*100

    stock_values = data[::-1]


    dates = []
    i = 0
    for row in data:
        dates.append(i)
        i = i + 1
    prices = []
    for row in data:
        prices.append(float(row[2]))

    def predict_prices(dates, prices, x):
        dates2 = np.reshape(dates, (len(dates), 1))

        svr_rbf = SVR(kernel = 'rbf', C=1e3, gamma=0.1)
        svr_rbf.fit(dates2, prices)

        return svr_rbf.predict(x)[0]

    predictprices = predict_prices(dates, prices, len(prices))

    def sell(predict, today):
        if predict < today :
            return "Sell"
        else:
            return "Buy"

    decision = sell(predictprices, prices[len(prices)-1])


    return render(request, 'home/company.html', {'news':news, 'description': description,
    'wallet':wallet, 'stock' : stock_values, 'dif': ("%.2f" % round(difference,2)),
    'per': ("%.2f" % round(percent,2)), 'c': code, 'decision':decision, 'predictprices': ("%.2f" % round(predictprices,2))})


def allcompanies(request):
    companies = DescriptionCompany.objects.all()
    image = ImageCompany.objects.all()
    return render(request, 'home/allcompanies.html', {'image':image, 'companies': companies})
