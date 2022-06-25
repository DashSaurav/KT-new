import pandas as pd

dff_kar = pd.read_csv("data_folder/processed_occ_df.csv")

dff_kar['date'] = pd.to_datetime(dff_kar['date'], format='%Y-%m-%d')
dff_kar['T_time'] = pd.to_datetime(dff_kar['T_time'], format='%H:%M:%S')
dff_kar['T_time'] = dff_kar['T_time'].dt.time
dff_kar['Camera3'] = dff_kar["Camera3"].astype(int)


def heat_map_func(date, thresh_1, thresh_2):
    """
    Takes in the dataframe created by AI engine with additional type and column changes and returns a dataframe containing records for given input date
    with 0-24 hour bucket where each row shows how many times the occupancy count went above the given threshold in that particular hour range.
    
    Args:
        df: Input dataframe
        date: date in string form (ex:-"2022-03-28")for which records have to be retrieved
        thresh: Threshold for occupancy
    Returns:
        op_df: Output Dataframe
    """
    data = dff_kar[dff_kar['date'] == pd.to_datetime(str(date))]
    data_m1 = data[data['Room No']=='M1 Separation Room']
    data_m2 = data[data['Room No']=='M2 Purification Room']
    try:
        last_hr_r1 = data_m1.iloc[-1]['Hour']
    except:
        last_hr_r1 = 0
    try:
        last_hr_r2 = data_m2.iloc[-1]['Hour']
    except:
        last_hr_r2 = 0
    last_hr = max(last_hr_r1, last_hr_r2)
    # print(last_hr)
    m1_thresh_val = []
    m2_thresh_val = []
    hour_index = []
    for hour in range(0,last_hr+1):
        hour_index.append(hour)
        data_m1_hour = data_m1[data_m1['Hour'] == hour]
        m1_thresh_count = 0
        for m1_occ in data_m1_hour['T_Occupancy']:
            if m1_occ > int(thresh_1):
                m1_thresh_count += 1
        m1_thresh_val.append(m1_thresh_count)
        data_m2_hour = data_m2[data_m2['Hour'] == hour]
        m2_thresh_count = 0
        for m2_occ in data_m2_hour['T_Occupancy']:
            if m2_occ > int(thresh_2):
                m2_thresh_count += 1
        m2_thresh_val.append(m2_thresh_count)
    dff = {'Hour':hour_index,'M1 Separation Room': m1_thresh_val,'M2 Purification Room': m2_thresh_val}
    op_df = pd.DataFrame(dff)
    m1 = op_df['M1 Separation Room'].to_list()
    m2 = op_df['M2 Purification Room'].to_list()
    return dict({'Room-1':m1, 'Room-2':m2})
#kar_df[(kar_df['date'] == pd.to_datetime(str('2022-03-23'))) & (kar_df['Room No'] == 'M1 Separation Room')]
#heat_map_func('2022-03-23',1, 0)

def func_1(date, thresh):
    """
    Takes in the dataframe and returns a dataframe where each row is a record for the coressponding date telling
    how many times the occupancy in that room went above the given "thresh" parameter.

    Args:
        
        date: date in string form (ex:-"2022-03-28")for which the data is required
        thresh: Threshold for the occupancy

    Returns:
        op_df: Returns an output dataframe where the row is a record for the input date telling
               how many times the occupancy in that room went above the given "thresh" parameter
    """
    data = dff_kar[dff_kar['date'] == pd.to_datetime(str(date))]
    data_m1 = data[data['Room No'] == 'M1 Separation Room']
    data_m2 = data[data['Room No'] == 'M2 Purification Room']

    m1_thresh_count = 0
    for i in data_m1['T_Occupancy']:
        if i > thresh:
            m1_thresh_count += 1

    m2_thresh_count = 0
    for j in data_m2['T_Occupancy']:
        if j > thresh:
            m2_thresh_count += 1

    dff = {'date': [date], 'M1 Separation Room': m1_thresh_count, 'M2 Purification Room': m2_thresh_count}
    op_df = pd.DataFrame(dff)
    # op_df.set_index(date)
    return op_df
# df_thres=func_1(today_,6)  # don't comment
# room_wise_non_compliance_occ=func_1(today_, 5)
# room_wise_non_compliance_occ_=room_wise_non_compliance_occ.set_index("date") # don't comment

