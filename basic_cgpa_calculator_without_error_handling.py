def main():
    n=int(input("Enter the number of courses in digits: "))
    result=get_result(n)
    points=get_points(result)
    weigthed_points=get_weigthed_points(points,result)
    units=extract_units(result)
    gpa=sum(weigthed_points)/sum(units)
    print(f"Your CGPA is {gpa:.2f}")

def get_result(n):
    k=1
    
    print("Enter your result")
    scores=[]
    units=[]
    while k<=n:
        print("**********************")
        input("Enter the course code:")
        score=int(input("Enter your score: "))
        unit=int(input("Enter the number of units: "))
        units.append(unit)
        scores.append(score)
        k+=1
    print("**********************")
        
    return scores,  units

def get_points(result):
    scores, _ = result 
    points=[]

    for score in scores:
        if score>=70 and score <100:
            point=5
            points.append(point)
        elif score>=60 and score<70:
            point=4
            points.append(point)
        elif score>=50 and score<60:
            point=3
            points.append(point)
        elif score>=45 and score<50:
            point=2
            points.append(point)
        else:
            point=0
    return points
        
def get_weigthed_points(points,result):
    _, units = result
    weigthed_points=[]
    for p, u in zip(points, units):
        weigthed_points.append(p * u)
    return weigthed_points


def extract_units(result):
    _, units = result
    return units


main()
