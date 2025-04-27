not runnable just explanation

okay 

how do we ste through chain of chains


okay so

myreceiptlist is a 2d list of all previous sice receipts

slice receipts contain 3 indexes before the actual slice

[index of start, direction you went, how far, 4th to end index is actually the slice returned as a chain....]


okay

myreceiptlist = 2D list of slices explained above

# step through every item of every list in my receipts

mycurrentlink = myreceiptlist.firstlink
for i in range(myreceiptlist.length):
    mycurrentreceipt = mycurrentlink.list_item

    for i in range(mycureentreceipt.length):
          mycurrentreceipt.get_index(i)

    mycurrentlink = mycurrentlink.nextlink 

      
    