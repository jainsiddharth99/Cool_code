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
        global cost
        for id in containerlist:
            cost=Container.findvolume()*pricepersqrft
            # if id==cid:
            #     cost=Container.findvolume()*pricepersqrft
        return cost
    def findlargest(self):
        for i in containerlist:
            large=max(i)
        return large
    
if __name__=="__main__":
    n=int(input())
    containerlist=[]
    
    for i in range(n):
        id =int(input())
        length=int(input())
        breadth=int(input())
        height=int(input())
        pricepersqrft=int(input())
        con=Container(id,length,breadth,height,pricepersqrft)
        containerlist.append(con)
    
    pk=PackagingCompany(containerlist)
    cid=int(input())
    
    a=pk.findcost(cid)
    print(a)
    
    b=pk.findlargest()
    print(b)