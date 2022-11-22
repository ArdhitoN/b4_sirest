from django.shortcuts import render

# Create your views here.

def p_berlangsung(response):
    return render(response, 'pesanan_berlangsung.html')

def p_detail(response):
    return render(response, 'pesanan_detail.html')