import pandas as pd


def region(selectYear, selectQ, selectMonth, selectBelong, data):
    data = data.rename(columns ={'originTotalProductPrice' : 'sales'}).set_index('sales').reset_index()
    data = data.loc[data['orderSheetId'].duplicated() == False]
   
    if selectYear == 'Year':
        if selectBelong == 'Belong' :
            #전체데이터
            #기관을 기준으로 매출액 합산
            regionSum = data.groupby('belong')[['sales']].sum().reset_index()  
        else :
            #기관만 선택
            #기관을 기준으로 매출액 합산
            regionSum = data.groupby(['belong'])[['sales']].sum().reset_index() 
            #선택한 기관 데이터만 추출
            regionSum = regionSum.loc[regionSum['belong'] == selectBelong]

        
    else :
        #해당 기간에 대한 데이터
        if selectQ == 'Quarter' :    
            if selectMonth == 'Month': 
                if selectBelong == 'Belong' :
                    #년도만 선택
                    regionSum = data.groupby(['belong','paymentcomplete_year']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[regionSum['paymentcomplete_year'] == selectYear]  
                
                else :
                    #년도 기관선택
                    regionSum = data.groupby(['belong','paymentcomplete_year']).sum()[['sales']].reset_index()
                    regionSum =  regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) & (regionSum['belong'] == selectBelong)]
            
            else :
                if selectBelong == 'Belong' :
                    #년도 달 선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_month']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) & (regionSum['paymentcomplete_month'] == selectMonth)]
                else :
                    #년도 달 기관선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_month']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) &(regionSum['belong'] == selectBelong) & (regionSum['paymentcomplete_month'] == selectMonth)]
            
        else :
            if selectMonth == 'Month': 
                if selectBelong == 'Belong' :
                    #년도 분기만 선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_Q']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) & (regionSum['paymentcomplete_Q'] == selectQ)]
                
                else :
                    #년도 분기 기관선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_Q']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) & (regionSum['belong'] == selectBelong) & (regionSum['paymentcomplete_Q'] == selectQ)] 
              
            
            else :
                if selectBelong == 'Belong' :
                    #년도 분기 달 선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_month','paymentcomplete_Q']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) & (regionSum['paymentcomplete_month'] == selectMonth) & (regionSum['paymentcomplete_Q'] == selectQ)] 
                
                else :
                    #년도 분기 달 기관선택
                    regionSum = data.groupby(['belong','paymentcomplete_year','paymentcomplete_month','paymentcomplete_Q']).sum()[['sales']].reset_index()
                    regionSum = regionSum.loc[(regionSum['paymentcomplete_year'] == selectYear) &(regionSum['belong'] == selectBelong) & (regionSum['paymentcomplete_month'] == selectMonth) & (regionSum['paymentcomplete_Q'] == selectQ)] 
            
    #상위 20개의 데이터만 추출
    regionSum = regionSum.sort_values('belong', ascending=False).head(20)
    return regionSum
    #pie 그래프 시각화
    # fig = px.pie( regionSum, names='belong', values='sales',title='소속별 매출액( Top 20 )',width=500, height=500, hole=.5)
    # fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=13)
    # st.plotly_chart(fig)
            
        
        