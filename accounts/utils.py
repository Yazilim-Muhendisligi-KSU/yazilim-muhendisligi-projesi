import yfinance as yf
from pprint import pprint
from .models import Stock

stock_list = ['AVOD.IS', 'A1CAP.IS', 'ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'ADGYO.IS', 'AFYON.IS', 'AGHOL.IS', 'AGESA.IS', 'AGROT.IS', 'AHGAZ.IS', 'AKBNK.IS', 'AKCNS.IS', 'AKYHO.IS', 'AKENR.IS', 'AKFGY.IS', 'AKFYE.IS', 'ATEKS.IS', 'AKSGY.IS', 'AKMGY.IS', 'AKSA.IS', 'AKSEN.IS', 'AKGRT.IS', 'AKSUE.IS', 'ALCAR.IS', 'ALGYO.IS', 'ALARK.IS', 'ALBRK.IS', 'ALCTL.IS', 'ALFAS.IS', 'ALKIM.IS', 'ALKA.IS', 'AYCES.IS', 'ALMAD.IS', 'ANSGR.IS', 'AEFES.IS', 'ANHYT.IS', 'ASUZU.IS', 'ANGEN.IS', 'ANELE.IS', 'ARCLK.IS', 'ARDYZ.IS', 'ARENA.IS', 'ARSAN.IS', 'ARTMS.IS', 'ARZUM.IS', 'ASGYO.IS', 'ASELS.IS', 'ASTOR.IS', 'ATAGY.IS', 'ATAKP.IS', 'AGYO.IS', 'ATSYH.IS', 'ATLAS.IS', 'ATATP.IS', 'AVGYO.IS', 'AVTUR.IS', 'AVHOL.IS', 'AVPGY.IS', 'AYDEM.IS', 'AYEN.IS', 'AYES.IS', 'AYGAZ.IS', 'AZTEK.IS', 'BAGFS.IS', 'BAKAB.IS', 'BALAT.IS', 'BNTAS.IS', 'BANVT.IS', 'BARMA.IS', 'BASGZ.IS', 'BASCM.IS', 'BEGYO.IS', 'BTCIM.IS', 'BSOKE.IS', 'BYDNR.IS', 'BAYRK.IS', 'BERA.IS', 'BRKSN.IS', 'BJKAS.IS', 'BEYAZ.IS', 'BIENY.IS', 'BLCYT.IS', 'BIMAS.IS', 'BIOEN.IS', 'BRKVY.IS', 'BRKO.IS', 'BRLSM.IS', 'BRMEN.IS', 'BIZIM.IS', 'BMSTL.IS', 'BMSCH.IS', 'BOBET.IS', 'BORSK.IS', 'BORLS.IS', 'BRSAN.IS', 'BRYAT.IS', 'BFREN.IS', 'BOSSA.IS', 'BRISA.IS', 'BURCE.IS', 'BURVA.IS', 'BUCIM.IS', 'BVSAN.IS', 'BIGCH.IS', 'CRFSA.IS', 'CASA.IS', 'CEOEM.IS', 'CCOLA.IS', 'CONSE.IS', 'COSMO.IS', 'CRDFA.IS', 'CVKMD.IS', 'CWENE.IS', 'CANTE.IS', 'CATES.IS', 'CLEBI.IS', 'CELHA.IS', 'CEMAS.IS', 'CEMTS.IS', 'CMBTN.IS', 'CMENT.IS', 'CIMSA.IS', 'CUSAN.IS', 'DAGI.IS', 'DAGHL.IS', 'DAPGM.IS', 'DARDL.IS', 'DGATE.IS', 'DMSAS.IS', 'DENGE.IS', 'DZGYO.IS', 'DERIM.IS', 'DERHL.IS', 'DESA.IS', 'DESPC.IS', 'DEVA.IS', 'DNISI.IS', 'DIRIT.IS', 'DITAS.IS', 'DMRGD.IS', 'DOCO.IS', 'DOFER.IS', 'DOBUR.IS', 'DOHOL.IS', 'DGNMO.IS', 'ARASE.IS', 'DOGUB.IS', 'DGGYO.IS', 'DOAS.IS', 'DOKTA.IS', 'DURDO.IS', 'DYOBY.IS', 'EDATA.IS', 'EBEBK.IS', 'ECZYT.IS', 'EDIP.IS', 'EGEEN.IS', 'EGGUB.IS', 'EGPRO.IS', 'EGSER.IS', 'EPLAS.IS', 'ECILC.IS', 'EKIZ.IS', 'EKOS.IS', 'EKSUN.IS', 'ELITE.IS', 'EMKEL.IS', 'EMNIS.IS', 'EKGYO.IS', 'ENJSA.IS', 'ENERY.IS', 'ENKAI.IS', 'ENSRI.IS', 'ERBOS.IS', 'ERCB.IS', 'EREGL.IS', 'KIMMR.IS', 'ERSU.IS', 'ESCAR.IS', 'ESCOM.IS', 'ESEN.IS', 'ETILR.IS', 'EUKYO.IS', 'EUYO.IS', 'ETYAT.IS', 'EUHOL.IS', 'TEZOL.IS', 'EUREN.IS', 'EUPWR.IS', 'FADE.IS', 'FMIZP.IS', 'FENER.IS', 'FLAP.IS', 'FONET.IS', 'FROTO.IS', 'FORMT.IS', 'FORTE.IS', 'FRIGO.IS', 'FZLGY.IS', 'GWIND.IS', 'GSRAY.IS', 'GARFA.IS', 'GRNYO.IS', 'GEDIK.IS', 'GEDZA.IS', 'GLCVY.IS', 'GENIL.IS', 'GENTS.IS', 'GEREL.IS', 'GZNMI.IS', 'GIPTA.IS', 'GESAN.IS', 'GLBMD.IS', 'GLYHO.IS', 'GOODY.IS', 'GOKNR.IS', 'GOLTS.IS', 'GOZDE.IS', 'GRTRK.IS', 'GSDDE.IS', 'GSDHO.IS', 'GUBRF.IS', 'GLRYH.IS', 'GRSEL.IS', 'SAHOL.IS', 'HLGYO.IS', 'HATSN.IS', 'HATEK.IS', 'HDFGS.IS', 'HEDEF.IS', 'HEKTS.IS', 'HKTM.IS', 'HTTBT.IS', 'HUBVC.IS', 'HUNER.IS', 'HURGZ.IS', 'ICBCT.IS', 'ICUGS.IS', 'INGRM.IS', 'INVEO.IS', 'INVES.IS', 'ISKPL.IS', 'IEYHO.IS', 'IDGYO.IS', 'IHEVA.IS', 'IHLGM.IS', 'IHGZT.IS', 'IHAAS.IS', 'IHLAS.IS', 'IHYAY.IS', 'IMASM.IS', 'INDES.IS', 'INFO.IS', 'INTEM.IS', 'IPEKE.IS', 'ISDMR.IS', 'ISFIN.IS', 'ISGYO.IS', 'ISMEN.IS', 'ISYAT.IS', 'ISBIR.IS', 'ISSEN.IS', 'IZINV.IS', 'IZENR.IS', 'IZMDC.IS', 'IZFAS.IS', 'JANTS.IS', 'KFEIN.IS', 'KLKIM.IS', 'KLSER.IS', 'KAPLM.IS', 'KRDMA.IS', 'KRDMB.IS', 'KRDMD.IS', 'KAREL.IS', 'KARSN.IS', 'KRTEK.IS', 'KARYE.IS', 'KARTN.IS', 'KTLEV.IS', 'KATMR.IS', 'KAYSE.IS', 'KENT.IS', 'KERVT.IS', 'KRVGD.IS', 'KERVN.IS', 'KZBGY.IS', 'KLGYO.IS', 'KLRHO.IS', 'KMPUR.IS', 'KLMSN.IS', 'KCAER.IS', 'KCHOL.IS', 'KLSYN.IS', 'KNFRT.IS', 'KONTR.IS', 'KONYA.IS', 'KONKA.IS', 'KGYO.IS', 'KORDS.IS', 'KRPLS.IS', 'KOTON.IS', 'KOZAL.IS', 'KOZAA.IS', 'KOPOL.IS', 'KRGYO.IS', 'KRSTL.IS', 'KRONT.IS', 'KSTUR.IS', 'KUVVA.IS', 'KUYAS.IS', 'KBORU.IS', 'KZGYO.IS', 'KUTPO.IS', 'KTSKR.IS', 'LIDER.IS', 'LIDFA.IS', 'LINK.IS', 'LOGO.IS', 'LKMNH.IS', 'LRSHO.IS', 'LUKSK.IS', 'MACKO.IS', 'MAKIM.IS', 'MAKTK.IS', 'MANAS.IS', 'MAGEN.IS', 'MARKA.IS', 'MAALT.IS', 'MRSHL.IS', 'MRGYO.IS', 'MARTI.IS', 'MTRKS.IS', 'MAVI.IS', 'MZHLD.IS', 'MEDTR.IS', 'MEGMT.IS', 'MEGAP.IS', 'MEKAG.IS', 'MNDRS.IS', 'MEPET.IS', 'MERCN.IS', 'MERIT.IS', 'MERKO.IS', 'METUR.IS', 'METRO.IS', 'MTRYO.IS', 'MHRGY.IS', 'MIATK.IS', 'MGROS.IS', 'MIPAZ.IS', 'MSGYO.IS', 'MPARK.IS', 'MMCAS.IS', 'MOBTL.IS', 'MOGAN.IS', 'MNDTR.IS', 'EGEPO.IS', 'NATEN.IS', 'NTGAZ.IS', 'NTHOL.IS', 'NETAS.IS', 'NIBAS.IS', 'NUHCM.IS', 'NUGYO.IS', 'OBAMS.IS', 'OBASE.IS', 'ODAS.IS', 'OFSYM.IS', 'ONCSM.IS', 'ORCAY.IS', 'ORGE.IS', 'ORMA.IS', 'OSMEN.IS', 'OSTIM.IS', 'OTKAR.IS', 'OTTO.IS', 'OYAKC.IS', 'OYYAT.IS', 'OYAYO.IS', 'OYLUM.IS', 'OZKGY.IS', 'OZGYO.IS', 'OZRDN.IS', 'OZSUB.IS', 'PAMEL.IS', 'PNLSN.IS', 'PAGYO.IS', 'PAPIL.IS', 'PRDGS.IS', 'PRKME.IS', 'PARSN.IS', 'PASEU.IS', 'PSGYO.IS', 'PCILT.IS', 'PGSUS.IS', 'PEKGY.IS', 'PENGD.IS', 'PENTA.IS', 'PEGYO.IS', 'PSDTC.IS', 'PETKM.IS', 'PKENT.IS', 'PETUN.IS', 'PINSU.IS', 'PNSUT.IS', 'PKART.IS', 'PLTUR.IS', 'POLHO.IS', 'POLTK.IS', 'PRZMA.IS', 'QNBFL.IS', 'QNBFB.IS', 'QUAGR.IS', 'RNPOL.IS', 'RALYH.IS', 'RAYSG.IS', 'REEDR.IS', 'RYGYO.IS', 'RYSAS.IS', 'RODRG.IS', 'ROYAL.IS', 'RGYAS.IS', 'RTALB.IS', 'RUBNS.IS', 'SAFKR.IS', 'SANEL.IS', 'SNICA.IS', 'SANFM.IS', 'SANKO.IS', 'SAMAT.IS', 'SARKY.IS', 'SASA.IS', 'SAYAS.IS', 'SDTTR.IS', 'SEKUR.IS', 'SELEC.IS', 'SELGD.IS', 'SELVA.IS', 'SNKRN.IS', 'SRVGY.IS', 'SEYKM.IS', 'SILVR.IS', 'SNGYO.IS', 'SKYLP.IS', 'SMRTG.IS', 'SMART.IS', 'SODSN.IS', 'SOKE.IS', 'SKTAS.IS', 'SONME.IS', 'SNPAM.IS', 'SUMAS.IS', 'SUNTK.IS', 'SURGY.IS', 'SUWEN.IS', 'SEKFK.IS', 'SEGYO.IS', 'SKYMD.IS', 'SKBNK.IS', 'SOKM.IS', 'TABGD.IS', 'TNZTP.IS', 'TARKM.IS', 'TATGD.IS', 'TATEN.IS', 'TAVHL.IS', 'TEKTU.IS', 'TKFEN.IS', 'TKNSA.IS', 'TMPOL.IS', 'TERA.IS', 'TETMT.IS', 'TGSAS.IS', 'TOASO.IS', 'TRGYO.IS', 'TLMAN.IS', 'TSPOR.IS', 'TDGYO.IS', 'TSGYO.IS', 'TUCLK.IS', 'TUKAS.IS', 'TRCAS.IS', 'TUREX.IS', 'MARBL.IS', 'TRILC.IS', 'TCELL.IS', 'TMSN.IS', 'TUPRS.IS', 'THYAO.IS', 'PRKAB.IS', 'TTKOM.IS', 'TTRAK.IS', 'TBORG.IS', 'TURGG.IS', 'GARAN.IS', 'HALKB.IS', 'ISATR.IS', 'ISBTR.IS', 'ISCTR.IS', 'KLNMA.IS', 'TSKB.IS', 'TURSG.IS', 'SISE.IS', 'VAKBN.IS', 'UFUK.IS', 'ULAS.IS', 'ULUSE.IS', 'ULUUN.IS', 'UMPAS.IS', 'USAK.IS', 'UZERB.IS', 'ULKER.IS', 'UNLU.IS', 'VAKFN.IS', 'VKGYO.IS', 'VKFYO.IS', 'VAKKO.IS', 'VANGD.IS', 'VBTYZ.IS', 'VERUS.IS', 'VERTU.IS', 'VESBE.IS', 'VESTL.IS', 'VKING.IS', 'YKBNK.IS', 'YAPRK.IS', 'YATAS.IS', 'YYLGD.IS', 'YAYLA.IS', 'YGGYO.IS', 'YEOTK.IS', 'YGYO.IS', 'YYAPI.IS', 'YESIL.IS', 'YBTAS.IS', 'YONGA.IS', 'YKSLN.IS', 'YUNSA.IS', 'ZEDUR.IS', 'ZRGYO.IS', 'ZOREN.IS']

def get_popular_stocks():
    popular_stocks = [
        "XU500.IS",
        "XU100.IS",
        "GARAN.IS",
        "ISCTR.IS",
        "KONTR.IS",
        "THYAO.IS",
    ]
    stocks = []
    for symbol in popular_stocks:
        print(symbol)
        try:
            stock = Stock.objects.get(symbol=symbol)
            if ((stock.current_price - stock.previous_close) / stock.previous_close) * 100 > 10 or ((stock.current_price - stock.previous_close) / stock.previous_close) * 100 < -10:
                continue
            stocks.append({
                "SYMBOL": stock.symbol,
                "BUY": stock.current_price,
                "SELL": stock.current_price,
                "CLOSE": stock.previous_close,
                "CHANGE": ((stock.current_price - stock.previous_close) / stock.previous_close) * 100,
            })
        except:
            ticker = yf.Ticker(symbol)
            
            stocks.append({
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["open"],
                "SELL": ticker.info["open"],
                "CLOSE": ticker.info["previousClose"],
                "CHANGE": ((ticker.info["open"] - ticker.info["previousClose"]) / ticker.info["previousClose"]) * 100,
            })

        continue

        ticker = yf.Ticker(symbol)
        try:
            pprint(ticker.info)
            stocks.append({
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["regularMarketPreviousClose"],
                "BID": ticker.info["currentPrice"],
                "CHANGE": ((ticker.info["regularMarketPreviousClose"] - ticker.info["regularMarketPreviousClose"]) / ticker.info["regularMarketPreviousClose"]) * 100,
            })
        except Exception as e:
            stocks.append({
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["open"],
                "BID": ticker.info["open"],
                "CHANGE": ((ticker.info["open"] - ticker.info["regularMarketPreviousClose"]) / ticker.info["regularMarketPreviousClose"]) * 100,
            })
            print(e)

    return stocks


def get_gaining_and_losing_stocks():
    stocks = []
    for symbol in stock_list:
        stock = Stock.objects.get(symbol=symbol)
        if ((stock.current_price - stock.previous_close) / stock.previous_close) * 100 > 10 or ((stock.current_price - stock.previous_close) / stock.previous_close) * 100 < -10:
            continue
        stocks.append({
            "SYMBOL": stock.symbol,
            "BUY": stock.current_price,
            "SELL": stock.current_price,
            "CLOSE": stock.previous_close,
            "CHANGE": ((stock.current_price - stock.previous_close) / stock.previous_close) * 100,
        })
        continue
        ticker = yf.Ticker(stock)
        try:
            stocks.append({
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["regularMarketPreviousClose"],
                "BID": ticker.info["currentPrice"],
                "CHANGE": ((ticker.info["currentPrice"] - ticker.info["regularMarketPreviousClose"]) / ticker.info["regularMarketPreviousClose"]) * 100,
            })
            pprint(stocks)
        except Exception as e:
            stocks.append({
                "SYMBOL": ticker.info["symbol"],
                "BUY": ticker.info["open"],
                "BID": ticker.info["open"],
                "CHANGE": ((ticker.info["open"] - ticker.info["regularMarketPreviousClose"]) / ticker.info["regularMarketPreviousClose"]) * 100,
            })
            print(e)
    stocks_sorted = sorted(stocks, key=lambda x: x["CHANGE"])
    
    top_5_stocks = stocks_sorted[-5:][::-1]
    bottom_5_stocks = stocks_sorted[:5]
    
    return top_5_stocks, bottom_5_stocks
    return stocks.sort(key=lambda x: x["CHANGE"], reverse=True)[:5], stocks.sort(key=lambda x: x["CHANGE"])[:5]


def get_stock_data(symbol):
    t = yf.Ticker(symbol).history("1mo")
    times = t.index.to_list()
    data = []
    for time in times:
        item = t.loc[time]
        data.append({
            "date": time.strftime('%d-%m'),
            "close": item["Close"]
        })
    print(data)
    return data