import math
import random
def is_close_to(d1,d2):#判断d2是否在d1开始顺时针方向pi的范围内,在则返回true
    if d1<math.pi:
        if d2>d1 and d2<d1+math.pi:
            return True
    else:
        if d2>d1 or d2<d1-math.pi:
            return True
    return False

def check_ducks(ducks):#输入4个角度，判断是否在一个半圆内
    for i in range(0,len(ducks)):
        all_close_to_i=1
        for j in range(0,len(ducks)):
            if i!=j:#不判断自身
                if not is_close_to(ducks[i],ducks[j]):
                    all_close_to_i=0
                    break
        if all_close_to_i==1:
            return True
    return False

def release_ducks(n):
    Ducks=[]
    for i in range(0,n):
        Ducks.append(random.uniform(0,2*math.pi))
    return Ducks



def main():
    ans_yes=0.0
    runtime=10000000
    for i in range(0,runtime):
        Ducks=release_ducks(4)#这里修改鸭子数
        if check_ducks(Ducks):
            ans_yes+=1
    print(ans_yes/runtime)

if __name__=="__main__":
    main()