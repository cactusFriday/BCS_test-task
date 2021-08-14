from django.shortcuts import render
from .models import Transaction
from .conf import NET_PARAMS

import requests

def gen_tx_table():
    txs = Transaction().objects.all()
    return txs, len(txs)

def transaction(request):
    return render(request, template_name='index.html', context={})

def index(request):
    # record, rec_len = gen_tx_table()
    record, rec_len = ['hlelo']*15, 15
    if request.method == 'POST':
        print('[METHOD]: POST')
        response = requests.post('http://bcs_tester:iLoveBCS@140.82.36.227:3669/', json={'method': method})
        print(response.text)
    elif request.method == 'GET':
        print('[METHOD]: GET')

    return render(request, template_name='tx_list.html', context = {'record': record, 'rec_len': rec_len})