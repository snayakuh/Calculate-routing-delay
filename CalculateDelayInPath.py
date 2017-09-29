
# coding: utf-8

# # Python Code To calculate the Total Delay in a Path

# In[1]:

class Link:
 
    def PktDelay(self, PacketLength):
        PropSpeed = input("Enter propagation speed:")
        if PropSpeed < 1:
            S = 3e7
        else:
            S = float(PropSpeed)
 
        LinkLen = input("Enter length of the link:")
        if LinkLen < 1:
            D = 1000
        else:
            D = float(LinkLen)
 
        TransRate = input("Enter transmission rate(B/W):")
        if TransRate < 1:
            R = 100e6
        else:
            R = float(TransRate)
        L=PacketLength
 
        #Lets Take a constant overhead of 128 bytes
        OverHead=128*8
        PropDelay=D/S
        TransDelay=L/R
        Delay=PropDelay+TransDelay+OverHead
        return Delay
 
    def Calculate_Delay(self, ListofLinks, PLength):
        TotalDelay=0
        for i in range(len(ListofLinks)):
            CurrentLink=ListofLinks[i]
            print("================\nLink %d Details:\n================" %(i+1))
            TotalDelay=TotalDelay+ CurrentLink.PktDelay(PLength)
        return TotalDelay

#Enter the size of the packet and no of links in the path
PLen = input("Enter packet length in Bits:")
PLen = int(PLen)
 
n=input("Enter number of links in the Path:")
n=int(n)
 
# Create a path with list of links(objects), Each object is Link Type. 
Path=[]
for i in range(n):
    ln=Link()
    Path.append(ln)
 
#Print total delay of packet along path[]
print("\nTotal delay along path: %f seconds" %(Link().Calculate_Delay(Path, PLen)))

"""
============
  REMARKS 
============
Queueing delay, which is not included in the calculation in this program may or may not be significant
as it depends on factors such as transmission rate of the link, time of arrival of packet to the queue,
nature of traffic (periodic or in bursts).
 
Processing delay, which is also not included in this delay calculation depends on the type of router and
the level of encryption used to modify packet content.
 
Header/trailer overhead is variable and depends on protocols at different layers.

"""
 


# In[ ]:



