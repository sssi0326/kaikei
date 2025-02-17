import PySimpleGUI as sg
import datetime
milk_price=200
ichi_price=200
cof_price=200
kal_price=200
total_price=0
ruikei=0
ruikei_cnt=0
#--------------
milk_cnt=0
ichi_cnt=0
cof_cnt=0
kal_cnt=0
ruikei_milk=0
ruikei_ichi=0
ruikei_cof=0
ruikei_kal=0
milk_per=0
ichi_per=0
cof_per=0
kal_per=0
total_cnt=0
cnt_list=[]
per_list=[]
syouhin=["ミルクテ","イチゴ","コーヒー","カルピス"]
max_syouhin=""
min_syouhin=""
#--------------
milk=0
ichi=0
cof=0
kal=0
#-------------------------------
size=(5,1)
size2=(8,1)
color=("black","white")
#---------------------------------

layout=[
    [sg.Text("ミルクテ",),sg.Text(f"単価：{milk_price}"),sg.Button("リセット",size=size2,button_color=color,key="milk_reset"),sg.Button("1個",size=size,button_color=color,key="milk_1"),sg.Button("2個",size=size,button_color=color,key="milk_2"),sg.Button("3個",size=size,button_color=color,key="milk_3"),sg.Button("4個",size=size,button_color=color,key="milk_4"),sg.Button("5個",size=size,button_color=color,key="milk_5"),sg.InputText(key="milk_count",size=(5,1),default_text=0),sg.Text("個")],
    [sg.Text("イチゴ　",),sg.Text(f"単価：{ichi_price}"),sg.Button("リセット",size=size2,button_color=color,key="ichi_reset"),sg.Button("1個",size=size,button_color=color,key="ichi_1"),sg.Button("2個",size=size,button_color=color,key="ichi_2"),sg.Button("3個",size=size,button_color=color,key="ichi_3"),sg.Button("4個",size=size,button_color=color,key="ichi_4"),sg.Button("5個",size=size,button_color=color,key="ichi_5"),sg.InputText(key="ichi_count",size=(5,1),default_text=0),sg.Text("個")],
    [sg.Text("コーヒー",),sg.Text(f"単価：{cof_price}"),sg.Button("リセット",size=size2,button_color=color,key="cof_reset"),sg.Button("1個",size=size,button_color=color,key="cof_1"),sg.Button("2個",size=size,button_color=color,key="cof_2"),sg.Button("3個",size=size,button_color=color,key="cof_3"),sg.Button("4個",size=size,button_color=color,key="cof_4"),sg.Button("5個",size=size,button_color=color,key="cof_5"),sg.InputText(key="cof_count",size=(5,1),default_text=0),sg.Text("個")],
    [sg.Text("カルピス",),sg.Text(f"単価：{kal_price}"),sg.Button("リセット",size=size2,button_color=color,key="kal_reset"),sg.Button("1個",size=size,button_color=color,key="kal_1"),sg.Button("2個",size=size,button_color=color,key="kal_2"),sg.Button("3個",size=size,button_color=color,key="kal_3"),sg.Button("4個",size=size,button_color=color,key="kal_4"),sg.Button("5個",size=size,button_color=color,key="kal_5"),sg.InputText(key="kal_count",size=(5,1),default_text=0),sg.Text("個")],
    [sg.Text(total_price,key="total"),sg.Text("円"),sg.Button("会計",key="kaikei",size=(8,2)),sg.Button("合計",size=(8,2),key="goukei")],
    [sg.Text("累計売上金額"),sg.Text(ruikei,key="ruikei"),sg.Text("円")],
    [sg.Text("累計売上個数"),sg.Text("ミルクテ"),sg.Text(ruikei_milk,key="ruimilk"),sg.Text("個"),sg.Text("イチゴ"),sg.Text(ruikei_ichi,key="ruiichi"),sg.Text("個"),sg.Text("コーヒー"),sg.Text(ruikei_cof,key="ruicof"),sg.Text("個"),sg.Text("カルピス"),sg.Text(ruikei_kal,key="ruikal"),sg.Text("個"),sg.Text("合計"),sg.Text(ruikei_cnt,key="ruikeicnt"),sg.Text("個")],
    [sg.Text("売上割合　　"),sg.Text("ミルクテ"),sg.Text(milk_per,key="permilk"),sg.Text("%"),sg.Text("イチゴ"),sg.Text(ichi_per,key="perichi"),sg.Text("%"),sg.Text("コーヒー"),sg.Text(cof_per,key="percof"),sg.Text("%"),sg.Text("カルピス"),sg.Text(kal_per,key="perkal"),sg.Text("%")],
    [sg.Text("最大"),sg.Text("商品名"),sg.Text(key="maxsyouhin"),sg.Text(key="maxcnt"),sg.Text("個"),sg.Text(key="maxper"),sg.Text("%")],
    [sg.Text("最小"),sg.Text("商品名"),sg.Text(key="minsyouhin"),sg.Text(key="mincnt"),sg.Text("個"),sg.Text(key="minper"),sg.Text("%")],
    [sg.Button("会計開始",key="kaisi",size=(8,2)),sg.Button("会計終了",key="owari",size=(8,2))],
]
window=sg.Window("かいけいくん",layout)

while True:
    event,value=window.read()
    if event==None:
        break
#-------------個数ボタン----------------------------------
    if event=="milk_reset":
        milk_cnt=0
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(0+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="milk_1":
        milk_cnt=1
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(1+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="milk_2":
        milk_cnt=2
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(2+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="milk_3":
        milk_cnt=3
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(3+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="milk_4":
        milk_cnt=4
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(4+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="milk_5":
        milk_cnt=5
        window["milk_count"].update(milk_cnt)
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(5+ichi_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
#----------------------------------------
    if event=="ichi_reset":
        ichi_cnt=0
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(0+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="ichi_1":
        ichi_cnt=1
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(1+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="ichi_2":
        ichi_cnt=2
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(2+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="ichi_3":
        ichi_cnt=3
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(3+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="ichi_4":
        ichi_cnt=4
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(4+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="ichi_5":
        ichi_cnt=5
        window["ichi_count"].update(ichi_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(5+milk_cnt+cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
#-------------------------------------------
    if event=="cof_reset":
        cof_cnt=0
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(0+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="cof_1":
        cof_cnt=1
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(1+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="cof_2":
        cof_cnt=2
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(2+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="cof_3":
        cof_cnt=3
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(3+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="cof_4":
        cof_cnt=4
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(4+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
    if event=="cof_5":
        cof_cnt=5
        window["cof_count"].update(cof_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(5+milk_cnt+ichi_cnt+kal_cnt)*200
        window["total"].update(total_price)
#-------------------------------------------
    if event=="kal_reset":
        kal_cnt=0
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(0+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
    if event=="kal_1":
        kal_cnt=1
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(1+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
    if event=="kal_2":
        kal_cnt=2
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(2+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
    if event=="kal_3":
        kal_cnt=3
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(3+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
    if event=="kal_4":
        kal_cnt=4
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(4+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
    if event=="kal_5":
        kal_cnt=5
        window["kal_count"].update(kal_cnt)
        milk_cnt=int(value["milk_count"])
        cof_cnt=int(value["ichi_count"])
        kal_cnt=int(value["cof_count"])
        total_price=(5+milk_cnt+ichi_cnt+cof_cnt)*200
        window["total"].update(total_price)
#-----------合計-----------------------------
    if event=="goukei":
        milk_cnt=int(value["milk_count"])
        ichi_cnt=int(value["ichi_count"])
        cof_cnt=int(value["cof_count"])
        kal_cnt=int(value["kal_count"])
        total_price=(milk_cnt+ichi_cnt)*200+(cof_cnt+kal_cnt)*200
        window["total"].update(total_price)
#----------------------------------------------
    if event=="kaikei":
        ruikei+=total_price
        ruikei_cnt=int(ruikei/200)
        window["ruikeicnt"].update(ruikei_cnt)
        max_syouhin=""
        min_syouhin=""
#--------個数リセット----------------------------
        window["milk_count"].update(0)
        window["ichi_count"].update(0)
        window["cof_count"].update(0)
        window["kal_count"].update(0)
        window["total"].update(0)
        window["ruikei"].update(ruikei)
#-------累計計算とか----------------------------------------
        ruikei_milk+=milk_cnt
        ruikei_ichi+=ichi_cnt
        ruikei_cof+=cof_cnt
        ruikei_kal+=kal_cnt
        window["ruimilk"].update(ruikei_milk)
        window["ruiichi"].update(ruikei_ichi)
        window["ruicof"].update(ruikei_cof)
        window["ruikal"].update(ruikei_kal)
        total_cnt=ruikei_milk+ruikei_ichi+ruikei_cof+ruikei_kal
        milk_per=int(ruikei_milk/total_cnt*100)
        ichi_per=int(ruikei_ichi/total_cnt*100)
        cof_per=int(ruikei_cof/total_cnt*100)
        kal_per=int(ruikei_kal/total_cnt*100)
        window["permilk"].update(milk_per)
        window["perichi"].update(ichi_per)
        window["percof"].update(cof_per)
        window["perkal"].update(kal_per)
        cnt_list=[ruikei_milk,ruikei_ichi,ruikei_cof,ruikei_kal]
        per_list=[milk_per,ichi_per,cof_per,kal_per]
        for i in range(4):
            if cnt_list[i]==max(cnt_list):
                max_syouhin=syouhin[i]
            if cnt_list[i]==min(cnt_list):
                min_syouhin=syouhin[i]
        window["maxsyouhin"].update(max_syouhin)
        window["maxcnt"].update(max(cnt_list))
        window["maxper"].update(max(per_list))
        window["minsyouhin"].update(min_syouhin)
        window["mincnt"].update(min(cnt_list))
        window["minper"].update(min(per_list))
#------------履歴---------------------------------------------------------------------------------------------
        text=f"\n{datetime.datetime.now()}\nミルクテ{milk_cnt}個\nイチゴ{ichi_cnt}個\nコーヒー{cof_cnt}個\nカルピス{kal_cnt}個\n合計金額{total_price}円\n---------------------------"
        print(text)
        f=open("log.txt","a",encoding='UTF-8')
        f.write(text)
        f.close()
#----------会計開始---------------------------------
    if event=="kaisi":
        f=open("total.txt","r",encoding="UTF-8")
        ruikei=int(f.read())
        window["ruikei"].update(ruikei)
        f.close()
        f=open("total_milk_cnt.txt","r",encoding="UTF-8")
        ruikei_milk=int(f.read())
        window["ruimilk"].update(ruikei_milk)
        f.close()
        f=open("total_ichi_cnt.txt","r",encoding="UTF-8")
        ruikei_ichi=int(f.read())
        window["ruiichi"].update(ruikei_ichi)
        f.close()
        f=open("total_cof_cnt.txt","r",encoding="UTF-8")
        ruikei_cof=int(f.read())
        window["ruicof"].update(ruikei_cof)
        f.close()
        f=open("total_kal_cnt.txt","r",encoding="UTF-8")
        ruikei_kal=int(f.read())
        window["ruikal"].update(ruikei_kal)
        f.close()
        total_cnt=ruikei_milk+ruikei_ichi+ruikei_cof+ruikei_kal
        ruikei_cnt=int(ruikei/200)
        window["ruikeicnt"].update(ruikei_cnt)
        milk_per=int(ruikei_milk/total_cnt*100)
        ichi_per=int(ruikei_ichi/total_cnt*100)
        cof_per=int(ruikei_cof/total_cnt*100)
        kal_per=int(ruikei_kal/total_cnt*100)
        window["permilk"].update(milk_per)
        window["perichi"].update(ichi_per)
        window["percof"].update(cof_per)
        window["perkal"].update(kal_per)
        cnt_list=[ruikei_milk,ruikei_ichi,ruikei_cof,ruikei_kal]
        per_list=[milk_per,ichi_per,cof_per,kal_per]
        for i in range(4):
            if cnt_list[i]==max(cnt_list):
                max_syouhin=syouhin[i]
            if cnt_list[i]==min(cnt_list):
                min_syouhin=syouhin[i]
        window["maxsyouhin"].update(max_syouhin)
        window["maxcnt"].update(max(cnt_list))
        window["maxper"].update(max(per_list))
        window["minsyouhin"].update(min_syouhin)
        window["mincnt"].update(min(cnt_list))
        window["minper"].update(min(per_list))
        print("会計が開始しました！")
#----------会計終了---------------------------------
    if event=="owari":
        f=open("total.txt","a",encoding="UTF-8")
        f.write(f"{ruikei}")
        f.close()
        f=open("total_milk_cnt.txt","a",encoding="UTF-8")
        f.write(f"{ruikei_milk}")
        f.close()
        f=open("total_ichi_cnt.txt","a",encoding="UTF-8")
        f.write(f"{ruikei_ichi}")
        f.close()
        f=open("total_cof_cnt.txt","a",encoding="UTF-8")
        f.write(f"{ruikei_cof}")
        f.close()
        f=open("total_kal_cnt.txt","a",encoding="UTF-8")
        f.write(f"{ruikei_kal}")
        f.close()
        print("会計が終了しました！")
window.close()