from random import random
import numpy as np
import pandas as pd
import itertools

dataset=pd.read_csv('banknote_authentication_data.txt')
X1 = dataset['x1'].tolist()
X2 = dataset['x2'].tolist()
X3 = dataset['x3'].tolist()
X4 = dataset['x4'].tolist()
Y  = dataset['y'].tolist()

rate=0.05
w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,b1,b2=(random() for x in range(22))



for i in range(100):
    fianl_delta_w1 = 0
    fianl_delta_w2 = 0
    fianl_delta_w3 = 0
    fianl_delta_w4 = 0
    fianl_delta_w5 = 0
    fianl_delta_w6 = 0
    fianl_delta_w7 = 0
    fianl_delta_w8 = 0
    fianl_delta_w9 = 0
    fianl_delta_w10 = 0
    fianl_delta_w11 = 0
    fianl_delta_w12 = 0
    fianl_delta_w13 = 0
    fianl_delta_w14 = 0
    fianl_delta_w15 = 0
    fianl_delta_w16 = 0
    fianl_delta_w17 = 0
    fianl_delta_w18 = 0
    fianl_delta_w19 = 0
    fianl_delta_w20 = 0
    fianl_delta_b1 = 0
    fianl_delta_b2 = 0
    average_error = 0

    for x1,x2,x3,x4,y in itertools.zip_longest(X1,X2,X3,X4,Y):
        net_h1= (w1*x1) + (w2*x2) + (w3*x3) + (w4*x4) + b1
        net_h2= (w5*x1) + (w6*x2) + (w7*x3) + (w8*x4) + b1
        net_h3= (w9*x1) + (w10*x2) + (w11*x3) + (w12*x4) + b1
        net_h4= (w13*x1) + (w14*x2) + (w15*x3) + (w16*x4) + b1

        out_h1= 1/(1+(np.exp(-net_h1)))
        out_h2= 1/(1+(np.exp(-net_h2)))
        out_h3= 1/(1+(np.exp(-net_h3)))
        out_h4= 1/(1+(np.exp(-net_h4)))

        net_o1= (w17*out_h1) + (w18*out_h2) + (w19*out_h3) + (w20*out_h4) + b2
        out_o1= 1/(1+(np.exp(-net_o1)))

        e_o1=0.5*((y-out_o1)*(y-out_o1))
        average_error=average_error+e_o1

        delta_o1 = (out_o1-y)*(out_o1*(1-out_o1))
        delta_w17= delta_o1*out_h1
        delta_w18= delta_o1*out_h2
        delta_w19= delta_o1*out_h3
        delta_w20= delta_o1*out_h4

        delta_b2 = delta_o1

        delta_h1 = (delta_o1*w17)*(out_h1*(1-out_h1))
        delta_w1= delta_h1*x1
        delta_w2= delta_h1*x2
        delta_w3= delta_h1*x3
        delta_w4= delta_h1*x4

        delta_h2 = (delta_o1*w18)*(out_h2*(1-out_h2))

        delta_w5= delta_h2*x1
        delta_w6= delta_h2*x2
        delta_w7= delta_h2*x3
        delta_w8= delta_h2*x4

        delta_h3 = (delta_o1*w19)*(out_h3*(1-out_h3))

        delta_w9= delta_h3*x1
        delta_w10= delta_h3*x2
        delta_w11= delta_h3*x3
        delta_w12= delta_h3*x4

        delta_h4 = (delta_o1*w20)*(out_h4*(1-out_h4))

        delta_w13= delta_h4*x1
        delta_w14= delta_h4*x2
        delta_w15= delta_h4*x3
        delta_w16= delta_h4*x4

        delta_b1 = delta_h4

        fianl_delta_w1 = fianl_delta_w1 + delta_w1
        fianl_delta_w2 = fianl_delta_w2 + delta_w2
        fianl_delta_w3 = fianl_delta_w3 + delta_w3
        fianl_delta_w4 = fianl_delta_w4 + delta_w4
        fianl_delta_w5 = fianl_delta_w5 + delta_w5
        fianl_delta_w6 = fianl_delta_w6 + delta_w6
        fianl_delta_w7 = fianl_delta_w7 + delta_w7
        fianl_delta_w8 = fianl_delta_w8 + delta_w8
        fianl_delta_w9 = fianl_delta_w9 + delta_w9
        fianl_delta_w10 = fianl_delta_w10 + delta_w10
        fianl_delta_w11 = fianl_delta_w11 + delta_w11
        fianl_delta_w12 = fianl_delta_w12 + delta_w12
        fianl_delta_w13 = fianl_delta_w13 + delta_w13
        fianl_delta_w14 = fianl_delta_w14 + delta_w14
        fianl_delta_w15 = fianl_delta_w15 + delta_w15
        fianl_delta_w16 = fianl_delta_w16 + delta_w16
        fianl_delta_w17 = fianl_delta_w17 + delta_w17
        fianl_delta_w18 = fianl_delta_w18 + delta_w18
        fianl_delta_w19 = fianl_delta_w19 + delta_w19
        fianl_delta_w20 = fianl_delta_w20 + delta_w20

        fianl_delta_b1 = fianl_delta_b1 + delta_b1
        fianl_delta_b2 = fianl_delta_b2 + delta_b2

    average_error=average_error/1373
    print("Average Cost= ",average_error)


    w1=w1-(rate*fianl_delta_w1)
    w2=w2-(rate*fianl_delta_w2)
    w3=w3-(rate*fianl_delta_w3)
    w4=w4-(rate*fianl_delta_w4)
    w5=w5-(rate*fianl_delta_w5)
    w6=w6-(rate*fianl_delta_w6)
    w7=w7-(rate*fianl_delta_w7)
    w8=w8-(rate*fianl_delta_w8)
    w9=w9-(rate*fianl_delta_w9)
    w10=w10-(rate*fianl_delta_w10)
    w11=w11-(rate*fianl_delta_w11)
    w12=w12-(rate*fianl_delta_w12)
    w13=w13-(rate*fianl_delta_w13)
    w14=w14-(rate*fianl_delta_w14)
    w15=w15-(rate*fianl_delta_w15)
    w16=w16-(rate*fianl_delta_w16)
    w17=w17-(rate*fianl_delta_w17)
    w18=w18-(rate*fianl_delta_w18)
    w19=w19-(rate*fianl_delta_w19)
    w20=w20-(rate*fianl_delta_w20)

    b1=b1-(rate*fianl_delta_b1)
    b2=b2-(rate*fianl_delta_b2)

print(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20)

# Check Accuracy:-
predicted_output=[]
for x1, x2, x3, x4, y in itertools.zip_longest(X1, X2, X3, X4, Y):
    net_h1 = (w1 * x1) + (w2 * x2) + (w3 * x3) + (w4 * x4) + b1
    net_h2 = (w5 * x1) + (w6 * x2) + (w7 * x3) + (w8 * x4) + b1
    net_h3 = (w9 * x1) + (w10 * x2) + (w11 * x3) + (w12 * x4) + b1
    net_h4 = (w13 * x1) + (w14 * x2) + (w15 * x3) + (w16 * x4) + b1

    out_h1 = 1 / (1 + (np.exp(-net_h1)))
    out_h2 = 1 / (1 + (np.exp(-net_h2)))
    out_h3 = 1 / (1 + (np.exp(-net_h3)))
    out_h4 = 1 / (1 + (np.exp(-net_h4)))

    net_o1 = (w17 * out_h1) + (w18 * out_h2) + (w19 * out_h3) + (w20 * out_h4) + b2
    out_o1 = 1 / (1 + (np.exp(-net_o1)))

    if(out_o1<0.5):
        predicted_output.append(0)
    else:
        predicted_output.append(1)
print("Predicted Output=",predicted_output)
print("Actual Output=",Y)

count=0
for pred_out,actual_out in itertools.zip_longest(predicted_output,Y):
    if(pred_out==actual_out):
        count=count+1

accuracy=(count/len(Y))*100

print("Accuracy=",accuracy)