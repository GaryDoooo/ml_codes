from scipy.stats import binom

def binomial(n,p,x=None,pvalue=None,print_out=True):
    rv = binom(n,p)
    res=dict()
    
    mean, var, skew, kurt = rv.stats(moments='mvsk')
    stdev=var**.5
    res["mean"],res["var"],res["skew"],res["kurt"],res["stdev"] = \
        mean, var, skew, kurt, stdev
    
    if print_out:
        print("mean = %.2f\tvariance = %.2f\tstdev=%.2f"%(mean,var,stdev))
        print("skewness coefficient = %.2f\tkurtosis coefficient = %.2f"%(skew,kurt))
    
    def acc_p(h,t,s,threshold):
        p=0
        for i in range(h,t,s):
            p+=rv.pmf(i)
            if p> threshold:
                return p-rv.pmf(i), i-s
            
    if not x is None:
        res["px"]=rv.pmf(x)
        res["left_acc_p"]=sum([rv.pmf(i) for i in range(x+1)])
        res["right_acc_p"]=sum([rv.pmf(i) for i in range(x,n+1)])
        if res["left_acc_p"]<res["right_acc_p"]:
            right_acc_p,right_x=acc_p(n,x,-1,res["left_acc_p"])
            left_acc_p,left_x=res["left_acc_p"],x
        else:
            left_acc_p,left_x=acc_p(0,x,1,res["right_acc_p"])
            right_acc_p,right_x=res["right_acc_p"],x
        res["equal_tail"]={
            "x_left":left_x,"x_right":right_x,
            "acc_p_left":left_acc_p, "acc_p_right":right_acc_p
        }
        
        if print_out:
            print("Prob at x = %d is %.3f."%(x,res["px"]))
            print("Prob 0 to x including x total is %.3f."%res["left_acc_p"])
            print("Prob x to n including x total is %.3f."%res["right_acc_p"])
            print("Equal tail at two sides \nLeft at %d, acc. prob is %.3f."%(
                    left_x,left_acc_p))
            print("Right at %d, acc. prob is %.3f."%(right_x,right_acc_p))
            
    elif not pvalue is None:
        res["left_acc_p"],res["x_left"]=acc_p(0,n+1,1,pvalue)
        res["right_acc_p"],res["x_right"]=acc_p(n,-1,-1,pvalue)
        left_acc_p,left_x=acc_p(0,n+1,1,pvalue/2)
        right_acc_p,right_x=acc_p(n,-1,-1,pvalue/2)
        res["equal_tail"]={
            "x_left":left_x,"x_right":right_x,
            "acc_p_left":left_acc_p, "acc_p_right":right_acc_p
        }
        
        if print_out:
            print("P value = %.3f"%pvalue)
            print("Prob 0 to x = %d including x total is %.3f."%
                  (res["x_left"],res["left_acc_p"]))
            print("Prob x = %d to n including x total is %.3f."%
                  (res["x_right"],res["right_acc_p"]))
            print("Equal tail at two sides \nLeft at %d, acc. prob is %.3f."%(
                    left_x,left_acc_p))
            print("Right at %d, acc. prob is %.3f."%(right_x,right_acc_p))
        
    res["pmf"]=[rv.pmf(i) for i in range(n+1)]
    return res
        
                    
    
