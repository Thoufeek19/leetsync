class Solution:
    def dayOfYear(self, date: str) -> int:
        count=0
        # d={'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
        d=[31,28,31,30,31,30,31,31,30,31,30,31]
        cal=list(date)
        days=int(cal[-2]+cal[-1])
        month=int(cal[5]+cal[6])
        year=int(cal[0]+cal[1]+cal[2]+cal[3])
        
        print(days, month, year)
        for i in range(month-1):
            count+=d[i]
        final=count+days
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return final+1 if month >= 2 else final
        else:
            return final

        

    