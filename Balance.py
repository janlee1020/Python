#Janet Lee
#Lab M3

def main():
    p= int(input("What is the investment? "))
    r=0.03
    balance=0
    for m in range(0,62,3):
        balance=p*((1+r/12))**m
        print(m, "\t", balance)
    
main()

#Trial 1
##What is the investment? 2500
##0 	 2500.0
##3 	 2518.7969140624996
##6 	 2537.735157716308
##9 	 2556.8157935854997
##12 	 2576.0398922837667
##15 	 2595.408532474498
##18 	 2614.9228009312988
##21 	 2634.583792598969
##24 	 2654.3926106549443
##27 	 2674.3503665711896
##30 	 2694.458180176571
##33 	 2714.7171797196825
##36 	 2735.1285019321554
##39 	 2755.69329209244
##42 	 2776.412704090067
##45 	 2797.287900490393
##48 	 2818.3200525998277
##51 	 2839.510340531563
##54 	 2860.859953271783
##57 	 2882.370088746382
##60 	 2904.041953888176

#Trial 2
##What is the investment? 1700
##0 	 1700.0
##3 	 1712.7819015624996
##6 	 1725.6599072470897
##9 	 1738.6347396381398
##12 	 1751.7071267529614
##15 	 1764.8778020826587
##18 	 1778.147504633283
##21 	 1791.5169789672989
##24 	 1804.9869752453621
##27 	 1818.558249268409
##30 	 1832.2315625200683
##33 	 1846.007682209384
##36 	 1859.8873813138655
##39 	 1873.8714386228592
##42 	 1887.9606387812457
##45 	 1902.155772333467
##48 	 1916.4576357678827
##51 	 1930.867031561463
##54 	 1945.3847682248127
##57 	 1960.0116603475399
##60 	 1974.7485286439598
