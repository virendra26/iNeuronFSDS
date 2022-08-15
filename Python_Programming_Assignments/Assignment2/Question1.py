#kilometers to miles

def kimtomiles(km):
    miles=0.621*km
    return miles

km=int(input('Input the kilometers travled '))

print('You have traveled ',kimtomiles(km),'miles')