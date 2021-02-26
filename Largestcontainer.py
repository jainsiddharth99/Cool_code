class Container:
    def __init__(self,id,length,breadth,height,pricepersqrft):
        self.id = id
        self.length = length
        self.breadth =breadth
        self.height = height
        self.pricepersqrft = pricepersqrft
        
    def findvolume(self):
        volume=self.length*self.breadth*self.height
        return volume
    
class PackagingCompany:
    def __init__(self,containerlist):
        self.containerlist = containerlist
        
    def findcost(self,cid):
        for i in self.containerlist:
            if i.id==cid:
                cost=i.findvolume()*i.pricepersqrft
                return cost
            return None
    def findlargest(self):
        vol={}
        for i in self.containerlist:
            volume=i.findvolume()
            volume=max(i.volume)
        return volume,i.id
            
    
if __name__=="__main__":
    # n=int(input())
    n=1
    containerlist=[]
    
    for i in range(n):
        id=100
        length=2
        breadth=3
        height=4
        pricepersqrft=100
        # id =int(input())
        # length=int(input())
        # breadth=int(input())
        # height=int(input())
        # pricepersqrft=int(input())
        con=Container(id,length,breadth,height,pricepersqrft)
        containerlist.append(con)
    
    pk=PackagingCompany(containerlist)
    cid=100
    # cid=int(input())
    
    a=pk.findcost(cid)
    if a==None:
        print("No Container Found")
    else:
        print(a)
    
    b=pk.findlargest()
    print(b)
