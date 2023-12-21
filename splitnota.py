
dricks = 0.10
summa = float(input("hur mycket kostade det ?"))
antalvanner = int(input("hur många ska dela på notan ?"))
dricks =  int(input("Hur mycket dricks i procent 0-100% "))
dricks = dricks/100
summaTot = (summa+(summa*dricks))/antalvanner
onClick() -- knappen klickas och functionen OnClick åberopas


function onClick(){
print("Den totala summan att betala är :"), summaTot

                    
}