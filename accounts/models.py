from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

import yfinance as yf


class User(AbstractUser):
    pass
    

class WatchedStock(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="watched_stocks"
    )
    date = models.DateTimeField(auto_now=True)
    stock_symbol = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"
    


class Analysis(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="analysis"
    )
    date = models.DateTimeField(auto_now=True)
    stock_symbol = models.CharField(max_length=255, null=True, blank=True)
    data = models.ImageField(upload_to="media/analysis")

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:15]}"


class Stock(models.Model):
    symbol = models.CharField(max_length=255)

    last_updated = models.DateTimeField(auto_now_add=True)

    open = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)
    high = models.FloatField(null=True, blank=True)
    low = models.FloatField(null=True, blank=True)
    previous_close = models.FloatField(null=True, blank=True)
    current_price = models.FloatField(null=True, blank=True)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        return super().__call__(*args, **kwds)
    
    def update_data(self):
        """
            {
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["open"],
                "BID": ticker.info["open"],
                "CHANGE": ((ticker.info["open"] - ticker.info["regularMarketPreviousClose"]) / ticker.info["regularMarketPreviousClose"]) * 100,
            }

            ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open',
              'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares']
        """
        ticker = yf.Ticker(self.symbol)

        self.open = ticker.info["open"]
        self.close = ticker.info["previousClose"]
        self.high = ticker.info["dayHigh"]
        self.low = ticker.info["dayLow"]
        self.previous_close = ticker.info["previousClose"]
        try:
            self.current_price = ticker.info["currentPrice"]
        except:
            self.current_price = ticker.info["open"]
        
        self.save()

    

class StockData(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.DO_NOTHING,
        related_name="data"
    )
    datetime = models.DateTimeField(auto_now=True)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    previous_close = models.FloatField()
    current_price = models.FloatField()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        return super().__call__(*args, **kwds)
    
    
    


"""
  modeller:
    custom kullanıcı modeli
    takip listesi
    çizim
    bildirim
"""