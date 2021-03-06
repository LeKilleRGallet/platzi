import random
import matplotlib.pyplot as plt

def least_squares(x,y):

    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    numerator=0
    for i in range(len(x)):
        numerator+=(x[i]-x_mean)*(y[i]-y_mean) #\sum(x_i-\bar{x})(y_i-\bar{y})
    denominator=0
    for i in range(len(x)):
        denominator+=(x[i]-x_mean)**2 #\sum(x_i-\bar{x})^2
    slope=numerator/denominator #\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}
    intercept=y_mean-slope*x_mean
    y_pred=[]
    for i in range(len(x)):
        y_pred.append(slope*x[i]+intercept) 

    print(f'\ny={round(slope,2)}x+{round(intercept,2)}')
    return y_pred

def scatter_trys(n,trys1,trys2=None):
    plt.scatter(n,trys1,label='custom',color='red')
    if trys2!=None:
        plt.scatter(n,trys2,label='swaping',color='blue')

    
    y_pred1=least_squares(n,trys1)
    plt.plot(n,y_pred1,label='custom',color='yellow')
    if trys2!=None:
        y_pred2=least_squares(n,trys2)
        plt.plot(n,y_pred2,label='swaping',color='green')
    

    #



    plt.xlabel('n')
    plt.ylabel('trys')
    plt.title(f'Scatter plot of trys{ " vs " if trys2!=None else ""}')
    plt.show()

def burble_sort(list):

    trys=0

    for i in range(len(list)):
        
        trys += 1

        n_0=list[0]
        n_1=list[int((len(list)-1-i)*(1/4))]
        n_2=list[int((len(list)-1-i)*(2/4))]
        n_3=list[int((len(list)-1-i)*(3/4))]
        n_4=list[(len(list)-1-i)]


        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

        if n_0==list[0] and n_1==list[int((len(list)-1-i)*(1/4))] and n_2==list[int((len(list)-1-i)*(2/4))] and n_3==list[int((len(list)-1-i)*(3/4))] and n_4==list[(len(list)-1-i)]:
            break

    return (list, trys)

def burble_sort_swaping(list, total_trys_custom):

    trys=0

    for i in range(len(list)):
        
        trys += 1
        swaping=False

        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                swaping=True
                list[j], list[j+1] = list[j+1], list[j]
                

        if trys==(total_trys_custom-2):
            a=1

        if swaping==False:
            break

    return (list, trys)

def run():
    trys_custom=[]
    trys_swaping=[]
    x=[]
    mx=1000
    for i in range(mx):
        print(f'\t\t{i+1} / {mx}', end='\r')
        list_size=random.randint(1,1000)
        list=[random.randint(1,random.randint(1,mx**2)) for _ in range(list_size)]
        # print(f'The list is: {list}')
        list_sorted, total_trys_custom=burble_sort(list[:])
        list_sorted_swaping, total_trys_swaping=burble_sort_swaping(list[:], total_trys_custom)
        list.sort()
        if list_sorted!=list and list_sorted_swaping!=list:
            print('The list is not sorted')
            print(list_sorted)
            print(list_sorted_swaping)
            print(list)
            raise SystemExit
        else:
            x.append(list_size)
            trys_custom.append(total_trys_custom)
            trys_swaping.append(total_trys_swaping)

    scatter_trys(x,trys_custom,trys_swaping)
    print('all is ok\n')

if __name__ == "__main__":
    run()