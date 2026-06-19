def calculate_total(*scores):
    count = 0
    for score in scores:
        if score >=50:
            count+=1
    return sum(scores),count
print(calculate_total(85,90,78,45,92))