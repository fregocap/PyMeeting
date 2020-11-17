from pymeetings.pymeet import *
from pymeetings.utils import *



if __name__ == '__main__':

    getmet = GetMeetingHour(['Chicago','Paris'],'2020/11/23')
    df = getmet.ConstructTable()
    print(df)
