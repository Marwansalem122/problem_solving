state=input()
values= [float(i) for i in state.split()]
if values[0] >0 and values[1]>0:
       print("Q1")
elif values[0] >0 and values[1]<0:
       print("Q4")
elif values[0] <0 and values[1]>0:
       print("Q2")
elif values[0] <0 and values[1]<0:
       print("Q3")
elif values[0]==0 and values[1]==0:
       print("Origem")
elif (values[0]>0 or values[0]<0 )and values[1]==0:
       print("Eixo X")
elif values[0]==0 and (values[1]>0 or values[1]<0):
       print("Eixo Y")
