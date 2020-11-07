import speedtest




if __name__ == "__main__":
    
    speed = speedtest.Speedtest()

    print("Choose the units to be Displayed \n1)Mbps  2)MBps\n")
    choice = int(input())
    print("\n\nPlease Wait......\n\n")
    if(choice == 1 or choice == 2):
        print("The source is : ",)
        Ds = speed.download()
        Us = speed.upload()
        servers = []   
        speed.get_servers(servers)   
        png = (speed.results.ping)

        if choice == 1:
            print("\nThe Download Speed is ",Ds/1000000," Mbps")
            print("\nThe Upload Speed is ",Us/1000000," Mbps")

        
        elif choice == 2:
            print("\nThe Download Speed is ",Ds*0.000000125," MBps")
            print("\nThe Upload Speed is ",Us*0.000000125," MBps")

        
        print("\nThe Ping is : ",png," ms\n")
